import random


def generate_random_value(min_value, max_value):
    
    """we are generating a random value between minimum and maximum values."""
    return random.randint(min_value, max_value)


def random_operator():
    """select a random operator like addition, subtraction, multiplication and division"""
    return random.choice(['+', '-', '*', '/'])


def create_questions(num1, num2, operator):
    # ask the question
    question = f"{num1} {operator} {num2}"
    
    # calculate the correct answer
    if operator == '+': result = num1 + num2
    elif operator == '-': result = num1 - num2
    elif operator == '/': result = num1/num2
    elif operator == '*': result = num1 * num2
    else: 
        # raise an error if an invalid operator is choosen
        raise ValueError("Invalid operator")
    return question, result

def math_quiz():
    """ Run the math quiz game by generating questions and evaluating user answers"""
    score = 0 # Initialize the user's score
    total_questions = 3 # Total number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    # Loop through the specified number of questions

    for _ in range(total_questions):
        # Generate random numbers and operator for the question 
        num1 = generate_random_value(1, 10); num2 = generate_random_value(1, 10); operator = random_operator()

        # Create the question and find the correct answer
        PROBLEM, ANSWER = create_questions(num1, num2, operator)
        
        # Print the question to the user
        print(f"\nQuestion: {PROBLEM}")
        
        # Get the user's answer with validation
        user_answer = input("Your answer: ")
        
        # Check if the user's answer is correct and update score
        user_answer = int(user_answer)

        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
