from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

# replace with the path to your webdriver
driver_path = "./chromedriver_mac_arm64/chromedriver"

# replace with the website you want to log in to"
url = "https://attend.informatechevents.virtual.informatech.com/event/asia-tech-x-singapore-2023/people/RXZlbnRWaWV3XzQzMzYwMw=="

# replace with your email and password
email = "weiyuxinexponential@gmail.com"
password = "%YuShit1%"


#unable to use chromedriver here: NoSuchDriverException
options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
driver = webdriver.Chrome(options=options)
loadtime = 3

def loginToAttendees():

    driver.get(url)
    time.sleep(loadtime)

    acceptCookies = driver.find_element(By.XPATH, "//button[@class='button__Wrapper-ui__sc-a2a0dz-0 kRLAfy']")
    acceptCookies.click()  


    login = driver.find_element(By.XPATH, "//button[@class='button__Wrapper-ui__sc-a2a0dz-0 kRLAfy sc-1a4ba045-1 iFbOXD']")
    login.click()                               

    # find the email input and enter the email
    time.sleep(loadtime)
    email_input = driver.find_element(By.ID,"lookup-email-input-id")
    email_input.send_keys(email)

    # find and click the "continue" button
    time.sleep(loadtime)
    continue_button = driver.find_element(By.XPATH, "//button[@class='button__Wrapper-ui__sc-a2a0dz-0 kRLAfy']")
    continue_button.click()

    # wait for next page to load
    time.sleep(loadtime)

    # find the password input and enter the password
    password_input = driver.find_element(By.ID, "login-with-email-and-password-password-id")
    password_input.send_keys(password)

    #click the continue button
    time.sleep(loadtime)
    continue_button = driver.find_element(By.XPATH, "//button[@class='button__Wrapper-ui__sc-a2a0dz-0 kRLAfy']")
    continue_button.click()
    # wait for next page to load
    time.sleep(4)



def getAttendees():
    time.sleep(6)
    driver.save_screenshot('logged_in.png')
    container = driver.find_elements(By.XPATH, "//div[@class='container__List-cmp__sc-14itgrz-0 dntXRq']")
    # container = container[1]
    a_tags = container.find_elements(By.TAG_NAME, "a")

    # Create an empty list to store the extracted href values
    href_list = []

    # Iterate over the <a> tags and extract the href attribute
    with open("./outputPersons.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Title", "Company"])
        for a_tag in a_tags:
            name = a_tag.find_element(By.XPATH, "//span[@class='clamp__Clamp-ui__sc-1aq2rfp-0 list__FullName-cmp__sc-88lus8-7 hAEPUd nlTRz']").text
            href_list.append(name)
            title = a_tag.find_element(By.XPATH, "//span[@class='clamp__Clamp-ui__sc-1aq2rfp-0 list__Job-cmp__sc-88lus8-9 hAEPUd iGKfpE']").text
            company = a_tag.find_element(By.XPATH, "//span[@class='clamp__Clamp-ui__sc-1aq2rfp-0 list__Organization-cmp__sc-88lus8-10 hAEPUd elKTsM']").text

            if not name:
                print("No name")
                name = "NIL"
            if not title:        
                print("No title")
                title = "NIL"
            if not company:
                print("No company")
                company = "NIL"

            writer.writerow([name, title, company])

    
    print(href_list)


loginToAttendees()
getAttendees()