def add(x, y):
    return x + y

print(add(1, 2))

def concatenate(x, y):
    return str(x) + str(y)

print(concatenate("python", "test"))

def operate(operation, x, y):
    """
    Performs a specified operation on two operands
    :param operation: The operation is to be performed
    :param x: The first operand
    :param y: The second operand
    :return: The result
    """

    result_sum = operation(add, 3, 5)
    result_concatenate = operate(concatenate, "Hello", "World")