# Write a program to find gcd with euclid approach?
def euclid_gcd(a,b):
    while (a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a
def main():
    a = int(input('Enter First Number :- '))
    b = int(input('Enter Second Number :- '))
    print(euclid_gcd(a,b))
if __name__ == '__main__':
    main()