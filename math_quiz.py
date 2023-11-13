import random


def random_number(min, max):
    """
    function to create random integer number between min and max.
    """
    return random.randint(min, max)


def random_choice():
    ''' function for randome operator selection'''

    return random.choice(['+', '-', '*'])


def math_operation(num1, num2, operation):
    ''' function to do math operation '''

    problem = f"{num1} {operation} {num2}" #represent the generated problem
    if operation == '+':
        answer = num1 + num2 #error resolved from '-' to '+'
    elif operation == '-':
        answer = num1 - num2 #error resolved from '+' to '-'
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    sum = 0 #initial score set to zero
    times_quiz = int(3.14159265359) #floating number converted to integer

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for num in range(times_quiz):
        num1 = random_number(1, 10); num2 = random_number(1, int(5.5)); operation = random_choice()

        PROBLEM, ANSWER = math_operation(num1, num2, operation)
        print(f"\nQuestion: {PROBLEM}")
        while True:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                break
            except ValueError:
                print("Error: Please enter a valid integer.")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            sum += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {sum}/{times_quiz}")

if __name__ == "__main__":
    math_quiz()
