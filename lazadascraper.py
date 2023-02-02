from selenium import webdriver
import pandas as pd
import time
import re

#get the link of the page

#open chrome
browser = webdriver.Chrome('/Applications/Google Chrome.app/Contents/chromedriver_mac_arm64/chromedriver.exe')
browser.get('https://www.lazada.com.my/shop-mobiles/apple/')

#Loop the web scraping function from page 1 to page 3 
listing_list = []
i = 0
count = 0
while (count<41):
    listing = browser.find_elements_by_class_name('buTCk')
    price = browser.find_elements_by_class_name('aBrP0')
    next_button = browser.find_element_by_class_name('ant-pagination-next')
    for l in listing:
        title = l.find_element_by_class_name('RfADt').text
        price = l.find_element_by_class_name('aBrP0').text
        l_item = { 
            'title' : title,
            'price' : price,
        }

        listing_list.append(l_item)
    browser.execute_script("arguments[0].click();", next_button)
    time.sleep(i+1)
    count +=1


len(listing_list)
#save the listings and their respective prices into a dataframe
df = pd.DataFrame(listing_list)

#Text Cleaning (remove emojis on the listings title)
def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

df["title"] = df["title"].apply(remove_emoji)

#export the data into a csv file
df.to_csv('iphone.csv')








