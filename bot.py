def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    number = int(input())
    i = 0
    while i <= number:
        print(i, '!')
        i = i + 1


def test():
    print("Let's test your programming knowledge.")
    print('When is the code from an "else" block executed?')
    print("""
    1. immediately after the code from an if statement is run
    2. it is run independently of an if statement
    3. when the value of condition is False
    4. when the value of condition is True
    """)

    ans = int(input())
    while ans != 3:
        print("Please, try again.")
        ans = int(input())

    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Samzon', '2021')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
