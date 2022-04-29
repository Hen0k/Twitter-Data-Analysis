import json
from pprint import pprint
from traceback import print_exc
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import inspect

from clean_tweets_dataframe import CleanTweets
from tweets_preprocess import SADataPreparation
from utils import DataLoader


LABLED_SCHEMA = "labled_schema.sql"
CLEANED_SCHEMA = "cleaned_schema.sql"
CSV_PATH = "processed_tweet_data.csv"
BANNER = "="*20


with open("db_cred.json", 'r') as f:
    config = json.load(f)

# Connect to the database
connections_path = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}/twitter_data"
engine = create_engine(connections_path)


# Create the tables
def create_tables():
    try:
        with engine.connect() as conn:
            for name in [LABLED_SCHEMA, CLEANED_SCHEMA]:
                with open(name) as file:
                    query = text(file.read())
                    conn.execute(query)
        print("Successfully created 2 tables")
    except:
        print("Unable to create the Tables")
        print(print_exc())


# Read the data
def get_data(labled=True):
    loader = DataLoader('./', CSV_PATH)
    tweets_df = loader.read_csv()
    print("Got the dataframe")
    cleaner = CleanTweets()
    cleand_df = cleaner.run_pipeline(tweets_df)
    print("Done Cleaning")
    if not labled:

        return cleand_df

    pprocessor = SADataPreparation()
    labled_df = pprocessor.preprocess_data(cleand_df)

    return cleand_df, labled_df


# Populate the tables
def insert_data(df: pd.DataFrame, table_name):
    try:
        with engine.connect() as conn:
            df.to_sql(name=table_name, con=conn,
                      if_exists='replace', index=False)
        print(f"Done inserting to {table_name}")
        print(BANNER)
    except:
        print("Unable to insert to table")
        print(print_exc())


# Implement Querying functions
def get_table_names():
    with engine.connect() as conn:
        inspector = inspect(conn)
        names = inspector.get_table_names()
        return names


def get_labled_texts():

    top_ten = engine.execute(
        "SELECT `original_text`, `score` from tweets_information LIMIT 10;").fetchall()
    pprint(top_ten)


if __name__ == "__main__":
    create_tables()
    cleand_df, labled_df = get_data()
    insert_data(labled_df, "tweets_information")
    get_labled_texts()
