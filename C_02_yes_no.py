# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not chose a valid response")


# Main routine

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    print("Instructions will be displayed")

print(f"The program will continue")
