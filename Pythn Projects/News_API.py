import json
import requests

def speak(str) :
    from win32com.client import Dispatch
    spk = Dispatch("SAPI.SpVoice")
    print(str)
    spk.speak(str)

def category():
    try :
        cat_dict = {1:"business", 2:"entertainment", 3:"health", 4: "science", 5:"sport", 6:"technology"}
        for i,j in cat_dict.items():
            print(f"\t{i} - {j.capitalize()}")
        choice = int(input("Your choice - "))
        speak(f"Loading Today's top news of {cat_dict[choice].capitalize()}...")
        return cat_dict[choice]

    except Exception as e :
        speak("Please enter valid choice!!")
        category()

if __name__ ==  '__main__' :
    Your_API = "87113de879484e73a7b43a50d54ce0ff"

    speak("Welcome to the News section!!")
    speak("Please Select a Number for the Category You want")
    Your_category = category()
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={Your_category}&apiKey={Your_API}"
    news = requests.get(url).text
    news_dict = json.loads(news)
    main = news_dict["articles"]
    try :
        for article in main:
            speak(article['title'])
            print(f"  For More Click HERE 👇👇 \n {article['url']}")
            speak("\nMoving on to the next news..Listen Carefully")

        speak("Thanks for listening...")

    except Exception as e:
        speak(f"No Latest News of {Your_category} for Today!!")
