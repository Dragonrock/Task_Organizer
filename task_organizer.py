list= []
def main():
	number = input("How many tasks do you have to do? ")
	print ("Write the tasks one by one:")
	for i in range(int(number)):
		item = input()
		list.append(item)
	for i in range(len(list)+1):
		if len(list) == 0:
			print ("No more tasks")
		elif len(list) > 0:
			print ("You have to do " ,list[0])
			answer = input("Are you done? ")
			if answer.lower() == "yes":
				list.pop(0)
if __name__ == '__main__':
	main()