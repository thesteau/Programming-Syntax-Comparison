# Programming-Syntax-Comparison

# TODO
Add details on how to access and use the app  
Add main.py

### Website Schematics


### Privacy
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

For Firebase credentials, you will need to initiate Firebase and replace the corresponding code accordingly.  
Thereafter, save the Firebase key into your private directory.

### Author
Steven Au

### License
See license for details
