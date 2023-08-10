while True:
    is_prime = True
    try:
        user_input = int(input("Enter number: "))

        if user_input < 0:
            break

        for i in range(2, int(user_input**0.5) + 1):
            if user_input % i == 0:
                is_prime = False
        else:
            print(is_prime)
    except ValueError:
        print("Not natural number")