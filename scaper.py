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

def authenticate(driver):
    """
    Authenticate to LinkedIn in order to browse it. Uses browser driver browser.
    """

    # driver.get("https://www.linkedin.com/")
    pass

def search_job(driver, search):
    """
    Searches for jobs that match search variable search.
    """

    pass

def see_connections(driver, company):
    """
    Returns a list of people I know that work at a company.
    """
    
    pass


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

###########################
# Wrighting to Files
###########################

def job_description(job_descriptions, file):
    """
    Saves job_descption to file. Takes a 2D array containing Job Titles, Connections Boolean and Descriptions job_descriptions.
    Saves to file, file.
    """

    pass