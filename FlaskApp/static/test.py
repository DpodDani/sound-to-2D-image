import os, argparse

# def main():
#     # Initialises the argument parser
#     parser = argparse.ArgumentParser()
#     # Adds the required arguments
#     parser.add_argument("text", help="Some text to be received from AJAX call")
#     # Enables the user of these arguments in the code below
#     args = parser.parse_args()
#
#     return "I received " + args.text
#
# if __name__ == "__main__":
#     main()

def confirmMessage():
    return "Python module: I got your message!"

def confirmColour(colour):
    return "Python module: I got the colour: " + colour

if __name__ == "__main__":
    confirmMessage()
