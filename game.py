#-*- coding: utf-8 -*-
import sys
from characters import *
from items import *
from text import *

def show_instructions():
  print('''
            ========

            Python's
                      ('-.        .-')               .-') _       ('-.     ('-._            .-') _    (`-.      ('-.       .-')               ('-.      .-')    .-') 
            ( OO ).-. ( OO ). (  OO) )            _(  OO)         ( OO ).-.( (  OO) )     _(OO  )_  _(  OO)     ( OO ) )(  OO) )             ( OO )  _(  OO)  ( OO ).  
   .-----.  / . --. /(_)---\_)/     '._ ,--.     (,------.        / . --. / \     .'_ ,--(_/   ,. \(,------.,--./ ,--,' /     '._ ,--. ,--.   ,------. (,------.(_)---\_) 
  '  .--./  | \-.  \ /    _ | |'--...__)|  |.-')  |  .---'        | \-.  \  ,`'--..._)\   \   /(__/ |  .---'|   \ |  |\ |'--...__)|  | |  |   |   /`. ' |  .---'/    _ |  
  |  |('-..-'-'  |  |\  :` `. '--.  .--'|  | OO ) |  |          .-'-'  |  | |  |  \  ' \   \ /   /  |  |    |    \|  | )'--.  .--'|  | | .-') |  /  | | |  |    \  :` `.  
 /_) |OO  )\| |_.'  | '..`''.)   |  |   |  |`-' |(|  '--.        \| |_.'  | |  |   ' |  \   '   /, (|  '--. |  .     |/    |  |   |  | |( OO )|  |_.' |(|  '--.  '..`''.) 
 ||  |`-'|  |  .-.  |.-._)   \   |  |  (|  '---.' |  .--'         |  .-.  | |  |   / :   \     /__) |  .--' |  |\    |     |  |   |  | | `-' /|  .  '.' |  .--' .-._)   \ 
(_'  '--'\  |  | |  |\       /   |  |   |      |  |  `---.        |  | |  | |  '--'  /    \   /     |  `---.|  | \   |     |  |  ('  '-'(_.-' |  |\  \  |  `---.\       / 
   `-----'  `--' `--' `-----'    `--'   `------'  `------'        `--' `--' `-------'      `-'      `------'`--'  `--'     `--'    `-----'    `--' '--' `------' `-----'  
            
            ''')

  print('''
            Welcome to Castle Adventuers! You are stuck in a castle, choose carefully to get out
            careful, there may be emenies your way
            collect items to survive

            ================
            ''')
inventory = []

def red_door():

  dragon();

  if len(inventory)==0:
    print('''
         You have nothing in you inventory
          ''')
    game_over()
  else:
    print('''
          What item would you like to use?
          ''')
      
def green_door():
  print('''
          You have found a healing potion! 
          Health + 100
          You may advance to the next door!
        ''')
  add_to_inventory("potion")
  display_inventory()

def blue_door():
  print('''
          You have found a sword!
          ''')
  show_sword()
  print('''
          This will be added to your inventory
          You may advance to the next door
          ''')
  add_to_inventory("sword")
  display_inventory()


          
def display_inventory():
  if len(inventory)==0:
    print('''
          =================================
          You have nothing in you inventory
          =================================
          ''')
  else:
    print("       ====================")
    for i in range(0,len(inventory)):
          print('''       Inventory:
                ''' + str(i+1) + '''. ''' + inventory[i])
    print("       ====================")

def add_to_inventory(item):
  inventory.append(item)


def game_over():
  game_over_text();
  sys.exit()

def main():
    show_instructions()
    print('''
            We commend your bravery great hero, but beyond a decision 
            lies ahead of you, and a great choice to be made.
            Three doors lie ahead of you: 
            Red door, Green door and a Blue door
            Which door will you choose?
            ''')
    door = raw_input('''
            Door: 
            ''')
    if door=="Red" or door=="red":
            red_door()
    elif door=="Blue" or door=="blue":
            blue_door()
    elif door=="Green" or door=="green":
            green_door()

    print('''
            With your heart on your sleeve and your first brand new item acquired
            you solder on ahead to the Corridor of Doom!!!!!!!!!!!!!!!!
            
        ''')
    show_owl()

    print('''
            Grettings! People call me THe Great Wise Owl!
            Only the wise of mind can pass through the Room of Knowledge....
            Complete this riddle and you may pass....
            Failure to do so will wake my 'little' friend....
            
            RIDLLE
            
            I have rivers without water,
            Forests without trees,
            Mountains without rocks
            Towns without houses.         ''')

    answer = raw_input('''What Am I? ''')

    if(answer=="Map" or answer=="map" or answer=="A map" or answer=="a map"):
        print('''
            Well Done my good friend!
            I never had doubt in you for a second....
            You may advance fowards, good luck!
        ''')
    else:
        game_over()

    print('''
        
            
    ''')


main()
