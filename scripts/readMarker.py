# read the marker file and save the content into a variable 

def getLines(uploadsPath, filename):
	text_file = open(uploadsPath+"/"+filename, "r")
	#text_file = open("/home/haris/Project/uploads/"+filename, "r")
	#text_file = open("../uploads/"+filename, "r")
	Lines = text_file.readlines()
	text_file.close()
	return Lines

	#print("Opening the sample text file...")
	"""
	text_file = open("sample.txt", "r")
	text_full = text_file.read()
	text_file.close()

	# did we get all the info?
	print('Here are the outputs')
	print(text_full)
	"""