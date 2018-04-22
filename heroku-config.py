import os

def removeQuotesFromValue(value):
	value = value.replace("'", '"')
	# value = value.replace('"', "")
	return value

def splitLineIntoParts(line):
	line = line.lstrip()
	line = line.rstrip()
	line = removeQuotesFromValue(line)
	line = line.split("=", 1)
	return line

def setConfigVar(name, value):
	os.system('heroku config:set ' + name + '=' + value)

with open('.env') as e:
	
	for line in e:
		l = splitLineIntoParts(line)
		if (len(l) > 1):
			name = l[0]
			value = l[1]
			print()
			print ("*** Setting " + name + " = " + value + " ***")
			setConfigVar(name, value)
			

