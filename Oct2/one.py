def listSum():
	a_list = [8, 2, 3, -1, 7]

	counter = 1
	print("Star:", counter ) 
	
	for number in a_list:
		# print(number)
		counter *= number
		print("Now counter is: ", counter)

	print("Total:", counter)

	

listSum()
