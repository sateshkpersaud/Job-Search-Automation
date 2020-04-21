from bs4 import BeautifulSoup
import requests

# URL to search
URL = 'https://www.jobbank.gc.ca/jobsearch/jobsearch?fn=2174&sort=D&fprov=ON#results-list-content'

# Get HTML
page = requests.get(URL)

# BEautify the returned results
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='result_block')

jobs = soup.findAll("a", class_="resultJobItem")

valid_jobs = []
for job_elem in jobs:
    queryString = job_elem.get("href")

    job_url = 'https://www.jobbank.gc.ca' + queryString
    #job_url = 'https://www.jobbank.gc.ca/jobsearch/jobposting/32263030?source=searchresults'
    job_page = requests.get(job_url)
    job_soup = BeautifulSoup(job_page.content, 'html.parser')
    # GEt the second paragraph to check if they require canadian pr or citizen
    job_results = job_soup.select(".job-posting-detail-apply p:nth-of-type(2)")
    if len(job_results) == 0:

        valid_jobs.append(job_url)

print(valid_jobs)








