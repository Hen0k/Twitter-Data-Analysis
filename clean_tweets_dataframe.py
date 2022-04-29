import pandas as pd


class CleanTweets:
    """
    The PEP8 Standard AMAZING!!!
    """

    def __init__(self):
        print('Automation in Action...!!!')

    def drop_unwanted_column(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = df[df['retweet_count']
                           == 'retweet_count'].index
        df.drop(unwanted_rows, inplace=True)
        df = df[df['polarity'] != 'polarity']

        return df

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        df.drop_duplicates(inplace=True)

        return df

    def drop_nan(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop rows with nan entries
        """
        df.dropna(inplace=True)

        return df

    def convert_to_datetime(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert column to datetime
        """
        df['created_at'] = pd.to_datetime(df['created_at'])
        df = df[df['created_at'] >= '2020-12-31']

        return df

    def convert_to_numbers(self, df: pd.DataFrame, column_names=None) -> pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        if not column_names:
            column_names = ['polarity', 'subjectivity',
                            'retweet_count', 'favorite_count',
                            'followers_count', 'friends_count']
        for column in column_names:
            df[column] = pd.to_numeric(df[column])

        return df

    def remove_non_english_tweets(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        remove non english tweets from lang
        """
        df = df[df['lang'] == 'en']

        return df

    def reset_index(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        reset the index after preprocessing
        """
        df.reset_index(drop=True, inplace=True)

        return df

    def run_pipeline(self, df: pd.DataFrame):
        df = self.drop_unwanted_column(df)
        df = self.remove_non_english_tweets(df)
        df = self.drop_duplicate(df)
        df = self.convert_to_datetime(df)
        df = self.convert_to_numbers(df)
        df = self.drop_nan(df)
        df = self.reset_index(df)

        return df
