from selenium import webdriver 
from bs4 import BeautifulSoup
import time 
import csv
start_url="https://exoplanets.nasa.gov/exoplanet-catalog/"
browser=webdriver.Chrome("/Users/adityabhattacharya/Downloads/chromedriver")
browser.get(start_url)
def scrap():
    headers=["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planetData=[]
    for i in range(0,428):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all('ul',attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,li_tag enumerate(li_tags):
                if index==0 :
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tags.contents[0])
                    except:
                        pmp_list.append("")
            planetData.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()         
    with open("scrapper_2.csv","w ")as f:    
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrap()               

                    