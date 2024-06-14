'''==========================================================[Joke  program]==============================================='''


Joke = input("Do you want to hear a joke? ")

joke_response_yes = ["yes", "y"]
joke_response_no = ["no", "n"]
joke_response_new = ["new"]
joke_response_once_more = ["once more"]

# if , elif , else condition for yes or no 
if Joke.lower() in joke_response_yes:
    print("Are you Siri? Because you autocomplete me.")
    
elif Joke.lower() in joke_response_no:
    print("Fine. It's your Choice")

elif Joke.lower() in joke_response_new:
    print("All the good pick up lines are taken but you aren't.")

elif Joke.lower() in joke_response_once_more:
    print(" Your hand looks heavy, can I hold it for you?")
        
else:
    print("I don't understand.[ Please , Give Right answer ]")
    



    