import requests
from bs4 import BeautifulSoup
import pandas as pd
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
#print(results.prettify())
job_elements = results.find_all("div", class_="card-content")
title=[]
company=[]
location=[]
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    title.append(title_element.text.strip())
    company.append(company_element.text.strip())
    location.append(location_element.text.strip())
    
df = pd.DataFrame({'Job Title':title,'Company Name':company,'Location':location}) 
df.to_csv('jobs.csv', index=False, encoding='utf-8')
