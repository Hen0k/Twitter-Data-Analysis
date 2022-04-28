import pandas as pd


class CleanTweets:
    """
    The PEP8 Standard AMAZING!!!
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')

    def drop_unwanted_column(self) -> pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = self.df[self.df['retweet_count']
                                == 'retweet_count'].index
        self.df.drop(unwanted_rows, inplace=True)
        self.df = self.df[self.df['polarity'] != 'polarity']

        return self.df

    def drop_duplicate(self) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        self.df.drop_duplicates(inplace=True)

        return self.df

    def convert_to_datetime(self) -> pd.DataFrame:
        """
        convert column to datetime
        """
        self.df['created_at'] = pd.to_datetime(self.df['created_at'])
        self.df = self.df[self.df['created_at'] >= '2020-12-31']

        return self.df

    def convert_to_numbers(self) -> pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        column_names = ['polarity', 'subjectivity',
                        'retweet_count', 'favorite_count',
                        'followers_count', 'friends_count']
        for column in column_names:
            self.df[column] = pd.to_numeric(self.df[column])

        return self.df

    def remove_non_english_tweets(self) -> pd.DataFrame:
        """
        remove non english tweets from lang
        """
        self.df = self.df[self.df['lang'] == 'en']

        return self.df

    def run_pipeline(self):
        self.drop_unwanted_column()
        self.remove_non_english_tweets()
        self.drop_duplicate()
        self.convert_to_datetime()
        self.convert_to_numbers()

        return self.df
