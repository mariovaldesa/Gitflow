def top_ten_days( tweets ):
    tweets['date'] = tweets['date'].dt.strftime('%Y-%m-%d')
    dates_list = tweets['date'].value_counts().index.tolist()[:10]
    for date in dates_list:
        print(date)
