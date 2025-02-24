import requests
from bs4 import BeautifulSoup


def scrape_cuba_info():
    url = "https://en.wikipedia.org/wiki/Tourism_in_Cuba"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text_data = "\n".join([p.get_text() for p in paragraphs])

        with open("cuba_info.txt", "w", encoding="utf-8") as file:
            file.write(text_data)

        print("✅ Data scraped successfully and saved to cuba_info.txt")
    else:
        print("❌ Failed to fetch data")


# Run the scraper
scrape_cuba_info()