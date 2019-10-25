#code to demonstrate the use of functions

#function to see if justice league is united
def is_league_united(hero_one, hero_two):

    #using if statement to check
    if (hero_one == "Superman" and hero_two == "Wonder Woman"):
        return True
    else:
        return False

#function to decide the plan
def decide_plan(hero_one, hero_two):
    #using if statement to check
    if (is_league_united(hero_one, hero_two) == True):
        return "Time to save the world!"
    else:
        return "We must unite the league!"


#function to run
def run():
    #ask user for first hero name
    print("Who is the first Hero?")
    hero_ones = input()

    #ask user for second hero name
    print("Who is the second Hero?")
    hero_twos = input()

    #ask user to enter the word "league" or "plan"
    print("Please choose (league or plan)")
    chosen_option = input()

    #using if statement to decide
    if (chosen_option == "league"):
        #display the is_league_united function
        print(is_league_united(hero_ones, hero_twos))
    elif (chosen_option == "plan"):
        #display the decide_plan function
        print(decide_plan(hero_ones, hero_twos))
    else:
        print("Invalid command. Please try again")

run()