# clearUploadsDir.py
# before user gets to upload a new .txt file, we clean out the uploads folder of all .txt files
import os, glob 

def clearUploadsFolder(uploadsPath):
	files = glob.glob(uploadsPath+'/*.txt')
	if len(files) > 0:
		for file in files:
			os.remove(file)
