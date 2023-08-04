name = "Keenan"

def checkName(name):
    answer = input("Is your name " + name + " ?")
	

    if answer.lower() == "yes":
        print ("Hello,", name)

    else:
        new_name = input("We're sorry about that. What is your name again? ") 
        print("Welcome,", new_name)

checkName("Keenan")
