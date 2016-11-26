import speech_recognition as sr
from os import system
import time
import serial
import pygame

r = sr.Recognizer()
m = sr.Microphone()

try:
    pygame.init()
    pygame.mixer.music.load("Beep1.wav")
    
    ser=serial.Serial("/dev/tty.usbserial-A9G7JH5T",9600)
    
    print("Wait a sec...")
    system('say -v Karen "Hi Ajin !"')
    time.sleep(0.3)
    system('say -v Karen "Please wait for a while. Till i callibrate the surroundings "')
    time.sleep(0.5)
    system('say -v Karen "Speak after the beep"')
    
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        
        while True:
            
            
            
            print("Say something!")
            
            pygame.mixer.music.play()
            time.sleep(0.2)
            audio = r.listen(source)
            print("Recognizing...")
            try:
                # recognize speech , scam scenes from google :p
                value = r.recognize_google(audio)
                print("Ajin said {}".format(value))
        
        
            
                
            except sr.UnknownValueError:
                print("Oops! Didn't understand anything")
            
            
            
            exit()

except KeyboardInterrupt:
    pass