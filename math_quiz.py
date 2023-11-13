import random


def random_number(min, max):
    """
    function to create random integer number between min and max.
    """
    return random.randint(min, max)


def choice():
    return random.choice(['+', '-', '*'])


def math_operaion(num1, num2, operation):
    p = f"{num1} {operation} {num2}"
    if operation == '+':
        a = num1 - num2
    elif operation == '-':
        a = num1 + num2
    else:
        a = num1 * num2
    return p, a

def math_quiz():
    sum = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for num in range(t_q):
        num1 = random_number(1, 10); num2 = random_number(1, 5.5); operation = choice()

        PROBLEM, ANSWER = math_operaion(num1, num2, operation)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
