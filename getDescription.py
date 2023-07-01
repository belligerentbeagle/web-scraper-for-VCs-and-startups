import requests
import re
from googlesearch import search
import time
import apiKey

# Define the URL of the website you want to scrape
website_urls = ["borneo.io","botmd.io","brainpooltech.com","braiven.com","brda.com.sg","bribooks.com","brightchamps.com","bringaboutmi.org","btrlyf.com","buildpan.com","bunkerchain.io","bussr.com","butleric.com","byteplus.com","c-log.io","caito.ai","capc.com.sg","carecam.ai","cashinasia.com","ceesuite.com","cerebry.co","cerekon.com","cdi-sg.com","childhealthimprints.com","chloropy.com","chordx.co","chynge.com","circularind.com"]

websites = ["https://" + url if not url.startswith("https://") else url for url in website_urls]
website_urls_for_snippet = ["borneo.io","botmd.io","brainpooltech.com","braiven.com","brda.com.sg","bribooks.com","brightchamps.com","bringaboutmi.org","btrlyf.com","buildpan.com","bunkerchain.io","bussr.com","butleric.com","byteplus.com","c-log.io","caito.ai","capc.com.sg","carecam.ai","cashinasia.com","ceesuite.com","cerebry.co","cerekon.com","cdi-sg.com","childhealthimprints.com","chloropy.com","chordx.co","chynge.com","circularind.com"] 

from googleapiclient.discovery import build
import csv

# Define your API key and search engine ID
api_key = apiKey.apikey
search_engine_id = apiKey.search_engine_id

# Create a service object for the Custom Search API
service = build("customsearch", "v1", developerKey=api_key)

# Open a CSV file to write the website URLs and snippets
with open("./outputDescription.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Website URL", "Snippet"])

    # Iterate through the website URLs
    for website_url in website_urls_for_snippet:
        # Perform the search request
        print("Writing for " + website_url)
        response = service.cse().list(
            q=f"site:{website_url}",
            cx=search_engine_id,
            num=1
        ).execute()

        # Extract the snippet from the search response
        items = response.get("items", [])
        if items:
            snippet = items[0].get("snippet")
            writer.writerow([website_url, snippet])
        else:
            writer.writerow([website_url, "NIL"])

print("Snippets saved to outputDescription.csv")