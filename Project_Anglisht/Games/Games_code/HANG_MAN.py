
#Import the needed libraries
import os
import sys
sys.path.append('..')
from Word_list import Word

import random
separator = "  "

def clear_i():
  os.system("cls")

#Prints the undersored word and chooses a random word from words
select = random.choice(Word)
used = []
tun = []
for i in range(len(select)):
  tun.append("_")

#Get the letter from the user
def quest():
  Al = input("What letter do you think is there? ")
  Al = Al.lower()
  return Al

#This function returns True if the input letter is in the word and False for the opposite
def check():
  for i in range(len(select)):
    if Al in select[i]:
      used.append(Al)
      return True
  for i in range(len(select)):
    if Al not in select[i]:
      used.append(Al)
      return False       
 
#This code checks if there are still underscores in the word
def check2():
  for i in range(len(tun)):
    if "_" in tun[i]:
      return True
  for i in range(len(tun)):
    if "_" not in tun[i]:
      return False

#This function replaces the underscore with the founded letter
def change():
  index = select.index(Al)
  tun.pop(index)
  tun.insert(index, Al)

#The sprites of the hangman
def non():
  clear_i()
  print("Hint : This word does not have double letters")
  print("    _______     ")
  print("   |     \|     ")
  print("   |      |     ")
  print("          |     ")
  print("          |     ")
  print("          |     ")
  print("          |     ")
  print("          |     ")
  print("      ____|____ ","\n")
  print("You have used --> ", separator.join(used))

def non2():
  clear_i()
  print("    _______     ")
  print("   |     \|     ")
  print("   |      |     ")
  print("  ( )     |     ")
  print("          |     ")
  print("          |     ")
  print("          |     ")
  print("          |     ")
  print("      ____|____ ","\n")
  print("You have used --> ", separator.join(used))

def non3():
  clear_i()
  print("    _______     ")
  print("   |     \|     ")
  print("   |      |     ")
  print("  ( )     |     ")
  print("   |      |     ")
  print("   |      |     ")
  print("          |     ")
  print("          |     ")
  print("      ____|____ ","\n")
  print("You have used --> ", separator.join(used))

def non4():
  clear_i()
  print("    _______     ")
  print("   |     \|     ")
  print("   |      |     ")
  print("  ( )     |     ")
  print("  /|      |     ")
  print("   |      |     ")
  print("          |     ")
  print("          |     ")
  print("      ____|____ ","\n")
  print("You have used --> ", separator.join(used))
  
def non5():
  clear_i()
  print("    _______     ")
  print("   |     \|     ")
  print("   |      |     ")
  print("  ( )     |     ")
  print("  /|\     |     ")
  print("   |      |     ")
  print("          |     ")
  print("          |     ")
  print("      ____|____ ","\n")
  print("You have used --> ", separator.join(used))
  
def non6():
  clear_i()
  print("    _______     ")
  print("   |     \|     ")
  print("   |      |     ")
  print("  ( )     |     ")
  print("  /|\     |     ")
  print("   |      |     ")
  print("  /       |     ")
  print("          |     ")
  print("      ____|____ ","\n")
  print("You have used --> ", separator.join(used))

#Winning and loosing text
R = chr(9608)  
A = chr(9618)  
L = chr(9617)  
U = chr(9600)  
M = chr(9632)  
D = chr(9604)  
E = chr(9612)  
I = chr(9616)  
X = chr(32)    
  
def ending():
  clear_i()
  print("    _______     ")
  print("   |     \|     ")
  print("   |      |     ")
  print("  ( )     |     ")
  print("  /|\     |     ")
  print("   |      |     ")
  print("  / \     |     ")
  print("          |     ")
  print("      ____|____ ","\n")
  print("YOUR WORD WAS ", separator.join(select),"\n")
  print(X+X+ A+R+U+U+U+R+L +X+ A+R+U+U+U+R+L +X+ A+R+U+E+I+U+R+L +X+ A+R+U+U+U+U+L +X+X+X+X+ A+R+U+U+U+R+L +X+ A+U+D+X+L+L+D+U+L +X+ A+R+U+U+U+U+L +X+ A+R+U+U+U+D+L)
  print(X+X+ A+R+X+L+L+R+L +X+ A+R+X+L+L+R+L +X+ A+R+X+E+I+X+R+L +X+ A+R+X+L+L+L+L +X+X+X+X+ A+R+X+L+L+R+L +X+ L+L+R+X+L+L+R+X+L +X+ A+R+X+L+L+L+L +X+ A+R+X+L+L+R+L)
  print(X+X+ A+R+X+L+L+L+L +X+ A+R+M+M+M+R+L +X+ A+R+X+E+I+X+R+L +X+ A+R+M+M+M+M+L +X+X+X+X+ A+R+X+L+L+R+L +X+ L+L+U+D+X+D+U+X+L +X+ A+R+M+M+M+M+L +X+ A+R+D+D+D+U+L)
  print(X+X+ A+R+X+U+U+R+L +X+ A+R+X+L+L+R+L +X+ A+R+X+L+L+L+R+L +X+ A+R+X+L+L+L+L +X+X+X+X+ A+R+X+L+L+R+L +X+ L+L+L+R+X+R+X+L+L +X+ A+R+X+L+L+L+L +X+ A+R+U+D+L+L+L)
  print(X+X+ A+R+D+D+D+R+L +X+ A+R+X+L+L+R+L +X+ A+R+X+L+L+L+R+L +X+ A+R+D+D+D+D+L +X+X+X+X+ A+R+D+D+D+R+L +X+ L+L+L+U+R+U+X+L+L +X+ A+R+D+D+D+D+L +X+ A+R+X+L+U+D+L,"\n")
    
def win():
  print(X+X+ A+R+U+U+U+R+L +X+ A+R+U+U+U+R+L +X+ A+R+U+D+X+L+R+L +X+ A+R+U+U+U+R+L +X+ A+R+U+U+U+D+L +X+ A+R+U+U+U+R+L +X+ A+U+U+R+U+U+L +X+ A+D+U+U+U+D+L)
  print(X+X+ A+R+X+L+L+L+L +X+ A+R+X+L+L+R+L +X+ A+R+X+U+D+X+R+L +X+ A+R+X+L+L+R+L +X+ A+R+X+L+L+R+L +X+ A+R+X+L+L+R+L +X+ L+L+L+R+X+L+L +X+ A+R+X+L+L+L+L)
  print(X+X+ A+R+X+L+L+L+L +X+ A+R+X+L+L+R+L +X+ A+R+X+L+U+D+R+L +X+ A+R+X+L+L+L+L +X+ A+R+D+D+D+U+L +X+ A+R+M+M+M+R+L +X+ L+L+L+R+X+L+L +X+ A+U+D+D+D+L+L)
  print(X+X+ A+R+X+L+L+L+L +X+ A+R+X+L+L+R+L +X+ A+R+X+L+L+U+R+L +X+ A+R+X+U+U+R+L +X+ A+R+U+D+L+L+L +X+ A+R+X+L+L+R+L +X+ L+L+L+R+X+L+L +X+ L+L+L+L+L+R+L)
  print(X+X+ A+R+D+D+D+R+L +X+ A+R+D+D+D+R+L +X+ A+R+X+L+L+L+R+L +X+ A+R+D+D+D+R+L +X+ A+R+X+L+U+D+L +X+ A+R+X+L+L+R+L +X+ L+L+L+R+X+L+L +X+ A+U+D+D+D+U+L)

#This creates the first sprite
non()
print(separator.join(tun),"\n") 
Al = quest()
  
#This loop run if the user inputs the first letter and returns True
while check() == True:
  non()
  change()
  print(separator.join(tun),"\n") 
  if check2() == True:
    Al = quest()
  elif check2() == False:
    win()
    break
   
#This one happends if the opposite happens and the first returns False
if check() == False:
  used.remove(Al)
  non2()
  print(separator.join(tun),"\n") 
  Al = quest()
  while check() == True:
    non2()
    change()
    print(separator.join(tun),"\n") 
    if check2() == True:
      Al = quest()
    elif check2() == False:
      win()
      break
      
#If again False the other sprite is shown and looped
if check() == False:
  used.remove(Al)
  non3()
  print(separator.join(tun),"\n") 
  Al = quest()
  while check() == True:
    non3()
    change()
    print(separator.join(tun),"\n") 
    if check2() == True:
      Al = quest()
    elif check2() == False:
      win()
      break

#If again False the other sprite is shown and looped
if check() == False:
  used.remove(Al)
  non4()
  print(separator.join(tun),"\n") 
  Al = quest()
  while check() == True:
    non4()
    change()
    print(separator.join(tun),"\n") 
    if check2() == True:
      Al = quest()
    elif check2() == False:
      win()
      break

#If again False the other sprite is shown and looped
if check() == False:
  used.remove(Al)
  non5()
  print(separator.join(tun),"\n") 
  Al = quest()
  while check() == True:
    non5()
    change()
    print(separator.join(tun),"\n") 
    if check2() == True:
      Al = quest()
    elif check2() == False:
      win()
      break

#If again False the other sprite is shown and looped
if check() == False:
  used.remove(Al)
  non6()
  print(separator.join(tun),"\n") 
  Al = quest()
  while check() == True:
    non6()
    change()
    print(separator.join(tun),"\n") 
    if check2() == True:
      Al = quest()
    elif check2() == False:
      win()
      break
    
#If again False the the last one is shown and the game_over text
if check() == False:
  ending()
input()
