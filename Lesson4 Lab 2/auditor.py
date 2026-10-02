inventory = 0
failed = 0

while True:
    stock = input("Enter stock quantity or quit: ")

    if stock == "quit":
        break

    elif stock.isdigit():
        stock = int(stock)
        inventory = inventory + stock

        if inventory > 500:
            print("Overstock Alert!")
            break

    else:
        print("Invalid input")
        failed = failed + 1

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed)