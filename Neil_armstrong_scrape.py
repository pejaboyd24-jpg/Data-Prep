import re
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

headers = {"User-Agent": "Mozilla/5.0"}
page = requests.get("https://en.wikipedia.org/wiki/Neil_Armstrong", headers=headers)

soup = BeautifulSoup(page.text, "html.parser")

text = ""
for p in soup.find_all("p"):
    text += p.get_text()

years = re.findall(r'\b(?:18|19|20)\d{2}\b', text)
years = [int(y) for y in years]

plt.hist(years, bins=20, orientation="horizontal")
plt.xlabel("Frequency")
plt.ylabel("Year")
plt.title("Years Mentioned in Neil Armstrong Article")
plt.show()
