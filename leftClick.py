import time
import keyboard #pip install keyboard
import pyautogui as pya #pip install pyautogui

counter = 0

delay = float(input('How fast would you like to click?>> '))
print('You have 3 seconds to navigate to your webpage')
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('GO')

while True:
  if keyboard.is_pressed('q'):
    print('Stoping loop')
    print('Space bar was pressed ' + numbs + ' times') 
    break
  pya.click()
  counter = counter + 1
  print('This is iteration#',counter)
  time.sleep(delay)
  
