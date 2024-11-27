from database import db
from collections import namedtuple


models = db.select_models()
emails = db.select_emails()
customers_count = db.select_customers_by_country()
employees_count = db.select_employees_by_country()
brands = db.select_brands()
filtered_brands = db.select_brands_over5()
orders = db.select_orders()
models_price = db.select_models_price()
brands_count = db.select_brands_count()
customers = db.select_customers()
employees = db.select_employees()
next_models = db.select_models_next()


Models = namedtuple("Models", ['Brand_Name', 'Color', 'Model_Name'])
Emails = namedtuple("Emails", ['emails'])
Customers_count = namedtuple("Customers", ['Country', 'Count'])
Employees_count = namedtuple("Employees", ['Country', 'Count'])
Brands = namedtuple("Brands", ['Brand', 'Count'])
Filtered_brands = namedtuple("Brands", ['Brand', 'Count'])
Orders = namedtuple("Orders", ['Id', 'Customers', 'Phone', 'Employees', 'Models', 'Price', 'Count', 'Date'])
Models_price = namedtuple('Models_Price', 'Price')
Brands_count = namedtuple('Brands_Count', 'Count')
Customers = namedtuple("Customers", ['ID', 'first_name', 'last_name', 'birth_date', 'phone', 'email', 'country', 'city'])
Employees = namedtuple("Employees", ['ID', 'first_name', 'last_name', 'birth_date', 'phone', 'email', 'country', 'city'])
Next_models = namedtuple("Models", ['ID', 'model_name', 'model_price', 'brand_id', 'color_id', 'car_count'])


def show_models():
    print('-' * 70)
    print("|", "Brand Name".center(25, ' '), "|", "Color".center(15, ' '), "|", "Model Name".center(20, ' '), "|")
    print('-' * 70)
    for mode in models:
        car = Models(*mode)
        print("|", str(car.Brand_Name).center(25, ' '), "|", str(car.Color).center(15, ' '), "|", str(car.Model_Name).center(20, ' '), "|")
        print('-' * 70)


def show_emails():
    print('-' * 29)
    print("|", "Emails".center(25, ' '), "|")
    print('-' * 29)
    for email in emails:
        ema = Emails(*email)
        print("|", str(ema.emails).center(25, ' '), "|")
        print('-' * 29)


def show_customers_count():
    print('-' * 37)
    print("|", "Country".center(15, ' '), "|", "Customer Count".center(15, ' '), "|")
    print('-' * 37)
    for customer in customers_count:
        cust = Customers_count(*customer)
        print("|", str(cust.Country).center(15, ' '), "|", str(cust.Count).center(15, ' '), "|")
        print('-' * 37)


def show_employee_count():
    print('-' * 37)
    print("|", "Country".center(15, ' '), "|", "Employee Count".center(15, ' '), "|")
    print('-' * 37)
    for employee in employees_count:
        emp = Employees_count(*employee)
        print("|", str(emp.Country).center(15, ' '), "|", str(emp.Count).center(15, ' '), "|")
        print('-' * 37)


def show_brands_count():
    print('-' * 37)
    print("|", "Brands".center(15, ' '), "|", "Models Count".center(15, ' '), "|")
    print('-' * 37)
    for brand in brands:
        br = Brands(*brand)
        print("|", str(br.Brand).center(15, ' '), "|", str(br.Count).center(15, ' '), "|")
        print('-' * 37)


def show_brands_filtered():
    print('-' * 37)
    print("|", "Brands".center(15, ' '), "|", "Models Count".center(15, ' '), "|")
    print('-' * 37)
    for filtered_brand in filtered_brands:
        br = Filtered_brands(*filtered_brand)
        print("|", str(br.Brand).center(15, ' '), "|", str(br.Count).center(15, ' '), "|")
        print('-' * 37)


def show_orders():
    print('-' * 185)
    print("|", "ORDER ID".center(10, ' '), "|", "CUSTOMERS".center(25, ' '), "|", "Phone".center(25, ' '), "|",
          "Employees".center(25, ' '), "|", "MODELS".center(25, ' '), "|",
          "Model Price".center(20, ' '), "|", "Count".center(15, ' '), "|",
          "Order Date".center(15, ' '), "|")
    print('-' * 185)

    for order in orders:
        ord_e = Orders(*order)
        print("|", str(ord_e.Id).center(10, ' '), "|",
              str(ord_e.Customers).center(25, ' '), "|",
              str(ord_e.Phone).center(25, ' '), "|",
              str(ord_e.Employees).center(25, ' '), "|",
              str(ord_e.Models).center(25, ' '), "|",
              str(ord_e.Price).center(20, ' '), "|",
              str(ord_e.Count).center(15, ' '), "|",
              str(ord_e.Date).center(15, ' '), "|")
        print('-' * 185)


def show_models_price():
    print('-' * 15)
    print("|", "Total Price".center(8, ' '), "|")
    print('-' * 15)
    print("|", str(models_price[0]).center(11, ' '), "|")
    print('-' * 15)


def show_total_brands():
    print('-' * 16)
    print("|", "Total Brands".center(8, ' '), "|")
    print('-' * 16)
    print("|", str(brands_count[0]).center(12, ' '), "|")
    print('-' * 16)


def show_customers():
    print('-' * 185)
    print("|", "ID".center(10, ' '), "|", "First Name".center(25, ' '), "|", "Last Name".center(25, ' '), "|", "Birth Date".center(25, ' '), "|",
          "Phone Number".center(25, ' '), "|", "Email".center(20, ' '), "|",
          "Country".center(15, ' '), "|", "City".center(15, ' '), "|")
    print('-' * 185)

    for customer in customers:
        custom = Customers(*customer)
        print("|", str(custom.ID).center(10, ' '), "|",
              str(custom.first_name).center(25, ' '), "|",
              str(custom.last_name).center(25, ' '), "|",
              str(custom.birth_date).center(25, ' '), "|",
              str(custom.phone).center(25, ' '), "|",
              str(custom.email).center(20, ' '), "|",
              str(custom.country).center(15, ' '), "|",
              str(custom.city).center(15, ' '), "|")
        print('-' * 185)


def show_employees():
    print('-' * 185)
    print("|", "ID".center(10, ' '), "|", "First Name".center(25, ' '), "|", "Last Name".center(25, ' '), "|", "Birth Date".center(25, ' '), "|",
          "Phone Number".center(25, ' '), "|", "Email".center(20, ' '), "|",
          "Country".center(15, ' '), "|", "City".center(15, ' '), "|")
    print('-' * 185)

    for employee in employees:
        emp = Employees(*employee)
        print("|", str(emp.ID).center(10, ' '), "|",
              str(emp.first_name).center(25, ' '), "|",
              str(emp.last_name).center(25, ' '), "|",
              str(emp.birth_date).center(25, ' '), "|",
              str(emp.phone).center(25, ' '), "|",
              str(emp.email).center(20, ' '), "|",
              str(emp.country).center(15, ' '), "|",
              str(emp.city).center(15, ' '), "|")
        print('-' * 185)


def show_next_models():
    print('-' * 149)
    print("|", "ID".center(10, ' '), "|", "Model Name".center(25, ' '), "|", "Price".center(25, ' '), "|", "Brand ID".center(25, ' '), "|",
          "Color ID".center(25, ' '), "|", "Count".center(20, ' '), "|")
    print('-' * 149)

    for next_model in next_models:
        nxt = Next_models(*next_model)
        print("|", str(nxt.ID).center(10, ' '), "|",
              str(nxt.model_name).center(25, ' '), "|",
              str(nxt.model_price).center(25, ' '), "|",
              str(nxt.brand_id).center(25, ' '), "|",
              str(nxt.color_id).center(25, ' '), "|",
              str(nxt.car_count).center(20, ' '), "|")
        print('-' * 149)
