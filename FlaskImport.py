from flask import Flask, render_template
request
from get_consent import get_consent
from get_adventurers_name import get_adventurers_name
from get_direction import get_direction
from get_your_age import get_your_age
from get_cave_entrance import get_cave_entrance
from get_treasure_chest import get_treasure_chest

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'] )
def home():
  consent = get_consent()

if consent == "yes":
    print("Let's go Adventurer!")

    adventurers_name = get_adventurers_name()
    print("Hello and Welcome to the enchanted Universe, " + adventurers_name)
    
    print("You find yourself in a forest on a mountain's side, you can barely see due to the lack of sunlight reflected by the dense foilage, you hear a river flowing nearby, you are being followed by a band of wild human-like creatures carrying clubs, too hairy and too broad and thick-boned to be humans, you think.....")
    


    if direction.lower() == "straight":
        print("You decide to walk straight towards the river bed, and soon enough, you come across a beautiful stream. You take a good look at it and notice that the water is clear and refreshing.")

      

    elif direction.lower() == "left":
        print("You go left, and you find a dirt road that you walk along for a while.")
    else direction.lower() == "right":
        your_age = input("Are you 21 or older? Y or N")  
        
    if your_age.upper() == "Y":
            print("You can proceed.")
            print("You decide to stay and watch the sunset over the mountain, and soon enough, you come across a small cave.")
                cave_entrance = input("Do you want to enter the cave? Y or N")
    elif your_age.upper() == "N":
            print("You are too young to proceed. Go back to the forest and find the way to the river bed, and look for the lotus flower that shines in the dark.")
            
   
    if cave_entrance.upper() == "Y":
        print("You enter the cave and find a secret passage leading to a hidden treasure chest.")
      
                 

            if treasure_chest.upper() == "Y":
                    print("You open the treasure chest and find a magical sword that can defeat any creature that comes your way.")
                    print("Congratulations " + adventurers_name + "! You have completed your adventure with Python and me!")  
                    
            else print("You decide not to enter the cave. Stay outside and wait for help.")        
    else print("You decide not to open the treasure chest, and you keep exploring the cave.")    
   
   return render_template('result.html', result=result)
    return render_template('index.html', name='Yes')

if __name__ == '__main__':
    app.run(debug=True)

# /Users/amakki/Library/Python/3.12/lib/python/site-packages/jedi/third_party/typeshed/third_party/2and3/jinja2