import pandas as pd
import string
import re
from nltk.corpus import stopwords
from sqlalchemy import column
from wordcloud import STOPWORDS
import contractions


class CleanTweets:
    """
    The PEP8 Standard AMAZING!!!
    """

    def __init__(self):
        print('Automation in Action...!!!')

    def drop_unwanted_rows(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = df[df['retweet_count']
                           == 'retweet_count'].index
        df.drop(unwanted_rows, inplace=True)
        df = df[df['polarity'] != 'polarity']

        return df

    def remove_links(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove links in tweets
        """
        df['original_text'] = df['original_text'].replace(
            r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True)

        return df

    def remove_special_characters(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove numbers and any especial charaters like @ for retweets
        """
        df['original_text'] = df['original_text'].str.replace(
            "[^a-zA-Z#]", " ", regex=True)

        return df

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        df.drop_duplicates(inplace=True)

        return df

    def fill_nan(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fill nan values in the possibly sensitive column with False
        """
        df[['possibly_sensitive']] = df[[
            'possibly_sensitive']].fillna(value=False)

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

    def to_lower(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert tweet and hashtags to lower case
        """
        df["original_text"] = df["original_text"].str.lower()
        df["hashtags"] = df["hashtags"].str.lower()
        df["source"] = df["source"].str.lower()
        df["original_author"] = df["original_author"].str.lower()
        df["user_mentions"] = df["user_mentions"].str.lower()
        df["place"] = df["place"].str.lower()

        return df

    def remove_stopwords(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Combine stopwords from different libraries and remove them from each tweet
        """
        my_stopwords = set(stopwords.words('english'))
        my_stopwords = STOPWORDS.union(my_stopwords)
        custom_stopwords = set(['t', 'rt', 'ti', 'vk', 'to', 'co',
                                'dqlw', 'z', 'nd', 'm', 's', 'kur', 'u', 'o', 'd'])
        my_stopwords = my_stopwords.union(custom_stopwords)
        df["original_text"] = df["original_text"].apply(
            lambda doc: " ".join([word for word in doc.split()
                                  if word not in my_stopwords])
        )

        return df

    def remove_mentions_and_hashtag(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove user mentions and hashtags from the tweet text
        """
        # in here the `df.loc[word.name...` the `word.name` part is to
        # access row index within the apply function
        df['original_text'] = df['original_text'].apply(
            lambda doc: " ".join(
                [word for word in doc.split()
                    if not word.startswith(("#", "@"))])
        )

        return df

    def expand_contractions(self, df: pd.DataFrame) -> pd.DataFrame:
        df['original_text'] = df['original_text'].apply(
            lambda doc: " ".join([contractions.fix(word) for word in doc.split()]))

        return df
    
    def rename_column(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.rename(columns={"original_text": "clean_text"})
        return df

    def run_pipeline(self, df: pd.DataFrame, save_csv: bool=False):
        df = self.drop_unwanted_rows(df)
        df = self.remove_non_english_tweets(df)
        df = self.drop_duplicate(df)
        df = self.convert_to_datetime(df)
        df = self.convert_to_numbers(df)
        df = self.fill_nan(df)
        df = self.drop_nan(df)
        df = self.remove_mentions_and_hashtag(df)
        df = self.remove_links(df)
        df = self.expand_contractions(df)
        df = self.remove_special_characters(df)
        df = self.reset_index(df)
        df = self.to_lower(df)
        df = self.remove_stopwords(df)
        df = self.rename_column(df)
        if save_csv:
            df.to_csv("cleaned_data.csv")

        return df
