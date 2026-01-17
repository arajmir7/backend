price = float(input("Enter product price: "))
gst_rate = float(input("Enter GST percentage: "))

gst_amount = (price * gst_rate) / 100
final_price = price + gst_amount

print("GST Amount:", gst_amount)
print("Final Price:", final_price)
