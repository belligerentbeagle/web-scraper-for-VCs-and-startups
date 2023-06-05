import requests
import re
from googlesearch import search
import time
import apiKey

# Define the URL of the website you want to scrape
website_urls = ["https://animeta.ai/","www.cyberx.com","www.cryptogpt.org","www.din.global","www.haive.tech","www.intnt.ai","www.medtrik.com","www.metagame.industries","www.mindverse.ai","www.mintechbrasil.com.br","https://www.ncinga.net/","onfinance.in","www.pipedata.co","www.port3.io","https://appmaster.io/","www.readout.ai","www.reclimate.earth","https://step1matrix.io/","www.tauexpress.com","www.ureca.com"]
websites = ["https://" + url if not url.startswith("https://") else url for url in website_urls]
website_urls_for_snippet = ["onfinance.in","opalai.com","ordisense.netlify.app","originhealth.ai","qritive.com","pickngo.com.sg","pipedata.co","pivotfintech.com","port3.io","privyr.com","profileprint.ai","proxtera.com","quikbot.ai","https://appmaster.io/","readout.ai","realestateanalytics.sg","reclimate.earth","regask.com","rescalers.com","respiree.com","salaryboard.com","scarlettpanda.com","schonell.co","seventhsense.ai","shoplinks.co","sixsense.ai","slab.rocks","somin.ai","https://somin.ai/","https://step1matrix.io/","strivemath.com","swatmobility.com","tablepointer.com","tauexpress.com","thegrowhub.co","tookitaki.com","trakomatic.com","transitry.com","traxretail.com","tritech.com.sg","trustingsocial.com","ureca.com","wastelabs.co","wavel.ai","spyderecg.com","willowmore.com.sg","workforceoptimizer.com","writerzen.net","yuma.ai","zensung.com"]

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