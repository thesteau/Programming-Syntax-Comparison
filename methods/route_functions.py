import os
import googleapiclient.discovery
import requests
import json
from private import private


class RouteData:
    """ General catch all for all the functions and data for the main.py """

    selection_danger = "Please submit a selection to view the other pages."
    wiki_err = """Currently, either the service provider is down, \
        Wikipedia is down, or there are multiple pages unable to be parsed for this language.
        Apologies for the inconvenience!
        """
    syntax_err = ["#Unfortunately, syntax details for this concept is not yet implemented."]

    def try_passer(self, setting, message):
        """ Attempt to fill in the message data to be returned as the target accordingly.
            This method eliminates the code try-except simple data insertion code smell
        """
        try:
            target = setting
        except:
            target = message
        return target

    def get_videos(self, language, concept):
        """ Per the youtube API documentation.
            Note that this code is based on the official documentation to make a query.
                Pass in the language and concept to be queried
        """
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service = "youtube"
        api_ver = "v3"

        API_KEY = private.PrivateKeys().youtube()

        youtube = googleapiclient.discovery.build(api_service, api_ver, developerKey = API_KEY)
        req = youtube.search().list(
            part="snippet",
            maxResults=5,
            q=language + ' ' + concept
        )

        # Get only the items list
        res = req.execute()["items"]

        return res

    def process_vid_ids(self, session):
        """ Get the session dictionary and process it into its own dictionary sets per the IDS"""
        youtube_key1 = {}
        youtube_key2 = {}

        youtube1 = self.get_videos(session["language"], session["topic"])
        youtube2 = self.get_videos(session["language2"], session["topic"])

        for each_value in range(5):
            # The items are in a list, since I am only requesting 5, look range up to 5.
            # This is also increase I decide to increase the amount of IDS to be queried later, my own restriction is
            # up to 5 results for my own requests.
            try:
                video1 = youtube1[each_value]["id"]["videoId"]
            except:
                video1 = "zOjov-2OZ0E"
            try:
                video2 = youtube2[each_value]["id"]["videoId"]
            except:
                video2 = "zOjov-2OZ0E"

            # USe the numbers as a string hard coded.
            youtube_key1.update({str(each_value): video1})
            youtube_key2.update({str(each_value): video2})

        data = {
            "youtube1": youtube_key1,
            "youtube2": youtube_key2
        }

        return data


    def get_wikipedia(self, query):
        """ Fetch wikipedia data
            Use of group mate's microservice from:
                Thomas, Thanh Thao Vu
            """
        url = "https://cs361-wiki-app.herokuapp.com/?search="
        sub_query = "_programming_language"

        # Fixes a bug with symbols
        conversion = {
            "C#": "c_sharp",
            "C++": "c_plus_plus"
        }

        if query in conversion:
            query = conversion[query]

        base_query = query + sub_query
        wikipedia_search = url + base_query

        json_query = requests.get(wikipedia_search)
        return json.loads(json_query.content)[base_query]
