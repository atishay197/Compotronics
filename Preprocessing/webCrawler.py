# WebCrawler - MobilePhone DB Creation

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

# display all .csv files that are present in the current directory
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

print "GSM arena webpage"
# log into linkedIn account
driver.get("http://www.gsmarena.com/makers.php3")
time.sleep(5)
print "GSM Arena phone page"

companylist = driver.find_elements_by_css_selector(".main-makers table td a")
totalCompanies = len(companylist)
if len(companylist) == 0:
	print "Phone list not found"
allCompanyLink = list()
allCompanyName = list()
totalPhones = 0
for td in companylist:
	companyDetailList = td.text.split()
	totalPhones += int(companyDetailList[len(companyDetailList) - 2])
	a = td.get_attribute("href")
	print a
	allCompanyLink.append(a)
	allCompanyName.append(companyDetailList[0])
print "Total Phones : " + str(totalPhones)
phonesDone = 0
companiesDone = 0
for CompanyLink in allCompanyLink:
	currentCompany = allCompanyName[companiesDone]
	companiesDone += 1
	driver.get(CompanyLink)
	try:
		print "Going to company phone page"
		element = WebDriverWait(driver, 10).until(EC.title_contains("All"))
		time.sleep(3)
	finally:
		phoneList = driver.find_elements_by_css_selector(".makers a")
		print len(phoneList)
		phoneLinkList = list()	
		for phone in phoneList:
			print "phone : " + phone.text
			phoneLink = phone.get_attribute("href")
			print phoneLink
			phoneLinkList.append(phoneLink)
		for phoneLink in phoneLinkList:
			driver.get(phoneLink)
			time.sleep(5)
			phoneName = driver.find_element_by_class_name("specs-phone-name-title")
			print phoneName.text
			specDiv = driver.find_element_by_id("specs-list")
			tableList = specDiv.find_elements_by_xpath("//table")
			for individualTable in tableList:
				tableHeader = individualTable.find_element_by_xpath("//th")
				print "~ " + tableHeader.text + " ~"
				divisionList = individualTable.find_elements_by_xpath("//tr")
				for inDiv in divisionList:
					title = inDiv.find_element_by_class_name("ttl")
					details = inDiv.find_element_by_class_name("nfo")
					print "& " + title.text + " # " + details.text + " &"



		try:
			driver.find_element_by_class_name("pages-next").click()
		except NoSuchElementException:
			print "No next page"
		except Exception:
			print "Some Other exception occoured"
