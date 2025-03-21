import requests
from bs4 import BeautifulSoup, Comment

url = "" # poner url aca
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = [a["href"] for a in soup.find_all("a", href=True)]
print("\nEnlaces encontrados:")
print(links)

comments = soup.find_all(string=lambda text: isinstance(text, Comment))
print("\nComentarios encontrados:")
for comment in comments:
    print(comment.strip())

emails = []
for word in response.text.split():
    if "@" in word and "." in word:
        clean_word = word.strip(" ,;<>\"'\n\t")
        if clean_word not in emails:
            emails.append(clean_word)

print("\nCorreos electronicos encontrados:")
print(emails)
