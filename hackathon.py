import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_website(url, tags_and_classes, scroll_pause_time=1, scroll_increment=1000, max_scrolls=25):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    last_height = driver.execute_script("return document.body.scrollHeight")
    increase = 150

    for i in range(max_scrolls):
        for j in range(0, last_height, scroll_increment):
            driver.execute_script(f"window.scrollTo(0, {j});")
            time.sleep(scroll_pause_time)
            
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        
        last_height = new_height
        scroll_increment += increase
        increase = int(increase / 1.1)

    wait_conditions = [EC.presence_of_element_located((By.CLASS_NAME, cls)) for _, cls in tags_and_classes]
    WebDriverWait(driver, 10).until(EC.any_of(*wait_conditions))

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extract name and date separately
    name = None
    date = None

    for tag, class_name in tags_and_classes:
        elements = soup.find_all(tag, {'class': class_name})
        texts = [element.get_text(strip=True) for element in elements]

        # Assign texts to name and date based on expected order 
        if tag == 'h3' or 'span' in tag:  # TAGS ARE ASSUMED
            name = texts
        elif tag == 'p' or 'div' in tag:  # TAGS ARE ASSUMED
            date = texts

    # Return paired name and date
    if name and date:
        return list(zip(name, date))
    else:
        return []

# URL mapping
url_tags_classes_map = {
    'https://devpost.com/hackathons': [
        ('span', 'label round host-label'),
        ('div', 'submission-period'),
    ],
    'https://mlh.io/seasons/2025/events': [
        ('h3', 'event-name'), 
        ('p', 'event-date'), 
    ],
}

all_data = []

for url, tags_and_classes in url_tags_classes_map.items():
    data = scrape_website(url, tags_and_classes)
    all_data.extend(data)

# Convert to DataFrame with only Name and Date columns
df = pd.DataFrame(all_data, columns=["Name", "Date"])

# Print DataFrame to terminal
print(df.to_string(index=False))
