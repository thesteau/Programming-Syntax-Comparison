# Programming-Syntax-Comparison

##### TODO
Add details on how to access and use the app  
Add main.py

## Microservice Architecture
A wikipedia and timer data microservices are used for this website. 

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

## Author
Steven Au

## License
See license for details
