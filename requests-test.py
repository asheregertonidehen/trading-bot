import requests
import json

data = requests.get("https://api.marketaux.com/v1/news/all?symbols=AMZN&filter_entities=true&language=en&api_token=tbHSLMUzhFDWyYv1DQYBNTCzcNtaluErsdP9koPk")
Headline1 = data.json()["data"][0]["description"]
Headline2 = data.json()["data"][1]["description"]
Headline3 = data.json()["data"][2]["description"]
news = [Headline1, Headline2, Headline3]
for headline in news:
        print(f"---> {headline}")
