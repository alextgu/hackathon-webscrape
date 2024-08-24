from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_website(url, tags_and_classes, scroll_pause_time=1, scroll_increment=1000, max_scrolls=30):
    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Open the website
    driver.get(url)
    # Scroll the page until all content is loaded or maximum scrolls reached
    last_height = driver.execute_script("return document.body.scrollHeight")
    # Increment of scroll
    increment = 150
    for i in range(max_scrolls):
        for j in range(0, last_height, scroll_increment):
            driver.execute_script(f"window.scrollTo(0, {j});")
            time.sleep(scroll_pause_time)  # Adjust sleep time to wait for content to load
            
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        # Break the loop if no more content is loaded
        if new_height == last_height:
            break
        
        last_height = new_height
        scroll_increment += increment
        # Decrease incrementing size (but still overall increasing scroll range) to ensure all content is loaded
        increment = int(increment/1.1)

    # Wait for the JavaScript to render the content
    wait_conditions = [EC.presence_of_element_located((By.CLASS_NAME, cls)) for _, cls in tags_and_classes]
    WebDriverWait(driver, 10).until(
        EC.any_of(*wait_conditions)
    )
    
    # Retrieve and parse the page source
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find and return the desired data
    data = []
    for tag, class_name in tags_and_classes:
        elements = soup.find_all(tag, {'class': class_name})
        data.extend([element.get_text(strip=True) for element in elements])
    
    # Close the browser
    driver.quit()
    
    return data

# Dictionary mapping URLs to their respective tags and class names (with multiple tags and classes per URL)
url_tags_classes_map = {
    'https://devpost.com/hackathons?challenge_type[]=online': [
        ('span', 'label round host-label'),
        ('div', 'submission-period'),
        ],  
    'https://mlh.io/seasons/2025/events': [
        ('h3','event-name'), 
        ('p','event-date'), 
        ('div','event-location')
        ],

}

# List to store all scraped data
all_data = []

for url, tags_and_classes in url_tags_classes_map.items():
    data = scrape_website(url, tags_and_classes)
    all_data.extend(data)

# For now it will be printing
for item in all_data:
    print(item)

# Class build to organize
class Hackathon(object):
    def __init__(self, name, time, location, prize, category) -> None:
        self.name = name
        self.time = time
        self.location = location
        self.prize = prize
        self.category = category



