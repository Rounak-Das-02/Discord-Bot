import json
import requests

def IndianNews():
     
    f = open(r".\tokens\token.json", )
    s = json.load(f)

    api_key = s["NewsApi"]

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

    try :
        response = requests.get(url)
        x = response.json()

        data = []
        results = ""
        articles = x["articles"]
        for ar in articles :
            data.append(ar["title"])
        
        for i in range(len(data)):
            results = results + f"{i+1}. {data[i]} \n" 
        # print (results)
        return (results)
    except:
        # print ("Problem")
        return "Sorry I can't fetch the data as of now .."
