# Twitter API authentication

import tweepy
import settings

from settings import twitter_json_mapping
from models import insert_json_data


def get_twitter_api(settings):
    # authorize the API Key
    authentication = tweepy.OAuthHandler(settings.api_key, settings.api_secret)

    # authorization to user's access token and access token secret
    authentication.set_access_token(settings.access_token, settings.access_token_secret)

    # call the api
    api = tweepy.API(
        authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True
    )

    if api.verify_credentials():
        return api
    else:
        return None


api = get_twitter_api(settings)

if api:

    print("connected Ok!")

    new_search = "iran -filter:retweets"
    tweets = tweepy.Cursor(
        api.search, q=new_search, result_type="recent", include_entities=True, lang="en"
    ).items(50)

    for tweet in tweets:

        if tweet._json.get("id", None) is None:
            continue

        data = {}
        for key, func in twitter_json_mapping.items():
            data[key] = func(tweet._json)

        data["keyword"] = "iran"
        insert_json_data(data, "tweets")
