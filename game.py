from mimetypes import init

from jinja2 import ChoiceLoader
from src.main import Run


if __name__ == '__main__':

    print("Welcome to the game!")
    print("You are Commander of the Village")
    print("Choose your player : King Or Queen")
    print("1. King")
    print("2. Queen")
    choice = '0'

    while choice != '1' or choice != '2':
        choice = input()
        if choice == '1':
            Run(1)
            break
        elif choice == '2':
            Run(2)
            break
        else:
            print("Invalid choice")
            print("Please choose 1 or 2")
            print("1. King")
            print("2. Queen")

