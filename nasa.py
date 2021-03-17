from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("/sohan_whjr/nasa/chromedriver")
browser.get(start_url)
time.sleep(10)
header = ["name", "light_years", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink",
 "temp_discovery_date", "temp_mass_planet", "plant_type", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]
planet_data = []
new_data = []

def scrap():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for i in range(1, 3):
        for ultag in soup.find_all("ul", attrs = {"class", "exoplanet"}): 
            li_tags = ultag.find_all("li")
            list1 = []
            for index, litag in enumerate(li_tags):
                if(index == 0):
                    list1.append(litag.find_all("a")[0].contents[0])
                else:
                    try:
                        list1.append(litag.contents[0])
                    except:
                        list1.append("")
            hyperlink_li_tag = li_tags[0]
            list1.append("https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a", href = True)[0]["href"])      
      
            planet_data.append(list1)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click() 
           

def scrape_more_data(hyperlink):
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content, "html.parser")
    for tr_tag in soup.find_all("tr", attrs = {"class":"fact_row"}):
        td_tags = tr_tag.find_all("td")
        list2 = []
        for td_tag in td_tags:
            try:
                list2.append(td_tag.find_all("div", attrs = {"class":"value"})[0].contents[0])
            except:
                list2.append("")    
        new_data.append(list2) 

scrap()        

for index, data in enumerate(planet_data):
    scrape_more_data(data[5])

final_data = []

for index, data in enumerate(planet_data):
    element = new_data[index]
    element = [elem.replace("\n", "")for elem in element]
    element = element[:7]
    final_data.append(data + element)    

with open("scraper.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(final_data)      

print(final_data)    