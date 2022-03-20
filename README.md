# Programming-Syntax-Comparison
Programming syntax comparison web application for the purpose of easily identify nuances across multiple programming syntaxes.

See this project live:  
https://programming-languages-compare.herokuapp.com/  

## Instructions
1. Choose two languages from the dropdown form. (Language 1 and Language 2)
2. Select a programming concept.
3. Click the "Submit" button.

## Navigation
* Submit the form as instructed to be redirected to the details page.
* Navigate to the other pages via the navigation bar
* Note that there is a 20 second timer in between subsequent form submissions - the submit button will be disabled during this time.
  * This is only noticeable if the user returns to the form before the timer expires.

## Microservice Architecture
Wikipedia scraper and timer data microservices are currently used for this website. 

JSON API:  
"Image of the Day"  
Accessible via the following URL route:  
https://programming-languages-compare.herokuapp.com/api

## Project Recreation and Code Analysis
Details to recreate this project is presented below. However, microservices may differ or become deprecated over time.  
After downloading the dependencies, simply run the app via Python3 from the terminal.

```
python3 main.py
```
Alternatively
```
python [Directory of the code]main.py
```

## Data
The database used is Firebase by Google.  
See the data directory for the raw data.  

## Privacy
Unfortunately, API keys stored in the "private" directory will not be included in this public repository.  
You can recreate the private key file as followed:  
```python
class PrivateKeys:
    """ Storage of all keys data and their processing """

    def __init__(self):
        self.youtube_api = ''   # Your API
        self.unsplash_api = ''  # Your API

    def youtube(self):
        """ Youtube API private"""
        # Youtube API
        return self.youtube_api

    def image(self):
        """ Image service private"""
        return self.unsplash_api
```
For Firebase credentials, you will need to initiate Firebase and replace the appropriate code accordingly.  
Thereafter, save the Firebase key into the private directory.

#### Directory
```graphql
└─ private/
    ├─ private.py         # Contains the PrivateKeys class
    └─ firebaseKeys.json  # Firebase credentials
```

## Motivation
I always wanted to see the differences between programming languages yet the existing websites available only navigates and displays syntax details one by one. Instead, why not have the syntax displayed side by side as an easier method to understand programming language syntax nuances?

## Author
Steven Au

## Special Thanks
Undisclosed team.

## License
See license for details
