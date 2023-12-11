from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pyfiglet import Figlet
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
    
    driver.get("https://www.linkedin.com/jobs/search/?keywords={0}&origin=SUGGESTION".format(search))
    return 0

###########################
# Scraping Functionality
###########################
def get_jobs(driver, search):
    """
    Gets a list of jobs that have search in there title. 
    Returns a 3D array with jobs, there company and there discriptions.
    """

    pass


def save_to_file(results, file):
    """
    Saves the output of the get_jobs function to file file.
    """

    # output = get_jobs(driver, search)
    pass

def main():
    # Launch
    f = Figlet(font='slant')
    print(f.renderText("LinkedIn Job Scraper"))

    ###################################
    # THE TO DO LIST
    ###################################
    # Make input fields arguemnts
    # Make Defaults like printing to STDER
    # Add Shebang to Script
    
    # Set up
    email = input("what is your email? ") # Make this an argument
    passwd = input("what is your password? ") # Make this an argument
    search = input("what jobs are you looking for? ") # Make this an argument
    out_file = input("which file would you like to save to? ") # Make this an argument (default print to stderr)
    
    # Do the search
    drive = create_driver()
    authenticate(drive, email, passwd)
    search_job(drive, search)
    
    # Scrape and Save
    output = get_jobs(drive, search)
    save_to_file(output, out_file)

if __name__ == '__main__':
    main()