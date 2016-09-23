import os
import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import strftime, localtime

urls = open("urlGathered.txt","r")
url = open("urlGathered.txt","r")
phoneDetails = open("phoneDetails.txt","a")
phoneDetailsJSON = open("phoneDetailJSON.txt","a")


myPath = os.path.realpath(__file__)
myPath = myPath[:-11]

# Launch chrome from chromedriver for LINUX
currentPath =  os.path.dirname(myPath)
chromedriver = currentPath + "/chromedriver"
print chromedriver
os.environ["webdriver.chrome.driver"] = chromedriver
print "OS environment set"
driver = webdriver.Chrome(chromedriver)
print "Launching chrome"

phoneDetails.write("[\n")
phoneDetailsJSON.write("[\n")
phoneDone = 0
totalPhones = sum(1 for line in url)

for phoneLink in urls:
	phoneDone += 1
	per = phoneDone/totalPhones
	print str(phoneDone) + " done out of " + str(totalPhones) + " ::: " + str(per) + " %"
	finalString = ""
	finalStringS = ""
	phoneName = ""
	urlNameList = phoneLink.split()
	driver.get(urlNameList[0])
	print "opening " + urlNameList[0]
	companyName = urlNameList[1]
	time.sleep(3)
	try:
		phoneName = driver.find_element_by_class_name("specs-phone-name-title").text
	except Exception:
		continue
	finalString += "{ company:\"" + companyName + "\", " + "phone:\"" + phoneName + "\", "
	finalStringS += "{ \"company\":\"" + companyName + "\", " + "\"phone\":\"" + phoneName + "\", " 
	specDiv = driver.find_element_by_id("specs-list")
	tableList = specDiv.find_elements_by_xpath("//table")
	individualTable = tableList[0]
	try:
		tableHeader = individualTable.find_element_by_xpath("//th").text
	except Exception:
		continue
	divisionList = individualTable.find_elements_by_xpath("//tr")
	for inDiv in divisionList:
		try:
			title = inDiv.find_element_by_class_name("ttl").text
			details = inDiv.find_element_by_class_name("nfo").text
			if title != "" and details != "" and title != " " and details != " ":
				finalString += title + ":\"" + details + "\", "
				finalStringS += "\"" + title + "\":\"" + details + "\", "
		except Exception:
			continue
		
	finalS = finalString.replace("\n","").replace("\r","") + "},\n"
	finalSS = finalStringS.replace("\n","").replace("\r","") + "},\n"
	phoneDetails.write(finalS)
	phoneDetailsJSON.write(finalSS)
	# print finalString
phoneDetails.write("]")
phoneDetailsJSON.write("]")

