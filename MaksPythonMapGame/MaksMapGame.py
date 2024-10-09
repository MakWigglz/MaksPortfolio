consent = input("Do you want to have an adventure with Python and me? yes or no?")
if consent.lower() == "yes":
    print("Let's go Adventurer!")

    adventurers_name = input("What is your name?")
    print("Hello and Welcome to the enchanted Universe, " + adventurers_name + "! Let us begin...")
    print("You find yourself in a forest on a mountain's side, you can barely see due to the lack of sunlight reflected by the dense foilage, you hear a river flowing nearby, you are being followed by a band of wild human like creatures carrying clubs, too hairy and too broad and thick boned to be humans, you think.....")
    direction = input("you can go left, right, or straight towards the river bed" + "what will be your choice")   
    if direction.lower() == "straight":
        print("You decide to walk straight towards the river bed, and soon enough, you come across a beautiful stream. You take a good look at it and notice that the water is clear and refreshing.")
         if direction.lower() == "straight":    
        print("you find an abandoned Canoe, can you row?")
        canoe_row = int(input("how many rows will you row?"))  
            if canoe_row <= "7":
                print("you are lazy, you drown")
            else canoe_row > "7":
                print("you row row, row your boat, gently down the stream, merrily merrily, and soon enough, you reach the shore.")
        
    elif direction.lower() =="left":
        print("you go left, and you find a dirt road that you walk along for a while")  
    elif direction.lower() == "right":
        your_age = input("are you 21 or older? Y or N")   
        if your_age.upper() == "Y":   
            print("you can proceed.")
        else your_age.upper() == "N":
            print("You are too young to proceed." + "go back to the forest and find the way to the river bed, and look for the lotus flower that shines in the dark.")
            if your_age.upper() == "y":
        print("You decide to stay and watch the sunset over the mountain, and soon enough, you come across a small cave.")
        cave_entrance = input("do you want to enter the cave? Y or N")
        if cave_entrance.upper() == "Y":
            print("You enter the cave and find a secret passage leading to a hidden treasure chest.")
            treasure_chest = input("do you want to open the treasure chest? Y or N")
            if treasure_chest.upper() == "Y":
                print("You open the treasure chest and find a magical sword that can defeat any creature that comes your way.")
                print("Congratulations " + adventurers_name + "! You have completed your adventure with Python and me!") 
    else:
        print("invalid direction" + adventurers_name + "go back, or get lost.")
       
   
else:
    print("Boohoo! I wouldve loved to see you take the adventure, maybe next time!!!", "have a great day")    

