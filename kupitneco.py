apples = 0

bananas = 0

oranges = 0

print("welcome to the shopping list program")

print("these are the items you can buy: ")

print("- apples for 100")

print("- bananas for 150")

print("- oranges for 200")

budget = int(input("enter your shopping budget: "))

if budget <= 0:
	print("Budget cannot be negative or zero")
	exit()

while budget > 99:

	item = str(input("select an item from the list: "))

	if item == "apples":
		if budget >= 100:
			print(f"you bought 1 apple, your current budget is: {budget-100}")
			budget = budget - 100
			apples = apples + 1
		else:
			print("you can't buy apple because your budget is low")

	elif item == "bananas":
		if budget >= 150:
			print(f"you bought 1 banana, your current budget is: {budget-150}")
			budget = budget - 150
			bananas = bananas + 1
		else:
			print("you can't buy banana because your budget is low")

	elif item == "oranges":
		if budget >= 200:
			print(f"you bought 1 orange, your current budget is: {budget-200}")
			budget = budget - 200
			oranges = oranges + 1
		else:
			print("you can't buy orange because your budget is low")

	print(f"You have: {apples} apples, {bananas} bananas, {oranges} oranges")

	if budget < 100:
		print("Your budget is low, you can't buy any more items")
