# Web Scraping using Selenium and Pandas

Selenium is a popular open-source web-based automation tool. Using the Python programming language, it is possible to “scrape” data from 
the web in a quick and efficient manner. The Selenium package is used to automate web browser interaction from Python. With Selenium,
programming a Python script to automate a web browser is possible.

I have used TECHOLUTION job listing page to scrape data about the job openings and export as a CSV file sorted in ascending order with
respect to date of job posting.

url = 'https://techolution.app.param.ai/jobs/'

APPROACH

The first approach was to understand the structure of the website from the source code. After that I ran a loop to traverse
through all the job listings and automate selenium to click on job title in every loop. In the job title page the job description 
html elements did not have any unique identifier. So I used xpath to find element and extract data. The data extracted was stores 
in a list. After the completion of the loop the data in the list was converted to a pandas dataframe. The dataframe is sorted in
ascending order with respect to date of job posting. Finally the data was extracted as a CSV file.

DATA VISUALIZATION

The data extracted in csv file was then visualised in a google colab jupyter notebook. Data visualization and exploratory analysis 
helps to find pattern and make sense of data. I used Matplotlib and seaborn libraries for data visualization.
