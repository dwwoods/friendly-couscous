#for loops iterate over a collection, like strings
#[] a list - strings, intergers etc

#for item in ["David", "Paul", 'Mark']:
 #   print(item)

#for item in range(5,10, 2): #(start, end, steps)
    #print(item)

cart_prices = [20, 30, 40, 50]
total = 0
for cart_price in cart_prices:
    total += cart_price
print(f"Total: {total}")