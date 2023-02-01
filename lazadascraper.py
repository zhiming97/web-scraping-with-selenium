from selenium import webdriver
import pandas as pd
import time

#get the link of the page

#open chrome
browser = webdriver.Chrome('/Applications/Google Chrome.app/Contents/chromedriver_mac_arm64/chromedriver.exe')
browser.get('https://www.lazada.com.my/catalog//?from=input&q=HP%20Pavillion%2015&ppath=100005888:12055,100005938:63523')

#Loop the web scraping function from page 1 to page 3 
listing_list = []
i = 0
count = 0
while (count<14):
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
    browser.execute_script("arguments[0].click();", button)
    time.sleep(i+1)
    count +=1


len(listing_list)
#save the listings and their respective prices into a dataframe
df = pd.DataFrame(listing_list)
df

#export the data into a csv file
df.to_csv('phonelists.csv')


