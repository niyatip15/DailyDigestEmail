import requests
from send_news_email import send_email

api_key = "34769740308a450ebfa7cddb6aa73b2d"
url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2024-04-23&sortBy=publishedAt&apiKey=34769740308a450ebfa7cddb6aa73b2d"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"]:
    title = article["title"]
    description = article["description"] if article["description"] else ""
    body = body + title + "\n" + description + "\n\n"
body= body.encode("utf-8")
send_email(message=body)
