import unittest
import pandas as pd
import numpy as np
import sys
import os
from pprint import pprint
import json
from clean_tweets_dataframe import CleanTweets
from extract_dataframe import TweetDfExtractor
from extract_dataframe import read_json

sys.path.append(os.path.abspath(os.path.join('../..')))


_, tweet_list = read_json("data/Economic_Twitter_Data.json")


class TestCleanTweets(unittest.TestCase):
    """
                A class for unit-testing function in the clean_tweets_dataframe.py file

                Args:
        -----
                        unittest.TestCase this allows the new class to inherit
                        from the unittest module
        """

    def setUp(self) -> pd.DataFrame:
        self.extractor = TweetDfExtractor(tweet_list[:5])
        self.clean_df = self.extractor.get_tweet_df()
        self.numerical_columns = ['polarity', 'subjectivity',
                                  'retweet_count', 'favorite_count',
                                  'followers_count', 'friends_count']

    def test_convert_to_numbers(self):
        for column in self.numerical_columns[:2]:
            self.assertEqual(str(self.clean_df[column].dtype), 'float64')
        for column in self.numerical_columns[2:]:
            self.assertEqual(str(self.clean_df[column].dtype), 'int64')

if __name__ == '__main__':
    unittest.main()
