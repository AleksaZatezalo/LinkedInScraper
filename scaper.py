from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

###########################
# Selenium Functionality
###########################

def create_driver():
    """
    Creates the driver needed to browse the web.
    """

    service = Service(executable_path='./chromedriver')
    driver = webdriver.Chrome(service=service)
    return driver

def authenticate(driver, username, password):
    """
    Authenticate to LinkedIn in order to browse it. Uses browser driver browser.
    """

    driver.get("https://www.linkedin.com/")
    email = driver.find_element(By.ID, "session_key")
    passwd = driver.find_element(By.ID, "session_password")
    email.send_keys(username)
    passwd.send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)

    return 0

def search_job(driver, search):
    """
    Searches for jobs that match search variable search.
    """
    
    # format search string to url format
    # driver.get("https://www.linkedin.com/jobs/search/?keywords={srch}&origin=SUGGESTION").format(srch = search)
    return 0

###########################
# Scraping Functionality
###########################
def get_jobs(search):
    """
    Gets a list of jobs that have search in there title. 
    Returns a 3D array with jobs, there company and there discriptions.
    """

    pass

def get_connections(company):
    """
    Gets a list of proffesional connections that work at a company.
    """
    
    pass

def job_description(job_descriptions, file):
    """
    Saves job_descption to file. Takes a 2D array containing Job Titles, Connections Boolean and Descriptions job_descriptions.
    Saves to file, file.
    """

    pass

def main():
    email = input("what is your email? ")
    passwd = input("what is your password? ")
    search = input("what jobs are you looking for? ")
    drive = create_driver()
    authenticate(drive, email, passwd)
    search_job(drive, search)

if __name__ == '__main__':
    main()