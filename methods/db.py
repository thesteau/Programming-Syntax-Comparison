# Database
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class DB:
    """ All database methods """

    def db_init(self):
        """ Log in creds"""
        # Firebase credentials
        cred = credentials.Certificate("./private/programming-language-compare-firebase-adminsdk-ia3t7-d90a6adec3.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://programming-language-compare-default-rtdb.firebaseio.com/'
        })

    def db_get(self):
        """ Grab all raw data"""
        data = db.reference('languages')
        return data.get()

    def process_group(self, language, topic):
        """ Grab the appropriate data."""
        data = db.reference('languages').get()

        # Conversion due to an error on keys.
        if language == "C#":
            language = "Cs"

        return data[language][topic]
