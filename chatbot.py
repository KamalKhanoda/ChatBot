import webbrowser
from pytube import Search
import os
from datetime import datetime, timedelta, date


def playYoutubeVideo(query):
    s = Search(query)
    if s.results:
        videoUrl = s.results[0].watch_url
        webbrowser.open(videoUrl)
    else:
        print("Bot: No video found.")

print("Hello ! I am your personal assistant. How can I Assist you today?")
while True:
    userInput = input("You: ")
    if userInput.lower() in ['bye', 'exit', 'quit']:
        print("Bot: Goodbye! Have a great day!")
        break
    elif any(phrase in userInput.lower() for phrase in ['hi', 'hello', 'hey']):
        print("Bot: Hello! How can I help you today?")
    elif any(phrase in userInput.lower() for phrase in ['what is your name', 'who are you']):
        print("Bot: I am your personal assistant created in python. You can call me 'Chatbot'")
    elif "date" in userInput.lower():
        today = date.today()
        print(f"Bot: Today's date is {today.strftime('%B %d, %Y')}.")

    elif "open youtube" in userInput.lower():
        print("Bot: Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in userInput.lower():
        print("Bot: Opening Google...")
        webbrowser.open("https://www.google.com")
    elif "open facebook" in userInput.lower():
        print("Bot: Opening Facebook...")
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in userInput.lower():
        print("Bot: Opening Instagram...")
        webbrowser.open("https://www.instagram.com")
    elif "play" in userInput.lower():
        searchQuery = " ".join(userInput.split()[1:])
        if searchQuery:
            print(f"Bot: Playing the first YouTube video for '{searchQuery}'...")
            playYoutubeVideo(searchQuery)
        else:
            print("Bot: Please provide a search term for the video.")
    elif any(phrase not in userInput.lower() for phrase in ['open', 'play', 'hello', 'hi']):
        webbrowser.open("https://www.google.com/search?q=" + userInput)
    else:
        app_name = userInput.lower().replace("open", "").strip()
        if app_name:
            try:
                os.system(f"start {app_name}")
                print(f"Bot: Opening {app_name}...")
            except Exception as e:
                print(f"Bot: Could not open {app_name}. Error: {e}")
        else:
            print("Bot: Please specify the application you want to open.")
