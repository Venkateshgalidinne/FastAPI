item = input("Enter the Items: ")
quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price: "))

subtotal = quantity * price 

if subtotal >= 10000:
    discount = subtotal * 20 / 100
elif subtotal >= 5000:
    discount = subtotal * 10 / 100
elif subtotal >= 2000:
    discount = subtotal * 5 / 100
else:
    discount = 0 

amount_after_discount = subtotal - discount

gst = amount_after_discount * 5/ 100

final_bill = amount_after_discount + gst

print("\n_______BILL________")
print("Item:",item)
print("Quantity:",quantity)
print("Price:",price)
print("Subtotal:",subtotal)
print("Discount:",discount)
print("GST:",gst)
print("FinalBill:",final_bill)