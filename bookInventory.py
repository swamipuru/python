def make_book_name_capitals(book):
	book_name = book.split(' ')
	book = ""
	for val in book_name:
		book += val[0].capitalize()+val[1:].lower() + " "
	return book[:-1]

def take_input_qty():
	flag = True
	while flag:
		try:
			number = input('Enter the qty: ')
			if int(number) > 0 :
				qty = int(number)
				flag = False
				return qty
			else:
				raise Exception
		except:
			print('Invalid input for qty.')

def take_input_price():
	flag = True
	while flag:
		try:
			number = input('Enter the price: ')
			num = number.split('.')
			if int(num[0]) > 0 and (len(num[1]) == 2):
				price = float(number)
				flag = False
				return  price
			else:
				raise Exception
		except:
			print('Invalid input for price.')

def calculateTotalAmount(theInventory):
	total_amt = 0.0
	for key in theInventory.keys():
		for book in theInventory[key]:
			total_amt += int(book[-2]) * float(book[-1])
	print('The total number of books is %2f'%(total_amt))

def totalQty(theInventory):
	total_num_of_books = 0
	for key in theInventory.keys():
		for book in theInventory[key]:
			total_num_of_books += int(book[-2])
	print('The total number of books is ',total_num_of_books)

def changeQty(theInventory):
	au_f_name = input('Enter the author\'s first name: ')
	au_l_name = input('Enter the author\'s last name: ')
	key = au_l_name[0].capitalize()+au_l_name[1:].lower()+", "+au_f_name[0].capitalize()+au_f_name[1:].lower()+","
	if key in theInventory.keys():
		book = input('Enter the title: ')
		book = make_book_name_capitals(book)
		#print('book ',book)
		avail_books = theInventory[key]
		books=[]
		for value in avail_books:
			books.append(value[0])
		if book in books:
			qty = int(take_input_qty())
			for bk in avail_books:
					if book == bk[0]:
						print('Qty will be updated from ',bk[-2],' to ',qty)
						bk[-2] = qty
		else:
			print('No book with the title ',book,' by ',key[:-1],' in inventory.')
	else:
		print('No such author in your database. So you cannot change the price.')

def changePrice(theInventory):
	au_f_name = input('Enter the author\'s first name: ')
	au_l_name = input('Enter the author\'s last name: ')
	key = au_l_name[0].capitalize()+au_l_name[1:].lower()+", "+au_f_name[0].capitalize()+au_f_name[1:].lower()+","
	if key in theInventory.keys():
		book = input('Enter the title: ')
		book = book[0].capitalize()+book[1:].lower()
		avail_books = theInventory[key]
		books=[]
		for value in avail_books:
			books.append(value[0])
		#print(books)
		if book in books:
			price = take_input_price()
			for bk in avail_books:
				if book == bk[0]:
					print('Price will be updated from ',bk[-1],' to ',price)
					bk[-1] = price
		else:
			print('No book with the title ',book,' by ',key[:-1],' in inventory.')
	else:
		print('No such author in your database. So you cannot change the price.')


def addBook(theInventory):
	au_f_name = input('Enter the author\'s first name: ')
	au_l_name = input('Enter the author\'s last name: ')
	key = au_l_name[0].capitalize()+au_l_name[1:].lower()+", "+au_f_name[0].capitalize()+au_f_name[1:].lower()+","
	#print('key is ',key)
	book = input('Enter the title: ')
	book = make_book_name_capitals(book)
	#print('book ',book)
	flag = True
	#check if book already in the inventory
	if key in theInventory.keys():
		avail_book = theInventory[key]
		flag = False
		for books in avail_book:
			#print('books [0] ',books[0])
			if book == books[0]:
				flag = True
		if flag:
			print('This book is already in the Inventory and cannot be added again.')
			return

	qty = take_input_qty()
	price = take_input_price()

	value = []
	value.append(book)
	value.append(qty)
	value.append(price)
	#print(value)
	theInventory.setdefault(key,[]).append(value)
	#print(key,'  ',theInventory[key])

def displayAuthorsWork(theInventory):
	au_f_name = input('Enter the author\'s first name: ')
	au_l_name = input('Enter the author\'s last name: ')
	key = au_l_name[0].capitalize()+au_l_name[1:].lower()+", "+au_f_name[0].capitalize()+au_f_name[1:].lower()+","
	#print('key is ',key)
	if key in theInventory.keys():
		book = sorted(theInventory[key])
		for books in book:
			print('\tThe title is: ',books[0])
			print('\tThe qty is: ',books[1])
			print('\tThe price is ',books[2])
			print('\t--------')
	else:
		print('Sorry, but no books by ',key[:-1],' in the inventory')

def displayInventory(theInventory):
	l = sorted(theInventory.keys())

	for key in l:
		print('The author is: ',key[:-1])
		book = sorted(theInventory[key])
		for books in book:
			print('\tThe title is: ',books[0])
			print('\tThe qty is: ',books[1])
			print('\tThe price is ',books[2])
			print('\t--------')

def printMenu():
	print("""-------------------------------
Enter 1 to display the inventory
Enter 2 to display the book by one author
Enter 3 to add a book
Enter 4 to change the price
Enter 5 to change the qty on hand
Enter 6 to view the total number of books in the inventory
Enter 7 to see the total amount of the entire inventory
Enter 8 to exit
		""")
	choice = input('Enter you choice: ')
	return str(choice)

def readDatabase(theInventory):
	while True:
		try:
			fileName = str(input("Enter the name of file: "))
			fileInput = open(fileName,'r+')
			for line in fileInput:
				line = line.split(',')
				key = line[0:-3]
				value = []
				for k in line[-3:]:
					value.append(k)
				temp_key = ""
				for k in key:
					temp_key += k+", "
				temp_key = temp_key[0:-1]
				if temp_key in theInventory.keys():
					#print('exist')
					theInventory[temp_key].append(value)
					#print(theInventory[ky])
				else:
					theInventory.setdefault(temp_key,[]).append(value)
			return
		except IOError:
			print("Error reading database")


def greeting():
	print('Welcome to the bookstore program')


def main():
	#print greeting
	greeting()
	#dictionary to hold the inventory
	theInventory ={}

	#put the data in the file into the dictionary
	readDatabase(theInventory)
	#print(theInventory)
	flag = True
	#keep looping till flag is set to False

	while flag:
		choice = printMenu()
		if choice == "1":
			displayInventory(theInventory)
		elif choice == "2":
			displayAuthorsWork(theInventory)
		elif choice == "3":
			addBook(theInventory)
		elif choice == "4":
			changePrice(theInventory)
		elif choice == "5":
			changeQty(theInventory)
		elif choice == "6":
			totalQty(theInventory)
		elif choice == "7":
			calculateTotalAmount(theInventory)
		elif choice == "8":
			print ("Thank you for using this program")
			flag = False
		else:
			print ("Invalid choice")

main()
