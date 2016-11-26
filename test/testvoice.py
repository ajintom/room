import speech_recognition as sr


r = sr.Recognizer()
m = sr.Microphone()

try:
    print("Wait a sec...")
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            audio = r.listen(source)
            print("Recognizing...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                print("Ajin said {}".format(value))
                
            except sr.UnknownValueError:
                print("Oops! Didn't understand anything")

            exit()

except KeyboardInterrupt:
    pass