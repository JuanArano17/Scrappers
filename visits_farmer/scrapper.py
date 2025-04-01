# scrapper.py
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
URL = os.getenv("URL_TO_VISIT", "https://google.com")

def visit_url(url, show_execution):
    """
    Configures Chrome, visits the specified URL, simulates interactions (scroll and click),
    and remains on the page for 12 seconds before closing the browser.

    Parameters:
      - url (str): The URL to visit.
      - show_execution (bool): If False, runs in headless mode; otherwise, shows the browser window.
    """
    chrome_options = Options()
    if not show_execution:
        chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Initialize the ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get(url)
    time.sleep(2)  # Allow the page to load
    
    # Simulate scrolling and clicking
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    time.sleep(2)
    try:
        body = driver.find_element(By.TAG_NAME, 'body')
        body.click()
    except Exception as e:
        print("Error during click:", e)
    
    time.sleep(8)  # Ensure a total duration of 12 seconds
    driver.quit()
