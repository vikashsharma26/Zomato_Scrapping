import requests
from bs4 import BeautifulSoup
import time
import json
url = "https://www.zomato.com/dharamshala/ram-nagar-restaurants?place_name=Dharamshala,%20Himachal%20Pradesh,%20India,%20India&dishv2_id=742929dcb631403d7c1c1efad2ca2700_2"
headers = {
    "User-Agent" : "chrome, version-86, win 7 64bit"
}
u = requests.get(url, headers=headers)
s = BeautifulSoup(u.text,"html.parser").find("body").find("div").find_all("div",class_="jumbo-tracker")
complete_detail = []
for i in s:
    details = {}
    helpper = i.find_all('a')
    details['Name'] = helpper[1].find('h4').text
    if "OFF" in helpper[0].p.text:
        details['Discount'] = helpper[0].p.text
    if "min" in helpper[0].p.text:
        details['Time Of Delivery'] = helpper[0].p.text
    else:
        details['Time Of Delivery'] = helpper[0].find_all('p')[1].text
    details['Rating'] = helpper[1].div.div.div.div.div.div.div.text
    details['Link'] = "https://www.zomato.com"+helpper[0]["href"]
    complete_detail.append(details)
print(complete_detail)
