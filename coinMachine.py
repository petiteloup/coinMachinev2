
cash = int(input())
print("Amount received: " + str(cash))

price = int(input())
print("Price of the item: " + str(price))

amount = cash - price
print("Required change: " + str(amount))
toonies = amount // 200
amount %= 200
print("Toonies x " + str(toonies))
loonies = amount // 100
amount %= 100
print("Loonies x " + str(loonies))
quarters = amount // 25
amount %= 25
print("Quarters x " + str(quarters))
dimes = amount // 10
amount %= 10
print("Dimes x " + str(dimes))
nickels = amount // 5
amount %= 5
print("Nickels x " + str(nickels))
print("Have a good day!")
