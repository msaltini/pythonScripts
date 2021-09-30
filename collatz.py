#This function prints the Collatz sequence of the inputted number
#Practice Project 1 from Chapter 3 in Automate the Boring Stuff

def collatz(number):
    if (number % 2) == 0:
        even = number / 2
        print(even)
        return even / 2
    else:
        odd = number * 3 + 1
        print(odd)
        return(odd)

num = input("Enter number:")
while num != 1:
    try:
        num = collatz(int(num))
    except ValueError:
        print("Must enter an integer")
        break

