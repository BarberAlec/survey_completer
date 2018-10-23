# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:36:33 2018

@author: alec barber
"""

from selenium import webdriver

def submit_form (submission):
    driver = webdriver.Firefox()
    driver.get('https://www.surveymonkey.com/r/YZ5JCDS')
    
    elem = driver.find_element_by_id("160943889_other")
    elem.clear()
    elem.send_keys(submission)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    elem = driver.find_element_by_class_name ("btn.small.done-button.survey-page-button.user-generated.notranslate")
    elem.click ()
    
    driver.quit()
    
def main():
    num_iterations = 1000
    for i in range(num_iterations):
        try:
            submit_form("Foody mcFoodPlace")
        except:
            print ("Error I guess, but really nothing to worry about bruh")
    
if __name__== "__main__":
    main()