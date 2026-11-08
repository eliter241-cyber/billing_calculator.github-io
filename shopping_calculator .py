
total = 0
products = []

while True:
    product = input("Enter product name: ").strip()
   
    while True: 
       try:
            price = float(input("Enter the product price: "))

            if price > 0:
                print("The price accepted!")               
                break
            else:
                print("Invalid price!")

       except ValueError:
             print("Enter a valid price!")

    print("Price accepted:", price)

    while True: 
       try:
            quantity = float(input("Enter the quantity : "))

            if quantity > 0:
                print("The quantity accepted!")              
                break
            else:
                print("Invalid quantity!")

       except ValueError:
             print("Enter a valid quantity!")

    print("Quantity accepted:", quantity)

    

    subtotal = price * quantity
    total += subtotal
    products.append([product, price, quantity, subtotal])

    print("Product:", product)
    print("Subtotal:", subtotal)
    print("Running total:", total)

    next_choice = input("Do you want to continue? ").strip().lower()   
    
     
    if next_choice == "no":
        print("Okay! Here is your final bill.")
        break 


while True: 
       try:
            discount = float(input("Enter the discount rate (0-100): "))

            if discount > 0 and discount<100:
                print("The discount rate accepted!")     
                break
            else:
                print("Invalid discount rate!")

       except ValueError:
             print("Enter a valid discount rate!")

print("Discount rate accepted:", discount)
    



def bill():
    if 0 <= discount <= 100:
        discount_amount = total * discount / 100
        final_bill = total - discount_amount

        print("Total before discount:", total)
        print("Discount amount:", discount_amount)

        return final_bill

    else:
        print("Invalid discount")
        return total


final_bill = bill()

print("\n--Shopping Bill--")

for item in products:
    print(item[0], "-", item[1], "x", item[2], "=", item[3])

print("Total before discount:", total)
print("Final bill:", final_bill)



if final_bill >= 1000:
    is_member = input("Are you a member? ").strip().lower() == "yes"

    if is_member:
        print("Membership offer unlocked!")
        print("You can get a free watch or scent.")

        free = input("Which one do you want: watch or scent? ").strip().lower()

        if free in ("watch", "scent"):
            print("Congratulations! You got a", free)
        else:
            print("Wrong option.")
            free = input("Choose watch or scent: ").strip().lower()

            if free in ("watch", "scent"):
                print("Congratulations! You got a", free)
            else:
                print("Invalid choice. No gift selected.")
    else:
        print("Membership offer not available.")

print("THANK YOU FOR SHOPPING.")