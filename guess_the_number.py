#Guess the number game...
n=21  #this is my original number which is to be guessed by user
print("\nNUMBER GUESSING GAME")
print("\nTotal number of chances is:5\n")
chance_left=5  #set total no. of chances=5
while(chance_left!=0):
    #Take input from user
    num=int(input("\nEnter your number:"))
    if(num>n): #check if the entered number is greater than hidden number
        print("Your entered number is greater than hidden number.")
    elif(num<n): #check if the entered number is less than hidden number
        print("Your entered number is less than hidden number.")
    else: #it executes when user find hidden number
        print("Congrats!you successfully find the hidden number.")
        break
#to be continued.....