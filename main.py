#This program is damaged :(


email=input("enter email")
if "@" in email and "." in email:
	user_name=email.split("@")[0]
	domen=email.split(".")[1]
	
	if user_name is not None and domen is not None:
		print("address is valid")
else:
	print("adress is not valid")
