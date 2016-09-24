import json

fileCheck = open("phoneDetailJSON.json","r")

number = 0
successNumber = 0
totalError = 0
jsonList = list()

for line in fileCheck:
	number += 1
	try:
		json_object = json.loads(line[0:-2])
		jsonList.append(json_object)
		successNumber += 1
	except ValueError:
		totalError += 1
		print "JSON Error : " + str(totalError)
# print jsonList
print "Success" + str(successNumber) + " Errors : " + str(totalError)
sqlQueryList = list()
curJson = 0
for individualJSON in jsonList:
	curJson += 1
	statement = "INSERT INTO PhoneTablet ("
	for keys in individualJSON:
		print "keys : " + keys + " value : " + individualJSON[keys]
	# coulmn = 
print curJson