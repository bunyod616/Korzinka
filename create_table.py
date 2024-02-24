from Base import Database

def created_table():
    country_table = f"""
        CREATE TABLE country(
            country_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            last_update TIMESTAMP DEFAULT now());"""

    city_table = f"""
        CREATE TABLE city(
            city_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            country_id INT REFERENCES country(country_id),
            last_update TIMESTAMP DEFAULT now());"""

    address = f"""
        CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            city_id INT REFERENCES city(city_id),
            last_update TIMESTAMP DEFAULT now());"""

    store = f"""
        CREATE TABLE store(
            store_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            address_id INT REFERENCES address(address_id ),
            last_update TIMESTAMP DEFAULT now());"""

    customer = f"""
        CREATE TABLE customer(
            customer_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            last_update TIMESTAMP DEFAULT now());"""


    product = f"""
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            customer_id int REFERENCES customer(customer_id),
            product text,
            price int,
            last_update TIMESTAMP DEFAULT now());"""

    product_type = f"""
        CREATE TABLE product_type(
            product_type_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price FLOAT NOT NULL,
            product_id INT REFERENCES product(product_id),
            last_update TIMESTAMP DEFAULT now());"""

    PaymentType = f"""
        CREATE TABLE payment_type(
            payment_type_id serial PRIMARY KEY,
            customer_id int references customer(customer_id),
            name varchar(20),
            last_update TIMESTAMP DEFAULT now());
    """

    Payment = f"""
        CREATE TABLE payment(
            payment_id serial PRIMARY KEY,
            customer_id int references customer(customer_id),
            price smallint,
            payment_type_id int references payment_type(payment_type_id),
            last_update TIMESTAMP DEFAULT now());
    """

    CustomerPurchose = f"""
        CREATE TABLE CustomerPurchose(
            customer_purchose_id serial PRIMARY key,
            customer_id int references customer(customer_id),
            product_id int references product(product_id),
            last_update TIMESTAMP DEFAULT now());"""


    Saller= f"""
        CREATE TABLE saller(
            seller_id serial PRIMARY KEY,
            name varchar(20),
            store_id int references store(store_id),
            last_update TIMESTAMP DEFAULT now());"""



    # data_table = {
        # "country_table": country_table,
        # "city_table": city_table,
        # "adddress": address,
        # "store": store,
        # "customer": customer,
        # "product": product,
        # "product_type": product_type,
        # "payment_type": PaymentType,
        # "payment": Payment,
#         "CustomerPurchose": CustomerPurchose,
#         "Saller": Saller
#
#     }
#     for i in data_table:
#         print(f"{i} {Database.connect(data_table[i], 'create')}")
#
#
#
# if __name__ == "__main__":
#     created_table()
