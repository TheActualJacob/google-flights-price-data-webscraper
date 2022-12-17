#importing all neccasary liabaries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd
import statistics
from selenium.webdriver.common.keys import Keys
import csv



date = 'tommorow'

req =urllib.request

#setting the website destination
icao1 = 'jfk'
icao2 = 'lax'
url = 'https://www.google.com/flights?q='+icao1+'+to+'+icao2+'&rlz=1C1VDKB_enUS1018US1018&source=lnms&impression_in_search=true&mode_promoted=true&tbm=flm&sa=X&ved=2ahUKEwjIhpO91uj7AhVgkWoFHRafDVQQ_AUoAXoECAQQAw'

#making sure url is correct
print(url)




#setting up the browser bot
options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(options=options, executable_path='C:/Users/danke/OneDrive/Documents/webscrape proj/geckodriver.exe')


#telling the bot what website to go to
driver.get(url)
time.sleep(3)

#telling the bot to find the date change button
button = driver.find_element('xpath', '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input')
button.click()
time.sleep(1)

#telling but to find the 
innerbutton = driver.find_element('xpath', '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input')

#entering the date as the variable we defined earlier, "today"
innerbutton.send_keys(date)
time.sleep(1)


#telling but to find the buttons necassary to save the changes to the dates
done = driver.find_element('xpath', '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[3]/div[3]/div/button')
done.click()
time.sleep(1)
oneway = driver.find_element('xpath', '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div[1]/div/button')
oneway.click()
time.sleep(1)

#telling the bot to find the one way button and click
onewaybutton = driver.find_element('xpath', '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/div[2]/ul/li[2]')
onewaybutton.click()
time.sleep(3)

#getting the javascript rendered html from the bot
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

#running html through a liabary called Beautiful soup to scrape for certain things within
soup = BeautifulSoup(html, 'html.parser')
stuff = soup.findAll('div', {'class':'YMlIz FpEdX jLMuyc'})



#Setting a filter to get all the ticket prices
prices = soup.findAll('span', {'role' : 'text'})

#putting all the found prices into a list
rawpricelist = []
for priceamount in prices:
    rawpricelist.append(priceamount.text)

#creating another list just for the flight data inside excel sheet we will be creating
flightdatalist = []
for pricees in prices:
    flightdatalist.append(icao1+'to'+icao2)
    flightdatalist.append(priceamount.text)

#getting rid of all extra unesecarry stuff that might of slipped in
out = ['AM', 'PM']
res = [ele for ele in rawpricelist if all(ch not in ele for ch in out)]
edited = [ele.replace(',','') for ele in res]
integ = [s.lstrip('$') for s in edited]

#saving the filter list as variable "pricelist" and making them all integers so we can run it through numpy liabry to get statstical data
pricelist = list(map(int, integ))

#sorting list from greatest to least
pricelist.sort()




print(res)
print(pricelist,'\n')




#getting highest and lowest prices
lowestprice = pricelist[0]
highestprice = pricelist[-1]

#putting the prices in a dataframe so it can be converted to .csv
dataframe = pd.DataFrame(pricelist)





    


#storing our data in a .csv file
with open("data.csv", 'a+') as f:
    #converting flightdata list to csv format
    csvwriter = csv.writer(f)
    data1 = csvwriter.writerow(flightdatalist)
    print(data1)
    #putting it on the file
    f.write(data1)

    f.write('\n\n Median : '+str(dataframe.median())+', \n\n Average : '+str(dataframe.mean())+', \n\n Highest Price : '+ str(highestprice)+', \n\n Lowest Price : '+str(lowestprice)+',')
    
