bot_name = "Stan"
year = "2020"

# 1
print("Hello! My name is {}.".format(bot_name))
print("I was created in {}.".format(year))

# 2
print("Please, remind me your name.")
user = input()
print("What a great name you have, {}!".format(user))
print("Let me guess your age.")

# 3
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

predicted_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is {}; that's a good time to start programming!".format(predicted_age))

# 4
print("Now I will prove to you that I can count to any number you want.")
counter = int(input().strip())
for i in range(counter + 1):
    print("{} !".format(i))
print("Completed, have a nice day!")

# 5
print("Let's test your programming knowledge.")
print("Why do we use methods?")
quiz = [
    "1. To repeat a statement multiple times.",
    "2. To decompose a program into several small subroutines.",
    "3. To determine the execution time of a program.",
    "4. To interrupt the execution of a program.",
]

for question in quiz:
    print(question)
right = 2
completed = False

error = "Please, try again."
success = "Completed, have a nice day!"

while not completed:
    answer = int(input().strip())
    if answer == right:
        completed = True
        print(success)
        break

    print(error)

print("Congratulations, have a nice day!")
