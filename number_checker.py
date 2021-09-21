# Functions go here


# Main routine goes here
def number_check(question):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the questions
            response = int(input("How much would you "
                                 "like to play with? "))
            # if the amount is to low / too high give
            if 0 < response <= 10 :
                print("You have asked to play "
                      "with ${}".format(response))
                # output an error
            else:
                print(error)

        except ValueError:
           print(error)

how_much = number_check("how much do you want to play with")


