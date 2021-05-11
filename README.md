
# Running locally

```bash
# Virtual Env
mkproject mario
workon mario
pip install -r requirements.txt

# Database
python marioshop/manage.py migrate
python marioshop/manage.py oscar_populate_countries --no-shipping
echo "from oscar.core.loading import get_model; Country = get_model('address', 'Country'); Country.objects.filter(iso_3166_1_a2='BR').update(is_shipping_country=True)" | python marioshop/manage.py shell
python marioshop/manage.py oscar_accounts_init

# Creating Super User
python marioshop/manage.py createsuperuser

# Running
python marioshop/manage.py runserver

```

## First Usage

1. Create a `product_type`:
    * Go to:  http://localhost:8000/dashboard/catalogue/product-types/
    * Create a product type, example: "Ferramenta"
2. Create a `partner`:
    * Go to: http://localhost:8000/dashboard/partners/
    * Create a partner, example: "Vendedor Teste"
3. Create a `category`:
   * Go to: http://localhost:8000/dashboard/catalogue/categories/
   * Create a category, example: "Manuais", "Elétricas"
4. Create a product:
   * Go to: http://localhost:8000/dashboard/catalogue/
   * Create a product, example: "Chave de fenda"
5. Create a Account with some Balance/Credit:
   * Go to: http://localhost:8000/dashboard/accounts/
   * Create a account, example: "Saldo do Italo"
6. Finally:
   * Go to: http://localhost:8000/catalogue/
   * See your product and try to buy
7. Extra:
   * Go to: http://localhost:8000/account-balance/
   * To see your balance/credits.

## Periodic Routines

TODO: Uses celery-beat to schedule routines

```bash
# Add a crontab to
python marioshop/manage.py close_expired_accounts
```


## Development Experience

* Install `pre-commit`: https://pre-commit.com/#installation
* Prefer to use `black` as autoformater for this project.
* Prefer to use `flake8` as linter for this project.
