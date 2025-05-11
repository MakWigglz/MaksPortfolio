# Import csv module using the import keyword.
import csv  
# Import json module using the import keyword.
import json  
# Open some random JSON file in read-only mode using the open() function 
# and store it in a variable
gvn_jsonfile =open('samplefile.json','r')
# Open an empty CSV file in write mode using the open() function 
# and store it in another variable
gvn_csvfile=open('demo.csv','w')

# Pass the above given json file to the load() function of the json module
# to convert the json file data into a dictionary
dictionary =json.load(gvn_jsonfile)
# Pass the above given csv file to writer() function of the csv module to 
# pass the given csv to writer() function of csv file and store it in a variable to write content/data to csv file
write=csv.writer(gvn_csvfile)
# Write all the key values of the json file using writerow() function and 
# apply it on the above writing object 
write.writerow(dictionary.keys())
# Write all the dictionary values of the json file using writerow() function and 
# apply it on the above writing object 
write.writerow(dictionary.values())

# Close the given JSON file using the close() function
gvn_jsonfile.close()
# Close the given CSV file using the close() function
gvn_csvfile.close()
