import re
import pandas as pd
import demoji
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def clean(text):
    # removes @mentions, punctuation, hyperlinks, retweet mentions, and all lowercase
    return re.sub("(@\w+)|([^\d\w \t])|(\w+:\/\/\S+)|(RT @\w+: )", " ", text).lower()

def vader(df):
    sentiment = df['text_2'].apply(lambda text: SentimentIntensityAnalyzer().polarity_scores(text))
    df = pd.concat([df,sentiment.apply(pd.Series)],axis = 1)
    return df

def remove_emoji(text): #removes emojis from text
    return demoji.replace(text, "")

def tweet_drop(df):
    df =df.drop(columns=
        ['usercreatedts','coordinates','quoted_status_id','quoted_status_userid',
         'quoted_status_username','following','is_retweet','original_tweet_id',
        'original_tweet_userid','original_tweet_username','in_reply_to_status_id',
        'in_reply_to_user_id','in_reply_to_screen_name','Unnamed: 0'])
    # select only English and no quote status
    df = df.loc[df['language'] == 'en'].loc[df['is_quote_status']== False].loc[df['location'].notna()]
    # delete all possible new media
    words = ['news', 'News', 'media', 'Media', 'channel', 'newspaper', 'commercial']
    word ='|'.join(words)
    df = df.drop(df[df['acctdesc'].str.contains(word, na=True)].index)
    df = (df.sort_values(by=['retweetcount'], ascending = False))