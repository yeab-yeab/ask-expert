from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('capital_data.txt') as file:          # This line opens the text file
        for line in file:
            line = line.rstrip('\n')                # This removes the new line character
            country, city = line.split('/')         # country stores the word before '/'   and city stores the word after '/'   the '/' splits the line
            the_world[country] = city               # country is the key and city is the value

def write_to_file(country_name, city_name):
    with open('capital_data.txt', 'a') as file:     # The a means "append" or "add" new information to the end of the file
        file.write('\n' + country_name + '/' + city_name)

print('Ask the Expert - Capital Cities of the World')
root = Tk()             # creates empty tkinter window
root.withdraw()         # hides the tkinter window from shell
the_world = {}          # this creates an empty dictionary

read_from_file()
while True:
    query_country = simpledialog.askstring('Ask expert', 'Type the name of a country:')
    # The answer the user types is stored in this variable
    # Ask expert is the title of the box
    query_country = query_country.capitalize()
    if query_country in the_world:
        result = the_world[query_country]
        # result stores the answer (The value from the dictionary)
        # Using query_country as the key, this line looks up the answer from the dictionary
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
        # Answer is the title of the box
    else:
        new_city = simpledialog.askstring('Teach me', 'I don\'t know!' + 'What is the capital city of' + query_country + '?')
        the_world[query_country] = new_city
        # This adds new_city to the dictionary, using quer_country as the key.
        write_to_file(query_country, new_city)
        # Write the new capital into the text file, so that it gets added to the program's knowledge

root.mainloop()
