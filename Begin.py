import os
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options  
import string
from selenium.webdriver.common.keys import Keys

chrome_driver = "C:\Program Files\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")

# Using chrome to access web
driver = webdriver.Chrome(chrome_driver, options = chrome_options)
print (driver.title)

# open the website

driver.get('https://ebay.com.au')
# please open manually ; I have opened

# # Select the search box
search_box = driver.find_element_by_id('gh-ac').clear()
driver.find_element_by_id('gh-ac').send_keys('Airpods')

# Click search button
search_button = driver.find_element_by_id('gh-btn').click()

# Select category
# category_box = driver.find_element_by_id('gh-cat')
# category_box.select_by_value

driver.implicitly_wait(10)

# Applying seller filter
more_refinements = driver.find_element_by_class_name('x-refine__main__list--more')
more_refinements.find_element_by_css_selector('button').click()
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, 'c2-mainPanel-seller'))
)
driver.find_element_by_id('c2-mainPanel-seller').click()
driver.find_element_by_id('c2-subPanel-_x-seller[0]_toggler').click()
driver.find_element_by_id('c2-subPanel-_x-seller[0]-8[2]-0_rbx').click()

to_submit = driver.find_element_by_class_name('x-overlay-footer__apply')
to_submit.find_element_by_css_selector('button').click()


# # Applying price filter
# price_tab = driver.find_element_by_xpath('//ul[@class= "x-refine__price"]') 
# price_filter = price_tab.find_elements_by_css_selector('.x-textrange__input')

# # Input values in price filter
# price_filter[0].send_keys(239)
# price_filter[1].send_keys(239)
# price_tab.find_element_by_css_selector('button').click()
# WebDriverWait(driver, 30).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "srp-river-results"))
# )


# Check if filter has been applied
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "s0-13-11-6-3-MULTI_ASPECT_GUIDANCE_APPLIED_ASPECTS-answer-2-1-0-list"))
)


# Number of results found
check_null = '//div[@id="mainContent"]/div[1]/div[2]/div[2]/div[1]/div[1]/h1/span[1]'
results_found = driver.find_element_by_xpath(check_null)
print(results_found.text)

while(results_found.text == '0'):   # Loop till number of results found is 0
    print("empty search")
    driver.refresh()
    driver.implicitly_wait(5)
    results_found = driver.find_element_by_xpath(check_null)


# Ends while when search result found
driver.implicitly_wait(5)
xpath = '//ul[@class="srp-results srp-list clearfix"]'
search_results = driver.find_element_by_xpath(xpath) # notice I use element //whole thing in one element
num_products=len(search_results.find_elements_by_css_selector('li'))
print(num_products)       #these are links
products = search_results.find_elements_by_css_selector('.s-item a')
required_product = products[0]  # First product

required_product.click()

# Add to cart
# NO ITEM SHOULD BE IN CART
add_to_cart = driver.find_element_by_id('atcRedesignId_btn').click()

# # View cart (ITEM ALREADY IN CART)
# elif(EC.presence_of_element_located((By.ID, 'atcLnk'))) :
#     view_cart = driver.find_element_by_id('vi-viewInCartBtn').click()
#     driver.implicitly_wait(5)
#     # CHECKOUT
#     driver.find_element_by_xpath('//div[@id="mainContent"]/div/div[3]/div/div[1]/button').click()
# //*[@id="atcRedesignId_overlay-atc-container"]/div/div[1]/div/div[2]/a[1]
# //*[@id="atcRedesignId_overlay-atc-container"]/div/div[1]/div/div[2]/a[1]/span/span
driver.implicitly_wait(10)
# CHECKOUT
driver.find_element_by_xpath('//div[@id="atcRedesignId_overlay-atc-container"]/div/div[1]/div/div[2]/a[1]').click()

driver.implicitly_wait(15)

# Select card method
driver.find_element_by_css_selector('.payment-entry--CC input').click()

# Enter code
coupon_code = driver.find_element_by_id('redemptionCode').clear()
driver.find_element_by_id('redemptionCode').send_keys('ABC10')

apply_code_button = driver.find_element_by_xpath('//div[@class = "incentives-button"]/button').click()
