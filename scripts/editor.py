from readMarker import *   # custom moduel that reads the marker file line by line
import makeCategories      # custom moduel to split each line into categories
import approveCategories   # custom moduel to validate the category entries
import clearUploadsDir     # custom moduel to clean out uplaods folder before user uploads new .txt file

def clearUploads(uploadsPath):
	clearUploadsDir.clearUploadsFolder(uploadsPath)

def extractFile(uploadsPath, filename):
	Lines = getLines(uploadsPath, filename)
	# Step 1 : break the line into categories,
	linesCategoried = makeCategories.splitLines(Lines) # returns dictionary, key is line#:value is a list of categories found in that line
	#print(linesCategoried)

	# Step 2 : validate each lines categories
	linesStatus = approveCategories.validateCategories(linesCategoried)

	#print(linesStatus)
	return linesStatus