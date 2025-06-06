def main():
    print("-------------------------------")
    print("1. Celcius to Farenheit")
    print("2. Farenheit to Celcius")
    try:
        choice = int(input("Choose an option [1 - 2]: "))
        if choice == 1:
            celToFaren()
        elif choice == 2:
            farenToCel()
        else:
            print("Invalid Choice")
    except ValueError:
        print("Enter valid input")

def celToFaren():
    cel = float(input("Enter value in Celcius: "))
    faren = (cel * 9 / 5) + 32
    print(f"{faren}° Farenheit")

def farenToCel():
    faren = float(input("Enter value in Farenheit: "))
    cel = (faren - 32) * 5 / 9
    print(f"{cel}° Celcius")

while True:
    main()
    print("-------------------------------")
    print()

    option = input("Do you wish to quit [Yes(y)/No(n)]: ")
    if option == "Y" or option == "y":
        break