from Base import Database


class Country:
    def __init__(self, name):
        self.name = name


    @staticmethod
    def select(table="country"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="country"):
        query = f"""INSERT INTO {table}(name) VALUES('{self.name}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="country"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="country"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

class City(Country):
    def __init__(self, name ,country_id):
        super().__init__(name)
        self.country_id = country_id

    def select(table="city"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")
    def insert(self, table="city"):
        query = f"""INSERT INTO {table}(name, country_id) VALUES('{self.name}',' {self.country_id}')"""
        return Database.connect(query, "insert")

    def delete(column, data, table="city"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, data, table="city"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    def update(query):
        return Database.connect(query, "update")

class Address(Country):
    def __init__(self, name, city_id):
        super().__init__(name)
        self.city_id = city_id

    def select(table="address"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")
    def insert(self, table="address"):
        query = f"""INSERT INTO {table}(name, city_id) VALUES('{self.name}', '{self.city_id}')"""
        return Database.connect(query, "insert")

    def delete(column, data, table="address"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, data, table="address"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    def update(query):
        return Database.connect(query, "update")

class Store(Address):
    def __init__(self, name, address):
        super().__init__(name,address)

    def select(table="store"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="store"):
        query = f"""INSERT INTO {table}(name, address_id) VALUES('{self.name}', '{self.address_id}')"""
        return Database.connect(query, "insert")

    def delete(column, data, table="store"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, data, table="store"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    def update(query):
        return Database.connect(query, "update")

class Customer:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name


    def insert(self, table="customer"):
        query = f"""INSERT INTO {table}(first_name,last_name) VALUES('{self.first_name}','{self.last_name}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table="customer"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class Product:
    def __init__(self, customer_id, product, price):
        self.customer_id = customer_id
        self.product = product
        self.price = price

    def select(table="product"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="product"):
        query = f"""INSERT INTO {table}(customer_id,product,price) VALUES('{self.customer_id}', '{self.product}','{self.price}')"""
        return Database.connect(query, "insert")

    def delete(column, data, table="product"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, data, table="product"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    def update(query):
        return Database.connect(query, "update")

class ProductType:
    def __init__(self, name, price,product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

    def select(table="product_type"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="product_type"):
        query = f"""INSERT INTO {table}(name,price,product_id) VALUES('{self.name}','{self.price}','{self.product_id}')"""
        return Database.connect(query, "insert")

    def delete(column, data, table="product_type"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, data, table="product_type"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    def update(query):
        return Database.connect(query, "update")

class PaymentType:
    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name

    def insert(self, table="payment_type"):
        query = f"""INSERT INTO {table}(customer_id,name) VALUES('{self.customer_id}', '{self.name}')"""
        return Database.connect(query, "insert")

    def select(table="payment_type"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class Payment:
    def __init__(self,customer_id,price,payment_type_id):
        self.customer_id = customer_id
        self.price = price
        self.payment_type_id = payment_type_id

    def insert(self, table="payment"):
        query = f"""INSERT INTO {table}(customer_id,price,payment_type_id) VALUES('{self.customer_id}','{self.price}','{self.payment_type_id}')"""
        return Database.connect(query, "insert")

    def select(table="payment"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class CustomerPurchose:
    def __init__(self,customer_id,product_id):
        self.customer_id = customer_id
        self.product_id = product_id

    def insert(self, table="CustomerPurchose"):
        query = f"""INSERT INTO {table}(customer_id,product_id) VALUES('{self.customer_id}', '{self.product_id}')"""
        return Database.connect(query, "insert")

    def select(table="CustomerPurchose"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class Saller:
    def __init__(self,customer_id,product_id):
        self.customer_id = customer_id
        self.product_id = product_id

    def insert(self, table="CustomerPurchose"):
        query = f"""INSERT INTO {table}(customer_id,product_id) VALUES('{self.customer_id}', '{self.product_id}')"""
        return Database.connect(query, "insert")

    def select(table="CustomerPurchose"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")