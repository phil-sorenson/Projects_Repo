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
print(f'{user_name}, lets figure out where youll be staying!' )

def random_dest():
    user_validator= False   # Still not 100% on how and where to use & why False
    while user_validator is False: 

        dest_item= random.choice(destinations)
        does_user_like= input(f'{dest_item} has been selected, do you like this option? yes or no: ')
        if does_user_like== "yes":
            print(f'Great, you will love it in {dest_item}! ')
            return dest_item    # Need to understand a little better
        elif does_user_like== "no":
            print('Okay, lets try again! ')
        
confirmed_dest= random_dest()  # confirmed_dest is created so the outcome of this function (random_dest) can be used later   



transport_list= ['Rental Car', 'Helicopter', 'Airplane']
print(f'{user_name}, now lets figure out your mode of transportation! ')

def random_transport():
    user_validator= False
    while user_validator is False:
        
        trans_item= random.choice(transport_list)
        does_user_like= input(f'{trans_item} has been selected, do you like this option? yes or no: ')
        if does_user_like== "yes":
            print(f'Great! {trans_item} will get you from point A to point B just fine! ')
            return trans_item
        elif does_user_like== "no":
            print('Okay, lets try again! ')

        
confirmed_trans= random_transport()




restaraunt_list= ['Mexican', 'French', 'Chinese']
print(f'{user_name}, now lets see what youll be eating!')

def random_rest():
    user_validator= False
    while user_validator is False:
        
        rest_item= random.choice(restaraunt_list)
        does_user_like= input(f'{rest_item}, has been selected, do you like this option? yes or no: ')
        if does_user_like== "yes":
            print(f'Great! {rest_item} sounds delicious! ')
            return rest_item
        elif does_user_like== "no":
            print('Okay, lets try again! ')
    

confirmed_rest= random_rest()




entertainment_list= ['Movie Theater', 'Sky Diving', 'Go Karts']
print(f'{user_name}, and lastly, lets see what youll be doing on your trip!')

def random_ent():
    user_validation= False
    while user_validation is False: 
        
        ent_item= random.choice(entertainment_list)
        does_user_like= input(f'{ent_item} has been chosen, do you like this option? yes or no: ')
        if does_user_like== 'yes':
            print(f'Great! {ent_item} should be a good time!')
            return ent_item
        elif does_user_like== 'no':
            print('Okay, lets try again!')

confirmed_ent= random_ent()


print(f'{user_name}, now that you have accepted all parts of trip, lets confirm one last time! ')

def finalized_trip():
    compiled_trip= (f'You chose {confirmed_dest}, {confirmed_trans}, {confirmed_rest}, {confirmed_ent}')
    print(compiled_trip)
    user_finalized= input('Type complete if this looks good')
    if user_finalized== 'complete':
        print(f'Thank you {user_name} for using the day trip generator! Have a fantastic time!')
        return finalized_trip

finalized_trip()




        






# QUESTION for meeting: Take me through the process of working on project via VScode and updating gitHub/gitHub bash seamlessly



# TODO: create function that will allow user to input "complete" and the output to terminal is each confirmed_"values"
# TODO: 
# TODO: 
        # Identify what my parameters will be and how function will recall the randomizer again 
# TODO: Randomly select all variables:



