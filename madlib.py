
import time
#asking if player is ready
print("Ready to play a round of MadLibs?")

while True:

    choice = input("Yes/No: ")

    if choice in ('Yes', 'yes'):

        if choice == 'Yes':
            print("Fabulous!")

            time.sleep( 1 ) #pause

            print("To play, enter in a word that satisfies the question")

            time.sleep( 3 )

            print("For example, if asked for an adjective, you could say big")

            time.sleep( 3 )

            print("Have fun!")

            time.sleep( 4 )

            adjective1 = input("Enter an Adjective: ")
            adjective2 = input("Enter an Adjective: ")
            typeofbird = input("Enter a type of bird: ")
            roominhouse = input("Enter a type of room in a house: ")
            verbpast = input("Enter a verb (past tense): ")
            verb = input("Enter a verb: ")
            name = input("Enter a name: ")
            noun1 = input("Enter a noun: ")
            liquid = input("Enter a type of liquid: ")
            verbing = input("Enter a verb (ending in -ing): ")
            body = input("Enter a part of the body (plural): ")
            noun2 = input("Enter a noun (plural): ")
            verbing2 = input("Enter a verb(ending in -ing): ")
            noun3 = input("Enter a noun: ")

            time.sleep( 5 )

            print("It was a " + adjective1 + ", cold November day. I woke up to the " + adjective2 + " smell of " + typeofbird + " roasting in the " + roominhouse + " downstairs. I " + verbpast + " down the stairs to see if I could help " + verb + " the dinner. My mom said, 'See if " + name + " needs a fresh " + noun1 + ".' So I carried a tray of glasses full of " + liquid + " into the " + verbing)
            print("room. When I got there, I couldn't believe my " + body + ". There were " + noun2 + " " + verbing2 + " " + noun3 + "!")

            time.sleep( 3 )

            print("Play again soon!")

            exit()
        
        if choice == 'yes':
            print("Fabulous!")

            time.sleep( 1 ) #pause

            print("To play, enter in a word that satisfies the question")

            time.sleep( 3 )

            print("For example, if asked for an adjective, you could say big")

            time.sleep( 3 )

            print("Have fun!")

            time.sleep( 4 )

            adjective1 = input("Enter an Adjective: ")
            adjective2 = input("Enter an Adjective: ")
            typeofbird = input("Enter a type of bird: ")
            roominhouse = input("Enter a type of room in a house: ")
            verbpast = input("Enter a verb (past tense): ")
            verb = input("Enter a verb: ")
            name = input("Enter a name: ")
            noun1 = input("Enter a noun: ")
            liquid = input("Enter a type of liquid: ")
            verbing = input("Enter a verb (ending in -ing): ")
            body = input("Enter a part of the body (plural): ")
            noun2 = input("Enter a noun (plural): ")
            verbing2 = input("Enter a verb(ending in -ing): ")
            noun3 = input("Enter a noun: ")

            time.sleep( 5 )

            print("It was a " + adjective1 + ", cold November day. I woke up to the " + adjective2 + " smell of " + typeofbird + " roasting in the " + roominhouse + " downstairs. I " + verbpast + " down the stairs to see if I could help " + verb + " the dinner. My mom said, 'See if " + name + " needs a fresh " + noun1 + ".' So I carried a tray of glasses full of " + liquid + " into the " + verbing)
            print("room. When I got there, I couldn't believe my " + body + ". There were " + noun2 + " " + verbing2 + " " + noun3 + "!")

            time.sleep( 3 )

            print("Play again soon!")

            exit()

    elif choice in ('No', 'no'):
        
        if choice == 'No':
            print("Darn. Maybe next time?")
            exit()
        
        elif choice == 'no':
            print("Darn. Maybe next time?")
            exit()
    else:
        print("Please enter a valid answer")
