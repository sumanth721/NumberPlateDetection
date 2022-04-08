def PasswordGen(data):
    print("Generating password with combination of",data)


if __name__ == "__main__":
    print("Welcome to Password Generator Project")

    # read input from user for combination
    value = int(input("Enter a number for combination: "))

    PasswordGen(value)

