def  next_palindrome(n):
    n=n+1
    while not is_palindrome(n):
        n=n+1
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]


if __name__ == '__main__':
    n=int(input("No of test cases you want to enter\n"))
    numbers=[]

    for i in range(n):
        number=int(input("Enter your number\n"))
        numbers.append(number)

    for i in range(n):
        print(f"The next palindrome of {numbers[i]} is {next_palindrome(numbers[i])}")
