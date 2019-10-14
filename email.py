urEM = input("What is your email address: ")
thrEM = input("Who are you sending email to: ")

print("\nfrom: " + urEM)
print("to: " + thrEM)
mess = input("Input message \n\n")
print("Do you wish to send: \n\n")
print("from: " + urEM)
print("to: " + thrEM)
print("\n" + mess + "\n")
ask = input("1. Yes\n2. No\n")
if(int(ask) == 1):
	print("Sent")
	f = open("email.txt", "a+")
	f.write(
	    "from: " + urEM + "\nto: " + thrEM + "\n" + mess + "\n"
	    )
	f.close()
else:
	print("Ok then.")