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
		print "Couldn't find Title"
		continue
	finalString += "{ company:\"" + companyName + "\", " + "phone:\"" + phoneName + "\", "
	finalStringS += "{ \"company\":\"" + companyName + "\", " + "\"phone\":\"" + phoneName + "\", " 
	specDiv = driver.find_element_by_id("specs-list")
	tableList = specDiv.find_elements_by_xpath("//table")
	individualTable = tableList[0]
	divisionList = individualTable.find_elements_by_xpath("//tr")			# find all <tr> in the webpage
	titleList = []				
	for inDiv in divisionList:
		try:
			title = inDiv.find_element_by_class_name("ttl").text
			if title in titleList:											# prevent duplicates in JSON String
				# print "Found"
				continue
			titleList.append(title)
			details = inDiv.find_element_by_class_name("nfo").text
			if title != "" and details != "" and title != " " and details != " ":
				finalString += title + ":\"" + details + "\", "				# adding things to JSON string
				finalStringS += "\"" + title + "\":\"" + details + "\", "
		except Exception:
			print "Exception here"
			continue

	if finalString[-2:-1] == ',':											# removing last , to get a valid JSON string
		finalString = finalString[0:-2]
		finalStringS = finalStringS[0:-2]
	finalS = finalString.replace("\n","").replace("\r","") + "},\n"			# terminating JSON and removing escape charecters
	finalSS = finalStringS.replace("\n","").replace("\r","") + "},\n"
	phoneDetails.write(finalS)
	phoneDetailsJSON.write(finalSS)
	# print finalString
phoneDetails.write("]")
phoneDetailsJSON.write("]")