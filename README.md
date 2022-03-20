# Programming-Syntax-Comparison
Access and see this project live:  
https://programming-languages-compare.herokuapp.com/  

## Instructions
1. Choose two languages from the dropdown form. (Language 1 and Language 2)
2. Select a programming concept.
3. Click the "Submit" button.

## Microservice Architecture
Wikipedia scraper and timer data microservices are currently used for this website. 

JSON API:  
"Image of the Day"  
Accessible via the following URL route:  
https://programming-languages-compare.herokuapp.com/api

## Project Recreation and Analysis
Details to recreate this project is presented below. However, microservices may differ or become deprecated over time.  
You may cite code snippets if and only if you have requested for my permission first. Otherwise, you do not have permission to present this project as your own.

## Data
The database used is Firebase by Google.  
See the data directory for the raw data.  

## Navigation
* Select the items from the form
* Navigate to the other pages via the navigation bar
* Note that this a 20 second timer in between subsequent form submissions - the submit button will be disabled until the timer ends.
  * This is only noticed if the user returns to the form before the timer elapses.

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

## License
See license for details
