import time

str = ''' 
                                                                                                                       
                                                                                                                       
           ~77^            :77:                                    :.                                       !7~            
          J###P        .   Y#B:              ..           .      ?PP.                  .    ..           . ~##?    ..      
        .5#57##^    ~YGGP57B#?^PP^   !PP~ ^JPPGGY^  .5PJ?5GGY: ?P##BJ ^PP~  !PP^ .5P?JGP.:JPPGGY^  .5P?JGP.~GJ :J5PPGPJ:   
        ^G#J  B#?   ?##7::J##B..B#? .J#B! ?##7::J#B: 7##5~:!##? ^P#G~: 5#G. .G#P  7##P7~:7##?::?##^ 7##P7~:     P#B!   ?    
       !###YYYB#G. ^##7   ^##?  J#P:P#5: ^##GJJJYGG: P#P.  ?##^ :B#?  ~##!  7##~ .G#P.  .B#GJJJJGB~ G#P.        ^YPBBGY~    
    .J##J??J?Y##~ ^##J:.~G#B:  :##B#?   :G#5^:~J?^ !##!  :B#Y  J##^. 5#B^:7B#5  !##!   .P#P^:^??^ !##~       :     !B#G.   
     ?GP^     .PG7  !PBG5YPG?    JGP~     :JGGPGP?. JG5.  !GG^  7GBG! !GBPYJGG~  JG5.    .?PGPGPJ: YG5         !5GGPGPY^    
     .                ...                    ...                  ..    ..                  ...                   ...       
                                                                                                                       
                                                                                                                       
                                   ~!!                               ..                                                     
                                  ^##5                             ^YG!                                                     
                                 J##^       :?PPPP5!&  !Y5PPP5~ :5B##P~                                                    
                                 :B#5        !YY  Y##: !##J     .?##J^.                                                    
                                 ?##^       ~Y5   B#P  .?PBBG57.  Y#B.                                                      
                                :B#G~^~^^~..##Y   ##! !    ^Y##! :##J                                                       
                                !GGGGGGGGG^ ?GBPYYGG^%^YGGPPGP7. :PBG5.4                                                    
                                .             ..         .::.      .:.                                                      
                                                                                                                       
                                                                                                                       
                       ^!!.                                                                                                
                       .G#P                                                                                                 
                       7##!  ~YPPPPJ^   !55:  75Y. :557JGY 75Y!YPG5~  .!YPPPY~  !5Y.   ?5Y.                                 
                      .G#P .5#B7^^J##~ .G#5  :B#Y  J##57~::B#B?^^B#P ^G#5   ##7 ~##! .Y#G^                                  
                 ..   !##! ?##^   ^##? 7##^  J#B: :B#Y    ?##~  ^##? 5##YJJJGB? .G#J.P#P:                                   
               YBG^:^G#5  7##!..^G#G: G#P.:?##J  J##^   .B#Y   Y#B. J#B~:   ?!.  ?#GP#Y.                                    
               ^5BBBBG?.   7PBGGBP?.  JBBPY5BG: .PBY    !BG^  :GB?  .?PGPPG5~   ^###?                                      
                  .::.        .::.      .:.  ..   ..     ...    ..      .::.   ^~Y##!                                       
                                                                              :5PPJ^                                        
                                                                                                                       
                                                                                                                                                                                                                                          
        '''
                
print(str)

txt_delay = 1.0
long_delay = 3.0

character_name = input("Enter a character name:")

def game_intro():
    print("")
    print("")
    print("An avalanche has blocked your only safe route back home,")
    time.sleep(txt_delay)
    print("")
    print("You have travelled for days in search of another route,")
    time.sleep(txt_delay)
    print("")
    print("The journey has been an arduous one and has left you with no supplies,")
    time.sleep(txt_delay)
    print("") 
    print("it has cost you your only way of defending yourself when you encounted a pack of wolves and had to flee,")
    time.sleep(txt_delay)
    print("")
    print("You arrive at the entrance of an ancient ruin, beaten and half frozen to death...")
    time.sleep(txt_delay)
    print("")
    print("This is the tale of an adventurer's last journey")
    time.sleep(txt_delay)
    print("")
    print(f"The adventurer's name is: {character_name} ")
    print("")
    print("")
    enter_dungeon()


def enter_dungeon():
    # global character_name
    answer = input(f"Would you like to enter the dungeon {character_name}? (Yes/No)").lower().strip()
    time.sleep(txt_delay)
    print("")
    if answer == "yes":
        print(f"{character_name} says: 'Looks like my only option, better head inside'.")
        print("")
        entrance_hall()
    else:
        print("You make your way back outside.")
        time.sleep(long_delay)
        print("")
        print("After some time you come to your senses and decide to enter the ruin.")
        time.sleep(txt_delay)
        print("")
        enter_dungeon()
   

def entrance_hall():
    # global character_name
    print("You have entered the entrance hall") 
    time.sleep(txt_delay)
    print("")
    print("The large hallway was rife with vermin scurrying along....") 
    time.sleep(txt_delay)
    print("")
    print("The walls crumbling, looking like they might give way any second...") 
    time.sleep(txt_delay)
    print("")
    print("As you enter deeper into the endless hallway you notice two doors...") 
    time.sleep(txt_delay)
    print("")

    entrance_choice = input("Which way would you like to go? (Left/Right)").lower().strip()
    time.sleep(txt_delay)
    print("")

    if entrance_choice == "left":

        print("You approach the left door and enter")
        time.sleep(txt_delay)
        print("")
        print("You enter the dark, foul smelling room") 
        time.sleep(txt_delay)
        print("Oh no!....the exit appears to be caved in by lots of rocks...") 
        time.sleep(txt_delay)
        print("If you are strong enough, you can attempt to remove the rocks one by one") 
        time.sleep(txt_delay) 
        print("therefore running home!...")
        print("") 
        time.sleep(txt_delay)
        print("however you decide against it and you go back through the entrance hall and take the other route")
        time.sleep(txt_delay)
        print("")
        #This is the blocked hallway
        #We have to return to the entrance hall
        
        #Decided to skip the process of making the player select the right path and instead just take them straight there.
        path_to_room2()


    #right path entrance hall choice
    elif entrance_choice == "right":
        print("You approach the right door....")
        time.sleep(txt_delay)
        print("")
        path_to_room2()
    else:
        print("Some how you manage to lose your way and have arrived back at the entrance hall")
        print("")
        time.sleep(long_delay)
        entrance_hall()
           

def path_to_room2():
    print("You enter the room")
    time.sleep(txt_delay)
    print("")
    print("You see another door on the other side and approach it...")
    print("") 
    time.sleep(txt_delay)
    room2_path = input("Go through the door? (Yes/No)")
    print("")
    time.sleep(txt_delay)
    if room2_path == "yes":
        print("You continue on to the second room")
        print("")
        time.sleep(txt_delay)
        room2()
    elif room2_path == "no":
        print(f"{character_name} says: 'I don't see any other options'")
        print("")
        time.sleep(txt_delay)
        print("You continue on to room 2")
        print("")
        room2()
    else:
        print("Some how you manage to lose your way and have arrived back at the entrance hall")
        print("")
        time.sleep(long_delay)
        entrance_hall()

def room2():
    print("The small room barely has any room as it is filled with carcass's of animals that have trapped themselves in....") , 
    time.sleep(txt_delay)
    print("")
    print("You see another set of doors on the other side and approach them...")
    print("")
    time.sleep(txt_delay)
    # ^describe scene and change to lines with time library 
    room_2 = input("which door would you like to enter? (Right/Left)").lower().strip()
    print("")
    time.sleep(txt_delay)

    if room_2 == "left":
        #left path from room 2 code goes here
        print("You approach the left door and enter")
        print("")
        time.sleep(txt_delay)
        print("You are now in a narrow hallway with only one door at the bottom")
        print("")
        time.sleep(txt_delay)
        #need a description of the hallway on the left and the door at the end
        room2_left_path()
    
    elif room_2 == "right":
        print("You approach the right door and enter")
        print("")
        time.sleep(txt_delay)
        print("This room appears to be a dead end, you decide to head back")
        print("")
        time.sleep(txt_delay)
        room2()
    else:
        print("Some how you manage to lose your way and have arrived back at the entrance hall")
        print("")
        time.sleep(long_delay)
        entrance_hall()
                    
def room2_left_path():
    print("you make your way to the next door")
    print("")
    time.sleep(txt_delay)
    two_l_door = input("open the door? (Yes/No)").lower().strip()
    print("")
    time.sleep(txt_delay)
    if two_l_door == "yes":
        print("you choose to enter into the next room")
        print("")
        time.sleep(txt_delay)
        room3()
    elif two_l_door == "no":
        print(F"{character_name} says: 'I don't have a choice'")
        print(())
        time.sleep(long_delay)
        print ("You enter the next room")
        print("")
        time.sleep(txt_delay)
        room3()
    else:
        print("Some how you manage to lose your way and have arrived back at the entrance hall")
        print("")
        time.sleep(long_delay)
        entrance_hall()
                
def room3():
        print("")
        print("You approach the right door and push it open with all your strength!")
        time.sleep(txt_delay)
        print("")
        print("As the door slams shut behind you, you hear the slithering of something sinister behind you.....")
        print("")
        time.sleep(txt_delay)
        print("...while the air is thick with a humid putrid stench...")
        print("")
        time.sleep(txt_delay) 
        print("To the back of the room you notice the remanents of what was a grand staircase, left in tatters..... ")
        time.sleep(txt_delay)
        print("")
        print("...As you look above you notice daylight breaking into a large whole in the wall...")
        print("")
        time.sleep(txt_delay) 
        print("...frantically you begin to look around for aids to get you to exit.....")
        print("")
        time.sleep(txt_delay) 
        print("and you find a big thick rope covered in dust and debris on the floor...")
        print("")
        time.sleep(txt_delay) 

        room3 = input("Would you like to pick up the rope and attempt to climb out Yes/No").lower().strip()
        print("")
        time.sleep(txt_delay)
        if room3 == "yes":
            print("you pick the rope up and tie a classic loop at one end.... you fling it on the top bannister")
            time.sleep(txt_delay)
            print("")
            print("using your skill, you aim to throw it on the top bannister, which is still intact.")
            time.sleep(txt_delay)
            print("")
            print("Fantastic! You managed it on your first try!")
            time.sleep(txt_delay)
            print("")
            print("you start the climb up towards the exit...")
            time.sleep(txt_delay)
            print("")
            print("Awesome you have reached the top! Run to the exit!")
            time.sleep(txt_delay)
            print("")
            last_choice()
                        
        else:
            print("You decide not to use the rope")
            print("")
            time.sleep(txt_delay)
            print("That was your only way out")
            print("")
            time.sleep(txt_delay)
            print("Game Over!")
        
def last_choice():
    final_choice = input("Exit the ruin? Yes/No").lower().strip()
    time.sleep(txt_delay)
                        
    if final_choice == "yes":
        print("As you walk out of ruin, you see a broken pathway covered by weeds....")
        time.sleep(txt_delay)
        print("")
        print("You begin to walk along the path...and what seems like an age..you finally see a road on the horizon")
        time.sleep(txt_delay)
        print("")
        print("You run towards the road. Finally! You recognise where you are and make your way home.")
        print("")
        time.sleep(long_delay)
        print("The End.")
        time.sleep(txt_delay)
        #brief description of the character leaving and getting back home
    else:
        print(F"{character_name}: I'm not ready")
        print("")
        time.sleep(long_delay)
        print ("You decide to remain in the ruin")
        print("")
        time.sleep(txt_delay)
        print("Game Over!")
        
    
    
game_intro()            

        