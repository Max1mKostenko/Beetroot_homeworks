from requests import get

url = "https://en.wikipedia.org/robots.txt"
text = get(url).text
print(text)

with open("robots.txt", "w", encoding="utf-8") as file:
    file.write(text)
