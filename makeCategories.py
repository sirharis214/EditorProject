import re   # moduel to use regex 

# split the text file per line
def splitLines(Lines):
	eachLineCategory = {}  # empty dictionary that will hold each line as key and category list as value
	count = 0   # start line

	for line in Lines:
	    count += 1
	    #print("Checking Line # "+str(count)) # line # that we are on
	    clean_line = line.rstrip("\n") # removing trailing newline char
	    #print(clean_line)
	    lineSectioned = re.split(r"\s{2,}", clean_line) # splitting the line into categories by 2 or more spaces
	    #print(lineSectioned)
	    eachLineCategory.update({count:lineSectioned})
	return eachLineCategory
	    # # Length of the array once each entry is split
	    # lineLength = len(lineSectioned)
	    # # if Length of array is odd, we are missing a category or category are not divided by multispaces
	    # if(lineLength % 2) == 0:
	    #     # Even number lengeth, so all categories are entered
	    #     print("Validating category entries...")
	    #     validateEntries(lineSectioned)
	    # else:
	    #     # Odd number length
	    #     print("Missing a category or categories are not divided by 2 or more spaces")
	    #     validateEntries(lineSectioned)
	    # print("\n")