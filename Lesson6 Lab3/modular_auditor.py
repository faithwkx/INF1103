def get_valid_input(): 
    while True: 
        stock = input("Enter stock quantity or quit: ") 
 
        if stock == "quit": 
            return "quit" 
 
        elif stock.isdigit(): 
            return int(stock) 

        else: 
            return None 
 
 
def process_delivery(current_total, new_value): 
    current_total = current_total + new_value 
    return current_total 
 
 
def calculate_tax(amount): 
    tax = amount * 0.10 
    return tax 
 
 
def generate_report(total_deliveries, failed_attempts): 
    print("Total Deliveries Processed:", total_deliveries) 
    print("Number of Failed/Rejected Entries:", failed_attempts) 
 
 
inventory = 0 
deliveries = 0 
failed = 0 
 
while True: 
    stock = get_valid_input() 
 
    if stock == "quit": 
        break 
     
    if stock is None: 
        failed = failed + 1 
        continue 
 
    inventory = process_delivery(inventory, stock) 
    tax = calculate_tax(stock) 
 
    deliveries += 1 
 
    print("Delivery tax:", tax) 
    print("Current inventory:", inventory) 
 
generate_report(deliveries, failed)