import speech_recognition as sr
from os import system
import time
import serial
import pygame
import os
import re

r = sr.Recognizer()
m = sr.Microphone()

#constants begins here

global speaker1
global speaker2
global speaker

speaker1='Karen'
speaker2='Veena'
speaker=speaker2

speed1='60'
speed2='80'

global iflag
iflag=0

global fname
fname='cow took'

index=0

blue_l=['blue', 'bluestacks', 'bluetooth', 'bluesteps','bruises']
RGB_l=['rgb','rcb','rdb','attributes','urgent','rgv']
both_l=['both','also','but']

on_l=['on']
off_l=['off','of','f','ok']
blink_l=['blink','blank','bling','drink','dublin','sibling','link','bring']
change_l=['change','swap']
dim_l=['dim','reduce','film','sim']

brightness_l=['brightness']
fast_l=['fast','quick','quickly','quicker']
slow_l=['slow','slowly']
diffspeed_l=['different speeds','different speed']
samespeed_l=['same speed','same speed']
seconds_l=['seconds']



subject_list=[blue_l,RGB_l,both_l]
function_list=[on_l,off_l,blink_l,change_l,dim_l]
property_list=[brightness_l,fast_l,slow_l,diffspeed_l,samespeed_l,seconds_l]


#constants end here

#functions begin here----------------------------------------------------------


#def ser_num(num):




def TextAI(str ):
    
    #fuckin declarations, fix this shit-------------
    bye=["done","buy","bye"]

    status=[]

    global s_flag
    global f_flag
    global p_flag
    
    s_flag=0
    f_flag=0
    p_flag=0
    
    #declarations end here for textAI---------------
    
    
    #list=re.findall(r'\w+', str)
    str=str.lower()
    
    str=str.replace('%',' ')
    num_list=[int(s) for s in str.split() if s.isdigit()]

    list=str.split()
    list=[x.encode('UTF8') for x in list]
    
    #list=[ 'the', 'bluetooth', 'on', 'off', 'and', 'rgb', 'strips', 'to', 'blink']
    #print list
    #print num_list
    f=0
    for word in list:
        if (word in bye):
            tell('Buh bye Ajin')
            ser.close()
            exit()
        
        
        if ('*' in word):
            tell('dare you fuckin swear at me. These I S T E Juniors will hate you')
            f=1
        for sl in subject_list:
            for w in sl:
                if (word == w):
                    #status.append(sl[0])
                    if (s_flag==0):
                        subject1=sl[0]
                        print "sub1="+subject1
                        ser.write(subject1+'\n')
                        tell(subject1)
                        s_flag=1
                    elif (s_flag==1):
                        subject2=sl[0]
                        print "sub2="+subject2
                        ser.write(subject2+'\n')
                        tell(subject2)
                        s_flag=2
                    break
            if (s_flag>1): break
    

        for fl in function_list:
            for fw in fl:
                if (word == fw):
                    #status.append(fl[0])
                    if (f_flag==0):
                        function1=fl[0]
                        print "f1="+function1
                        ser.write(function1+'\n')
                        tell(function1)
                        f_flag=1
                    elif (f_flag==1):
                        function2=fl[0]
                        print "f2="+function2
                        ser.write(function2+'\n')
                        tell(function2)
                        f_flag=2
                    break
            if (f_flag>1): break


        for pl in property_list:
            for pw in pl:
                if (word == pw):
                    #status.append(pl[0])
                    if (p_flag==0):
                        property1=pl[0]
                        print "Pr1="+property1
                        ser.write(property1+'\n')
                        p_flag=1
                    elif (p_flag==1):
                        property2=pl[0]
                        print "Pr2="+property2
                        ser.write(property2+'\n')
                        p_flag=2
                    break
        if (p_flag>1): break
            
#ser_num(num_list[0])
#   ser_num(num_list[1])
    #ser.write("reset"+'\n')
    if (f==0):
        tell('.. executing ..')
    
    #time.sleep(1)
    ser.write("execute"+'\n')
    
    
    return



def tell(sentence):
    command='say --rate '+speed1+' -v '+speaker+' '+sentence
    system(command)
    return


def hear(iflag ):
    ser.write('\n')
    #print "\n\ninside hear\n"
    while True:
        
        
        print("\n\n-Hit enter to continue...\n-Hit space to exit\n-Type command\n\n")
        if ((iflag==1) or (iflag==0)):
            i=raw_input()
            if (i==' '):
                #tell('exiting program....fuck off ' +fname+'.... i fuckin hate you')
                tell('thank you babe ')
                ser.close()
                exit()
            elif (i==''):
                randomshit=0
            else:
                #tstr=raw_input("\n\nType it out: \n\n")
                TextAI(i )
                hear(iflag )
    
    
        print iflag
        
        n = sr.Microphone()
        os.system('clear')
        print("\n\nSay something!")
        pygame.mixer.music.play()
        time.sleep(0.2)
        
        
        
        with n as source:
            audio = r.listen(source)
            print("\n\nRecognizing...\n\n")
            try:
                # recognize speech , scam scenes from google :p
                value = r.recognize_google(audio)
                print("Ajin said {}".format(value))
                print "\n\n"
                TextAI(value )
                #print status
                iflag=1
            except sr.UnknownValueError:
                print("\n\nOops! Didn't understand anything")
                tell('Oops ! I dint get you...')
                hear(iflag )
                return

def callibrate():
    with m as source:
        r.adjust_for_ambient_noise(source)
        os.system('clear')
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        
        #if (os.path.isfile("threshold.txt")):
        f=open("threshold.txt","w")
        f.write('%d'%r.energy_threshold)
        f.seek(0)
        f.close()
        print(r.energy_threshold)
        hear(iflag )
            
            
            
        print "\n\nEnd\n\n"

#functions end here---------------------------------------------------------

try:
    pygame.init()
    pygame.mixer.music.load("Beep1.wav")
    
    iflag=0
    
    #ser=serial.Serial("/dev/tty.usbserial-A9G7JH5T",9600)
    ser=serial.Serial("/dev/cu.usbmodem1421",9600)
    
    os.system('clear')
    os.system('open -a Terminal')
    check=raw_input("\n-Press enter to initiate\n-Press c to callibrate\n-Press q to initiate quick start\n\n")
    
    if (check=='q'):
        f=open("threshold.txt","r")
        f.seek(0)
        thresh=int(f.read())
        print thresh
        f.close()
        r.energy_threshold=thresh+1
        print r.energy_threshold
        hear(iflag )
    
    elif (check=='c'):
        tell('Speak after the beep')
        callibrate()
    
    else:
        
        print("Wait a sec...")
        tell('Hi ajin')
        time.sleep(0.3)
        tell('Please wait for a while. Till i callibrate the surroundings')
        time.sleep(0.5)
        tell('Speak after the beep')

        callibrate()
        
#        with m as source:
#            r.adjust_for_ambient_noise(source)
#            os.system('clear')
#            print("Set minimum energy threshold to {}".format(r.energy_threshold))
#            
#            #if (os.path.isfile("threshold.txt")):
#            f=open("threshold.txt","w")
#            f.write('%d'%r.energy_threshold)
#            f.seek(0)
#            f.close()
#            print(r.energy_threshold)
#            hear(iflag)
#            
#
#
#            print "\n\nEnd\n\n"

except KeyboardInterrupt:
    pass



