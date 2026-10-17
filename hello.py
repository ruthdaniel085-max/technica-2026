print("================================")
print(" TECH INTEREST FINDER")
print("================================")

name = input("What is your name? ")

print("\nChoose your favorite area:")
print("1. Artificial Intelligence")
print("2. Web Development")
print("3. Cybersecurity")
print("4. Data Science")

choice = input("Enter a number from 1 to 4: ")

if choice == "1":
    area = "Artificial Intelligence"
elif choice == "2":
    area = "Web Development"
elif choice == "3":
    area = "Cybersecurity"
elif choice == "4":
    area = "Data Science"
else:
    area = "an area you will discover"

print("\nHello, " + name + "!")
print("Your technology interest is " + area + ".")
print("Keep learning and building!")
