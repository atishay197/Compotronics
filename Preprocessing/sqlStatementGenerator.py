import json

fileCheck = open("phoneDetailJSON.json","r")
sqlFile = open("tableCreation.sql","a")

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
keylist = list()
keylist2 = list()
finalList = list()
statementList = list()
for individualJSON in jsonList:
	for key in individualJSON:
		key = key.replace("-","_")
		key = key.replace(" ","_")
		if key not in keylist and key != "3.5mm_jack":
			keylist.append(key)
		keylist2.append(keylist)

curList = keylist[0]

for keylist in keylist2:
	for key in keylist:
		if key not in curList:
			print key
			finalList.append(key)
	curList = keylist

print finalList



for individualJSON in jsonList:
	curJson += 1
	columns = ""
	values = ""
	for keys in individualJSON:
		value = individualJSON[keys]
		if keys != "3.5mm jack":
		# print "keys : " + keys + " value : " + value
			keys = keys.replace("-","_")
			keys = keys.replace(" ","_")
			columns += keys + ","
			values += "\'" + value + "\',"
	columns.strip(",")
	values.strip(",")
	statement = "INSERT INTO PhoneTablet (" + columns + ") VALUES (" + values + ");\n"
	statementList.append(statement)
	# print statement

create = "CREATE TABLE PhoneTablet\n(\n"
create += "id int NOT NULL AUTO_INCREMENT,\n"
for key in keylist:
	create += key + " varchar(2048) ,\n"
create += "PRIMARY KEY (id)\n)\n\n"
sqlFile.write(create) 
for statement in statementList:
	sqlFile.write(statement)
