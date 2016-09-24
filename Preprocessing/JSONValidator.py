import json

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True

fileCheck = open("phoneDetails.txt","r")

number = 0

for line in fileCheck:
	number += 1
	if is_json(line):
		print number