print("1. Celcius to Farenheit")
print("2. Farenheit to Celcius")

choice = int(input("Choose an option [1 - 2]: "))

if choice == 1:
  cel = float(input("Enter value in Celcius: "))
  faren = (cel * 9 / 5) + 32
  print(faren, "° Farenheit")
elif choice == 2:
  faren = float(input("Enter value in Farenheit: "))
  cel = (faren - 32) * 5 / 9
  print(cel, "° Celcius")
else:
  print("Invalid Choice")