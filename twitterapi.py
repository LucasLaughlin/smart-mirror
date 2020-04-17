#!/usr/bin/python3

import twitter

api = twitter.Api(consumer_key='wKLcgF2gPeJUFT5aMgB4UU5p7',
		consumer_secret='g86W2E1K2oqBtRr5U9W5luZOuT3n7avEqqkezvo3ULFgUqedyu',
		access_token_key='nokeys',
		access_token_secret='nokeys')

# Twitter timeline info taken from here 
# https://python-twitter.readthedocs.io/en/latest/twitter.html?highlight=timeline#twitter.api.Api.GetHomeTimeline

timeline = api.GetHomeTimeline(count=5)
print([t.text for t in timeline])
