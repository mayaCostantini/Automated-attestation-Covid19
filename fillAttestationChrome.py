import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import sendFile
import time 
import os 



if os.path.exists(os.getcwd() + '/attestations') and len(os.listdir('./attestations')) != 0 : 

    os.chdir(os.getcwd() + '/attestations')

    if os.path.basename(os.path.normpath(os.getcwd())) == 'attestations' and len(os.listdir(os.getcwd())) != 0: 
        os.system('rm *')
        print('Old attestations files removed')

    elif len(os.listdir(os.getcwd())) == 0 : 
        print('Directory already empty')

    elif os.path.basename(os.path.normpath(os.getcwd())) != 'attestations' : 
        print('attestation : No such file or directory')

    os.chdir(os.path.dirname(os.getcwd()))


options = webdriver.ChromeOptions()

if os.path.exists(os.getcwd()) : 
    downloadPath = os.getcwd() + '/attestations'
else : 
    raise FileNotFoundError

options.add_experimental_option('prefs', {
"download.default_directory": downloadPath, #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.plugins_disabled": ["Chrome PDF Viewer"],
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})

chromedriverPath = '/Users/your/path/to/chromedriver' # Replace this line with the path to your chromedriver download

driver = webdriver.Chrome(chromedriverPath, options=options)

wait = WebDriverWait(driver, 5)
driver.get("https://media.interieur.gouv.fr/deplacement-covid-19/")

wait.until(ec.element_to_be_clickable((By.ID, "reload-btn"))).click()

# Replace the values in keyboardEntries by your personal information. The zipcode must contain five numbers to be valid. 
keyboardEntries = {"firstname" : "Jon", "lastname" : "Snow", "placeofbirth" : "Westeros", "address" : "5 Street of Silver", "city" : "King's Landing", "zipcode" : "10000"}

for entry in keyboardEntries.keys() : 
    elem = driver.find_element_by_name(entry)
    elem.clear()
    elem.send_keys(keyboardEntries[entry])
    elem.send_keys(Keys.RETURN)


birthday = driver.find_element_by_name("birthday")
birthday.send_keys(Keys.RETURN)
birthday.send_keys("01") # Your day of birth 
birthday.send_keys("01") # Your month of birth 
birthday.send_keys("1999") # Your year of birth 

currentTime = time.localtime()
currentHour = str(currentTime.tm_hour)
currentMinutes = str(currentTime.tm_min)

goingOutTime = driver.find_element_by_name("heuresortie")
goingOutTime.send_keys(Keys.RETURN)
goingOutTime.send_keys(currentHour)
goingOutTime.send_keys(currentMinutes)



def chooseMotiveCheckbox(motive) : 
    motives = {"achats" : "checkbox-achats", "sport" : "checkbox-sport_animaux", "cours" : "checkbox-travail"}
    if motive in motives.keys() : 
        return motives[motive]
    else : 
        raise KeyError


motive = "achats"
motiveCheckboxName = chooseMotiveCheckbox(motive)

checkBox = driver.find_element_by_id(motiveCheckboxName)
checkBox.click()

generateAttestation = driver.find_element_by_id("generate-btn" )
generateAttestation.click()

time.sleep(5)

if os.path.exists(downloadPath) and len(os.listdir(downloadPath)) != 0 :  

    os.chdir(downloadPath)

    if len(os.listdir(os.getcwd())) == 1 : 
        os.system('mv * attestation.pdf')

    os.chdir(os.path.dirname(os.getcwd()))


assert "No results found." not in driver.page_source

driver.close()

sendFile.sendFile()
