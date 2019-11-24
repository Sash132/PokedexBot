#Imported to allow access to an external CSV file
import pandas as pd

"""This file holds a collection of functions that I created in order to make my chatbot. 
   I created all of the functions myself except for two of them which are modifications 
   of the end_chat function in A3-Chatbots. I took this function's general layout and made 
   two separate implementations of it that work for my project called check_quit and 
   check_other. I only used concepts that were taught in class; although, I did have to 
   use pandas which was vaguely mentioned in class so I had to look up its documentation 
   by myself. This led me to create a multitude of dictionaries that are utilized throughout 
   most of the functions.
"""

#Variable utilized to access external CSV file that holds all data about the Pokemon
csv_access = pd.read_csv("Pokemon_Data.csv")

#Dictionaries used to differentiate between different information from the CSV file
number_dict = dict(zip(csv_access.Name, csv_access.Number))
type_dict = dict(zip(csv_access.Name, csv_access.Type))
HP_dict = dict(zip(csv_access.Name, csv_access.HP))
attack_dict = dict(zip(csv_access.Name, csv_access.Attack))
defense_dict = dict(zip(csv_access.Name, csv_access.Defense))
special_attack_dict = dict(zip(csv_access.Name, csv_access.Special_Attack))
special_defense_dict = dict(zip(csv_access.Name, csv_access.Special_Defense))
speed_dict = dict(zip(csv_access.Name, csv_access.Speed))
BST_dict = dict(zip(csv_access.Name, csv_access.Total))
legendary_dict = dict(zip(csv_access.Name, csv_access.Legendary))
height_dict = dict(zip(csv_access.Name, csv_access.Height))
weight_dict = dict(zip(csv_access.Name, csv_access.Weight))
happiness_dict = dict(zip(csv_access.Name, csv_access.Happiness))
capture_rate_dict = dict(zip(csv_access.Name, csv_access.Capture_Rate))
classification_dict = dict(zip(csv_access.Name, csv_access.Classification))
abilities_dict = dict(zip(csv_access.Name, csv_access.Abilities))

#Functions used to access data from the dictionaries
def get_number(name):
    """Gets the number position of a Pokemon in the Pokedex when
       prompted with its name.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    output: int
        Number position of the specific Pokemon in the Pokedex
    """ 
    output = number_dict[name]
    return output

def get_type(name):
    """Gets the typing of a Pokemon in the Pokedex when
       prompted with its name.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    output: String
        Typing of the specific Pokemon in the Pokedex
    """ 
    output = type_dict[name]
    return output

def get_stats(name):
    """Gets the stats of a Pokemon in the Pokedex when
       prompted with its name.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    output: String
        All six stats of the specific Pokemon in the Pokedex
    """ 
    hp_text = "HP: " + str(HP_dict[name])
    attack_text = "Attack: " + str(attack_dict[name])
    defense_text = "Defense: " + str(defense_dict[name])
    special_attack_text = "Special Attack: " + str(special_attack_dict[name])
    special_defense_text = "Special Defense: " + str(special_defense_dict[name])
    speed_text = "Speed: " + str(speed_dict[name])
    return hp_text + ", " + attack_text + ", " + defense_text + ", " + special_attack_text + ", " + special_defense_text + ", " + speed_text

def get_BST(name):
    """Gets the base stat total of a Pokemon in the Pokedex when
       prompted with its name.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    output: int
        Base Stat Total of the specific Pokemon in the Pokedex
    """ 
    output = BST_dict[name]
    return output

def get_legendary_status(name):
    """Gets the legendary status of a Pokemon in the Pokedex when
       prompted with its name.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    output: boolean
        Whether the specific Pokemon in the Pokedex is
        a legendary or not.
    """ 
    output = None
    if(legendary_dict[name] is True):
        output = True
    else:
        output = False
    return output

def get_height(name):
    """Gets the height of a Pokemon in the Pokedex when
       prompted with its name.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    output: String
        Height of the specific Pokemon in the Pokedex
    """ 
    output = str(height_dict[name]) + " meters"
    return output

def get_weight(name):
    """Gets the weight of a Pokemon in the Pokedex when
       prompted with its name.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    output: String
        Weight of the specific Pokemon in the Pokedex
    """ 
    output = str(weight_dict[name]) + " kilograms"
    return output

def get_happiness(name):
    """Gets the base happiness of a Pokemon in the Pokedex when
       prompted with its name.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    output: int
        Happiness of the specific Pokemon in the Pokedex
    """ 
    output = happiness_dict[name]
    return output

def get_capture_rate(name):
    """Gets the standard capture rate of a Pokemon in the Pokedex
       when prompted with its name.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    output: int
        Standard capture rate of the specific Pokemon in the Pokedex
    """ 
    output = capture_rate_dict[name]
    return output

def get_classification(name):
    """Gets the classification of a Pokemon in the Pokedex when
       prompted with its name.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    output: String
        Classification of the specific Pokemon in the Pokedex
    """ 
    split_list = classification_dict[name].split()
    output = split_list[0] + " Pokemon"
    return output

def get_abilities(name):
    """Gets the abilities of a Pokemon in the Pokedex when
       prompted with its name.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    output: String
        Abilities of the specific Pokemon in the Pokedex
    """ 
    output = abilities_dict[name]
    return output

#Functions taken from A3-Chatbots
def check_quit(input_string):
    """Checks whether or not the input_string is 'Quit'.
    Parameters
    ----------
    input_string: String
        A string that holds a user-input string
        
    Returns
    -------
    boolean
        Whether or not the string is 'Quit'
    """ 
    if input_string == "Quit":
        return True
    else:
        return False
    
def check_other(input_string):
    """Checks whether or not the input_string is 'Other'.
    Parameters
    ----------
    input_string: String
        A string that holds a user-input string
        
    Returns
    -------
    boolean
        Whether or not the string is 'Other'
    """ 
    if input_string == "Other":
        return True
    else:
        return False

#Functions used to create the Pokedex Bot
def is_pokemon(name):
    """Checks if the input is actually a Pokemon.
    Parameters
    ----------
    name: String
        A string that holds supposed name of the Pokemon that
        user has supplied.
        
    Returns
    -------
    boolean
        Whether or not the input is in number_dict
    """ 
    if name in number_dict:
        return True
    else:
        return False
    
def is_info(name):
    """Checks if the input is actually a type of information
       in the Pokedex.
    Parameters
    ----------
    name: String
        A string that holds a type of information that the
        user wants to know more about when dealing with their
        specific Pokemon.
        
    Returns
    -------
    boolean
        Whether or not the input equivalent to "Number", "Type",
        "Stats", "Bst", "Legendary", "Height", "Weight", 
        "Happiness", "Capture", "Classification", or "Abilities".
    """ 
    if name == "Number" or name == "Type" or name == "Stats" or name == "Bst" or name == "Legendary" or name == "Height" or name == "Weight" or name == "Happiness" or name == "Capture" or name == "Classification" or name == "Abilities":
        return True
    return False

def text_matcher(input_string):
    """Changes the input_string such that it will accomodate 
       to the requirements of the other methods.
    Parameters
    ----------
    input_string: String
        A string that holds either a Pokemon name or type
        of information.
        
    Returns
    -------
    output_string: String
        A string that holds the original input but modified 
        such that the first letter is capitalized and all 
        following letters are lowercase.
    """ 
    uppercase = input_string[0:1]
    uppercase = uppercase.upper()
    lowercase = input_string[1:]
    lowercase = lowercase.lower()
    output_string = uppercase + lowercase
    return output_string

def initialize():
    """Prints out the greeting message of the Pokedex Bot."""
    print("Welcome to the Kanto (Generation 1) Pokedex!")
    print("Which Pokemon would you like to look up?")
    print("Type in 'quit' at any point to leave the Dex.\n")
    
def gather_info():
    """Prints out the question asking the user what type of 
       information they want to know."""
    print("Which of the following things would you like to know about this Pokemon?")
    print("Options: Number, Type, Stats, BST, Legendary, Height, Weight, Happiness, Capture, Classification, Abilities")
    print("Type in 'other' at any point to look up another Pokemon.")
    print("Type in 'quit' at any point to leave the Dex.\n")
    
def info_printer(info_string, name_string):
    """Prints out information defined by info_string about 
       a Pokemon defined by name_string.
    Parameters
    ----------
    info_string: String
        A string that holds a type of information that the
        user would like to know more about.
    
    name_string: 
        A string that holds supposed name of the Pokemon that
        user has supplied.
    """ 
    if info_string == "Number":
        print(name_string + " is #" + str(get_number(name_string)) + " in the Kanto Pokedex.")
    elif info_string == "Type":
        print(name_string + "'s typing is " + str(get_type(name_string)) + ".")
    elif info_string == "Stats":
        print(name_string + " has the following base stats - " + str(get_stats(name_string)) + ".")
    elif info_string == "Bst":
        print(name_string + " has a total base stat value of " + str(get_BST(name_string)) + ".")
    elif info_string == "Legendary":
        if get_legendary_status(name_string):
            print(name_string + " is a legendary Pokemon.")
        else:
            print(name_string + " is not a legendary Pokemon.")
    elif info_string == "Height":
        print(name_string + " is " + str(get_height(name_string)) + " tall.")
    elif info_string == "Weight":
        print(name_string + " weighs " + str(get_weight(name_string)) + ".")
    elif info_string == "Happiness":
        print(name_string + " has a base happiness level of " + str(get_happiness(name_string)) + ".")
    elif info_string == "Capture":
        print(name_string + " has a standard capture rate of " + str(get_capture_rate(name_string)) + ".")
    elif info_string == "Classification":
        print(name_string + " is classified as the " + str(get_classification(name_string)) + ".")
    elif info_string == "Abilities":
        print(name_string + " has the following abilities - " + str(get_abilities(name_string)) + ".")
    
def other_lookup():
    """Prints out statement if user prompts that they would
       like to look up another Pokemon."""
    print("Which other Pokemon would you like to look up?\n")

def not_a_pokemon():
    """Prints out statements if user types in a name that is
       not in the Kanto Pokedex."""
    print("This is not a Pokemon that exists in the Kanto Dex.")
    print("Please type in another Pokemon's name.\n")
    
def not_info():
    """Prints out statements if user types in a type of
       information that is not in the Kanto Pokedex."""
    print("This is not valid information that we have in our Dex.")
    print("Please type in another piece of information that you would like to know about your Pokemon\n")
    
def close_pokedex():
    """Prints out statements if user wants to leave the
       Pokedex Bot."""
    print("\nHave fun on the rest of your Pokemon journey!")
    print("Goodbye!\n")
    
def activate_pokedex_bot():
    """Main function that activates the entire Pokedex Bot."""
    
    #prints out starting statements to user and instantiates the Pokedex Bot
    initialize()
    
    #flag that is used to keep user in the Bot until they choose to 'quit'
    chat = True
    
    #while loop that keeps the user in constant interaction with the Bot
    while chat:
        
        #gets an input from the user
        name_string = input(">");
        #formats input to be used by other methods
        name_string = text_matcher(name_string)
        #checks if input is an actual Pokemon in the Kanto Pokedex
        is_pokemon_flag = is_pokemon(name_string)
        
        #if statement that is accessed if the input is an actual Pokemon
        if is_pokemon_flag:
            
            #prints out statements to the user prompting them to ask for information about the specific Pokemon they entered.
            gather_info()
            
            #flag that is used to keep user in the information section until they choose to 'quit' or check 'other' Pokemon
            info = True
            
            #while loop that keeps the user in constant interaction with the information section
            while info:
                #gets an input from the user
                info_string = input(">")
                #formats input to be used by other methods
                info_string = text_matcher(info_string)
                #checks if input is an actual type of information that the Bot has
                is_info_flag = is_info(info_string)
                
                #if statement that is accessed if input is an actual type of information that the Bot has
                if is_info_flag:
                    #prints out information dependent on both inputs
                    info_printer(info_string, name_string)

                #elif statement that is accessed if the user types in 'other'
                elif check_other(info_string):
                    #changes flag such that the Bot will break out of the information section after this iteration
                    info = False
                    #prints out statement asking user for a Pokemon they would like to know about
                    other_lookup()
                    
                #elif statement that is accessed if the user types in 'quit'
                elif check_quit(info_string):
                    #changes flag such that the Bot will break out of the information section after this iteration
                    info = False
                    #changes flag such that the Bot will stop interacting with the user after this iteration
                    chat = False
                    
                #else statement that is accessed if the input is not a Pokemon, 'quit', or 'other'
                else:
                    #prints out statements if user input is not a type of information
                    not_info()
                    #goes to next iteration of the inner while loop
                    continue
        
        #elif statement that is accessed if the user types in 'quit'
        elif check_quit(name_string):
            #changes flag such that the Bot will stop interacting with the user after this iteration
            chat = False
        
        #else statement that is accessed if the input is neither a Pokemon or 'quit'
        else:
            #prints out statements if user input is not a Pokemon
            not_a_pokemon()
            #goes to next iteration of the while loop
            continue
    
    #prints out closing statements of the Bot
    close_pokedex()