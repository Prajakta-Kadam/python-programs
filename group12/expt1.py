# Write a Python program to create a simple math quiz.


def startQuiz(questions, results):
    score = 0
    for i in range(len(questions)):
        ans = int(input(questions[i]+" = "))
        if ans == results[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    score = score / len(questions) * 100
    print("Your score is ", score,"%. Thank you.")


def addQuiz():
    questions = ["55 + 14", "83 + 39", "37 + 82", "35 + 43", "25 + 89"]
    results = [69, 122, 119, 78, 114]
    startQuiz(questions, results)


def subQuiz():
    questions = ["94 - 91", "18 - 18", "68 - 16", "35 - 64", "42 - 71"]
    results = [3, 0, 52, -29, -29]
    startQuiz(questions, results)


def mulQuiz():
    questions = ["55 * 14", "8 * 9", "3 * -8", "35 * 11", "-25 * 8"]
    results = [385, 72, -24, 385, 114, -200]
    startQuiz(questions, results)


def divQuiz():
    questions = ["45 / 15", "8 / 5", "32 / 4", "18 / 8", "69 / 18"]
    results = [3, 1, 8, 2, 3]
    startQuiz(questions, results)

print("************************")
print("** A Simple Math Quiz **")
print("************************")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Integer Division")
print("5. Exit")
print("------------------------")
choice = int(input("Enter your choice: "))

if choice == 1:
    addQuiz()
elif choice == 2:
    subQuiz()
elif choice == 3:
    mulQuiz()
elif choice == 4:
    divQuiz()
elif choice == 5:
    exit(0)
else : 
    print("Incorrect Choice!")