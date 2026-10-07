import datetime
import math
import random


def run_program_1():
    print("--- Program 1: Print Hello World ---")
    print("Hello World")


def run_program_2():
    print("--- Program 2: Print Hello + Username ---")
    usertext = input("What is your name? ")
    print("Hello", usertext)


def run_program_3():
    print("--- Program 3: Add 2 Numbers ---")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    total_sum = float(num1) + float(num2)
    print("The sum of {0} and {1} is {2}".format(num1, num2, total_sum))


def run_program_4():
    print("--- Program 4: Average of 2 Numbers ---")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    average = (float(num1) + float(num2)) / 2
    print("average: {0}".format(average))


def run_program_5():
    print("--- Program 5: Visa and Final Grade Average ---")
    visagrade = input("enter your visa grade: ")
    finalgrade = input("enter your final grade: ")
    average = (float(visagrade) * 0.3) + (float(finalgrade) * 0.7)
    print("average : {0} ".format(average))


def run_program_6():
    print("--- Program 6: Average of 3 Written Grades ---")
    firstexam = input("your first exam: ")
    secondexam = input("your second exam: ")
    thirdexam = input("your third exam: ")
    average = (float(firstexam) + float(secondexam) + float(thirdexam)) / 3
    print("average: {0} ".format(average))


def run_program_7():
    print("--- Program 7: Class Pass Status ---")
    average = input("enter average : ")
    if int(average) >= 50:
        print("Passed")
    else:
        print("Failed")


def run_program_8():
    print("--- Program 8: Odd or Even ---")
    num = int(input("Enter a number: "))
    if (num % 2) == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))


def run_program_9():
    print("--- Program 9: Positive, Negative, or 0 ---")
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")


def run_program_10():
    print("--- Program 10: Body Mass Index (BMI) ---")
    print("body mass index calculation program")
    height = float(input("enter height (m):"))
    weight = int(input("enter weight (kg):"))

    index = weight / (height * height)

    if index <= 18:
        print("\n underweight BMİ:{}".format(index))
    elif index > 18 and index <= 25:
        print("\n normal weight BMİ:{}".format(index))
    elif index > 25 and index <= 30:
        print("\n obese BMİ: {}".format(index))
    elif index > 30:
        print("\n severely obese BMİ: {}".format(index))


def run_program_11():
    print("--- Program 11: Driver's License Eligibility ---")
    age = input("enter age: ")
    if int(age) < 18:
        print("Your Age Is Not Eligible To Get A Driver's License")
    else:
        print("Your Age Is Eligible To Get Your License")


def run_program_12():
    print("--- Program 12: List Numbers 1-100 ---")
    for i in range(1, 101):
        print(i)


def run_program_13():
    print("--- Program 13: List Even Numbers 1-100 ---")
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)


def run_program_14():
    print("--- Program 14: List Odd Numbers 1-100 ---")
    for i in range(1, 101):
        if i % 2 != 0:
            print(i)


def run_program_15():
    print("--- Program 15: Numbers Divisible by 3 and 5 (1-100) ---")
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            print(i)


def run_program_16():
    print("--- Program 16: List Numbers from 1 to User Input ---")
    num = input("enter number: ")
    for i in range(1, int(num) + 1):
        print(i)


def run_program_17():
    print("--- Program 17: Area and Perimeter of a Rectangle ---")
    short = input("Enter short side: ")
    tall = input("Enter tall side: ")
    area = int(short) * int(tall)
    perimeter = 2 * (int(short) + int(tall))
    print("area: {0}".format(area))
    print("perimeter: {0}".format(perimeter))


def run_program_18():
    print("--- Program 18: Print Letters Vertically ---")
    word = "mrhuseyin"
    for char in word:
        print(char)


def run_program_19():
    print("--- Program 19: Sum of Numbers Between Two Inputs ---")
    sumofnumbers = 0
    num1 = input("first number: ")
    num2 = input("second number: ")
    for i in range(int(num1) + 1, int(num2)):
        sumofnumbers += i
    print(
        "Sum of numbers between {0} and {1} : {2}".format(
            num1, num2, sumofnumbers
        )
    )


def run_program_20():
    print("--- Program 20: Cinema or Theater Ticket Fee ---")
    selection = input("Press (1) for Cinema, (2) for Theater: ")
    student = input("Are you student (Y/N): ")
    price = 0
    if selection == "1":
        price = 10
    elif selection == "2":
        price = 5
    if student == "Y" or student == "y":
        price = price / 2
    print(" The fee you have to pay : {}".format(price))


def run_program_21():
    print("--- Program 21: Prime Number Checker ---")
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


def run_program_22():
    print("--- Program 22: Sum of Odd and Even Numbers in a List ---")
    NumList = []
    Even_Sum = 0
    Odd_Sum = 0
    Number = int(input("Please enter the Total Number of List Elements: "))
    for i in range(1, Number + 1):
        value = int(input("Please enter the Value of %d Element: " % i))
        NumList.append(value)
    for j in range(Number):
        if NumList[j] % 2 == 0:
            Even_Sum = Even_Sum + NumList[j]
        else:
            Odd_Sum = Odd_Sum + NumList[j]
    print("\nThe Sum of Even Numbers in this List = ", Even_Sum)
    print("The Sum of Odd Numbers in this List = ", Odd_Sum)


def run_program_23():
    print("--- Program 23: Raised Salary Calculation ---")
    salary = input("enter new salary: ")
    raise_rate = input("salary raise rate(%): ")
    newsalary = int(salary) + (int(salary) * int(raise_rate) / 100)
    print("increased salary:", newsalary)


def run_program_24():
    print("--- Program 24: Circle Calculations Using Functions ---")

    def find_Diameter(radius):
        return 2 * radius

    def find_Circumference(radius):
        return 2 * math.pi * radius

    def find_Area(radius):
        return math.pi * radius * radius

    r = float(input("Please Enter the radius of a circle: "))
    diameter = find_Diameter(r)
    circumference = find_Circumference(r)
    area = find_Area(r)
    print("\n Diameter Of a Circle = %.2f" % diameter)
    print(" Circumference Of a Circle = %.2f" % circumference)
    print(" Area Of a Circle = %.2f" % area)


def run_program_25():
    print("--- Program 25: Rectangle Area with Functions ---")

    def areaRectangle(a, b):
        return a * b

    def perimeterRectangle(a, b):
        return 2 * (a + b)

    a = 5
    b = 6
    print("Area = ", areaRectangle(a, b))
    print("Perimeter = ", perimeterRectangle(a, b))


def run_program_26():
    print("--- Program 26: Number Guessing Game ---")
    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))
    x = random.randint(lower, upper)
    chances = round(math.log(upper - lower + 1, 2))
    print("\n\tYou've only ", chances, " chances to guess the integer!\n")
    count = 0
    while count < chances:
        count += 1
        guess = int(input("Guess a number: "))
        if x == guess:
            print("Congratulations you did it in ", count, "try")
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")
    if count >= chances and x != guess:
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")


def run_program_27():
    print("--- Program 27: Day of the Year Find ---")
    date = str(input("Enter the date (for example:09 02 2019):"))
    day_name = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    day = datetime.datetime.strptime(date, "%d %m %Y").weekday()
    print(day_name[day])


def run_program_28():
    print("--- Program 28: Find Missing Numbers ---")

    def find_missing(lst):
        return [x for x in range(lst[0], lst[-1] + 1) if x not in lst]

    lst = [1, 2, 4, 6, 7, 9, 10]
    print(find_missing(lst))


def run_program_29():
    print("--- Program 29: Character Check in String ---")
    char_list = ["a", "b", "c"]
    string = "abcd"
    matched_list = [character in char_list for character in string]
    print(matched_list)
    string_contains_chars = all(matched_list)
    print(string_contains_chars)


def run_program_30():
    print("--- Program 30: Averages of Whole Numbers ---")
    total = 0
    evenSums = 0
    oddSums = 0
    evenCount = 0
    oddCount = 0
    done = False
    while not done:
        user_in = input("Give me an integer or type 'done' to be done: ")
        if user_in.lower() == "done":
            done = True
        elif user_in.lstrip("-").isdigit():
            num = int(user_in)
            total += num
            if num % 2 == 0:
                evenSums += num
                evenCount += 1
            else:
                oddSums += num
                oddCount += 1
        else:
            print("Please enter a valid integer.")

    print(total)
    evenAverage = evenSums / evenCount if evenCount > 0 else 0
    oddAverage = oddSums / oddCount if oddCount > 0 else 0
    print("Even Average: " + str(evenAverage))
    print("Odd Average: " + str(oddAverage))

def main_menu():
    programs = {
        1: run_program_1,
        2: run_program_2,
        3: run_program_3,
        4: run_program_4,
        5: run_program_5,
        6: run_program_6,
        7: run_program_7,
        8: run_program_8,
        9: run_program_9,
        10: run_program_10,
        11: run_program_11,
        12: run_program_12,
        13: run_program_13,
        14: run_program_14,
        15: run_program_15,
        16: run_program_16,
        17: run_program_17,
        18: run_program_18,
        19: run_program_19,
        20: run_program_20,
        21: run_program_21,
        22: run_program_22,
        23: run_program_23,
        24: run_program_24,
        25: run_program_25,
        26: run_program_26,
        27: run_program_27,
        28: run_program_28,
        29: run_program_29,
        30: run_program_30,
    }
    while True:
        print("\n" + "=" * 50)
        print("      LAB ACTIVITY #1: PYTHON PRACTICE APPLICATION      ")
        print("=" * 50)
        print('Select a program to run (1-30) or type "0" to exit.')
        choice = input("Enter your choice: ")
        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        if choice.isdigit():
            choice_num = int(choice)
            if choice_num in programs:
                print("\nExecuting...")
                programs[choice_num]()
                input("\nPress Enter to return to the menu...")
            else:
                print("Invalid choice! Please pick a number between 1 and 30.")
        else:
            print("Please enter a valid numeric value.")


if __name__ == "__main__":
    main_menu()
