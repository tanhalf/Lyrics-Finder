from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, request, redirect
import os; import rstr; import urllib.parse
#use port 8000 and name redirect page callback
class findSongScript:
  def __init__(self):
    self.driver = webdriver.Edge()
    self._state = None

  # app =  Flask(__name__)

  # @app.route('/callback')
  # def callback(self):
  #   redirect_state = request.args.get('state')
  #   if redirect_state != self._state:
  #     print("state mismatch, retrying...")
  #     return self.user_login_auth()
  #   else:
  #     auth_code = request.args.get('code')
  #     body = {
  #       "grant_type": "authorization_code", 
  #       "code": auth_code,
  #       "redirect_uri": request.url
  #     }
  #     headers = {
  #       "content-type": "application/x-www-form-urlencoded",
  #       "Authorization": 
  #     }
      
    
  
  # if __name__ == "__main__":
  #   app.run(port=8000)
  
  # #def manual_option():
    
  # #def auto_option():

  # #def common_words(song):
  # #  words = []
  # #  if 
  
  # def user_login_auth(self):
  #   base_url = "https://accounts.spotify.com/authorize?"
  #   state_pattern = r"[A-Za-z0-9!@#$%]{16}"
  #   self._state = rstr.xeger(state_pattern)
  #   client_id = os.getenv("CLIENT_ID")
  #   redirect_uri = "https://localhost:8000/callback"
  #   client_secret = os.getenv("CLIENT_SECRET")
  #   scope = {"playlist-read-private " +
  #   "playlist-read-collaborative " +
  #   "user-read-email " +
  #   "user-read-private " +
  #   "user-library-read"}
  #   auth_params = {
  #     "client_id": client_id,
  #     "response_type": "code",
  #     "redirect_uri": redirect_uri,
  #     "scope": scope,7
  #     "state": self._state
  #   }
  #   auth_url = f"{base_url}{urllib.parse.urlencode(auth_params)}"
  #   self.driver.get(auth_url)


  #def is_user_login_auth_sus(state): 



  #def search_playlist(self):
   
    
  
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
  
