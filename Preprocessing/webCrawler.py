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
from time import strftime, localtime

urls = open("urls.txt","a")
logfile = open("crawler.log","a")

def printReport(start,companyDone,phonesDone,totalPhones,totalCompanies):
	logString = strftime("%Y-%m-%d %H:%M:%S", localtime())
	logString += " >>"
	elapsedTime = int((time.time() - start))
	m, s = divmod(elapsedTime, 60)
	h, m = divmod(m, 60)
	logString += "\nTotal Elapsed Time : %d:%02d:%02d\n" % (h, m, s)
	percentCompanies = 100*companiesDone/totalCompanies
	percentPhones = 100*phonesDone/totalPhones
	timeLeft = 360000
	if phonesDone > 0:
		timeLeft = totalPhones * elapsedTime/phonesDone
	timeLeft -= elapsedTime
	logString += "Companies Done : " + str(companiesDone)
	logString += " & Phones Done : " + str(phonesDone)
	logString += "\nPercent Companies Done : " + str(percentCompanies) + " %"
	logString += " & Percent Phones Done : " + str(percentPhones) + " %\n\n"
	logfile.write(logString)
	print "\n\t\t\t FINAL REPORT : "
	print "\n#####################################################################\n"
	print "\tTotal Elapsed Time : %d:%02d:%02d" % (h, m, s)
	print "\tCompanies Done : " + str(companiesDone)
	print "\tPhones Done : " + str(phonesDone)
	print "\tPercent Companies Done : " + str(percentCompanies) + " %"
	print "\tPercent Phones Done : " + str(percentPhones) + " %"
	m, s = divmod(timeLeft, 60)
	h, m = divmod(m, 60)
	print "\tEstimated Time left : %d:%02d:%02d" % (h, m, s)
	print "\n#####################################################################\n"	


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


start = time.time()
elapsedTime = 0
flag = 0

for CompanyLink in allCompanyLink:
	if flag == 0:
		currentCompany = allCompanyName[companiesDone]
		companiesDone += 1
		driver.get(CompanyLink)
	try:
		print "Going to company phone page"
		element = WebDriverWait(driver, 10).until(EC.title_contains("All"))
		time.sleep(10)
	finally:
		phoneList = driver.find_elements_by_css_selector(".makers a")
		phonesDone += len(phoneList)
		for phone in phoneList:
			phoneLink = phone.get_attribute("href")
			writeToText = phoneLink + " " 
			writeToText += currentCompany + " " + phone.text
			print writeToText
			urls.write(writeToText)
			urls.write("\n")
	try:
		driver.find_element_by_class_name("pages-next").click()
		flag = 1
	except NoSuchElementException:
		print "No next page"
		flag = 0
	except Exception:
		print "Some Other exception occoured"
		flag = 0
	printReport(start,companiesDone,phonesDone,totalPhones,totalCompanies)
url.close()





