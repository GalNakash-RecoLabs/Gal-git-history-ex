import sys


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


functions = {
    "add": add,
    "sub": sub,
    "mul": mul,
}


def main():
    if len(sys.argv) != 4:
        print('Usage: calculator.py <function> <number> <number>')
        sys.exit(1)

    function = sys.argv[1]
    if function not in functions:
        print('Error: Invalid function. Functions are: {}'.format(', '.join(functions.keys())))
        sys.exit(1)

    try:
        a = float(sys.argv[2])
        b = float(sys.argv[3])
    except ValueError:
        print('Error: Invalid numbers. Numbers must be integers.')
        sys.exit(1)

    result = functions[function](a, b)
    print(result)


if __name__ == '__main__':
    main()
