import psycopg2


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='autosalon',
            user='postgres',
            host='localhost',
            password='1'
        )

    def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return result

    def select_models(self):
        sql = '''SELECT brands.brand_name, colors.color_name, models.model_name FROM models
            JOIN brands USING(brand_id)
            JOIN colors USING(color_id);
        '''
        return self.manager(sql, fetchall=True)

    def select_emails(self):
        sql = '''SELECT email from employees
            UNION ALL
            SELECT email from customers;
        '''
        return self.manager(sql, fetchall=True)

    def select_customers_by_country(self):
        sql = '''SELECT country, COUNT(country) FROM customers GROUP BY country ORDER BY count;
        '''
        return self.manager(sql, fetchall=True)

    def select_employees_by_country(self):
        sql = '''SELECT country, COUNT(*) FROM employees GROUP BY country ORDER BY count;
        '''
        return self.manager(sql, fetchall=True)

    def select_brands(self):
        sql = '''SELECT brands.brand_name, COUNT(models.model_name) FROM models 
            JOIN brands USING(brand_id)
            GROUP BY brands.brand_name ORDER BY brand_name;
        '''
        return self.manager(sql, fetchall=True)

    def select_brands_over5(self):
        sql = '''SELECT brands.brand_name, COUNT(models.model_name) FROM models 
            JOIN brands USING(brand_id) GROUP BY brands.brand_name HAVING COUNT(models.model_name) > 5 ORDER BY brand_name;
        '''
        return self.manager(sql, fetchall=True)

    def select_orders(self):
        sql = '''SELECT orders.order_id,
            customers.first_name || ' ' || customers.last_name AS customers,
            customers.phone_number AS customer_phone_number,
            employees.first_name || ' ' || employees.last_name AS employees,
            models.model_name,
            models.model_price,
            orders.car_count,
            orders.order_date
            FROM orders
            JOIN customers ON customers.customer_id = orders.customer_id
            JOIN employees ON employees.employee_id = orders.employee_id
            JOIN models ON models.model_id = orders.model_id;
        '''
        return self.manager(sql, fetchall=True)

    def select_models_price(self):
        sql = '''select SUM(model_price) AS all_models_price from models;
        '''
        return self.manager(sql, fetchone=True)

    def select_brands_count(self):
        sql = '''select COUNT(brand_id) from brands;
        '''
        return self.manager(sql, fetchone=True)

    def input_brands(self, brand_name):
        sql = '''INSERT INTO brands(brand_name) VALUES (%s) ON CONFLICT DO NOTHING'''
        self.manager(sql, brand_name, commit=True)

    def input_colors(self, color_name):
        sql = '''INSERT INTO colors(color_name) VALUES (%s) ON CONFLICT DO NOTHING'''
        self.manager(sql, color_name, commit=True)

    def input_employees(self, employee_id, first_name, last_name, birth_date, phone_number, email, country, city):
        sql = '''INSERT INTO employees(employee_id, first_name, last_name, birth_date, phone_number, email, country, city)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING'''
        self.manager(sql, employee_id, first_name, last_name, birth_date, phone_number, email, country, city, commit=True)

    def select_customers(self):
        sql = '''SELECT * FROM customers'''
        return self.manager(sql, fetchall=True)

    def select_employees(self):
        sql = '''SELECT * FROM employees'''
        return self.manager(sql, fetchall=True)

    def select_models_next(self):
        sql = '''SELECT * FROM models'''
        return self.manager(sql, fetchall=True)

    def input_orders(self, customer_id, employee_id, model_id, car_count, order_date):
        sql = '''INSERT INTO orders(customer_id, employee_id, model_id, car_count, order_date) VALUES
        (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING'''
        self.manager(sql, customer_id, employee_id, model_id, car_count, order_date, commit=True)


db = DataBase()
