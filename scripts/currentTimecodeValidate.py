import re # moduel to use regex
"""
checkTimecodes() is being called from currentListValidation.py
They broke the categories input list into 2 Lists, metadata (first 4 inputs) timecodes (remaining inputs)
This function is given the timecodes list as a @param

1. Go through each input and check if it meets its criteria.
return a list, valid/invalid per input
"""

def checkTimecodes(timeCodesList):
	allTimecodes = timeCodesList
	validTimecodeFormat = re.compile("^\d{2};\d{2};\d{2};\d{2}$") # the formart we want the timecodes to be in
	timecodesStatus = []
	#print(allTimecodes)
	# List of all Invalid timecodes 
	invalidTimecodes = [timecode for timecode in allTimecodes if validTimecodeFormat.match(timecode) is None]
	# List of all Valid timecodes 
	validTimecodes = [timecode for timecode in allTimecodes if validTimecodeFormat.match(timecode) is not None]
	
	# Now loop through the timecodes we were given, can check which list was that timecode in, valid or invalid list
	timecodePlace = 1
	for time in allTimecodes:
		if time in invalidTimecodes:
			# this is a invalid timecode, get its index in allTimecodes list
			i = allTimecodes.index(time)
			if i%2==0:
				TimecodeStatus = "Invalid IN "	
			else:
				TimecodeStatus = "Invalid OUT "
				timecodePlace -=1	

		else:
			# this timecode is valid, get its index in allTimescodes list
			i = allTimecodes.index(time)
			if i%2==0:
				TimecodeStatus = "Valid IN "	
			else:
				TimecodeStatus = "Valid OUT "
				timecodePlace -=1
		timecodesStatus.append(str(TimecodeStatus)+str(timecodePlace))
		timecodePlace +=1

	return timecodesStatus