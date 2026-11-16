import streamlit as st

def calculate(num1, num2, operation):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "You cannot divide by zero"

    return result

def main():
    st.title("Calculator")

    num1 = st.number_input("Enter first number", step=1)
    num2 = st.number_input("Enter second number", step=1)

    operation = st.radio("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])
    result = calculate(num1, num2, operation)

    st.write(f"Result of the {operation} of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()