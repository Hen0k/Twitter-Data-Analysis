# Twitter-Data-Analysis

## Data-Preparation

This part is handled by classes from `extract_dataframe.py`, `clean_tweets_dataframe.py`, and `tweets_preprocess.py`
* The first converts the raw JSON files into a pandas dataframe
* Then the cleaner takes care of duplicates, nan values, datatype casting and similar operations
* The last one prepares the cleaned data for modeling by assigning a label for each row

## MySQL integration


SQLAlchamy is used with pandas to have a higher level interface to the database. All the database related functionalities will be in the `mysql_manager.py` file

## EDA and Modeling

There are 3 jupyter notebooks inside the notebooks folder. I have tried to play with the data and extract what I thought was interesting. Most of them are presented with visualizations. 

## Dashboard

For this part I used streamlit to show different finding I got from the EDA notebook. In addition there are wordclouds gennerated using hashtags and tweet texts

# Future tasks

* More test coverage
* Add logging
* More and better exception handling
* More data analysis and modeling
* Add Model drift detection
* Integrate model to the dashboard