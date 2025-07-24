
import decimal

def calculate_pi(n):
    """
    Calculates Pi to n decimal places using the Chudnovsky algorithm.
    """
    decimal.getcontext().prec = n + 3
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6
    M = 1
    X = 1
    L = 13591409
    S = L

    for i in range(1, n + 1):
        M = (K**3 - 16*K) * M // i**3
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
        K += 12

    pi = C / S
    return round(pi, n)

def main():
    """
    Prompts the user for the number of decimal places and prints Pi.
    """
    while True:
        try:
            num_digits = int(input("How many digits of Pi do you want to print? "))
            if num_digits < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    pi_value = calculate_pi(num_digits)
    print(f"Pi to {num_digits} decimal places is:")
    print(pi_value)

if __name__ == "__main__":
    main()
