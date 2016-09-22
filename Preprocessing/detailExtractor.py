
		
for phoneLink in phoneLinkList:
	finalString = currentCompany
	driver.get(phoneLink)
	time.sleep(5)
	phoneName = driver.find_element_by_class_name("specs-phone-name-title")
	# print phoneName.text
	finalString += phoneName.text 
	specDiv = driver.find_element_by_id("specs-list")
	tableList = specDiv.find_elements_by_xpath("//table")
	for individualTable in tableList:
		tableHeader = individualTable.find_element_by_xpath("//th").text
		# print "~ " + tableHeader + " ~"
		finalString += "~ " + tableHeader + " ~"
		divisionList = individualTable.find_elements_by_xpath("//tr")
		for inDiv in divisionList:
			title = inDiv.find_element_by_class_name("ttl")
			details = inDiv.find_element_by_class_name("nfo")
			# print "& " + title.text + " # " + details.text + " &"
			finalString += "& " + title.text + " # " + details.text + " &"
	finalString = finalString.strip("\n")
	print finalString