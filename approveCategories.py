import re # moduel to use regex 
from datetime import datetime
# first take each line and check the category list length
# the length of category list must be even, otherwise they are missing a category field

def validateCategories(linesCategoried):
	def checkMetadata(mainCategoryList):
		#print("Main Categories are...")
		#print(mainCategoryList)
		metadata = {"show_name":"", "show_ID":"", "show_type":"", "show_date":""}
		metadata.update({"show_name":mainCategoryList[0], "show_ID":mainCategoryList[1], "show_type":mainCategoryList[2], "show_date":mainCategoryList[3]})
		#print(metadata)
		# check show_name. Must be 1-100 chars in length
		if len(metadata["show_name"]) >=1 and len(metadata["show_name"]) <=100:
			# Valid show_name
			pass
		else:
			# Invalid show_name
			metadata.update({"show_name":"invalid"})

		# check show ID. first 4 letters A-Z followed by 9 digits
		pattern = '^[A-Z]{4}[0-9]{9}$'
		resultID = re.match(pattern, metadata["show_ID"])
		if resultID:
			# valid id
			pass
		else:
			#invalid id
			metadata.update({"show_ID":"invalid"})

		# check show_type. must be either of these options [movie,episode,sports,news]
		showTypes = ["movie","episode","sports","news"]
		resultType = metadata["show_type"].lower() in showTypes
		if resultType:
			# valid show type
			#print("Valid show type")
			pass
		else:
			# invalid show type
			#print("invalid show type")
			metadata.update({"show_type":"invalid"})

		# check show_date. must be in format "mm-dd-yyyy" 
		dateFormat = '%m-%d-%Y'
		resultDate = True
		try:
			resultDate = bool(datetime.strptime(metadata["show_date"], dateFormat))
		except ValueError:
			resultDate = False
		if resultDate:
			# valid date format
			#print("valid date format")
			pass
		else:
			# invalid date format
			#print("invalid date format")
			metadata.update({"show_date":"invalid"})
		#print(metadata)
		return metadata


	def checkTimecodes(timeCodesList):
		timecodeFormat = re.compile("^\d{2};\d{2};\d{2};\d{2}$")
		#print(timeCodesList)
		#["seg_start", "seg_end"]
		timescodesDic = {}
		count = 0
		for timecode in timeCodesList:
			if timecodeFormat.match(timecode) is not None:
				#timecode format matches
				#print("timecode format matches")
				#pass
				if count % 2 == 0:
					if count == 0:
						timescodesDic.update({"Timecode IN "+str(count+1):timecode})
					else:
						timescodesDic.update({"Timecode IN "+str(count):timecode})
				else:
					if count == 1:
						timescodesDic.update({"Timecode OUT "+str(count):timecode})
					else:
						timescodesDic.update({"Timecode OUT "+str(count-1):timecode})
			else:
				#timecode format does not match
				#print("timecode does not match")
				if count % 2 == 0:
					if count == 0:
						timescodesDic.update({"Timecode IN "+str(count+1):"invalid"})
					else:
						timescodesDic.update({"Timecode IN "+str(count):"invalid"})
				else:
					if count == 1:
						timescodesDic.update({"Timecode OUT "+str(count):"invalid"})
					else:
						timescodesDic.update({"Timecode OUT "+str(count-1):"invalid"})
			count +=1
		#print(timeCodesList)
		return timescodesDic



	def checkCategoryInputs(currentList):
		# split the first 4 categories apart, thats metadata. The rest is timecodes
		main_categories = currentList[:4] # indexs 0 upto-but-not-including 4
		time_codes = currentList[4:] # index 4 upto-last-index. 
		metadataDic = checkMetadata(main_categories)
		timecodeList = checkTimecodes(time_codes)
		
		print(metadataDic)
		print(timecodeList)

	categoryStatus = {}
	for line in linesCategoried:
		currentList = linesCategoried[line]
		listLength = len(currentList)

		if listLength % 2 != 0:
			categoryStatus.update({line:"Line "+str(line)+" has an invalid number of categories."})
		else:
			#categoryStatus.update({line:"Line "+str(line)+" has valid number of category count."})
			print("Line "+str(line)+": ")
			checkCategoryInputs(currentList)

	#print(categoryStatus)


# # Each line is split into categories, the category count is a even number, we must validate the entries
# def validateEntries(current_line):
#     #print(current_line)
#     #lineLength = len(current_line)
#     main_categories = current_line[:4] # index 0 upto but not including 4
#     time_codes = current_line[4:] # index 4 upto last index
#     print(main_categories)
#     print(time_codes)
#     # Second time verifying timecode start and end pair
#     if(len(time_codes) % 2) != 0:
#         # odd length, not complete start and stop time codes
#         print("Must have pair of timecode start AND timecode end")
#     else:
#         print("Pairs of timecards Valid")