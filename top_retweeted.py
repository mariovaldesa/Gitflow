
def top_ten_retweeted( tweets ):
    return tweets.sort_values(by=['retweetCount'], ascending=False).head(10)
    
