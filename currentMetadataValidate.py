import re # moduel to use regex
from datetime import datetime
"""
checkMetadata() is being called from currentListValidation.py
They broke the categories input list into 2 Lists, metadata (first 4 inputs) timecodes (remaining inputs)
This function is given the meatdata list as a @param

1. Go through each input and check if it meets its criteria.
return a list, valid/invalid per category value

"""

def checkMetadata(mainCategoryList):
	#print("Main Categories are...")
	#print(mainCategoryList)
	#["show_name", "show_ID", "show_type", "show_date"]
	metadata = ["show_name", "show_ID", "show_type", "show_date"]
	currentMetadataList = mainCategoryList # in the order (showName, showID, showType, showDate)
	#metadata.update({"show_name":mainCategoryList[0], "show_ID":mainCategoryList[1], "show_type":mainCategoryList[2], "show_date":mainCategoryList[3]})
	#print(metadata)
	# check show_name. Must be 1-100 chars in length
	if len(currentMetadataList[0]) >=1 and len(currentMetadataList[0]) <=100:
		# Valid show_name
		metadata[metadata.index("show_name")] = "Valid show_name"
	else:
		# Invalid show_name
		metadata[metadata.index("show_name")] = "Invalid show_name"

	# check show ID. first 4 letters A-Z followed by 9 digits
	pattern = '^[A-Z]{4}[0-9]{9}$'
	resultID = re.match(pattern, currentMetadataList[1])
	if resultID:
		# valid id
		metadata[metadata.index("show_ID")] = "Valid show_ID"
	else:
		#invalid id
		metadata[metadata.index("show_ID")] = "Invalid show_ID"

	# check show_type. must be either of these options [movie,episode,sports,news]
	showTypes = ["movie","episode","sports","news"]
	resultType = currentMetadataList[2].lower() in showTypes
	if resultType:
		# valid show type
		#print("Valid show type")
		metadata[metadata.index("show_type")] = "Valid show_type"
	else:
		# invalid show type
		#print("invalid show type")
		metadata[metadata.index("show_type")] = "Invalid show_type"

	# check show_date. must be in format "mm-dd-yyyy" 
	dateFormat = "%m-%d-%Y"
	resultDate = True
	try:
		resultDate = bool(datetime.strptime(currentMetadataList[3], dateFormat))
	except ValueError:
		resultDate = False
	if resultDate:
		# valid date format
		#print("valid date format")
		metadata[metadata.index("show_date")] = "Valid show_date"
	else:
		# invalid date format
		#print("invalid date format")
		metadata[metadata.index("show_date")] = "Invalid show_date"
	#print(metadata)
	return metadata