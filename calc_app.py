def main():
    # Continuously prompt the user until a valid input is provided
    while True:
        choice = input("Enter the number of what you would like to do:\n1. "
        "Perform an equation\n2. Print previous equations from a text file\n")
        if choice == "1":
            # Perform the equation
            calculate()
            break
        elif choice == "2":
            # Print previous equations from a text file
            print_prev()
            break
        else:
            print("That is not a valid entry. Please try again...")


def calculate():
    """
    Calculate a user provided equation.
    
    Print the output of the equation and save the equation and answer to a 
    text file.
    """
    num_1 = 0
    num_2 = 0
    operator = ""
    answer = 0
    file = None
    # Prompt user to enter an equation
    equation = input("Please enter your equation\nNote that the equation can "
    "only consist of two numbers and one of the following operations:\n"
    " + , - , * , / \n")
    equation = equation.strip()
    equation = equation.split(" ")
    # Check if input is valid
    if len(equation) != 3:
        print("That is not a valid entry. Please ensure that you:\n"
        "1. only have 2 numbers with an operator between them\n"
        "2. have spaces around the operator")
        calculate()
    else:
        operator = equation[1]
        try:
            num_1 = float(equation[0])
            num_2 = float(equation[2])
        except ValueError:
            print("That is not a valid entry. Please ensure that your numbers"
            " are both valid numbers.")
            calculate()
        if operator == "+":
            answer = num_1 + num_2
        elif operator == "-":
            answer = num_1 - num_2
        elif operator == "*":
            answer = num_1 * num_2
        elif operator == "/":
            answer = num_1 / num_2
        else:
            print("That is not a valid entry. Please ensure that your operator"
            " is one of the following: + - * /")
            calculate()
        print(f"Answer: {answer}")
        file = open("equations.txt", "a")
        file.write(f"{num_1} {operator} {num_2} = {answer}")
        file.close()


def print_prev():
    """
    Print the previous equations (if there are any) from a text file.
    """
    
    file = None

    try:
        open("equations.txt", "r")
        print(file.read())
    except FileNotFoundError:
        print("There are no previous equations")
    
    finally:
        if file is not None:
            file.close()


if __name__ == "__main__":
    main()