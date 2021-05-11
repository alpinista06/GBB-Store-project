from oscar_accounts.checkout import gateway
from oscar_accounts.views import AccountBalanceView
from django.http import HttpResponse
from django.views import View
from apps.customer.resources import UserResource
from tablib import Dataset
from django.shortcuts import render


class AccountBalanceView(AccountBalanceView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Add accounts that are linked to this user
        if self.request.user.is_authenticated:
            ctx["user_accounts"] = gateway.user_accounts(self.request.user)
        return ctx



def GetImportUsers(request, *args, **kwargs):
    if request.method == 'POST':
        user_resource = UserResource()
        dataset = Dataset()
        doc_byte = request.FILES['arquivo'].read()
        doc = doc_byte.decode('utf-8')

        imported_data = dataset.load(doc, format='csv')
        #result = user_resource.import_data(dataset, dry_run=True)  # Test the data import
        user_resource.import_data(dataset, dry_run=False)

        #if not result.has_errors():
        #    user_resource.import_data(dataset, dry_run=False)  # Actually import now
        return render(request, 'import.html')
    else:
        return render(request, 'import.html')

