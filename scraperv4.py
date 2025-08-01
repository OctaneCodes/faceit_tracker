from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up ChromeDriver
driver = webdriver.Chrome()  # Or specify the path: Service(...) if needed

url = ("https://www.faceit.com/en/cs2/league/ESEA%20League/a14b8616-45b9-4581-8637-4dfd0b5f6af8/"
       "3de05c27-da01-4ede-9319-f5b3f16dfb1f/teams?"
       "region=63c30440-d4c7-4754-8111-11c4ccfbefd1&"
       "division=7100087c-63d2-4a65-95db-55fd3a3336a6&"
       "stage=232468e6-acf9-4877-9ecb-a810dcffb875&"
       "conference=84065e93-393d-49e9-8972-f557f80a4922")

driver.get(url)
wait = WebDriverWait(driver, 30)  # Longer wait timeout

# CSS selector for team name elements
selector = 'div[class^="styles__TeamMetaContainer"] span[class^="Text-sc"]'

# Wait for the first team element to appear
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

team_names_set = set()

max_no_new_teams = 5   # Number of scroll attempts without new teams before stopping
no_new_count = 0
scroll_pause = 4       # Seconds to wait after each scroll

while no_new_count < max_no_new_teams:
    # Scroll to bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause)  # Wait for new content to load

    # Collect current team names
    team_elements = driver.find_elements(By.CSS_SELECTOR, selector)
    current_teams = {el.text.strip() for el in team_elements if el.text.strip()}

    # Check if new teams were found
    if len(current_teams) > len(team_names_set):
        team_names_set.update(current_teams)
        no_new_count = 0  # Reset counter if new teams found
    else:
        no_new_count += 1  # Increment if no new teams

print(f"\n✅ Found {len(team_names_set)} unique teams:\n")
for team in sorted(team_names_set):
    print("-", team)

driver.quit()
