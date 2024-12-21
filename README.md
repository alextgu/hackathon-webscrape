HACKATHON DATASCRAPE PROJECT

This program automates the process of gathering hackathon information from specified websites, focusing on extracting the "name" and "date" of each event. It leverages the Selenium automation tool to handle JavaScript-driven content that traditional web scrapers often struggle with. After ensuring all dynamic content is loaded, the program uses BeautifulSoup for data extraction. 

Websites this program scans: 

https://devpost.com/hackathons

https://mlh.io/seasons/2025/events

Characteristics:

Name

Date

HOW TO RUN CODE:
1. Installations:
    Terminal
    - pip install selenium
    - pip install beautifulsoup4
    - pip install pandas
    - pip install TIME-python
    - pip install openpyxl
    - pip install webdriver manager (this handles the webdriver stuff)

    if you want to manually install webdriver manager:
    - Webdriver Chrome
        check your version - chrome://settings/help
      
        a. for 114.0.5735.90 and older - https://sites.google.com/chromium.org/driver/downloads

        b. newer versions - https://googlechromelabs.github.io/chrome-for-testing/ 

2. (Optional): Add more links and specifications, and make sure all of the code is adjusted towards the changes.

3. Run


Sample Output

<img width="361" alt="Screenshot 2024-08-26 at 7 56 15 PM" src="https://github.com/user-attachments/assets/4b8b5ae7-eae1-4ed0-ba0b-fc0f7dad8a0b">




This program is straightforward but versatile. Feel free to use and modify the code as needed. 

This project is licensed under the MIT License. See the LICENSE file for details.
