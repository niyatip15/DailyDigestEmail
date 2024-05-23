import requests
from send_news_email import send_email

api_key = "34769740308a450ebfa7cddb6aa73b2d"

topic = "tesla"
url = f"https://newsapi.org/v2/everything?q={topic}&"\
    "from=2024-04-23&sortBy=publishedAt&apiKey=34769740308a450ebfa7cddb6aa73b2d&language=en"

# Make a request 
request = requests.get(url)

# Get dictionary with data 
content = request.json()

# Initialize the body with the Subject line
body = "Subject: Today's News\n\n"

# Access the title, article, description, and URL
for article in content["articles"][:20]:
    title = article["title"]
    description = article["description"] if article["description"] else ""
    url = article["url"]
    # Append each article's details to the body
    body += f"{title}\n{description}\n{url}\n\n"

# Encode the message as UTF-8 before sending
body = body.encode("utf-8")

# Send the email
send_email(message=body)
