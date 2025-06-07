def main():
    print("-------------------------------")
    print("1. Celcius to Farenheit")
    print("2. Farenheit to Celcius")
    print("3. Celcius to Kelvin")
    print("4. Kelvin to Celcius")
    print("5. Farenheit to Kelvin")
    print("6. Kelvin to Farenheit")

    def conditionalChoice():
        choice = int(input("Choose an option [1 - 6]: "))
        if choice == 1:
            celToFaren()
        elif choice == 2:
            farenToCel()
        elif choice == 3:
            celToKel()
        elif choice == 4:
            kelToCel()
        elif choice == 5:
            farenToKel()
        elif choice == 6:
            kelToFaren()
        else:
            print("Invalid Choice!")

    try:
        conditionalChoice()
    except ValueError:
        print("Enter valid input")

def celToFaren():
    cel = float(input("Enter value in Celcius: "))
    faren = (cel * 9 / 5) + 32
    print(f"{faren:.2f}° Farenheit")

def farenToCel():
    faren = float(input("Enter value in Farenheit: "))
    cel = (faren - 32) * 5 / 9
    print(f"{cel:.2f}° Celcius")

def celToKel():
    cel = float(input("Enter value in Celcius: "))
    kel = cel + 273.15
    print(f"{kel:.2f}° Kelvin")

def kelToCel():
    kel = float(input("Enter value in Kelvin: "))
    cel = kel - 273.15
    print(f"{cel:.2f}° Celcius")

def farenToKel():
    faren = float(input("Enter value in Farenheit: "))
    kel = (faren - 32) / 1.8 + 273.15
    print(f"{kel:.2f}° Kelvin")

def kelToFaren():
    kel = float(input("Enter value in Kelvin: "))
    faren = (kel - 273.15) * 1.8 + 32
    print(f"{faren:.2f}° Farenheit")

while True:
    main()
    print("-------------------------------")
    print()

    option = input("Do you wish to quit [Yes(y)/No(n)]: ")
    if option == "Y" or option == "y":
        break