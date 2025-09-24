import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit 
import user_config
import Gemin_request as ai
from wheaterapi import get_weather


import mtranslate




engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)  # Adjust index based on output
engine.setProperty("rate",180)

''' Tasu Ai means In Japanese:
“たす (tasu)” is a verb that means “to add” or “to help”'''

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Hi, I'm Tasu AI — here to make your day easier.")

def command():
    content = " "
    while content == " ":
    # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

         # recognize speech using Google Speech Recognition
        try:
            content =r.recognize_google(audio,language='en-in')
            print("you said . . . . . . . .  . "+content)
            content = mtranslate.translate(content,to_language="en-in")
            print("you said . . . . . . . .  . "+content)
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
            
        except Exception as e:
            print("please try again")


    return content
def main_process():
    while True:
        request  = command().lower()
        if "hello" in request :
            speak("welcome , How can i help You Sir")
        elif "play music" in request:
            speak("playing music")
            song =random.randint(1,7)
            if song==1:
                webbrowser.open("https://www.youtube.com/watch?v=DdLl-leD32o&list=RDDdLl-leD32o&start_radio=1")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=1onhvVnL8B8&list=RD1onhvVnL8B8&start_radio=1")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=8of5w7RgcTc&list=RD8of5w7RgcTc&start_radio=1")
            elif song == 4:
                webbrowser.open("https://www.youtube.com/watch?v=3Cp2QTBZAFQ&list=PLZpGmomA_BkAOPJ-OjIFoxUVWXGv-scqW&index=8")
            elif song == 5:
                webbrowser.open("https://www.youtube.com/watch?v=fhs6wYi4Jr0&list=PLZpGmomA_BkAOPJ-OjIFoxUVWXGv-scqW&index=16")
            elif song ==6:
                webbrowser.open("https://www.youtube.com/watch?v=5IdGjLg6m5Q&list=RD5IdGjLg6m5Q&start_radio=1")
            elif song == 7:
                webbrowser.open("https://www.youtube.com/watch?v=TdrL3QxjyVw&list=RDTdrL3QxjyVw&start_radio=1")
                # day and time
        elif "time" in request:
            Now_time=datetime.datetime.now().strftime("%H:%M")
            speak("current time is "+ str(Now_time))
        elif "date kitna hai" in request:
            Now_time=datetime.datetime.now().strftime("%d:%m")
            speak("current date is "+ str(Now_time))
        # Todolist add task
        elif "new task" in request:
            task= request.replace("new task"," ")
            task=task.strip()
            if task != " ":
                speak("Adding task :"+task)
                with open("Todo.txt","a") as file:
                    file.write(task+"\n")
      

        elif "speak task" in request:
            with open("todo.txt","r") as file:
                speak("work we have to do today is :"+file.read())

        
        # Delete Task
        elif "delete task" in request:
            task_to_delete = request.replace("delete task", "").strip().lower()
            if not task_to_delete:
                speak("Please specify which task to delete.")
            else:
                try:
                     # Read all tasks
                    with open("Todo.txt", "r") as file:
                        tasks = [task.strip() for task in file]

                       # Remove the matching task
                    updated_tasks = [task for task in tasks if task.lower() != task_to_delete]

                    if len(updated_tasks) < len(tasks):
                        with open("Todo.txt", "w") as file:
                            file.write("\n".join(updated_tasks) + "\n")
                            speak(f"Deleted task: {task_to_delete}")
                    else:
                        speak(f"Task not found: {task_to_delete}")

                except FileNotFoundError:
                    speak("Todo list not found.")

                
                #notification
        elif "notification" in request:
            with open("todo.txt","r") as file:
                tasks =file.read()
            notification.notify(
                title =" Today's work",
                message=tasks
            )
        #opening a web apps 

        elif "opening youtube" in request:
            webbrowser.open("https://www.youtube.com/")
        elif "opening facebook" in request:
            webbrowser.open("https://www.facebook.com/")
        elif "opening instagram" in request:
            webbrowser.open("https://www.instagram.com/")
        elif "opening linkedin" in request:
            webbrowser.open("https://www.linkedin.com/")
        elif "opening flipkart" in request:
            webbrowser.open("https://www.flipkart.com/")
        elif "opening whatsapp" in request:
            webbrowser.open("https://web.whatsapp.com/")
        elif "opening unstop" in request:
            webbrowser.open("https://unstop.com/")
        elif "opening gmail" in request:
            webbrowser.open("https://mail.google.com/")
        elif "opening prepinsta" in request:
            webbrowser.open("https://prepinsta.com/")
        elif "opening naukri" in request:
            webbrowser.open("https://www.naukri.com/")
        
        
                
        # opening Desktop Applications
        elif "app" in request :
            query = request.replace("open","")
            pyautogui.press("super")
      
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        #Advance comammds of wikipedia
        elif "wikipedia" in request :
            request = request.replace("Aishia","")
            request =request.replace("Search wikipedia ","")
            # print(request)
            result =wikipedia.summary(request,sentences=2)
            print(result)
            speak(result)
            # automatically search topic in google search browser
        elif "search google" in request :
            request = request.replace("Aishia","")

            request =request.replace("Search google ","")
            webbrowser.open("https://www.google.com/search?q="+request)


        #sending whatsapp messages
        elif "sending message" in request :
            pywhatkit.sendwhatmsg("+919652938339","hi",21,45,40)
            pywhatkit.sendwhatmsg_instantly("+919652938339", "hi", wait_time=20, tab_close=True)
        elif "send message" in request :
            try:
                pywhatkit.sendwhatmsg_instantly("+919652938339", "hi! hello", wait_time=20, tab_close=True)
                print("Message sent instantly")
            except Exception as e:
                print("Error:", e)
        #sending email messages
        elif "send email" in request:
            pywhatkit.send_mail("rafiquieahmed04@gmail.com", user_config.gmail_password, "hello", "how are you", "frozengamer386@gmail.com") 
            #send_mail(email_sender: str, password: str, subject: str, message: str | MIMEText, email_receiver: str) -> None
        
        elif "ask about" in request or "ask ai" in request:
            request = request.replace("Tasu", "")
            request = request.replace("ask about", "")

            request = request.replace("ask ai", "")
            request = request.strip()

            print("Cleaned Request:", request)

            response = ai.send_request(request)
            print("AI Response:", response)

            speak(response)

            # Store request and response
            with open("history.txt", "a", encoding="utf-8") as f:
                f.write(f"User: {request}\n")
                f.write(f"AI: {response}\n")
                f.write("=" * 50 + "\n")


            # wheter details provding
      
        elif "weather in" in request or "wheather in" in request:
    # Clean keywords to extract city name
            for word in ["weather", "wheather", "in", "temperature", "temperture", "tasu", "ask about"]:
                request = request.replace(word, "")
            city = request.strip()

            if city:
                get_weather(city)
            else:
                speak("Please mention a valid city name.")



       


                
        
            


    


            
            


            
         

main_process()



# speak("how are you")


