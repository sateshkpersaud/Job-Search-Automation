# Job-Search-Automation
A python script used to search the Canadian Job Bank website for software developer jobs, that does not require you to be a permanent resident or citizen, every two days and send me an email of new additions. 


Pseudocode
1. Use the url to search for software developer jobs posted in the last two days
2. If jobs are returned, iterate through each job in the list. 
3. If job does not have an intended job posting audience of anyone who can legally work in canada, then add to a global list.
4. On completion, send an email to me.


Possible technology/languageto use:
1. Python to request the data and send the email
2. BeautifulSoup to parse and search the returned HTML
