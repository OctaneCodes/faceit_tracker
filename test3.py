from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.delete_all_cookies()  # Clear cookies on start

url = ("https://www.faceit.com/en/cs2/league/ESEA%20League/a14b8616-45b9-4581-8637-4dfd0b5f6af8/"
       "3de05c27-da01-4ede-9319-f5b3f16dfb1f/teams?"
       "region=63c30440-d4c7-4754-8111-11c4ccfbefd1&"
       "division=7100087c-63d2-4a65-95db-55fd3a3336a6&"
       "stage=232468e6-acf9-4877-9ecb-a810dcffb875&"
       "conference=84065e93-393d-49e9-8972-f557f80a4922")

driver.get(url)
wait = WebDriverWait(driver, 30)

selector = 'div[class^="styles__TeamMetaContainer"] span[class^="Text-sc"]'
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

team_names_set = set()
no_new_count = 0
max_no_new = 5

scroll_pause = 3
scroll_step = 500  # Scroll by 500px increments

last_height = driver.execute_script("return document.body.scrollHeight")
scroll_position = 0

while no_new_count < max_no_new:
    scroll_position += scroll_step
    driver.execute_script(f"window.scrollTo(0, {scroll_position});")
    time.sleep(scroll_pause)

    team_elements = driver.find_elements(By.CSS_SELECTOR, selector)
    current_teams = {el.text.strip() for el in team_elements if el.text.strip()}

    if len(current_teams) > len(team_names_set):
        print(f"Found new teams: {len(current_teams)} total")
        team_names_set.update(current_teams)
        no_new_count = 0
    else:
        no_new_count += 1
        print(f"No new teams found in attempt {no_new_count}")

    new_height = driver.execute_script("return document.body.scrollHeight")
    if scroll_position >= new_height:
        # Reset scroll to bottom if reached end of page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)

print(f"\n✅ Found {len(team_names_set)} unique teams:\n")
for team in sorted(team_names_set):
    print("-", team)

driver.quit()
