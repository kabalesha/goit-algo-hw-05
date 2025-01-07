# Task 1
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()
# print(fib(10))

# Task 2

import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:

    pattern = r'\b\d+(\.\d+)?\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:

    return sum(func(text))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

# Task 3

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone, please."
        except IndexError:
            return "Insufficient arguments provided."
        except Exception as e:
            return f"Unexpected error: {e}"

    return inner


contacts = {}


@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}."


@input_error
def get_phone(args):
    name = args[0]
    phone = contacts[name]
    return f"{name}'s phone: {phone}"


@input_error
def show_all(_):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


@input_error
def unknown_command(_):
    return "Unknown command. Please try again."


def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ""
    args = parts[1:]
    return command, args


def main():
    print("Hello! I'm your assistant. Enter a command:")
    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() in {"exit", "close", "bye"}:
            print("Goodbye!")
            break

        command, args = parse_input(user_input)
        if command == "add":
            print(add_contact(args))
        elif command == "phone":
            print(get_phone(args))
        elif command == "all":
            print(show_all(args))
        else:
            print(unknown_command(args))


if __name__ == "__main__":
    main()
