import requests
import re
from googlesearch import search
import time

# Define the URL of the website you want to scrape
website_urls =["borneo.io","botmd.io","brainpooltech.com","braiven.com","brda.com.sg","bribooks.com","brightchamps.com","bringaboutmi.org","btrlyf.com","buildpan.com","bunkerchain.io","bussr.com","butleric.com","byteplus.com","c-log.io","caito.ai","capc.com.sg","carecam.ai","cashinasia.com","ceesuite.com","cerebry.co","cerekon.com","cdi-sg.com","childhealthimprints.com","chloropy.com","chordx.co","chynge.com","circularind.com"] 
websites = ["https://" + url if not url.startswith("https://") else url for url in website_urls]
website_urls_for_snippet =["borneo.io","botmd.io","brainpooltech.com","braiven.com","brda.com.sg","bribooks.com","brightchamps.com","bringaboutmi.org","btrlyf.com","buildpan.com","bunkerchain.io","bussr.com","butleric.com","byteplus.com","c-log.io","caito.ai","capc.com.sg","carecam.ai","cashinasia.com","ceesuite.com","cerebry.co","cerekon.com","cdi-sg.com","childhealthimprints.com","chloropy.com","chordx.co","chynge.com","circularind.com"] 

for website_url in websites: 
    try: 
        # Send a GET request to the website
        print("Trying " + website_url)
        response = requests.get(website_url)

        # Extract the domain from the website URL
        domain = re.findall(r"https?://([A-Za-z_0-9.-]+).*", website_url)[0]

        # Find email addresses with the same domain using regular expressions
        email_addresses = re.findall(r"\b[A-Za-z0-9._%+-]+@" + domain + r"\b", response.text)

        # Print the found email addresses
        for email in email_addresses:
            print(email)
    except:
        print(website_url + " failed.")