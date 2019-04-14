# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 03:44:37 2019

@author: Heisenberg
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import pandas as pd

#launch url
url = 'https://techolution.app.param.ai/jobs/'

#create a new chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

records = []#empty list

num_links = len(driver.find_elements_by_class_name('job_list_card'))#total number of job titles listed
for i in range(num_links):
    #selenium visits each job title page
    button = driver.find_elements_by_class_name('job_name')[i]
    button.click()
    job_title = \
        driver.find_element_by_xpath("//*[@id='app']/div[2]/section/div/div[1]/h1"
            ).text.strip()
    job_id = \
        driver.find_element_by_xpath("//*[@id='app']/div[2]/section/div/div[2]/div/div[2]/div/div[2]/div/div[1]/span"
            ).text.strip()
    job_type = \
        driver.find_element_by_xpath("//*[@id='app']/div[2]/section/div/div[2]/div/div[2]/div/div[2]/div/div[2]/span"
            ).text.strip()
    job_location = \
        driver.find_element_by_xpath("//*[@id='app']/div[2]/section/div/div[2]/div/div[2]/div/div[2]/div/div[3]/span"
            ).text.strip()
    job_experience = \
        driver.find_element_by_xpath("//*[@id='app']/div[2]/section/div/div[2]/div/div[2]/div/div[2]/div/div[4]/span/span"
            ).text.strip()
    business_unit = \
        driver.find_element_by_xpath("//*[@id='app']/div[2]/section/div/div[2]/div/div[2]/div/div[2]/div/div[5]/span/span"
            ).text.strip()
    organisation = \
        driver.find_element_by_xpath("//*[@id='app']/div[2]/section/div/div[2]/div/div[2]/div/div[2]/div/div[6]/span/span"
            ).text.strip()
    post_date = \
        driver.find_element_by_xpath("//*[@id='app']/div[2]/section/div/div[2]/div/div[2]/div/div[2]/div/div[7]/span"
            ).text.strip()
    posted_by = \
        driver.find_element_by_xpath("//*[@id='app']/div[2]/section/div/div[2]/div/div[2]/div/div[2]/div/div[8]/span"
            ).text.strip()
    contact = \
        driver.find_element_by_xpath("//*[@id='app']/div[2]/section/div/div[2]/div/div[2]/div/div[2]/div/div[8]/a"
            ).text.strip()
    
    #stores data in a list
    records.append((
        job_title,
        job_id,
        job_type,
        job_location,
        job_experience,
        business_unit,
        organisation,
        post_date,
        posted_by,
        contact,
        ))

    # print(job_title)
    # print(job_type)
    # print(job_id)
    # print(job_location)
    # print(job_experience)
    # print(business_unit)
    # print(organisation)
    # print(post_date)
    # print(posted_by)
    # print(contact)
    
    #asks selenium to click back button
    driver.execute_script('window.history.go(-1)')
    #end loop block

#end the selenium browser session
driver.quit()

#store data in a pandas dataframe
df = pd.DataFrame(records, columns=[
    'job_title',
    'job_id',
    'job_type',
    'job_location',
    'job_experience',
    'business_unit',
    'organisation',
    'date_posted',
    'posted_by',
    'contact',
    ])
df['date_posted'] = pd.to_datetime(df['date_posted'])#convert date_posted to datetime format
df.sort_values(by='date_posted', inplace=True, ascending=True)#sorts the dataframe in ascending order of the date_posted
df.to_csv('record.csv', index=False, encoding='utf-8')#exported as a csv file