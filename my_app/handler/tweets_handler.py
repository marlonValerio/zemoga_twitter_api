import requests

class tweets_handler():
    """
    Tweets handler
    """
    def __init__(self):
        """
        Initialize the tweets_handler class

        Variables:
            __bearer_token: Token which lets you use the Twitter API
        """
        self.__bearer_token = "AAAAAAAAAAAAAAAAAAAAAGFMcAEAAAAAc8bD5LmqyltgbEhQ8ihLz8Kp6xc%3DtOs4YvanYWWNn36IeFdPEl0ZZ28Xw2pVsSjpzWyRj9Jln9Mkun"

    def __bearer_oauth(self, r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer {self.__bearer_token}"
        r.headers["User-Agent"] = "v2UserTweetsPython"
        return r


    def __connect_to_endpoint(self, url, params={}):
        """
        Connects to the endpoint the get twitter information

        Params:
            url: endpoint
            params: endpoint paramaters

        Returns:
            Endpoint response

        """
        response = requests.request("GET", url, auth=self.__bearer_oauth, params=params)
        
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

    def get_user_id(self, user_name):
        """
        Get twitter user ID fron its user name

        Params:
            user_name: name of the user

        Returns:
            user id
        """
        url = "https://api.twitter.com/2/users/by/username/{}".format(user_name)
        params = {
            "user.fields": "profile_image_url,description"
        }
        json_response = self.__connect_to_endpoint(url, params=params)

        return json_response["data"]["id"]

    def get_tweets_from_id(self, user_id):
        """
        Gets the last five tweets of the user specified by its id

        Params:
            user_id: id of the user

        Returns:
            json which contains the tweets
        """
        url = "https://api.twitter.com/2/users/{}/tweets".format(user_id)
        params = {
            "tweet.fields": "created_at",
            "max_results": 5
            }
        json_response = self.__connect_to_endpoint(url, params)

        return json_response["data"]

    def get_tweets_from_name(self, user_name):
        """
        Gets the last five tweets of the user specified by its user name

        Params:
            user_name: name of the user

        Returns:
            json which contains the tweets
        """
        user_id = self.get_user_id(user_name)
        return self.get_tweets_from_id(user_id)