import requests
import re
from googlesearch import search
import time

# Define the URL of the website you want to scrape
website_urls = ["https://animeta.ai/","www.cyberx.com","www.cryptogpt.org","www.din.global","www.haive.tech","www.intnt.ai","www.medtrik.com","www.metagame.industries","www.mindverse.ai","www.mintechbrasil.com.br","https://www.ncinga.net/","onfinance.in","www.pipedata.co","www.port3.io","https://appmaster.io/","www.readout.ai","www.reclimate.earth","https://step1matrix.io/","www.tauexpress.com","www.ureca.com"]
websites = ["https://" + url if not url.startswith("https://") else url for url in website_urls]
website_urls_for_snippet = ["onfinance.in","opalai.com","ordisense.netlify.app","originhealth.ai","qritive.com","pickngo.com.sg","pipedata.co","pivotfintech.com","port3.io","privyr.com","profileprint.ai","proxtera.com","quikbot.ai","https://appmaster.io/","readout.ai","realestateanalytics.sg","reclimate.earth","regask.com","rescalers.com","respiree.com","salaryboard.com","scarlettpanda.com","schonell.co","seventhsense.ai","shoplinks.co","sixsense.ai","slab.rocks","somin.ai","https://somin.ai/","https://step1matrix.io/","strivemath.com","swatmobility.com","tablepointer.com","tauexpress.com","thegrowhub.co","tookitaki.com","trakomatic.com","transitry.com","traxretail.com","tritech.com.sg","trustingsocial.com","ureca.com","wastelabs.co","wavel.ai","spyderecg.com","willowmore.com.sg","workforceoptimizer.com","writerzen.net","yuma.ai","zensung.com"]

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