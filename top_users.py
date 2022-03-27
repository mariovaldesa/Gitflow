def top_ten_users( tweets, users ):
    top_userId_list = tweets['userId'].value_counts().index.tolist()[:10]
    return users[users["userId"].isin(top_userId_list)]
