# read the marker file and save the content into a variable 

text_file = open("sample.txt", "r")
Lines = text_file.readlines()
text_file.close()

#print("Opening the sample text file...")
"""
text_file = open("sample.txt", "r")
text_full = text_file.read()
text_file.close()

# did we get all the info?
print('Here are the outputs')
print(text_full)
"""