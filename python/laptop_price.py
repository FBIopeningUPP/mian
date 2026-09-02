first_price = int(input("Enter the price of the first laptop in rupees: "))
second_price = int(input("Enter the price of the second laptop: "))

print("Sum:", first_price + second_price)
print("Difference:", first_price - second_price)

is_first_cheaper = first_price < second_price
print(is_first_cheaper)

if is_first_cheaper:
    print("Yes, the first laptop is cheaper.")
else:
    print("No, the first laptop is not cheaper.")
