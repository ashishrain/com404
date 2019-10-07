#football game

#explain the game to the users
print()
print("Welcome to this game. This is a Football game where you will have 5 stamina (♥) to go your way and score the goal. Each action requires one stamina.")
print()
print("You (U) will have two teammates i.e. Right Teammate (RT) and Left Teammate (LT) on the pitch to support you.")
print()
print("There will be a Goal Keeper (K) who will do his best to stop you and your teammates from scoring the goal.")
print()
print("Good Luck on your journey.")
print()
print("Please enter any key and press enter to continue.")

input()

#show the pitch
print()
print(""" 
This is your football pitch:

The ball is represented by "ѳ"

                  ♥ ♥ ♥ ♥ ♥
  -------------------------
  |      |          |     |
  |      |          |     |
  |      ------------     |
  |            K          |
  |                       |
  |   LT             RT   |
  |                       |
  |            ѳ          |
  |            U          |
  -------------------------
""")

print()
print("Please choose and type the action you want to do? (shoot/ pass/ dribble forward)")
act_one = input()

#decice what the user chooses
#if user chooses to shoot
if (act_one == "shoot"):
    print()
    print("Where do you want to shoot? (left/ middle/ right)")
    act_one_shoot = input()

    #decide where user chooses to score
    #if user decides to shoot left
    if (act_one_shoot == "left"):
        print()
        print(""" 
                    ♥ ♥ ♥ ♥
  -------------------------
  |      |          |     |
  |      |          |     |
  |      ------------     |
  |       K               |  *U shoots the ball to the left but*
  |       ѳ               |  *K saves it*
  |   LT             RT   |
  |                       |
  |                       |
  |            U          |
  -------------------------
""")
        print()
        print("Your shot was blocked by the keeper and therefore you lost.")
        print()
        print("Game Lost!")
    
    #if user decides to shoot middle
    elif(act_one_shoot == "middle"):
        print()
        print(""" 
                    ♥ ♥ ♥ ♥
  -------------------------
  |      |          |     |
  |      |          |     |
  |      ------------     |
  |            K          |  *U shoots the ball to the middle but*
  |            ѳ          |  *K saves it*
  |   LT             RT   |
  |                       |
  |                       |
  |            U          |
  -------------------------
""")
        print()
        print("Your shot was blocked by the keeper and therefore you lost.")
        print()
        print("Game Lost!")

    #if user decides to shoot right
    elif(act_one_shoot == "right"):
        print()
        print(""" 
                    ♥ ♥ ♥ ♥
  -------------------------
  |      |          |     |
  |      |          |     |
  |      ------------     |
  |               K       |  *U shoots the ball to the right but*
  |               ѳ       |  *K saves it*
  |   LT             RT   |
  |                       |
  |                       |
  |            U          |
  -------------------------
""")
        print()
        print("Your shot was blocked by the keeper and therefore you lost.")
        print()
        print("Game Lost!")
    
    else:
        print("The action is not identified.")

#if user chooses to pass
elif(act_one == "pass"):
    print()
    print("Where do you want to pass the ball? (left/ right)")
    act_one_pass = input()

    #if user decides to pass the ball to the left
    if (act_one_pass == "left"):
        print()
        print(""" 
                    ♥ ♥ ♥ ♥
  -------------------------
  |      |          |     |
  |      |          |     |
  |      ------------     |
  |            K          |  *U passes the ball to his teammate LT*
  |                       |
  |   LTѳ            RT   |
  |                       |
  |                       |
  |            U          |
  -------------------------
""")
        print("What do you want to do now? (ask for pass/ ask to shoot/ run forward)")
        act_two_pass = input()
