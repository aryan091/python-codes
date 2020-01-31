def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

def tellnews(url):
    news = requests.get(url=url).text
    news = json.loads(news)
    arct = news['articles']

    for article in arct:
        print(article['title'])
        speak(article['title'])
        speak("Moving to the next news...Listen Carefully")
    else:
        speak("That all for today.....")
        print(len(article))


if __name__ == '__main__':

    import requests
    import json

    print("_____________________NEWS APPILICATION________________")
    print("1.Press 1 for Technology Related News")
    print("2.Press 2 for Business Related News")
    print("3.Press 3 for Entertainment Related News")
    print("4.Press 4 for Health Related News")
    print("5.Press 5 for Science Related News")
    print("6.Press 6 for Sports Related News")
    print("Press Any Key for exit")
    choice = input("Please enter your choice for particular news")
    speak("Please enter your choice for particular news")


    if choice == "1":
        speak("Technology Related Headlines for Today")
        url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=0d23a7184dd047f2afde7fc4bca4f5ae"
        tellnews(url)
    elif choice == "2":

        speak("Business Related Headlines for Today")
        url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=0d23a7184dd047f2afde7fc4bca4f5ae"
        tellnews(url)

    elif choice == "3":

        speak("Entertainment Related Headlines for Today")
        url="https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=0d23a7184dd047f2afde7fc4bca4f5ae"
        tellnews(url)
    elif choice == "4":

        speak("Health Related Headlines for Today")
        url="https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=0d23a7184dd047f2afde7fc4bca4f5ae"
        tellnews(url)
    elif choice == "5":

        speak("Science Related Headlines for Today")
        url="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=0d23a7184dd047f2afde7fc4bca4f5ae"
        tellnews(url)

    elif choice == "6":

        speak("Sports Related Headlines for Today")
        url="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=0d23a7184dd047f2afde7fc4bca4f5ae"
        tellnews(url)

    else:
        exit()
