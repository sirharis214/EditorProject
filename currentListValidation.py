import currentMetadataValidate
import currentTimecodeValidate
"""
checkCategoryInputs() is being called from approveCategories.py
@param  we are given a list which holds the current lines category input values.
Will will return a dictionary, Key=CategoryName+valid/invalid:Value=theCategoryInputValue
1. Split the category List into 2 Lists, metadata (first 4 index) timecodes (index 4 and beyond)
2. Validate metadata values. 
3. Validate timecode values.
"""

def checkCategoryInputs(currentList):
	# split the first 4 categories into a list called main_categories 
	# The remaining values in a list called time_codes
	#["show_name", "show_ID", "show_type", "show_date"]
	main_categories = currentList[:4] # indexs 0 upto-but-not-including 4
	#["seg_start", "seg_end"]
	time_codes = currentList[4:] # index 4 upto-last-index. 
	currentMetadataStatus = currentMetadataValidate.checkMetadata(main_categories) # return list of invalid/valid
	currentTimecodeStatus = currentTimecodeValidate.checkTimecodes(time_codes) # return list of invalid/valid
	#print(currentMetadataStatus)
	#print(currentTimecodeStatus)
	validatedInputs = currentMetadataStatus+currentTimecodeStatus # combine the two validated lists
	currentDict ={} # our return dictionary
	c = 0
	for inputVal in currentList:
		currentDict.update({inputVal:validatedInputs[c]})
		c +=1

	#print(currentDict)
	return currentDict