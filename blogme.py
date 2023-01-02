# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:48:23 2022

@author: Erik
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# reading excel or xlsx files
data = pd.read_excel('articles.xlsx')

# summary of the data and columns
data.describe()
data.info()

# counting number of articles per source
# format of groupby: df.groupby(['column_to_group'])['column_to_count'].count()
data.groupby(['source_id'])['article_id'].count()

# number of reactions per source
data.groupby(['source_id'])['engagement_reaction_count'].sum()

# dropping a column
data = data.drop('engagement_comment_plugin_count', axis=1)

# keyword flag loop
    
def keywordflag(keyword):
    keyword_flag=[]
    for title in data['title']:
        if keyword in str(title):
            flag=1
        else:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag

data['keyword_flag'] = pd.Series(keywordflag('murder'))

# SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()
sent = sent_int.polarity_scores(data['title'][16])
sent_int.polarity_scores('')

# new columns
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

for title in data['title']:
    try:
        sent = SentimentIntensityAnalyzer().polarity_scores(title)
        title_neg_sentiment.append(sent['neg'])
        title_pos_sentiment.append(sent['pos'])
        title_neu_sentiment.append(sent['neu'])
    except:
        title_neg_sentiment.append(0)
        title_pos_sentiment.append(0)
        title_neu_sentiment.append(0)
    
data['title_neg_sentiment'] = pd.Series(title_neg_sentiment)
data['title_pos_sentiment'] = pd.Series(title_pos_sentiment)
data['title_neu_sentiment'] = pd.Series(title_neu_sentiment)

# writing data to file
data.to_excel('blogme_clean.xlsx', sheet_name='blogmedata', index=False)
    
    
    