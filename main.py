from classes import Country, City, Address,Store,Customer,Product,ProductType,PaymentType,Payment,CustomerPurchose,Saller



def services_country():
    services = input("""
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. Back
            >>> """)

    if services == "1":
        for i in Country.select("country"):
            print(i)
        return services_country()

    elif services == "2":
        name = input("Name: ")
        country = Country(name)
        print(country.insert("country"))

        return services_country()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "country_id":
            print(Country.delete(column, data, 'country'))

        else:
            print(Country.delete_id(column, data, 'country'))

        return services_country()

    elif services == "4":
        country = input("New Country: ")
        id = int(input("Old Country ID: "))
        query = f"""UPDATE country SET name = '{country}' WHERE country_id = {id};"""
        print(Country.update(query))
        return services_country()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return services_country()

def services_city():
    services = input("""
            1. Select
            2. Insert
            3. Delete
            4. Update
            0. Back
                >>> """)

    if services == "1":
        for i in City.select("city"):
            print(i)
        return services_city()

    elif services == "2":
        name = input("Name: ")
        country_id = int(input("Country ID: "))
        city = City(name, country_id)
        print(city.insert("city"))

        return services_city()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "city_id":
            print(City.delete(column, data, 'city'))

        else:
            print(City.delete_id(column, data, 'city'))

        return services_city()

    elif services == "4":
        city = input("New City: ")
        id = int(input("Old City ID: "))
        query = f"""UPDATE city SET name = '{city}' WHERE city_id = {id};"""
        print(City.update(query))
        return services_city()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return services_city()


def services_address():
    services = input("""
                1. Select
                2. Insert
                3. Delete
                4. Update
                0. Back
                    >>> """)

    if services == "1":
        for i in Address.select("address"):
            print(i)
        return services_address()

    elif services == "2":
        name = input("Name: ")
        city_id = int(input("City ID: "))
        address = Address(name,city_id)
        print(address.insert("address"))

        return services_address()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "address_id":
            print(Address.delete(column, data, 'address'))

        else:
            print(Address.delete_id(column, data, 'address'))

        return services_address()

    elif services == "4":
        address = input("New Address: ")
        id = int(input("Old Address ID: "))
        query = f"""UPDATE address SET name = '{address}' WHERE address_id = {id};"""
        print(Address.update(query))
        return services_address()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return services_address()

def services_store():
    services = input("""
                1. Select
                2. Insert
                3. Delete
                4. Update
                0. Back
                    >>> """)

    if services == "1":
        for i in Store.select("store"):
            print(i)
        return services_store()

    elif services == "2":
        name = input("Name: ")
        address = int(input("address ID: "))
        store = Address(name,address)
        print(store.insert("address"))

        return services_store()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "store_id":
            print(Store.delete(column, data, 'store'))

        else:
            print(Store.delete_id(column, data, 'store'))

        return services_store()

    elif services == "4":
        store = input("New Store: ")
        id = int(input("Old Store ID: "))
        query = f"""UPDATE store SET name = '{store}' WHERE store_id = {id};"""
        print(Store.update(query))
        return services_store()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return services_store()


def services_customer():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in Customer.select("customer"):
            print(i)
        return services_customer()

    elif services == "2":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        customer = Customer(first_name,last_name)
        print(customer.insert("customer"))

        return services_customer()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "customer_id":
            print(Customer.delete(column, data, 'customer'))

        else:
            print(Customer.delete_id(column, data, 'customer'))

        return services_customer()

    elif services == "4":
        first_name = input("New First Name: ")
        last_name = input("New Last Name: ")
        id = int(input("Old Customer ID: "))
        query = f"""UPDATE customer SET first_name = '{first_name}',last_name = '{last_name}' WHERE customer_id = {id};"""
        print(Customer.update(query))
        return services_customer()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return services_customer()

def services_product():
    services = input("""
                1. Select
                2. Insert
                3. Delete
                4. Update
                0. Back
                    >>> """)

    if services == "1":
        for i in Product.select("product"):
            print(i)
        return services_product()

    elif services == "2":
        customer_id = input("Customer Id: ")
        product = input("Product: ")
        price = input("Price: ")
        product = Product(customer_id,product,price)
        print(product.insert("product"))

        return services_product()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "product_id":
            print(Product.delete(column, data, 'product'))

        else:
            print(Product.delete_id(column, data, 'product'))

        return services_product()

    elif services == "4":
        customer_id = input("New Customer ID: ")
        product = input("New Product : ")
        price = input("New Price : ")
        id = int(input("Old Product ID: "))
        query = f"""UPDATE customer SET customer_id = '{customer_id}',product = '{product}',price = '{price}' WHERE product_id = {id};"""
        print(Product.update(query))
        return services_product()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return services_product()


def services_product_type():
    services = input("""
                 1. Select
                 2. Insert
                 3. Delete
                 4. Update
                 0. Back
                     >>> """)

    if services == "1":
        for i in ProductType.select("product_type"):
            print(i)
        return services_product_type()

    elif services == "2":
        name = input("Name: ")
        price = input("Price: ")
        product_id = input("Product ID: ")
        product = ProductType(name, price, product_id)
        print(product.insert("product_type"))

        return services_product_type()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "product_type_id":
            print(ProductType.delete(column, data, 'product_type'))

        else:
            print(ProductType.delete_id(column, data, 'product_type'))

        return services_product_type()

    elif services == "4":
        name = input("New Name: ")
        price = input("New Price")
        product_id = input("New Product ID")
        id = int(input("Old Product Type ID: "))
        query = f"""UPDATE product_type SET name = '{name}',price = '{price}',product_id = '{product_id}' WHERE product_type_id = {id};"""
        print(ProductType.update(query))
        return services_product_type()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return services_product_type()

def payment_type():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in PaymentType.select("payment_type"):
            print(i)
        return payment_type()

    elif services == "2":
        customer_id = input("customer_id: ")
        name = input("name: ")
        completed = PaymentType(customer_id,name)
        print(completed.insert("payment_type"))

        return payment_type()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "payment_type_id":
            print(PaymentType.delete(column, data, 'payment_type'))

        else:
            print(PaymentType.delete_id(column, data, 'payment_type'))

        return payment_type()

    elif services == "4":
        customer_id = input("New customer id: ")
        name = input("New name: ")
        id = int(input("Old payment type ID: "))
        query = f"""UPDATE payment_type SET customer_id = '{customer_id}',name = '{name}' WHERE payment_type_id = {id};"""
        print(PaymentType.update(query))
        return payment_type()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return payment_type()

def payment():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in Payment.select("payment"):
            print(i)
        return payment()

    elif services == "2":
        customer_id = input("customer_id: ")
        price = input("price: ")
        payment_type_id = input("payment_type_id: ")
        completed = Payment(customer_id,price,payment_type_id)
        print(completed.insert("payment"))

        return payment()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "payment_id":
            print(Payment.delete(column, data, 'payment'))

        else:
            print(Payment.delete_id(column, data, 'payment'))

        return payment()

    elif services == "4":
        customer_id = input("New customer id: ")
        price =input("New price: ")
        id = int(input("Old payment type ID: "))
        query = f"""UPDATE payment SET customer_id = '{customer_id}',price = '{price}' WHERE payment_id = {id};"""
        print(Payment.update(query))
        return payment()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return payment()

def customer_purchose():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in CustomerPurchose.select("CustomerPurchose"):
            print(i)
        return customer_purchose()

    elif services == "2":
        customer_id = input("customer_id: ")
        product_id = input("product_id: ")
        completed = CustomerPurchose(customer_id,product_id,services)
        print(completed.insert("CustomerPurchose"))

        return payment()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "customer_purchose_id":
            print(CustomerPurchose.delete(column, data, 'CustomerPurchose'))

        else:
            print(CustomerPurchose.delete_id(column, data, 'CustomerPurchose'))

        return payment()

    elif services == "4":
        customer_id = input("New customer id: ")
        product_id =input("New product id: ")
        id = int(input("Old customer purchose type ID: "))
        query = f"""UPDATE CustomerPurchose SET customer_id = '{customer_id}',product-id = '{product_id}' WHERE customer_purchose_id = {id};"""
        print(CustomerPurchose.update(query))
        return payment()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return payment()

def saller():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in Saller.select("saller"):
            print(i)
        return saller()

    elif services == "2":
        name = input("Enter name")
        store_id = input("store idd: ")
        completed = Saller(name, store_id)
        print(completed.insert("saller"))

        return payment()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "saller_id":
            print(Saller.delete(column, data, 'saller'))

        else:
            print(Saller.delete_id(column, data, 'saller'))

        return saller()

    elif services == "4":
        name = input("New name : ")
        store_id =input("New Store_id: ")
        id = int(input("Old saller  ID: "))
        query = f"""UPDATE saller SET name = '{name}',store_id = '{store_id}' WHERE saller_id = {id};"""
        print(Saller.update(query))
        return saller()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return saller()
def main():
    tables = input("""
       1. Country
       2. City 
       3. Adddress 
       4. Store
       5. Customer
       6. Product
       7. Product Type
       8. Payment Type
       9. Payment
       10. Customer Purchose
       11. Saller
            >>> """)

    if tables == "1":
        return services_country()

    elif tables == "2":
        return services_city()

    elif tables == "3":
        return services_address()

    elif tables == "4":
        return services_store()

    elif tables == "5":
        return services_customer()

    elif tables == "6":
        return services_product()

    elif tables == "7":
        return services_product_type()

    elif tables == "8":
        return payment_type()

    elif tables == "9":
        return payment()

    elif tables == "10":
        return customer_purchose()

    elif tables == "11":
        return saller()

    else:
        print("Invalid")
        return main()


if __name__ == "__main__":
    main()