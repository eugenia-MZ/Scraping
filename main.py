import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")

content_html = response.text

soup = BeautifulSoup(content_html, "html.parser")

print(soup.title.get_text(strip=True))

resultats = soup.find_all("strong")
print(resultats)

prix = [float(p.get_text()[2:]) for p in soup.find_all("p", class_="price_color")]

print(f"Voici les prix : {prix}")

somme = sum(prix)
print(somme)
moyenne = somme / len(prix)
print(f"Voici la moyenne des prix : {moyenne:.2f}£")

# with open("test.html", "w") as file:
#    file.write(content_html)
