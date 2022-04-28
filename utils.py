from os import chdir
import pandas as pd

class DataLoader:
    def __init__(self,dir_name,file_name):
        self.dir_name = dir_name
        self.file_name = file_name


    def read_csv(self):
        chdir(self.dir_name)
        tweets_df = pd.read_csv(self.file_name)
        chdir("notebooks")
        return tweets_df