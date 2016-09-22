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
print len(companylist)
if len(companylist) == 0:
	print "Phone list not found"
allCompanyLink = list()
for td in companylist:
	a = td.get_attribute("href")
	print a
	allCompanyLink.append(a)
for CompanyLink in allCompanyLink:
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
			phoneLink = phone.get_attribute("href")
			print phoneLink
			phoneLinkList.append(phoneLink)
		for phoneLink in phoneLinkList:
			driver.get(phoneLink)
			time.sleep(5)
			phoneName = driver.find_element_by_class_name("specs-phone-name-title")
			print phoneName
			specDiv = driver.find_element_by_id("specs-list")
			tableList = specDiv.find_elements_by_xpath("//table")
			print "Table List : \n\n"
			print tableList

		try:
			driver.find_element_by_class_name("pages-next").click()
		except NoSuchElementException:
			print "No next page"
		except Exception:
			print "Some Other exception occoured"
