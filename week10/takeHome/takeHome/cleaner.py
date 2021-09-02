import csv
import json

# Define the header names so we can specify them when reading the CSV
fieldnames = (
    "trip_id","starttime","stoptime","bikeid","from_station_id","from_station_name","to_station_id",
    "to_station_id","to_station_idto_station_id","usertype","gender","birthday","trip_duration"
)

# Open both files so we can interact with them
# Using the `with` keyword lets us close the files automatically after these
# with blocks end and we're done writing and reading the files
with open('./DivvyChallenge.csv', 'r') as csvfile:
    with open('./DivvyChallenge.json', 'w') as jsonfile:
        # `next` will simply skip over the header row in the csvfile
        next(csvfile)
        # We use the csv library to create a 'reader' of the file
        # This reader patse through the csvfile and the headers 
        # and allow us to interact with it as a Python object
        reader = csv.DictReader(csvfile, fieldnames)
        # This creates an empty dictionary to hold the final set of 
        # data that we'll eventually dump into the JSON file
        final_data = {}
        # Now we use the reader to iterate over all the rows of the CSV
        # (except for the header) and then keep the values we want 
        for row in reader:
            # We also restructure the data so that it exists as 
            # a set of date keys with the value as a dictionary of
            # different data elements from the CSV.
            final_data[row["trip_id"]] = {
                "starttime": row["starttime"],
                "stoptime": row["stoptime"]
            }
        # Finally, we use the json library to output the final_data
        # dictionary to the jsonfile we opened earlier
        json.dump(final_data, jsonfile)
        # And then we write a final newline to the end of the file 
        # (this is just a best practice)
        jsonfile.write('\n')