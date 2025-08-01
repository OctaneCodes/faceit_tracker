from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up ChromeDriver
driver = webdriver.Chrome()  # or use driver_path with Service(...)

url = "https://www.faceit.com/en/cs2/league/ESEA%20League/a14b8616-45b9-4581-8637-4dfd0b5f6af8/3de05c27-da01-4ede-9319-f5b3f16dfb1f/teams?region=63c30440-d4c7-4754-8111-11c4ccfbefd1&division=7100087c-63d2-4a65-95db-55fd3a3336a6&stage=232468e6-acf9-4877-9ecb-a810dcffb875&conference=84065e93-393d-49e9-8972-f557f80a4922"
driver.get(url)
wait = WebDriverWait(driver, 30)  # increased wait timeout

selector = 'div[class^="styles__TeamMetaContainer"] span[class^="Text-sc"]'
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

team_names_set = set()
same_count = 0
max_same_count = 5  # allow more scroll attempts without new teams
scroll_pause = 4  # seconds to wait after scrolling

while same_count < max_same_count:
    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause)  # wait longer for new content to load

    # Get team names
    team_elements = driver.find_elements(By.CSS_SELECTOR, selector)
    current_team_names = {el.text for el in team_elements if el.text.strip()}

    if len(current_team_names) > len(team_names_set):
        team_names_set.update(current_team_names)
        same_count = 0
    else:
        same_count += 1

print(f"\n✅ Found {len(team_names_set)} unique teams:\n")
for team in sorted(team_names_set):
    print("-", team)

driver.quit()
