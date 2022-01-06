sum = 0
item_price = []
item_name = []
Bill=[]
while True:
	userInput = input("Enter the item price or press q to quit: \n")
	if userInput != 'q':
		item_price.append(userInput)
	else:
		break
	if userInput != 'q':
		sum = sum + int(userInput)
		print(f"Order total so far: {sum}")
	else:
		print(f"Your Bill total is {sum}. Thanks for shopping with us")
		break

print(f"price per object is {item_price}")

while True:
	ValueInput = input("Enter the items in order of price and press q to generate bill : ")
	if ValueInput!= 'q':
		item_name.append(ValueInput)
	else:
		for (item1, item2) in zip(item_price, item_name):
			Bill.append(item2 + ' = RS ' + item1)

		print(f"Your Bill is : {Bill}")
		break

