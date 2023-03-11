coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input())

try:
	#your code goes here
	choice >= 0 and choice <= 5
	print(coffee[choice])
		
except:
	#and here
	print('Invalid number')
	
finally:
	#and finally here
	print('Have a good day')