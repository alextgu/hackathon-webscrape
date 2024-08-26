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

    if you want to manually install it:
    - Webdriver Chrome
        check your version - chrome://settings/help  
        a. for 114.0.5735.90 and older - https://sites.google.com/chromium.org/driver/downloads
        b. newer versions - https://googlechromelabs.github.io/chrome-for-testing/ 

2. (Optional): Add more links and specifications, make sure all of the code is adjusted towards the changes.

3. Run


Sample Output
                                    Name                  Date
                                  Convex Jul 30 - Sep 17, 2024
                                    Dell Aug 14 - Oct 02, 2024
                          Code4TheFuture Jun 12 - Aug 29, 2024
                              RevenueCat Aug 05 - Sep 19, 2024
                   Constellation Network Jul 15 - Sep 09, 2024
                                TRON DAO Jul 25 - Oct 08, 2024
                        ForestHackathons May 25 - Oct 31, 2024


This program is straightforward but versatile. Feel free to use and modify the code as needed. Feedback is always appreciated (even the mean ones).

This project is licensed under the MIT License. See the LICENSE file for details.
