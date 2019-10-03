#code to demonstrate the use of a nested decision statement

#ask what type of of book cover
print("What type of cover does the book have? (hard or soft)")
book_cover = input()

#find out the type of book cover

#if the book cover is soft then do:
if (book_cover == "soft"):

    #ask if the book is perfect bound or not
    print("Is the book perfect bound or not? (yes or no)")
    bound = input()

    #checks if the book is perfect bound or not
    if (bound == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")

#if the book cover is hard then do:
elif (book_cover == "hard"):
    print("Books with hard covers can be more expensive!")

#if the book cover is anything else then do:
else:
    print("Cannot recognize which cover it is!")