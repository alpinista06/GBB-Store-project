from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views import generic
from oscar.core.loading import get_model
from oscar.templatetags.currency_filters import currency
from oscar_accounts import exceptions, facade, names
from oscar_accounts.checkout import gateway
from django.urls import reverse_lazy
from oscar_accounts import codes
from django.views import View
from apps.customer.resources import ToolResource
from tablib import Dataset
from django.shortcuts import render
from django.contrib.auth import get_user_model

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .forms import ToolForm, ToolImportForm
from .models import Tool, ToolType

AccountType = get_model("oscar_accounts", "AccountType")
Account = get_model("oscar_accounts", "Account")
User = get_user_model()


class InserirCreditoView(generic.FormView):
    model = Tool
    form_class = ToolForm
    #fields = ["name", "type", "quantity"]
    template_name = 'creditos.html'
    success_url = reverse_lazy('inserir-credito-view')

    def _get_user_account(self, form):
        user = form.cleaned_data.get("user")
        user_accounts = gateway.user_accounts(user)
        if len(user_accounts) :
            return user_accounts[0]
        else:
            return self._create_user_account(user=user)

    def _create_user_account(self, user):
        AccountType.objects.all()
        deferred_income = AccountType.objects.get(name=names.DEFERRED_INCOME)
        types = deferred_income.get_children()
        if types.count() != 1:
            # é preciso escolher qual dos tipos ou criar um
            raise exceptions.ImproperlyConfigured(
                "You need to define some 'deferred income' account types")
        # fora do if segue o jogo:
        account_type = types[0]
        
        dados_da_carteira = {
            "name": f"Créditos do: {user.username}",
            "description": "Conta com os créditos recebidos pela inserção de Ferramentas.",
            "account_type": types[0],
            "primary_user" : user,
            "code": codes.generate()
        }
        user_account = Account.objects.create(**dados_da_carteira)
        return user_account 


    def _get_source_account(self):
        unpaid_sources = AccountType.objects.get(name=names.UNPAID_ACCOUNT_TYPE)
        sources = unpaid_sources.accounts.all()
        if not sources.exists():
            messages.errors("Carteira não configurada")
            raise ImproperlyConfigured("You need to define some 'unpaid source' accounts")
        return sources[0]

    def form_valid(self, form):
        # O formulario foi validado e o obj do type ferramenta foi criado
        self.object = form.save()
        ferramenta = self.object

        account = self._get_user_account(form)
        amount = ferramenta.value
        try:
            transfer = facade.transfer(
                self._get_source_account(),
                account,
                amount,
                user=form.cleaned_data.get("user"),
                description=_(f"Inserção da Ferramenta: {ferramenta.name}"),
            )
            ferramenta.transfer = transfer
            ferramenta.save()
        except exceptions.AccountException as e:
            messages.error(
                self.request,
                _("Tive um problema para inserir a sua ferramenta, procure o mario: %s")
                % e,
            )
        else:
            messages.success(
                self.request, _("%s adicionado ao seu saldo") % currency(amount)
            )

        return HttpResponseRedirect(self.get_success_url())


class HelloThereView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello there")

class CriarFerramentaView(generic.CreateView):
    model = ToolType
    fields = ['name', 'type', 'description', 'value']
    template_name = 'ferramenta.html'
    success_url = reverse_lazy('criar-ferramenta-view')

def GetImportTools(request, *args, **kwargs):
    if request.method == 'POST':
        
        tool_resource = ToolResource()
        dataset = Dataset()
        doc_byte = request.FILES['arquivo'].read()
        doc = doc_byte.decode('utf-8')

        imported_data = dataset.load(doc, format='csv')
        print(imported_data)
        #result = user_resource.import_data(dataset, dry_run=True)  # Test the data import
        tool_resource.import_data(dataset, dry_run=False)

        for line in imported_data:
            
            name = User.objects.filter(username=line[0])
            type = ToolType.objects.filter(name=line[1],type=line[2])
            data={
                'user': name[0].id,
                'type': type[0].id,
                'quantity': line[3],
            }

            form = ToolImportForm(data)
            #print(form)
            if form.is_valid():
                print("form is valid")
                form_valid(form,request)
            else:
                print("Form i'snt valid")

        return render(request, 'import.html')
        
    else:
        return render(request, 'import.html')
        
    
def form_valid(form, request):
# O formulario foi validado e o obj do type ferramenta foi criado
    object = form.save()
    ferramenta = object

    account = get_imported_user_account(form)
    amount = ferramenta.value
    try:
        transfer = facade.transfer(
            get_imported_source_account(),
            account,
            amount,
            user=form.cleaned_data.get("user"),
            description=_(f"Inserção da Ferramenta via arquivo de solicitações: {ferramenta.name}"),
        )
        ferramenta.transfer = transfer
        ferramenta.save()
    except exceptions.AccountException as e:
        messages.error(
            resquest,
            _("Tive um problema para processar o arquivo de solicitação, procure o mario: %s")
            % e,
        )
    else:
        messages.success(
            request, _("%s adicionado ao seu saldo via arquivo de solicitações") % currency(amount)
        )

    return render(request, 'import.html')

def get_imported_user_account(form):
        user = form.cleaned_data.get("user")
        user_accounts = gateway.user_accounts(user)
        if len(user_accounts) :
            return user_accounts[0]
        else:
            return create_imported_user_account(user=user)

def get_imported_source_account():
    unpaid_sources = AccountType.objects.get(name=names.UNPAID_ACCOUNT_TYPE)
    sources = unpaid_sources.accounts.all()
    if not sources.exists():
        messages.errors("Carteira não configurada")
        raise ImproperlyConfigured("You need to define some 'unpaid source' accounts")
    return sources[0]

def create_imported_user_account(user):
    AccountType.objects.all()
    deferred_income = AccountType.objects.get(name=names.DEFERRED_INCOME)
    types = deferred_income.get_children()
    if types.count() != 1:
        # é preciso escolher qual dos tipos ou criar um
        raise exceptions.ImproperlyConfigured(
            "You need to define some 'deferred income' account types")
    # fora do if segue o jogo:
    account_type = types[0]
    
    dados_da_carteira = {
        "name": f"Créditos do: {user.username}",
        "description": "Conta com os créditos recebidos pela inserção de Ferramentas.",
        "account_type": types[0],
        "primary_user" : user,
        "code": codes.generate()
    }
    user_account = Account.objects.create(**dados_da_carteira)
    return user_account 
