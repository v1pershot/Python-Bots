import time
import keyboard #pip install keyboard

counter = 0

while True:
  if keyboard.is_pressed('q'):
    print('Stoping loop')
    print('Space bar was pressed ' + numbs + ' times') 
    break
  keyboard.press_and_release('space')
  counter = counter + 1
  print('This is iteration#',counter)
  
