""" Import necessary packages """
from flask import Flask

""" Step 1: Inside the repo, create a basic flask app that has a 'hello world' as the main index (/), 
and create at least two additional pages """

# Assign variable "app" to Flask
app = Flask(__name__)


#Assign flask route and website message
@app.route('/')
def main():
    return 'Hello World'

@app.route('/sbu') 
def sbu():
    return 'Welcome to the Stony Brook University Test Page'

@app.route('/hants')
def hants():
    return 'Hello Dr.Williams'

#Assign DNS 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)