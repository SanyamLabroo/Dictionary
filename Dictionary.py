#Downloading necessary modules
import json
from difflib import get_close_matches
import time
import os
from termcolor import colored

#For opening json file
data = json.load(open("C:\\Users\\HP\\OneDrive\\Desktop\\Python\\Projects\\Dictionary\\data.json"))

#For clearing the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

#Function for printing that the user has entered a wrong input
def wrong_input():
    
    print(colored("\nYou have Entered an Invalid Input!", 'red', attrs=['bold']))
    time.sleep(2)
    print(colored("\nPlease try again later!", 'red', attrs=['bold']))
    exit()
    

#Function for getting the meaning of word from the json file
def translate(word):
    
    #For making the word(input) to lower case
    word = word.lower()
    
    #For checking if the word is present in the json file
    if word in data:
        return data[word]
    
    #For checking if the word title is present in the json file
    elif word.title() in data:
        return data[word.title()]
    
    #For checking if the word has uppercase characters and is present in the json file
    elif word.upper() in data:
        return data[word.upper()]
    
    #For checking if a word related(close matched) to the given word is present in the json file
    elif len(get_close_matches(word , data.keys())) > 0 :
            
        print(colored("\ndid you mean %s instead" %get_close_matches(word, data.keys())[0], 'yellow', attrs=['bold']))
        
        #For asking the user if the selected word is the word he has been searching for or not
        decide = input(colored("\npress 'y' for yes or 'n' for no: ", 'magenta', attrs=['bold'])).lower()
        
        #If it is the word then the meaning of that word will get printed
        if decide == "y" or decide == "yes":
                
            return data[get_close_matches(word , data.keys())[0]]
            
        #If it is not then it will print word not found
        elif decide == "n" or decide == "no":
                
            print(colored("\nSorry..But Your Word is not FOUND in the dictionary.", 'cyan', attrs=['bold']))
            exit()
            
        else:
            
            #Else it will say that user has entered an invalid input
            wrong_input()
            
    else:
            
        wrong_input()
            
#For giving the word as user input to be searched in the dictionary file
word = input(colored("Enter the word you want to search: ", 'blue', attrs=['bold']))

#Calling the translate function(With the input as argument) to get the meaning
output = translate(word)

#For checking if the word is in the list
if type(output) == list:
    
    print(colored("\nThe meaning of the given word will be: ", 'yellow', attrs=['bold']))
    
    #If the word has more than one meaning then those will be printd seperately using this for loop
    for item in output:
        
        time.sleep(3)
        print()
        print(colored(item, 'green', attrs=['bold']))
        
else:
    
    #Else if the word has only one meaning then only that will be printed
    time.sleep(3)
    print(colored(output, 'green', attrs=['bold']))



