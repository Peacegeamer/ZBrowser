print("Hello User!")
while True:
    Name = input("Please input your name: ")
    b = input(f"you will be called {Name}. Y/N: ")
    if b == "Y":
        break
        print("Horray you've started your incognito signup.")
    elif b == "y":
        print("Horray you've started your incognito signup.")
        break
    elif b == "N":
        continue

while True:
    Search = input("search query: ")
    if Search == "helpme" or Search == "help":
        print("To exit the browser press `ctrl c`")
        print("Here is a list is of search queries that you can use;")
        print("helpme or help; These search queries open up a help menu (the one you are on right now). They are probably the most important queries on the browser.")
        print("beans; This search query was added by MayonaiseSoup (github).")
        continue
    if Search == "beans":
        print("Beans are tasty :D")
        continue
    if Search == "goofy":
        print("Goofy is a character of walt disney, it is also a word used when someone did somthing that is crazy/silly. also used in 'That was goofy ahh'.")
        continue