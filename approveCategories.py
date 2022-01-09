import currentListValidation
"""
validateCategories() is being called form editor.py
@param : a dictionary, Key=line#:Value=List of category inputs
We will return a dictionary with Key=Line#:Value= Dictionary of categoryValid/categoryInvalid:categoryValue

1. Itirate through the dictionary. Confirm if the Category input list is valid. The length must be an even number.
   If number of categories NOT valid, update dictionary key=Line#:value="Invalid number of categories"
   If number of categoies IS valid, send the list to have its values validated.
"""

# first take each line and check the category list length
# the length of category list must be even, otherwise they are missing a category field
# VV- The function being called from editor.py -VV
def validateCategories(linesCategoried):
	categoryStatus = {} # initilize return dictionary.
	for line in linesCategoried: # itirate through each key in Dictionary (the dict recieved as param)
		currentList = linesCategoried[line] # the category list of the current key.
		listLength = len(currentList) # get the length of the list
		# Check the length 
		if listLength % 2 != 0: # if the length is not even
			# category list length is odd, missing a category or not seperated by 2 or more spaces
			msg = {"Line has an invalid number of categories.":" Seperate each category by 2 or more spaces."}
			categoryStatus.update({"Line "+str(line):msg})
		else:
			#categoryStatus.update({line:"Line "+str(line)+" has valid number of category count."})
			#print("Line "+str(line)+": ")
			returnedValidation = currentListValidation.checkCategoryInputs(currentList) # send the current category List to be validated, returns a dict
			categoryStatus.update({"Line "+str(line):returnedValidation}) # update our return dictionary
	#print(categoryStatus)
	return categoryStatus