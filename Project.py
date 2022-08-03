# Day Trip Generator
    # (5 Points): As developer, I want to make at least 3 commits w/ descriptive messages (gitHub commits -m "    ")
    # (5 points): As developer, I want to Store Destinations, restaraunts, mode of transport, and entertainment in their own seperate lines
    # (5 points) x4 : As user, I want destination, restaraunt, transportation, & entertainment to be randomly selected
    # (15 points): As user, I want to be able to RE-SELECT a dest, rest, transport, and/or ent if i dont like what I've randomly been given
    # (10 points): As user, I want to be able to confirm that my day-trip is "complete" once i like all the random selections
    # (10 points): As user, I want to display a completed trip in the console/terminal
    # (5 points): As developer, I want all of my functions to have a SINGLE RESPONSIBILITY. **REMEMBER, each function should do just ONE THING!**

print('')
user_name= input('Please Enter Your Name: ')
print(f'Hello {user_name} I am your Trip Generator!')
print('')

import random


destinations= ['Miami', 'Mexico', 'Milwaukee'] 

def random_dest():
    user_validater= False   # Still not 100% on how and where to use & why False
    while user_validater is False: 

        dest_item= random.choice(destinations)
        does_user_like= input(f'{dest_item} has been selected, do you like this option? yes or no: ')
        if does_user_like== "yes":
            print(f'Great, you will love it in {dest_item}! ')
            return dest_item    # Need to understand a little better
        elif does_user_like== "no":
            print('Okay, lets try again! ')
        
confirmed_dest= random_dest()  # confirmed_dest is created so the outcome of this function (random_dest) can be used later   



transport_list= ['Rental Car', 'Helicopter', 'Airplane']
random_transport= random.choice(transport_list)
print(random_transport)

restaraunt_list= ['Mexican', 'French', 'Chinese']
random_restaraunt= random.choice(restaraunt_list)
print(random_restaraunt)

entertainment_list= ['Movie Theater', 'Sky Diving', 'Go Karts']
random_ent= random.choice(entertainment_list)
print(random_ent)


# QUESTION for meeting: Take me through the process of working on project via VScode and updating gitHub/gitHub bash seamlessly



# TODO: Make list for destinations, restaraunt, transport, entertainment
# TODO: Try introducing RANDOM into IF,ELIF,ELSE conditional ??
# TODO: 
# TODO: Craete a FUNCTION (def) for each list
        # Identify what my parameters will be and how function will recall the randomizer again 
# TODO: Randomly select all variables:
    # Allow user to randomize singular value at a time (e.g re-randomize ONLY transportation and nothing else)
    # Take list-Get Length
    # Take Length and generate random number
    # Get value from list from random number
# TODO: Re-select if user doesnt like option
    # Get user input ('yes' or 'no')
    
