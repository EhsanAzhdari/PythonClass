import qrcode

PRODUCTS = []

def read_from_database():
    f = open("database.txt", "r")
    for line in f:
        result = line.split(",")
        my_dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
        PRODUCTS.append(my_dict)
    f.close

def write_to_database():
    f = open("database.txt", "w")
    for product in PRODUCTS:
        f.write(f"{product['code']},{product['name']},{product['price']},{product['count']}\n")
    f.close()

def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- QR Code")
    print("8- Exit")

def add():
    code = input("Enter Code: ")
    name = input("Enter Name: ")
    price = input("Enter Price: ")
    count = input("Enter Count: ")
    new_product = {'code': code, 'name': name, 'price': price, 'count': count}
    PRODUCTS.append(new_product)

def edit():
    user_input = input("Enter Code: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            while True:
                print("Select Field for Edit: ")
                print("1- Name")
                print("2- Price")
                print("3- Count")
                choice = int(input("Enter Number: "))
                if choice == 1:
                    new_name = input("Enter New Name: ")
                    product["name"] = new_name
                    break
                elif choice == 2:
                    new_price = input("Enter New Price: ")
                    product["price"] = new_price
                    break
                elif choice == 3:
                    new_count = input("Enter New Count: ")
                    product["count"] = new_count
                    break
                else:
                    print("mese adam vared kon :|")
            print("PRODUCT Edit Successfully..")
            break
    else:
        print("not found")
    
    
def remove():
    user_input = input("Enter Code: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            PRODUCTS.remove(product)
            print("PRODUCT Remove Successfully..")
            break
    else:
        print("not found")
    
def search():
    user_input = input("type your keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])
            break
    else:
        print("not found")

def show_list():
    print("code\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"])
    
def buy():
    Cart = []
    while True:
        user_input = input("Enter Code OR type 'EXIT': ")
        if user_input == "EXIT":
            break
        for product in PRODUCTS:
            if product["code"] == user_input:
                user_count = input("Enter the Quantity you want to buy: ")
                if int(product["count"]) >= int(user_count):
                    product["count"] = str(int(product["count"]) - int(user_count))
                    user_dict = {"code": product["code"], "name": product["name"], "price": product["price"], "count": user_count}
                    Cart.append(user_dict)
                    break
                else:
                    print("The Quantity you want is not available!")
                    break
        else:
            print("not found")
            
    if len(Cart) != 0:
        Sum_Price = 0
        for product in Cart:
            print(f"NAME: {product['name']}  COUNT: {product['count']}  PRICE: {product['price']}")
            Sum_Price = Sum_Price + int(product["price"])*int(product["count"])
        print("You Should PAY: ", Sum_Price)
    else:
        print("Your Cart is Empty!")
        
def QR_Code():
    user_input = input("Enter Code: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            QR = qrcode.make(f"Code: {product['code']} | Name: {product['name']} | Price: {product['price']} | Count: {product['count']}")
            QR.save(f"{product['name']}.jpg")
            print("PRODUCT QR Code Generate Successfully..")
            break
    else:
        print("not found")
    

print("Welcome to EHSAN Store")
print("Loading...")
read_from_database()
print("Data loaded.")

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        QR_Code()
    elif choice == 8:
        write_to_database()
        exit(0)
    else:
        print("mese adam vared kon :|")
    
