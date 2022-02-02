"""
Implement all functions in only one line of code!
They should contain a single return statement.
If you think of several implementations, do them all.
No need to validate user input anywhere.
"""


def sum_digits(num):
    """
    Computes the sum of digits of an integer.
    """
    return sum(int(digit) for digit in str(num))
# print(sum_digits(456))


def is_palindrome(seq):
    """
    Checks whether a given sequence is a palindrome.
    (without changing the original sequence)

    Hints:
    - there are 2 easy ways:
        - one using builtin functions
        - another using a knife
    """
    # return str(seq) == str(seq)[::-1]
    return str(seq) == ''.join(reversed(str(seq)))
# print(is_palindrome('abcba'))


def is_gmail(string):
    """
    Checks whether a string is a Gmail email address.

    For our purposes, a valid address looks like "abcd@gmail.com".
    It must be a string of alphabetic letters (no dots) followed by '@gmail.com'.
    """
    return string.endswith('@gmail.com', 1) and string.split('@')[0].isalpha()
# print(is_gmail('qwer@gmail.com'))

def union(items, more_items):
    """
    Unites 2 lists/tuples into a list/tuple that contains all their elements without duplication.
    The return type must be that of the first argument `items`.
    """
    return(type(items)(list(set(more_items).union(set(items)))))
# print(union((1,2,3,5),[4,2,1,5,6]))


# This is not a one-liner challenge, but should be 4 lines max
def distribution(items):
    """
    Finds how many times each item appears in a sequence of items.
    """
    # count_set = {}
    # for a in items:
    #     count_set[a] = count_set[a] + 1 if(a in count_set) else 1
    # return count_set
    return {item: items.count(item) for item in items}
# print(distribution([1,2,3,3,3,3,2,1]))

# remember us? :)
formula1Champions = [
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Alonso",
    "Alonso",
    "Räikkönen",
    "Hamilton",
    "Button",
    "Vettel",
    "Vettel",
    "Vettel",
    "Vettel",
    "Hamilton",
    "Hamilton",
    "Rosberg",
    "Hamilton",
    "Hamilton",
    "Hamilton",
    "Hamilton"
]


def all_time_champion(champions):
    """
    Finds the person has the most wins.

    Hints:
    - distribution
    - max
    - lambda
    """
    return max(distribution(champions), key=distribution(champions).get)
# print(all_time_champion(formula1Champions))


def dictify(keys, values):
    """
    Creates a dict mapping the given keys to the given values.
    """
    return dict(zip(keys, values))
# print(dictify(['a','d','e','h'], (7,2,4,9)))


def is_prime(num):
    """
    Checks whether a number is prime.

    Hints:
    - I can do this any day, and all day long!
    """
    return len([i for i in range(2,num) if num % i == 0]) == 0
# print(is_prime(7))


def caesar_encrypt(plain, key):
    """
    Encrypts a string using caesar cipher, with the given key as the offset.

    Hints:
    - from string import ascii_letters
    - https://www.youtube.com/watch?v=IjcX3MVSdyA
    """
    from string import ascii_letters as al
    return ''.join(al[(al.index(char) + key) % len(al)] if char in al else char for char in plain)
# print(caesar_encrypt('abcmnoxyzABCMNOXYZ qrs', 3))

def all_time_champion2(champions):
    """
    Your previous code is cool, but now make it shorter!

    Hints:
    - from
    - collections
    - import
    - Counter
    """
    from collections import Counter
    return Counter(champions).most_common(1)[0][0]
# print(all_time_champion2(formula1Champions))


def factorial(num):
    """
    Computes the factorial of a number (1 * 2 * 3 * ... * num).

    Hints:
    - def factorial(num):
          '''
          Computes the factorial of a number (1 * 2 * 3 * ... * num).

          Hints:
          - ...
          '''
          pass
    """
    return num if num == 1 else num * factorial(num - 1)
# print(factorial(7))


def compose(*funcs):
    """
    Composes all given functions.
    compose(f, g, h)(x) == f(g(h(x)))

    Hints:
    - from functools import reduce
    """
    from functools import reduce
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)
f = lambda x: x*3
g = lambda x: x+2
h = lambda x: x**2
print(compose(f,g,h)(5))