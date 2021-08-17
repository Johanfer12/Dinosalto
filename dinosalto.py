import pyautogui, time
salto = 0
agacho = 0
while salto < 200:
    if pyautogui.pixelMatchesColor(1300, 468, (83, 83, 83)) or pyautogui.pixelMatchesColor(1290, 468, (83, 83, 83)) == True:
        pyautogui.press('up', 2)
        #pyautogui.press('down')
        salto += 1
        print(salto)
   # if  pyautogui.pixelMatchesColor(857, 377, (83, 83, 83)) == True:
    #    pyautogui.press('down')
     #   agacho += 1
      #  print(agacho)

