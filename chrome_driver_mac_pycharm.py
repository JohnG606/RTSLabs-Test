import os
from selenium import webdriver

# create a new Chrome session for search
driver = webdriver.Chrome(executable_path='../drivers/chromedriver')

# expanded browser was personal preference
driver.maximize_window()

# Go to the search engine website
driver.get("http://google.com")

# retrieve the search textbox (inspected google.com search box to retrieve name="q")
search_field = driver.find_element_by_name("q")

# enter search keyword and submit
search_field.send_keys("RTS Labs")
search_field.submit()

# choose first result (RTS Labs website- inspected first search result to retrieve h3 element)
driver.find_element_by_tag_name("h3").click()

# close the browser window
driver.quit()

