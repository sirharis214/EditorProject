from readMarker import *   # custom moduel that reads the marker file line by line
import makeCategories      # custom moduel to split each line into categories
import approveCategories   # custom moduel to validate the category entries

# Step 1 : break the line into categories, each category is seperated by multiple spaces
linesCategoried = makeCategories.splitLines(Lines) # returns dictionary, key is line# and value is list of categories found in line
#print(linesCategoried)

# Step 2 : validate each lines categories
linesStatus = approveCategories.validateCategories(linesCategoried)


        
    
        
    

        
    

#["show_name", "show_ID", "show_type", "show_date", "seg_start", "seg_end"]
