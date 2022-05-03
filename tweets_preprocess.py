from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer


class SADataPreparation:
    """
    This class handles the labeld data creation for a Sentiment Analysis task
    It takes in a cleaned datafrane and adds a new column that holds the label
    """

    def __init__(self):
        print("Pre-Processing the Tweets")

    def text_label(self, p) -> str:
        if p > 0:
            return 'positive'
        elif p < 0:
            return 'negative'
        else:
            return 'neutral'

    def preprocess_data(self, df, drop_neutral=False):
        polarity = df['polarity']
        score = polarity.apply(
            lambda x: self.text_label(x))
        labled_df = df.copy()
        labled_df['score'] = score
        if drop_neutral:
            neutrals = labled_df[labled_df['score'] == 'neutral']
            labled_df = labled_df.drop(neutrals.index)
        labled_df = labled_df.reset_index(drop=True)

        return labled_df

    def prepare_features(self, df):
        df = self.preprocess_data(df)
        score_series = df['score'].map({'positive': 1, 'negative': -1, "neutral":0})
        text_series = df['clean_text']
        X = text_series.tolist()
        y = score_series.tolist()

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.4)

        return X_train, X_test, y_train, y_test

    def vectorize_features(self, df):
        X_train, X_test, y_train, y_test = self.prepare_features(df)
        trigram_vect = CountVectorizer(ngram_range=(1, 2))
        trigram_vect.fit(X_train)
        X_train_trigram = trigram_vect.transform(X_train)
        X_test_trigram = trigram_vect.transform(X_test)

        return X_train_trigram, X_test_trigram, y_train, y_test, trigram_vect
