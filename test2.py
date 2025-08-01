from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

url = "https://www.faceit.com/en/cs2/league/ESEA%20League/a14b8616-45b9-4581-8637-4dfd0b5f6af8/3de05c27-da01-4ede-9319-f5b3f16dfb1f/teams?region=63c30440-d4c7-4754-8111-11c4ccfbefd1&division=7100087c-63d2-4a65-95db-55fd3a3336a6&stage=232468e6-acf9-4877-9ecb-a810dcffb875&conference=84065e93-393d-49e9-8972-f557f80a4922"
driver.get(url)

wait = WebDriverWait(driver, 30)

selector = 'a[href*="/team/"] span'

# Scroll and wait for content to load
team_ids_and_names = {}

prev_count = 0
same_count = 0
max_same_count = 5  # Stop if no new teams after 5 scrolls
scroll_pause = 3  # seconds to wait after each scroll

while same_count < max_same_count:
    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause)

    # Wait for at least one team to appear
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    except:
        pass  # Continue anyway

    team_link_elements = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/team/"]')

    # Collect unique teams
    for elem in team_link_elements:
        try:
            team_name = elem.text.strip()
            team_url = elem.get_attribute('href')
            if team_url and '/team/' in team_url and team_name:
                team_id = team_url.split('/team/')[-1].split('/')[0]
                team_ids_and_names[team_id] = team_name
        except:
            continue

    current_count = len(team_ids_and_names)
    print(f"Teams found so far: {current_count}")

    if current_count > prev_count:
        same_count = 0
        prev_count = current_count
    else:
        same_count += 1

print(f"\n✅ Found {len(team_ids_and_names)} unique teams (ID : Name):\n")
for team_id, team_name in team_ids_and_names.items():
    print(f"{team_id} : {team_name}")

driver.quit()
