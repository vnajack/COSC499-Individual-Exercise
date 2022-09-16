# Main Python file for the assignment

from operator import attrgetter

# Given 5 wine names and scores, create a Wine object list, and then sort by name and by score
wine_names = ["Chardonnay", "Viognier", "Gewurtztraminer", "Pinot Gris", "Riesling"]
wine_scores = [76, 86, 94, 92, 88]

# Wine object with attributes ID, name, score
class Wine(object):

    class_counter = 0

    def __init__(self, name, score):
        self.id = Wine.class_counter
        self.name = name
        self.score = score
        Wine.class_counter += 1 # auto-incrementing class counter for ID

    def __repr__(self):
        return '{}\t{}\t{}'.format(self.id, self.score, self.name)

# function to create a list of Wine objects from the given names and scores
def make_wine_list(names, scores):
    my_wines = []
    for i in range(5):
        my_wines.append(Wine(names[i], scores[i]))
    return my_wines

# function to print a wine list
def print_wine_list(list_name, wine_list):
    print("\n========= "+list_name+" =========")
    print('ID\tScore\tName')
    for wine in wine_list:
        print(wine)
    print()

# function to sort the wine list by name
def sort_by_name(wine_list):
    return sorted(wine_list, key=attrgetter("name"))

# function to sort the wine list by score
def sort_by_score(wine_list):
    return sorted(wine_list, key=attrgetter("score"), reverse=True)

# function to ask the user how they want to sort their wine list
def ask_to_sort(list_name, wine_list):
    ans1 = "name"
    ans2 = "score"
    question = "How would you like to sort your wine list? By "+ans1+" or by "+ans2+"? "
    
    while True:
        user_ans = input(question).lower()

        if (ans1 in user_ans) and (ans2 in user_ans):
            print("I'm sorry, I don't understand.")
        elif (ans1 in user_ans):
            return "SORTED BY NAME", sort_by_name(wine_list)
        elif (ans2 in user_ans):
            return "SORTED BY SCORE", sort_by_score(wine_list)
        elif ("none" in user_ans) or ("neither" in user_ans):
            print("Ok, no sorting this time.")
            return list_name, wine_list
        else:
            print("I'm sorry, I don't understand.")

def ask_to_sort_again():
    while True:
        answer = input("Do you want to sort your wine again? (Y/N) ").lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else: print("I'm sorry, I don't understand.")

if __name__ == '__main__':
    # Introduce as mini simulation
    print("Congratulations! You now own a winery.")

    # Create Wine (object) list from given wine names and scores
    my_wines = make_wine_list(wine_names, wine_scores)
    list_name = "MY WINES"

    # Continue simulation and present wine list
    print("All five of your wines have already been tasted and scored by wine critics.")
    print_wine_list(list_name, my_wines)
    print("Now, let's sort your wine!")

    # ask the user how they want to sort their wine, then sort it accordingly
    while True:
        list_name, my_wines = ask_to_sort(list_name, my_wines)
        print_wine_list(list_name, my_wines)

        if(ask_to_sort_again() is False):
            break

    print("That's the end of the program.\nThank you. Goodbye.")