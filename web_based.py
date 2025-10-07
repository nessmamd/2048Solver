from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os 
import re
import time

#first get the page open and running 
def openGame(): 
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    #give full access to it so we can get containers 
    user_data_dir = os.path.expanduser("~/chrome_selenium_profile")
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    #go on website
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://2048game.com/")
    return driver

def getContents(driver): 
    #you want to clear it after every move
    grid = [[0 for _ in range(4)] for _ in range(4)]

    tile_container = driver.find_element(By.CLASS_NAME, "tile-container")
    tiles = tile_container.find_elements(By.CLASS_NAME, "tile")

    for tile in tiles:
        classes = tile.get_attribute("class")  # The full class string

        value_match = re.search(r'tile-(\d+)', classes)
        if value_match:
            tile_value = int(value_match.group(1))
        
        position_match = re.search(r'tile-position-(\d+)-(\d+)', classes)
        if position_match:
            row = int(position_match.group(1))
            col =int(position_match.group(2))
        grid[col - 1][row - 1] = tile_value

    for x in grid: 
        print(x)
    print("--------------")
    return grid

def decision(grid, driver): 
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(5)

if __name__ == "__main__":
    instance = openGame() 
    grid = getContents(instance)
    for x in range(3):
        decision(grid, instance)
        getContents(instance)






