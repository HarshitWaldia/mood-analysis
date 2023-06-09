# Importing module
from module_Mood import check_mood
import mysql.connector

# Creating connection object


mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "Harshit",
    database ="healthsys"
)

# checking connection establishment 
if (mydb.is_connected):
    print("connection established")

# Printing the connection object    
print(mydb)


# Importing image module PIL i.e Python Image Library

import PIL

# Importing  Image 

from PIL import Image


#Importing MODULE 1 CREATED BY TEAM HSP
import module_img

from module_img import *

print("\n")


# MAIN PROGRAM


"""USER NAME """

USER=input("ENTER NAME >>> ")


o=USER.title() #new code edited resently
"""import re
if(bool(re.match('^[0-9]*$',o))==True):
    print("invalid !!!!")
    quit()
else:
    print("valid name")"""
import re
if(bool(re.match('^[a-zA-Z" "]*$',o))==True):
    print("valid")
    
else:
    print("invalid")
    quit()


print("HI !! ",o," HOW ARE YOU FEELING ....")

# Moods
which_mood = {
    'happy':0,
    'sad':1,
    'angry':2,
    'gaming':3,
    'neutral':4,
    'all':5
}

mood = input(">>> ")
mood=mood.lower()

# if mood not in set("heartbroken",
# "unhappy","depressed","miserable","sorry","bad","melancholy","upset","worried",
# "sorrowful","disappointed","saddened","mournful","uneasy","hopeless","dejected","heartsick",
# "troubled","gloomy","forlorn","crestfallen","doleful","melancholic","depressing","glum","downhearted"
# ,"disconsolate","woebegone","inconsolable","joyless","despondent","downcast","wretched","woeful","brokenhearted","very good"
# ,"distressed","heavyhearted","droopy","suicidal","discouraged","low","regretful","somber","aggrieved",
# "bleak","disheartened","dispirited","weeping","morbid","desolate","sunk","unquiet","sad" ,"bitter" ,"unhappy", "sorry" ,"heartbroken","happy","happy","glad","joyous"
# ,"joyful","cheerful","cheery","jubilant","ecstatic","gleeful"
# ,"delighted","blissful","upbeat","overjoyed","elated","sunny","excited","exuberant","euphoric"
# ,"merry","hopeful","jolly","buoyant","optimistic","jovial","buoyed","exultant","enraptured","rapturous"
# ,"exhilarated","mirthful","chipper","rhapsodic","rhapsodical","blithe","jocular","gladdened","thrilled","rosy","jocund",
# "blithesome","jocose","entranced","sanguine","gladsome","lightsome","vital","smiling","energetic","spirited","pleased","satisfied"
# ,"vivacious","laughingperky","encouraged","frisky","lively","content","animated","gratified","peppy","careless","unconcerned","jaunty"
# ,"sprightly","carefree","lighthearted","springy","heartened","bouncing","grinning","zippy","easygoing","cavalier","boon","beaming","insouciant"
# ,"sprightful","happy-go-lucky","devil-may-care","good","great","gaming","games","playing" ,"game" ,"play" ,"sports" , "sporty" ,"gamer" ,"racing","food","eating","eat" ,"pastime","timepass","free","good","foody"):
#     print("invalid")
#     quit()

if check_mood(mood,which_mood['all']):
    print('invalid')
    quit()

    
    

#user data for database

#age=int(input("Whats your AGE !!\n>>>" ))
"""if (age>100):
    print("buddy !! life span of homosepians is less than 110 years")"""
while True:
  try:
    age = int(input("Enter age: ")) 
    if age>1 and age<100:
      print("Age entered successfully...")
      break;
    else:
      print("Age should be >1 and <100...")      
  except ValueError:
    print("Provide an integer value...")
    continue
    
while True:
    try:
        gender = str(input('Enter your gender (male or female):   ')).lower()
        if gender in ['male', 'female']:
            break
        else:
            print("error")
    except ValueError:
        print("Provide an string value...")
        continue    
        


print("By The Way , Where are you from ")
address=input("Address >>>")



"""
Pushing  Data To Database
"""
mood=mood.lower()



#condition for health

if (mood =="sad" or mood =="bitter" or mood=="unhappy" or mood== "sorry" or mood in[
"heartbroken",
"unhappy","depressed","miserable","sorry","bad","melancholy","upset","worried",
"sorrowful","disappointed","saddened","mournful","uneasy","hopeless","dejected","heartsick",
"troubled","gloomy","forlorn","crestfallen","doleful","melancholic","depressing","glum","downhearted"
,"disconsolate","woebegone","inconsolable","joyless","despondent","downcast","wretched","woeful","brokenhearted"
,"distressed","heavyhearted","droopy","suicidal","discouraged","low","regretful","somber","aggrieved",
"bleak","disheartened","dispirited","weeping","morbid","desolate","sunk","unquiet"]):

    health = "bad"
    

elif (mood =="happy"or mood in[
"happy","glad""joyous","joyful","cheerful","cheery","jubilant","ecstatic","gleeful"
,"delighted","blissful","upbeat","overjoyed","elated","sunny","excited","exuberant","euphoric"
,"merry","hopeful","jolly","buoyant","optimistic","jovial","buoyed","exultant","enraptured","rapturous"
,"exhilarated","mirthful","chipper","rhapsodic","rhapsodical","blithe","jocular","gladdened","thrilled","rosy","jocund",
"blithesome","jocose","entranced","sanguine","gladsome","lightsome","vital","smiling","energetic","spirited","pleased","satisfied"
,"vivacious","laughingperky","encouraged","frisky","lively","content","animated","gratified","peppy","careless","unconcerned","jaunty"
,"sprightly","carefree","lighthearted","springy","heartened","bouncing","grinning","zippy","easygoing","cavalier","boon","beaming","insouciant"
,"sprightful","happy-go-lucky","devil-may-care","good","great","very good"]):

    health = "good"
    

elif(mood=="gaming" or mood=="games" or mood=="playing" or mood=="game" or mood=="play" or mood=="sports"   or mood == "sporty" or mood=="gamer" or mood=="racing" or mood=="pastime" or mood=="timepass" or mood=="free"):
    health = "good"
elif (mood == "food" or mood in["eating","eat","foody"]):
    health="good"

     
#creating cursor{establishes conn between sql and python IDLE} 

cursor=mydb.cursor()

cursor.execute ("INSERT INTO moodlog (Name,Age,Gender,City,Mood,Health) VALUES ('{}','{}','{}','{}','{}','{}');".format(USER,age,gender,address,mood,health))





mydb.commit()





#STARTING OF MOOD DEPENDENCIED 

# NO STRING ERROR

# CONDITIONS :

if (mood =="sad" or mood =="bitter" or mood=="unhappy" or mood== "sorry" or mood in[
"heartbroken",
"unhappy","depressed","miserable","sorry","bad","melancholy","upset","worried",
"sorrowful","disappointed","saddened","mournful","uneasy","hopeless","dejected","heartsick",
"troubled","gloomy","forlorn","crestfallen","doleful","melancholic","depressing","glum","downhearted"
,"disconsolate","woebegone","inconsolable","joyless","despondent","downcast","wretched","woeful","brokenhearted"
,"distressed","heavyhearted","droopy","suicidal","discouraged","low","regretful","somber","aggrieved",
"bleak","disheartened","dispirited","weeping","morbid","desolate","sunk","unquiet"]):

    print("SO, what can i do to make your day !!\n")

    print("I Can do some cool things ,,i can play music , give you motivation , make you laugh.n")

    print("would you like to hear some music : ")

    __ans__=input("Y/N\n>>>")
    __ans__=__ans__.lower()
    
    if (__ans__=="y" or __ans__== "yes"):

        import module_music as music
        music.sad()

    else:
        pass
        
    print("Would you like to see some memes ....?\n ")
    __ans__=input("Y/N\n>>>")
    __ans__=__ans__.lower()
    
    if (__ans__=="y" or __ans__=="yes"):

        import module_img as joke
        joke.jokes()

    else:
        pass

    print("What again NOOOOOOOO....\n            THEN my boy you really need some motivation ? ")
    __ans__=input("Y/N\n>>>")
    __ans__=__ans__.lower()
    
    if (__ans__=="y" or __ans__=="yes"):

        import module_music as music
        music.motivational()

    
        
    
    
    else:
        #(__ans__=="n" or __ans__=="no"):

        print("THERE IS NOTHING I CAN DO NOW .............!!!")
        

elif (mood =="happy"or mood in[
"happy","glad""joyous","joyful","cheerful","cheery","jubilant","ecstatic","gleeful"
,"delighted","blissful","upbeat","overjoyed","elated","sunny","excited","exuberant","euphoric"
,"merry","hopeful","jolly","buoyant","optimistic","jovial","buoyed","exultant","enraptured","rapturous"
,"exhilarated","mirthful","chipper","rhapsodic","rhapsodical","blithe","jocular","gladdened","thrilled","rosy","jocund",
"blithesome","jocose","entranced","sanguine","gladsome","lightsome","vital","smiling","energetic","spirited","pleased","satisfied"
,"vivacious","laughingperky","encouraged","frisky","lively","content","animated","gratified","peppy","careless","unconcerned","jaunty"
,"sprightly","carefree","lighthearted","springy","heartened","bouncing","grinning","zippy","easygoing","cavalier","boon","beaming","insouciant"
,"sprightful","happy-go-lucky","devil-may-care","good","great","very good"]):

    print("Hope you make someone SMILE !!\n")

    print("SO, HOW can i make your day more joyful , here are certain things i can do - i can play music  , make you laugh , or i can give you motivation \n")

    print("Would you like to hear some music ???\n ")

    __ans__=input("Y/N\n>>>")
    __ans__=__ans__.lower()
    
    if (__ans__=="y" or __ans__== "yes"):
        import module_music as music
        music.happy()
    else:
        pass
        
    print("Would you like to see some memes ....?\n ")
    __ans__=input("Y/N\n>>>")
    __ans__=__ans__.lower()
    
    if (__ans__=="y" or __ans__=="yes"):

        import module_img as joke
        joke.happy()

    else:
        pass
    print(" DO need some motivation ? ")
    __ans__=input("Y/N\n>>>")
    __ans__=__ans__.lower()
    
    if (__ans__=="y" or __ans__=="yes"):

        import module_music as music
        music.motivation()

    else:
        pass
    
    print("Your chooice is : \n1- Play GAME \n2-  GAMING MUSIC")
    
    ch=int(input(">>>"))

    #gaming web site
    
    def play_game():
        import webbrowser
        webbrowser.open('http://poki.com', new=2)
        
    #memes 
      
    def memes():
        import module_img as joke
        joke.happy()
        


    #gaming music

    def gaming_music():
        music.gaming()
   


    if(ch==1):
        play_game()


    elif(ch==2):
        import module_music as music
        gaming_music()
    else :
        
       print("ALPHA TO CHARLIE !!! ITS MAY_DAY BUT YOU ARE NOOB......")
        

    


elif(mood=="gaming" or mood=="games" or mood=="playing" or mood=="game" or mood=="play" or mood=="sports" or mood=="gamer" or mood=="racing"  or mood == "sporty" or mood=="pastime" or mood=="timepass" or mood=="free"):
    print("Alpha to Charli ! Alpha to Charli!!! ")
    print("\n")
    print("Your chooice is : \n1- Play GAME \n2- MEMES\n3- GAMING MUSIC")
    
    ch=int(input(">>>"))

    #gaming web site
    
    def play_game():
        import webbrowser
        webbrowser.open('http://poki.com', new=2)
        
    #memes 
      
    def memes():
        import module_img as joke
        joke.happy()
        


    #gaming music

    def gaming_music():
        music.gaming()
   


    if(ch==1):
        play_game()
        

    elif(ch==2):
        memes()
    elif(ch==3):
        import module_music as music
        gaming_music()
    else :
        
       print("ALPHA TO CHARLIE !!! ITS MAY_DAY BUT YOU ARE NOOB......")


elif (mood == "food" or mood in["eating","eat","foody"]):

    print("1=PIZZA\n2=BURGER\n3FRENCHFRIES\n4NOODLES\n5PASSTA\n ")
    fav_food=int(input("What do you like to have : "))
    if (fav_food==1):
        import webbrowser
        webbrowser.open('https://www.dominos.co.in/',new=1)
    elif (fav_food==2):
        import webbrowser
        webbrowser.open('http://burgerking.com', new=1)
    elif (fav_food==6):
        import webbrowser
        webbrowser.open('https://www.zomato.com/',new=2)
    else :
        site=input("Enter Your Favourite site with domain : ")
        import webbrowser
        webbrowser.open(site)
