from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class findSongScript:

  def find_song(song, artist, driver):
    search = driver.find_element("name","q")
    search.send_keys(song + " " + artist)
    search.submit()
    try:
      search = WebDriverWait(driver,20).until(EC.presence_of_element_located(
      (By.CSS_SELECTOR, "[class*=u-quarter]"))
      )
      top_song = driver.find_elements(By.CSS_SELECTOR, "[class*=u-quarter]")[0]
      top_song.click()
      
    except:
      driver.quit()
    
  
  driver = webdriver.Edge()
  driver.get("https://genius.com")
  print("song?")
  song = input()
  print("artist?")
  artist = input()
  find_song(song, artist, driver)  
  print("finding song lyrics...")
  try:
    search = WebDriverWait(driver,20).until(EC.presence_of_element_located(
      (By.ID, "lyrics-root"))
    )
    print(search.text)
  finally:
    driver.quit()
  
