"""My first exercise in COMP110!"""

__author__ = "730621608"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


###conditional statement that only runs in the run tab, not in the REPL###
if __name__ == "__main__":
    print(greet(name=input("What is your name?")))
###^^^there is going to be some line that asks for your name###
