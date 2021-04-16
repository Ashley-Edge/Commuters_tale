import time

black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'

def game_over():
    print(" ")
    print(red(r"""
          _____   ___  ___  ___ _____   _____  _   _ ___________ 
         |  __ \ / _ \ |  \/  ||  ___| |  _  || | | |  ___| ___ \ 
         | |  \// /_\ \| .  . || |__   | | | || | | | |__ | |_/ /
         | | __ |  _  || |\/| ||  __|  | | | || | | |  __||    / 
         | |_\ \| | | || |  | || |___  \ \_/ /\ \_/ / |___| |\ \ 
          \____/\_| |_/\_|  |_/\____/   \___/  \___/\____/\_| \_|
    """))
    time.sleep(1)
    print(" ")
    print(" ")
    print("Brought to you by The Three Amigos; Ashley Edge, Robert Holland and Tom Neuman")
    time.sleep(2)
    print(" ")
    print(" ")
def at_work():
    print(" ")
    time.sleep(0.5)
    print("Finally you made it")
    time.sleep(1.5)
    print(r"""
            .........
            .'------.' |       
           | .-----. | |
           | |     | | |
         __| |     | | |;. _______________
        /  |*`-----'.|.' `;              //
       /   `---------' .;'              //
 /|   /  .''''////////;'               //
|=|  .../ ######### /;/               //|
|/  /  / ######### //                //||
   /   `-----------'                // ||
  /________________________________//| ||
  `--------------------------------' | ||
   : | ||      | || |__LL__|| ||     | ||
   : | ||      | ||         | ||     `""'
   n | ||      `""'         | ||
   M | ||                   | ||
     | ||                   | ||
     `""'                   `""'
""")
    time.sleep(1)
    print("Thankfully no more unexpected events......")
    time.sleep(1.5)
    print("     ....Until the journey home.....")
    time.sleep(1.5)
    print(" ")
    time.sleep(0.5)
    print(" ")
    time.sleep(0.5)
    print("Brought to you by The Three Amigos; Ashley Edge, Robert Holland and Tom Neuman")
    time.sleep(2)
def you_loose():
    game_over()
    time.sleep(1)
def dragon():
    print ("With your shiny new sword in hand you leave the wizard behind and carry on with your walk.")
    print(" ")
    time.sleep(1)
    print("You see some smoke in the distance.....")
    time.sleep(0.5)
    print(r"""
                        _                                                               
                 (`  ).                   _                   
                 (     ).              .:(`  )`.           
    )           _(       '`.          :(   .    )         
            .=(`(      .   )     .--  `.  (    ) )         
           ((    (..__.:'-'   .+(   )   ` _`  ) )                     
    `.     `(       ) )       (   .  )     (   )  ._  
      )      ` __.:'   )     (   (   ))     `-'.-(`  ) 
    )  )  ( )       --'       `- __.'         :(      )) 
    .-'  (_.'          .')                    `(    )  ))  
                      (_  )                     ` __.:'     
    --..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.     
""")
    print(" ")
    print(" ")                                    
    time.sleep(2)
    print("The smoke leads you to a dragon! Sound asleep blocking your path to work.")
    time.sleep(2)
    print(" ")
    print(" ")
    print(magenta(r"""
                            ^    ^  
                           / \  //\ 
             |\___/|      /   \//  .\ 
             /O  O  \__  /    //  | \ \ 
            /     /  \/_/    //   |  \  \ 
            @___@'    \/_   //    |   \   \ 
               |       \/_ //     |    \    \ 
               |        \///      |     \     \ 
              _|_ /   )  //       |      \     _\ 
             '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
             ,-{        _      `-.|.-~-.           .~         `.
             '/\      /                 ~-. _ .-~      .-~^-.  \ 
                 `.   {            }                   /      \  \ 
               .----~-.\        \-'                 .~         \  `. \^-.
              ///.----..>    c   \             _ -~             `.  ^-`   ^-_
               ///-._ _ _ _ _ _ _}^ - - - - ~                     ~--,   .-~
                                                                     /.-'
"""))
    print(" ")
    time.sleep(2)
    print(" ")
    print("It's blocking your path, {} you can't be late to work again!".format(name))
    print(" ")
    time.sleep(0.5)
    print("You have 3 options.......")
    time.sleep(0.5)
    print("1 - Wave your sword at the dragon screaming. 2 - Try to sneak past, it is asleep afterall. 3 - Softly ask politly If she doesnt mind moving to let you past. ")
    time.sleep(0.5)
    print(" ")
    time.sleep(0.5)
    response = input ("What will you do? [1/2/3] ")
    time.sleep(0.5)
    print(" ")
    if response == "1":
        print("'AAAAAAAAA---oof.... ouch! ")
        time.sleep(0.5)
        print(" ")
        print(r"""
                 .---")
                / # o        
                \,__>          
             .o-'-'--._          You drop the sword!!  
            / |\_      '.")
           |  |  \   -,  \           {} it's far to heavy!
           \  /   \__| ) |    
            '|_____[)) |,/               You've dropped it right on your leg.
               |===H=|\ >> 
               \  __,| \_\                   GO TO A&E, you arn't cut out for this.
            \/   \  \_\ 
                |\    |  \/ 
                | \   \   \\ 
                |  \   |   \\ 
                |__|\ ,-ooD \\ 
                |--\_(\.-'   \o 
                '-.__)
""".format(name))
        print(" ")
        time.sleep(2)
        you_loose()
    elif response == "2":
        print(" ")
        time.sleep(0.5)
        print("                'WHO DISTURDES MY SLUMBER?' the dragon shouts  'RAWW!!'")
        time.sleep(0.5)
        print("")
        print(magenta(r"""
                                        /|               |\                              
                                       / | ___-------___ | \                             
           CHOMP, MUNCH, CRUNCH     vv/  \/ ^ /\   /\ ^ \/  \                            
                                   vv|   (  O-. \ / .-O  )   |                          
                                  /-\/   ^-----^-V-^-----^   \/-\                        
                                /-      (~ 0O0 ~) (~ 000 ~)     -\                       
                               <        (~ OOO ~) (~ 000 ~)       >                      
                                \-      (____---===---____)     -/                       
                                 \-   /\ \ \|         |/ / /\  -/                        
                                 -/\-/  \ \ V         V / /  \-/\-                       
                                    v    \ \           / /    v                          
                                          \ \ A     A / /                                
                                           \_\^-----^/_/                                 
                                            \_/\___/\_/                                  
                                              \_____/  
"""))
        print(" ")
        time.sleep(2)
        print("          All that is left of you {} is your briefcase and shiny new sword.".format(name))
        time.sleep(2)
        print(" ")
        you_loose()
    elif response == "3":
        print("Really? You're going to ask?....... well ok.")
        print(" ")
        time.sleep(0.5)
        print("     The dragon awakes... rolls over and looks straight at you.")
        print(" ")
        time.sleep(0.5)
        print(magenta(r"""
                                    ^\    ^                  
                                   / \\  / \                
                                  /.  \\/   \      |\___/|   
               *----*           / / |  \\    \  __/  O  O\       What? Where? Who are you my dear?' the says dragon softly 
               |   /          /  /  |   \\    \_\/  \     \     
              / /\/         /   /   |    \\   _\/    '@___@      'Sorry ma'am, I'm sorry to have disturbed you, 
             /  /         /    /    |     \\ _\/       |U                but I need to get to work and your lovely tail is blocking the path'"
             |  |       /     /     |      \\\/        |          
             \  |     /_     /      |       \\  )   \ _|_         'Such lovely manners from a human is rare! 
             \   \       ~-./_ _    |    .- ; (  \_ _ _,\               Back in my day a human would sooner wack you with a sword that have a lovely chat with me.
             ~    ~.           .-~-.|.-*      _        {-,        
             \      ~-. _ .-~                 \      /\'          
             \                   }            {   .*               
                ~.                 '-/        /.-~----.             
                  ~- _             /        >..----.\\\               
                      ~ - - - - ^}_ _ _ _ _ _ _.-\\\                  
        """))
        print(" ")
        time.sleep(2)
        print("The dragon steps aside to let you pass, waving 'Bye {}! Have a good day at work!'".format(name))
        time.sleep(0.5)
        at_work()
        time.sleep(1)
    else:
        print("That is not what i asked.....")
        time.sleep(0.5)
        dragon()
        time.sleep(1)
def wrong_answer():
    print(" ")
    time.sleep(1)
    print(red("BOOM!!!") + yellow(" THE CAULDREN EXPLODES"))
    time.sleep(1)
    print(r"""
       _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
              /   \
_____________/_ __ \_____________
    """)
    time.sleep(2)
    print("'Oh dear thats the wrong answer, go back to when we first met'")
    time.sleep(1.5)
    wizard_interaction()
def recieve_sword():
    print(" ")
    print(yellow("'!!CONGRATULATIONS!!'"))
    print(" ")
    time.sleep(0.5)
    print("'{} you have really helped me'".format(name))
    time.sleep(0.5)
    print("'To show my gratitude please take this new shiny sword'")
    time.sleep(0.5)
    print(yellow(r"""
            _
 _         | |
| | _______| |---------------------------------------------\
|:-)_______|==[]============================================>
|_|        | |---------------------------------------------/
           |_|
"""))
    time.sleep(2)
    dragon()
def wizard_interaction():
    print(r"""                   
                   .
         /^\     .
    /\   "V"
   /__\   I      O  o
  //..\\  I     .
  \].`[/  I
  /l\/j\  (]    .  O
 /. ~~ ,\/I          .
 \\L__j^\/I       o
  \/--v}  I     o   .
  |    |  I   _________
  |    |  I c(`       ')o
  |    l  I   \.     ,/
_/j  L l\_!  _//^---^\\_  
""")
    time.sleep(2)
    print("You stumble upon a wizard huddled around a cauldron")
    print(" ")
    time.sleep(0.5)
    print("He cackles '{}, if you can help me finish my potion by answering my maths puzzle'".format(name))
    time.sleep(0.5)
    print(" ")
    time.sleep(0.5)
    print("'I shall reward you with a nice shiny sword")
    print(" ")
    time.sleep(0.5)
    answer = input("'What is 5 * 10??' ")
    time.sleep(0.5)
    if answer == "50":
        recieve_sword()
        time.sleep(1)
    else:
        wrong_answer()
        time.sleep(1)
def walk():
    print(" ")
    print("You have decided to take a nice stroll to work, very healthy.")
    time.sleep(1)
    wizard_interaction()
    time.sleep(1)
def music():
    print("If you're late you're late, its a rubbish job anyway.")
    print(" ")
    time.sleep(0.5)
    print("You sit back and indulge your dodgy taste in music.")
    time.sleep(0.5)
    print("You join in loudly," )
    time.sleep(0.5)
    print("")
    print("'uh, uh, uh, uh staying ....?'.")
    time.sleep(0.5)
    song = ("alive, staying alive") 
    song = input("      Go on, its you're favourite song (HINT - finish the lyric) ").lower()
    print(" ")
    if  song == "alive":
        print("Very nice singing. a little embarrassing maybe.")
        time.sleep(0.5)
        print(r"""
             
            //\\ \
\|/        ///_\\\\
:/>`      /(| '|'\\\
 Y/\      )))\_~_/((
  \ \       _/ V  \_
   \ \.-" ._ \___/   \
    \ _.-" \   o    / |      ***You got it right!****
     "     |       / ||      You could be professional
          /       /  ||
        /        /   ||
       |    __  :    ||_
       |   / \   \  '|\`
       |  |   \   \
       |  |    `.  \
       |  |      \  \
       |  |       \  \
       |  |        \  \
       |  |         \  \
       /__\          |__\
       /.|            |.\_
      `-''            ``--'
        """)
        time.sleep(2)
        print("That made the traffic jam fly by")
        time.sleep(1)
        at_work()
        time.sleep(1)    
    else:
        print("Wrong.......So close yet so far")
        time.sleep(0.5)
        another_go = input("Would you like another go? [Y/N] ").upper()
        if another_go == "Y":
                print("Great")
                time.sleep(0.5)
                drive2()
                time.sleep(1)
        else:
            game_over()
            time.sleep(1)
def strop():
    print(" ")
    print("Feel better? Still stuck in traffic though, maybe try something else.")
    print(" ")
    time.sleep(1)
    drive2()
    time.sleep(1)
def drive2():
    print("...[1]Get out and walk, [2]Settle in, lean back and listen to some music, or [3]Beep your horn furiously. ")
    time.sleep(0.5)
    walk_music_strop = input("It's your day [1/2/3] ")
    if walk_music_strop == "1":
        walk()
        time.sleep(1)
    elif walk_music_strop == "2":
        music()
        time.sleep(1)
    elif walk_music_strop == "3":
        strop()
        time.sleep(1)
    else:
        print("That is not what I asked.....")
        time.sleep(0.5)
        drive2()
        time.sleep(1)
def drive1():
    print(" ")
    time.sleep(0.5)
    print(green(r"""
      ________________
      /        |       \            You get in the car, it eventually starts
 ____/_________|________\ _______ 
 )______/-\________________ /-\__):,
        \_/                 \_/ 
    """))
    time.sleep(2)
    print("Oh no! {}, you have got caught in the traffic and are barely moving.".format(name))
    time.sleep(0.5)
    print(" You dont want to be late again")
    print(" ")
    time.sleep(0.5)    
    print("What are you going to do?")
    print(" ")
    drive2()
    time.sleep(1)
def sickie():
    print(" ")
    print(red("You're an adult. Go to work!"))
    time.sleep(0.5)
    level_one()
    time.sleep(1)
def level_one():
    print(" ")
    print("Its a nice day today and you have the choice of how to travel to the office")
    time.sleep(0.5)
    print(" ")
    print("You have 3 options.... [1] Walk to work [2] Pull a sickie  or [3] Drive.")
    time.sleep(0.5)
    print(" ")
    walk_sickie_drive = input("Which do you choose? [1/2/3] ")
    if walk_sickie_drive == "1":
        walk()
        time.sleep(1)
    elif walk_sickie_drive == "2":
        sickie()
        time.sleep(1)
    elif walk_sickie_drive == "3":
        drive1()
        time.sleep(1)
    else:
        print("That is not what I asked.....")
        time.sleep(0.5)
        print(" ")
        level_one()
def start_game():
    print(" ")
    print(" ")
    print(red("Sit back, maximise your screen (so this is all on one line for full effect) and enjoy! ----------------------------------------------------------------------->"))
    time.sleep(2)

    print(r"""

     ___          ______   ______   .___  ___. .___  ___.  __    __  .___________. _______ .______      __     _______.   .___________.    ___       __       _______ 
    /   \        /      | /  __  \  |   \/   | |   \/   | |  |  |  | |           ||   ____||   _  \    (_ )   /       |   |           |   /   \     |  |     |   ____|
   /  ^  \      |  ,----'|  |  |  | |  \  /  | |  \  /  | |  |  |  | `---|  |----`|  |__   |  |_)  |    |/   |   (----`   `---|  |----`  /  ^  \    |  |     |  |__   
  /  /_\  \     |  |     |  |  |  | |  |\/|  | |  |\/|  | |  |  |  |     |  |     |   __|  |      /           \   \           |  |      /  /_\  \   |  |     |   __|  
 /  _____  \    |  `----.|  `--'  | |  |  |  | |  |  |  | |  `--'  |     |  |     |  |____ |  |\  \----.  .----)   |          |  |     /  _____  \  |  `----.|  |____ 
/__/     \__\    \______| \______/  |__|  |__| |__|  |__|  \______/      |__|     |_______|| _| `._____|  |_______/           |__|    /__/     \__\ |_______||_______|
                                                                                                                                                                      

""")
    time.sleep(2)

    print(blue(r"""
       .-.-.
  ((  (__I__)  ))
    .'_....._'.
   / / .12 . \ \
  | | '  |  ' | |
  | | 9  /  3 | |
   \ \ '.6.' / /
    '.`-...-'.'
     /'-- --'\
    |||||||||||
    """))
    time.sleep(1)
    print("Wakey Wakey! Good morning")
    time.sleep(0.5)
    global name
    name = input("What is your name? ")
    time.sleep(0.5)
    print("Hello {}, it's so great to meet you.".format(name))
    time.sleep(0.5)
    print(" ") 

    response = input("Would you like to play? [Y/N] ").upper()
    print(" ")
    if response == "Y":
        print("Great, let's start.")
        level_one()
        time.sleep(1)  
    elif response == "N":
        print("Fine then, be like that and go back to bed.")
        time.sleep(1)
        game_over()
    else:
        print("Try again, I didn't recognise that.")
        start_game()
start_game()