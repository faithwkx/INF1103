

# # Function Arguments 
# def greet(name):
#     print("Hello, " + name + "!")

# greet("Alice")

# #Positional Arguments
# def create_order(customer, product, quantity):
#     print(customer, "ordered", quantity, product)

# create_order("Bob", "Apples", 5)
# create_order("Charlie", "Bananas", 10)

# # #Keyword Arguments
# def create_order(customer, product, quantity):
#     print(customer, "ordered", quantity, product)

# create_order(customer="Bob", product="Apples", quantity=5)
# create_order(quantity=2, product="Oranges", customer="Charlie")

# #Calculate Final Order Price
# def calculate_total(price):
#     discount = price * 0.10
#     subtotal = price - discount
#     gst = subtotal * 0.09
#     return subtotal + gst

# print(calculate_total(20))
# print(calculate_total(50))
# print(calculate_total(100))

# #Tuple
# numbers = (10, 20, 30)
# print(numbers)

# firstRank, secondRank, thirdRank = numbers
# print(firstRank)

# # Function return values
# def calculate_discount(price):
#     discount = price * 0.10
#     return discount

# #This is a tuple!
# def calculate(a,b):
#     return a+b, a*b
# sum_value, product_value = calculate(4,5)
# print("Sum:", sum_value)
# print("Product:", product_value)

# #Function Arguments including *args
# def calculate_total(*prices):
#     print(prices)

# print(calculate_total(20,15,30))
# print(calculate_total(50,100,200,300))

# #Scope of a variable 
# def calculate_discount(price):
#     discount = price * 0.10
#     return discount

# #Setting a value for discount variable in the global scope

# # while True:
# #     discount = input("Enter a price (or 'q' to quit): ")
# #     if discount.lower() == 'q':
# #         break
# #     else:
# #         discount = calculate_discount(float(discount))
# #         print("Discount:", discount)


# print(calculate_discount(100))
# print(discount)  # This will raise an error because 'discount' is not defined in this scope

# #Task for the day!! Parking-charge system

# def calculate_parking_charge(hours):
#     if hours <=2:
#         return None
#     elif hours >= 2:
#         charge = (hours - 2) * 2
#         return charge

# hours = float(input("Enter the number of hours parked: "))
# charge = calculate_parking_charge(hours)
# if charge is not None:
#     print("Parking Charge:", charge)
# else:
#     print("No charge for the first 2 hours.")


