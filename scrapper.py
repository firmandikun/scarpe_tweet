import streamlit as st
import pandas as pd
import tweepy



st.title('Twitter Scraper Python M Firman Setiawan')

# Key Token
mykeys = open('API_key/apikey.txt', 'r').read().splitlines()

api_key = "GzshP54XKTuAvtsMha9d6LYKp"
api_key_secret = "V9l3PkaK4Xw0gcz4KCRQim2aHF5CvSYgK43xdf45l2AFd9OpMu"
access_token = "1588033254220652545-G020MdNeu9aaik4P4p0gInZCNdbNYt"
access_token_secret = "Hz272xfk8bO6tdvFcclbFsdgEEzoRx59fgugUbpPVtdd2"
auth_hendler = tweepy.OAuthHandler(api_key, api_key_secret)
auth_hendler.set_access_token(access_token, access_token_secret)



# code streamlit
st.sidebar.header('Masukan kata untuk melakukan scrape :')
option_form = st.sidebar.form("option_form")
value_input = option_form.text_input('Masukan Kata')

add_data = option_form.form_submit_button(label='Submit')

if add_data :
    if value_input == '' : 
         result = 'Anda tidak menginputkan apapun!'
         st.write(result)  
    else : 
        # Crawling data
        api = tweepy.API(auth_hendler, wait_on_rate_limit= True)
        search_term = value_input
        remove_rt = '-filter:retweets'
        # Tweepy Cursor
        tweets = tweepy.Cursor(api.search_tweets, q=search_term + remove_rt, lang='id').items(1000)
        # Pulling information from tweets iterable 
        tweets_ = [[tweet.user.screen_name, tweet.text] for tweet in tweets]
        #Make DataFrame for tweets after crawling
        tweets_list = pd.DataFrame(data=tweets_, columns=['Username', 'Komentar'])
        # Creation of dataframe from tweets list
        tweets_df = pd.DataFrame(tweets_list)
        st.table(tweets_df)
        tweets_df.to_excel('data_kotor.xlsx', "rb")


