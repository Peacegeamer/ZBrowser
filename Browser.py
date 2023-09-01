# Import required modules
import os
import psycopg2

dbPassword = os.getenv("DBPASS")

# Connection Data
conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        host="localhost",
                        password="insert your password here!",
                        port=5432)

cur = conn.cursor()

os.system("clear")

# Greet the user
print("Hello User!")

# Ask the user what they want to search!
while True:

    print("Please choose an option: ")
    print("1. Make a definition")
    print("2. Search for a definition")

    option = input("\nEnter a number: ")

    if option == "1":
        os.system("clear")
        
        word = input("Which word do you want to add: ")

        word = word.lower()

        meaning = input("What is the meaning of the word: ")

        cur.execute(f"insert into definitions (word, meaning) values ('{word}', '{meaning}')")
        conn.commit()

        os.system("clear")
        print("Successfully added the meaning to CouscousDB")

    if option == "2":
        os.system("clear")
        word = input("Which word are you looking for? ")
        word = word.lower()

        cur.execute("select * from definitions")

        rows = cur.fetchall()

        conn.commit()

        os.system("clear")

        for row in rows:
            if row[0] == word:
                print(f"{word}:")
                print(f"{row[1]}\n")

        