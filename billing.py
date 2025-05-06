# Printing a welcome message for the user #
print ("Welcome to the Rollercoaster")
#asking user for their height #
height=int(input("what is your height in cm? "))
bill=0
#checking whether their height is atleast 120 cm #
if height >=120:
    print("You can ride the roller coaster")
    # Asking user for their age and telling them their ticket type #
    age=int(input("What is your age? "))
    if age<=12:
        bill=5
        print("Child tickets are $5\n")
    elif age <=18:
        bill=7
        print("Teen tickets are $7\n")
    else:
        bill=12
        print("Adult tickets are $12\n")
        # Asking user whether they want a photo ticket or not #
    wants_photo=input("Do you want a photo ticket?If yes type Y If no type \n")
    if wants_photo=="Y":
        bill +=3
        # Printing their final bill#
        print(f"Your final bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride")


