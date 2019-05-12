import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print incoming
    
    if 'Play/Pause' in incoming: #Type Hello Everyone
        pyautogui.typewrite('Hello Everyone! Welcome To Our Project.')
        
    if 'Rewind' in incoming: #Select All
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')

    if 'Forward' in incoming: #Copy Selected Text
        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')

    if 'Vup' in incoming: #Cut Selected Text
        pyautogui.keyDown('ctrl')
        pyautogui.press('x')
        pyautogui.keyUp('ctrl')
        

    if 'Vdown' in incoming: #Pasting Text
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')

    incoming = "";
