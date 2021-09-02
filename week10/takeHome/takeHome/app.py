# We now need the json library so we can load and export json data
import json

from flask import Flask
    
app = Flask(__name__)

# We're using the new route that allows us to read a trip from the URL
@app.route('/trip/<trip_id>')
def trip(trip_id):
    # Additionally, we're now loading the JSON file's data into file_data 
    # every time a request is made to this endpoint
    with open('./DivvyChallenge.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    # We can then find the data for the requested date and send it back as json
    return json.dumps(file_data[trip_id])

if __name__ == '__main__':
    app.run(debug=True)