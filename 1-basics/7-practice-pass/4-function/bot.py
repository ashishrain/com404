#code to demonstrate the use of function

#declaring a function to find item from suitcase
def item_from_suitcase(item):

    #display what is in the suitcase
    print("I wonder what is in my suitcase...")

    #using if statement
    if (item == "toothbrush"):
        print("A toothbrush. Well, got to have clean teeth!\n")
    elif (item == "spidey suit"):
        print("My Spidey suit! I won't be needing this. I am on holiday.\n")
    else:
        print("An unexpected item! It could be useful.\n")

item_from_suitcase("toothbrush")
item_from_suitcase("belt")
item_from_suitcase("spidey suit")