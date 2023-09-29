import pandas as pd
import random
from text_animator import TextAnimation, Border

def main(): # Get the user's mood choice
    answer = input(""" 
1 for Need to Inspire
2 for Sad
3 for Happy
4 for Excited
How do you feel?: """)
    
    try:
        if answer in ['1', '2', '3', '4']: # Display quotes based on the selected mood
            quotes(answer)
        else:
            print("Please enter 1, 2, 3, or 4")
            main() # Ask for selection again in case of invalid input
    except ValueError:
        print("Invalid input, please enter a number between 1 and 4")
            
    
def quotes(answer):
    veri_df = pd.read_excel("quotes.xlsx")  # Load the Excel file containing quotes
    random_number = random.randint(0, 9)  # Use the random module to choose a random quote
    
    if answer == '1': # Get a quote from the columns
        find_quotes = veri_df.loc[random_number, 'Inspire']  
    elif answer == '2':
        find_quotes = veri_df.loc[random_number, 'Sad']  
    elif answer == '3':
        find_quotes = veri_df.loc[random_number, 'Happy']  
    elif answer == '4':
        find_quotes = veri_df.loc[random_number, 'Excited']  
# Use the text animator to print the quote 
    TextAnimation(find_quotes, border=Border(lm=0, tm=0, bm=0, tp=0, bp=0))()

if __name__ == "__main__":
    main()

