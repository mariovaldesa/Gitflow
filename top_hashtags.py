import re
import pandas as pd

def top_ten_hashtags( tweets ):
    hashtags_list = list()
    for content in tweets["renderedContent"]:
        content_list = re.split( '\n| ', content )
        for word in content_list:
            if word.startswith('#'):
                hashtags_list.append(word)

    hashtags = pd.DataFrame( hashtags_list, columns = ['hashtag'] )
    for hashtag in hashtags['hashtag'].value_counts().index.tolist()[:10]:
        print( hashtag )

