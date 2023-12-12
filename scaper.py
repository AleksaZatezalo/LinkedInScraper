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

def search_profile(driver, search):
    """
    Searches for jobs that match search variable search.
    """
    
    driver.get("https://www.linkedin.com/in/{0}".format(search))
    return 0

###########################
# Scraping Functionality
###########################
def get_profile(driver, search):
    """
    Gets a list of jobs that have search in there title. 
    Returns a 3D array with jobs, there company and there discriptions.
    """

    search_profile(driver,  search)
    src = driver.page_source

    # Scroll to the bottom
    

    start = time.time()
    # will be used in the while loop
    initialScroll = 0
    finalScroll = 1000
 
    # while True:
    #     driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    #     # this command scrolls the window starting from
    #     # the pixel value stored in the initialScroll 
    #     # variable to the pixel value stored at the
    #     # finalScroll variable
    #     initialScroll = finalScroll
    #     finalScroll += 1000
    
    #     # we will stop the script for 3 seconds so that 
    #     # the data can load
    #     time.sleep(3)
    #     # You can change it as per your needs and internet speed
    
    #     end = time.time()
    
    #     # We will scroll for 20 seconds.
    #     # You can change it as per your needs and internet speed
    #     if round(end - start) > 20:
    #         break

    soup = BeautifulSoup(src, 'lxml')
    intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
    return intro

def save_to_file(results, file):
    """
    Saves the output of the get_jobs function to file file.
    """

    # output = get_jobs(driver, search)
    pass

def main():
    # Launch
    f = Figlet(font='slant')
    print(f.renderText("LinkedIn Profile Scraper"))

    ###################################
    # THE TO DO LIST
    ###################################
    # Make input fields arguemnts
    # Make Defaults like printing to STDER
    # Add Shebang to Script
    
    # Set up
    email = input("what is your email? ") # Make this an argument
    passwd = input("what is your password? ") # Make this an argument
    search = input("what jobs are you profile for? ") # Make this an argument
    
    # Do the search
    drive = create_driver()
    authenticate(drive, email, passwd)
    search_profile(drive, search)
    
    # Scrape and Save
    output = get_profile(drive, search)
    print(output)

if __name__ == '__main__':
    main()