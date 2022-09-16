# Main Python file for the assignment

from operator import attrgetter

# Given 5 wine names and scores, create a Wine object and sort by name and by score
wine_names = ["Chardonnay", "Viognier", "Gewurtztraminer", "Pinot Gris", "Riesling"]
wine_scores = [76, 86, 94, 92, 88]

# TODO: create a wine object with attributes ID, name, score
class Wine(object):

    class_counter = 0

    def __init__(self, name, score):
        self.id = Wine.class_counter
        self.name = name
        self.score = score
        Wine.class_counter += 1

    def __repr__(self):
        return '{}\t{}\t{}'.format(self.id, self.score, self.name)

def make_wine_list(names, scores):
    my_wines = []
    for i in range(5):
        my_wines.append(Wine(names[i], scores[i]))
    return my_wines

# TODO: create a function to print a wine list
def print_wine_list(list_name, wine_list):
    print("\n========= "+list_name+" =========")
    print('ID\tScore\tName')
    for wine in wine_list:
        print(wine)
    print()

# TODO: create a function to ask the user how they want to sort their wine list

if __name__ == '__main__':
    print("Congratulations! You now own a winery.")

    my_wines = make_wine_list(wine_names, wine_scores)

    print("All five of your wines have already been tasted and scored by wine critics.")
    
    # TODO: present the wine list
    print_wine_list("MY WINES", my_wines)

    # TODO: ask the user how they want to sort their wine

    # TODO: sort the wine or exit the program