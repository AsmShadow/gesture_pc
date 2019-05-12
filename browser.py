import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('com4',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print incoming
    
    if 'Play/Pause' in incoming: #Go To Arduino Website
        pyautogui.typewrite('https://www.arduino.cc/')
        pyautogui.press('enter')
        
    if 'Rewind' in incoming: #Closing A Tab
        pyautogui.keyDown('ctrl')
        pyautogui.press('f4')
        pyautogui.keyUp('ctrl')

    if 'Forward' in incoming: #Opening A New Tab
        pyautogui.keyDown('ctrl')
        pyautogui.press('t')
        pyautogui.keyUp('ctrl')

    if 'Vup' in incoming: #Scrooling Web Page
        pyautogui.press('pagedown')

    if 'Vdown' in incoming: #Changing the web tab
        pyautogui.keyDown('ctrl')
        pyautogui.press('tab')
        pyautogui.keyUp('ctrl')

    incoming = "";
