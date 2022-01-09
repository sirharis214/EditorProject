import re   # moduel to use regex 
""" This moduel is used in editor.py
	the function splitLines takes a @param Lines, which is a list all the lines in the file.
	We will return a dictionary : Key = line# : Value = a list after splitting the line into categories
	1. Itirate through each line, strip the line of the new line char
	2. Split the line into categories using regex, each category is seperated by 2 or more blank spaces.
	3. Once complete, return the dictionary back to editor.py
"""
def splitLines(Lines):
	eachLineCategory = {}  # empty dictionary that will hold each line as key and category list as value
	count = 0   # start line

	for line in Lines:
	    count += 1 # the current line#
	    #print("Checking Line # "+str(count)) # line # that we are on
	    clean_line = line.rstrip("\n") # removing trailing newline char
	    #print(clean_line)
	    lineSectioned = re.split(r"\s{2,}", clean_line) # splitting the line into categories by 2 or more spaces
	    #print(lineSectioned)
	    eachLineCategory.update({count:lineSectioned})
	return eachLineCategory