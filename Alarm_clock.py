# import the libraries(pyttsx3,datetime and webdriver)
import pyttsx3,datetime,time
print("Welcome to the Abhinav's Alarming Interface")
print("This is a 24 hours format alarm clock")
name=input("Enter your name")
tym=input("Enter the time in 24 hrs format with hour and minute seperated with :")
while True:
    time.sleep(1)
    now_time=datetime.datetime.now().strftime("%H:%M")
    if tym==now_time:
        c=0
        while c<10:
            c=c+1
            engine=pyttsx3.init()
            v=engine.getProperty("voices")
            engine.setProperty("voice",v[32].id)
            engine.say("Wake up"+str(name))
            engine.runAndWait()
        print("Thankyou for using this interface")
        break