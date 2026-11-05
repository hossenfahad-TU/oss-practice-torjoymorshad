
import argparse
from tabulate import tabulate

def main():
    parser = argparse.ArgumentParser(
        description="My Open Source Learning Tool"
    )
    parser.add_argument("--name", default="Student")
    args = parser.parse_args()

    print(f"\nWelcome to my Python project, {args.name}!")
    print("Here are the technologies I am learning:\n")

    tools = [
        ["Python", "Programming and automation"],
        ["Git", "Tracking code changes"],
        ["GitHub", "Collaborating on projects"],
        ["Tabulate", "Displaying organized information"],
    ]

    print(tabulate(
        tools,
        headers=["Technology", "Learning Purpose"],
        tablefmt="grid"
    ))

    print(f"\nKeep exploring open source, {args.name}!")

if __name__ == "__main__":
    main()
