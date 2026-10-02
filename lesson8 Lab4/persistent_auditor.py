import os


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


def load_inventory():
    file_path = os.path.join(os.path.dirname(__file__), "inventory.txt")

    try:
        file = open(file_path, "r")

        inventory_line = file.readline().strip()
        history_line = file.readline().strip()

        file.close()

        if inventory_line == "":
            inventory = 0
        else:
            inventory = int(inventory_line)

        if history_line == "":
            history = []
        else:
            history = history_line.split(",")

            for i in range(len(history)):
                history[i] = int(history[i])

        return inventory, history

    except FileNotFoundError:
        return 0, []


def save_inventory(inventory, history):
    file_path = os.path.join(os.path.dirname(__file__), "inventory.txt")

    file = open(file_path, "w")

    file.write(str(inventory) + "\n")

    for i in range(len(history)):
        file.write(str(history[i]))

        if i < len(history) - 1:
            file.write(",")

    file.close()


inventory, transaction_history = load_inventory()

deliveries = 0
failed = 0

print("Current inventory:", inventory)
print("Transaction history:", transaction_history)

while True:
    stock = get_valid_input()

    if stock == "quit":
        save_inventory(inventory, transaction_history)

        print("Inventory successfully saved to inventory.txt")

        break

    if stock is None:
        failed = failed + 1
        continue

    inventory = process_delivery(inventory, stock)

    transaction_history.append(stock)

    tax = calculate_tax(stock)

    deliveries = deliveries + 1

    print("Delivery tax:", tax)
    print("Current inventory:", inventory)
    print("Transaction history:", transaction_history)

generate_report(deliveries, failed)