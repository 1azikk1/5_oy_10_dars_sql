from database import db
import named_tuple_base
from datetime import datetime
date_format = "%Y-%m-%d"


if __name__ == '__main__':
    while True:
        command = input("Buyruqni kiriting: ").lower()
        if command == 'stop':
            print("Dastur to'xtadi!")
            break
        elif command == 'help':
            print("Buyruqlar:\n1.Select Models - Avtomobil model, brand va ranglarini ko'rsatadi!\n"
                  "2.Select Emails - Xodimlar hamda xaridorlarning emaillarini ko'rsatadi!\n"
                  "3.Select Customers - Buyurtmachilar haqida ma'lumot beradi!\n"
                  "4.Select Employees - Xodimlar haqida ma'lumot beradi!\n"
                  "5.Select Brands - Brendlar haqida umumiy ma'lumot beradi\n"
                  "6.Select Filtered Brands - Brendlar haqida filtrlangan ma'lumot beradi!\n"
                  "7.Select Orders - Buyurtmalar haqida to'liq ma'lumot beradi!\n"
                  "8.Select Sum Models - Modellarning umumiy narxini chiqarib beradi!\n"
                  "9.Select Total Brands - Jami brendlar sonini chiqarib beradi!\n"
                  "10.Add Brand - Yangi brend yaratadi!\n"
                  "11.Add Color - Yangi rang kiritadi!\n"
                  "12.Add Employee - Yangi ishchi qo'shadi!\n"
                  "13.Add Order - Yangi buyurtma qo'shadi!")
        elif command == 'select models':
            named_tuple_base.show_models()
        elif command == 'select emails':
            named_tuple_base.show_emails()
        elif command == 'select customers':
            named_tuple_base.show_customers_count()
        elif command == 'select employees':
            named_tuple_base.show_employee_count()
        elif command == 'select brands':
            named_tuple_base.show_brands_count()
        elif command == 'select filtered brands':
            named_tuple_base.show_brands_filtered()
        elif command == 'select orders':
            named_tuple_base.show_orders()
        elif command == 'select sum models':
            named_tuple_base.show_models_price()
        elif command == 'select total brands':
            named_tuple_base.show_total_brands()
        elif command == 'add brand':
            brand_name = input("Qo'shish uchun brend nomini kiriting: ").title()
            if not brand_name.isalpha():
                print("Brend nomi faqat matndan iborat bo'lishi kerak!")
            else:
                db.input_brands(brand_name)
                print(f"{brand_name} brendi ma'lumotlar omboriga saqlandi!")
        elif command == 'add color':
            color_name = input("Qanday rang kiritmoqchisiz?: ").title()
            if not color_name.isalpha():
                print("Rang nomi faqat matndan iborat bo'lishi kerak!")
            else:
                db.input_colors(color_name)
                print(f"Yangi rang qo'shildi!: {color_name}")
        elif command == 'add employee':
            try:
                employee_id = int(input("Xodim uchun 4 xonalik id kiriting: "))
            except ValueError:
                print("ID uchun faqat sonlardan foydalaning!")
                continue

            first_name = input("Xodim uchun ism kiriting: ").title()
            last_name = input("Xodimning familiyasini kiriting: ").title()
            birth_date = input("Xodimning tug'ilgan sanasini kiriting (namuna: 1995-05-19): ")
            try:
                datetime.strptime(birth_date, date_format)
            except ValueError:
                print("Tug'ildan sanani ko'rsatilgan formatda kiriting!")
                continue

            phone_number = input("Xodimning telefon raqamini kiriting: ")
            if not phone_number.startswith("+998") and len(phone_number) == 13:
                print("Telefon raqam faqat +998 dan boshlanib 13 xonadan iborat bo'lishi kerak!")
                continue

            email = input("Xodimning e-pochta manzilini kiriting: ")
            if "@" and '.' not in email:
                print("Emailda @ hamda . belgilaridan biri mavjud emas!")
                continue

            country = input("Xodimning qaysi davlat fuqarosi?: ")
            city = input(f"Xodim {country} ning qaysi shahrida yashaydi?: ")
            db.input_employees(employee_id, first_name, last_name, birth_date, phone_number, email, country, city)
            print(f"Yangi xodim yaratildi!: {first_name} {last_name}")

        elif command == 'add order':
            print("\"Xaridorlar haqida ma'lumot\"")
            named_tuple_base.show_customers()
            try:
                customer_id = int(input("Yuqoridagi id lardan foydalanib xaridor id sini kiriting: "))
            except ValueError:
                print("ID uchun raqamlardan foydalaning!")
                continue

            print("\"Xodimlar haqida ma'lumot\"")
            named_tuple_base.show_employees()
            try:
                employee_id = int(input("Yuqoridagi id lardan foydalanib xodim id sini kiriting: "))
            except ValueError:
                print("ID uchun faqat raqamlardan foydalaning!")
                continue

            print("\"Modellar haqida ma'lumot\"")
            named_tuple_base.show_next_models()
            try:
                model_id = int(input("Yuqoridagi id lardan foydalanib model id sini kiriting: "))
            except ValueError:
                print("ID uchun faqat raqamlardan foydalaning!")
                continue

            car_count = int(input(f"{model_id} ushbu id dagi avtomildan nechta kerak: "))
            order_date = input("Xarid sanasini kiriting (2024-11-27 formatda bo'lsin): ")
            try:
                datetime.strptime(order_date, date_format)
            except ValueError:
                print("Formatni xato kiritdingiz!")
                continue

            db.input_orders(customer_id, employee_id, model_id, car_count, order_date)
            print("Xarid muvaffaqiyatli amalga oshirildi!")
        else:
            print("Nomalum buyruq kiritildi!")
