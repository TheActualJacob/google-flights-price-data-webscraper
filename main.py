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
from fake_useragent import UserAgent
import datetime
import sys

c=1
while True:
    timern = datetime.datetime.now()
    day = datetime.date.today()
    
    print(c, ' cycle')
    c = c+1

    
    #if True:
        
    if timern.hour == 0 and timern.minute == 48 and day.weekday() == 5:

        date = 'December 24th'

        req =urllib.request


        icaos = ['jfk+to+lax', 'ord+to+jfk', 'lax+to+ord', 'clt+to+atl', 'mia+to+jfk', 'lhr+to+jfk']

        for o in icaos:

            #setting the website destination
            
            url = 'https://www.google.com/flights?q='+o+'&rlz=1C1VDKB_enUS1018US1018&source=lnms&impression_in_search=true&mode_promoted=true&tbm=flm&sa=X&ved=2ahUKEwjIhpO91uj7AhVgkWoFHRafDVQQ_AUoAXoECAQQAw'

            #making sure url is correct
            print(url)




            #setting up the browser bot
            options = Options()

            ua = UserAgent()
            user_agent = ua.random
            print(user_agent)
            options.add_argument(f'user-agent={user_agent}')

            options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
            driver = webdriver.Firefox(options=options, executable_path='C:/Users/danke/OneDrive/Documents/webscrape proj/geckodriver.exe')


            #telling the bot what website to go to
            driver.get(url)
            time.sleep(3)

            #telling the bot to find the date change button
            while True:
                try:
                    print('test')
                    button = driver.find_element('xpath', '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input')
                    button.click()
                    print(2)
                    

                except:
                    i1 = 0
                    i1 = i1 + 1
                    time.sleep(1)
                    if i1 == 3:
                        print('i1 error')
                        break
                
                else:
                    break
                    

                
            
            
            time.sleep(2)

            #telling but to find the 

            while True:
                try:
                    innerbutton = driver.find_element('xpath', '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input')

                    #entering the date as the variable we defined earlier, "today"
                    innerbutton.send_keys(date)
                    print(2)
                    

                except:
                    i2 = 0
                    i2 = i2 + 1
                    time.sleep(1)
                    if i2 == 3:
                        print('i2 error')
                        break
                else:
                    break
               
            time.sleep(2)


            #telling but to find the buttons necassary to save the changes to the dates
            while True:
                try:
                    done = driver.find_element('xpath', '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[3]/div[3]/div/button')
                    done.click()
                    print(2)
                    
                except:
                    i3 = 0
                    i3 = i3 + 1
                    time.sleep(1)
                    if i3 == 3:
                        print('i3 error')
                        break
                
                else:
                    break
                
            time.sleep(3)

            while True:
                try:
                    oneway = driver.find_element('xpath', '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div[1]/div/button')
                    oneway.click()
                    print(2)
                    
                except:
                    i4 = 0
                    i4 = i4 + 1
                    time.sleep(1)
                    if i4 == 3:
                        print('i4 error')
                        break
                else:
                    break
              
            time.sleep(2)

            #telling the bot to find the one way button and click
            while True:
                try:
                    onewaybutton = driver.find_element('xpath', '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/div[2]/ul/li[2]')
                    onewaybutton.click()
                    
                except:
                    i5 = 0
                    i5 = i5 + 1
                    time.sleep(1)
                    if i5 == 3:
                        print('i5 error')
                        break

                else:
                    break
                
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



            #getting rid of all extra unesecarry stuff that might of slipped in
            out = ['AM', 'PM']
            res = [ele for ele in rawpricelist if all(ch not in ele for ch in out)]
            edited = [ele.replace(',','') for ele in res]
            integ = [s.lstrip('$') for s in edited]




            #saving the filter list as variable "pricelist" and making them all integers so we can run it through numpy liabry to get statstical data
            pricelist = list(map(int, integ))

            #creating another list just for the flight data inside excel sheet we will be creating
            flightdatalist = []
            for i in range(len(pricelist)):
                flightdatalist.append(date)
                flightdatalist.append(pricelist[i])
                i = i + 1

            #sorting list from greatest to least
            pricelist.sort()




            print(res)
            print(pricelist,'\n')




            #getting highest and lowest prices
            lowestprice = pricelist[0]
            highestprice = pricelist[-1]


            #for loop for good indexing
            indext = []
            for i in pricelist:
                indext.append(date)
                

            #putting the prices in a dataframe so it can be converted to .csv
            dataframe = pd.DataFrame(pricelist, index=indext)








            #storing our data in a .csv file
            with open('C:/Users/danke/OneDrive/Documents/webscrape proj/csv info/'+o+".csv", 'a+') as f:

                #converting flightdata list to csv format
                
                csvwriter = csv.writer(f)
                csvwriter.writerow(flightdatalist)
                


                
                f.write('DATE FROM THIS TRANSMISSION '+date+'\n\n Median : '+str(dataframe.median())+', \n\n Average : '+str(dataframe.mean())+', \n\n Highest Price : '+ str(highestprice)+', \n\n Lowest Price : '+str(lowestprice)+', \n\n\n\n')
                
                f.close()
            print(dataframe.median())


            driver.close()

            

            time.sleep(2)
        sys.exit()
    time.sleep(59)


        