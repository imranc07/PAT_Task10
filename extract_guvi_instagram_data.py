"""
Using python selenium automation and the URL https://www.instagram.com/guviofficial/ kindly do the following mentioned tasks:-
1.	Use either Relative or Absolute XPATH only for the task.
2.	Extract the total number of followers and following from the URL mentioned above
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Class data to manipulate and handle data
class Data:

    # Defining the target URL and login credentials for Instagram

    # GUVI Profile URL
    url = "https://www.instagram.com/guviofficial/"  

    # Login URL for Instagram

    login_url = "https://www.instagram.com/accounts/login/"  

    # Replace with your username
    username = "abc@abc.com"  

    # Replace with your password
    password = "Abc@xyz1"  
    
# Class AutomaneGuviInstagram to GUVI Instagram page
class AutomateGuviInstagram:

    def __init__(self):
    
        # Initialize the Chrome driver using ChromeDriverManager
        self.driver = webdriver.Chrome()

    # Method to start the autmoation
    def start_automation(self):

        # Open the Instagram login page
        self.driver.get(Data().login_url)

        # Maximize the browser window
        self.driver.maximize_window()

        # Wait for the page to load
        sleep(3)

        # Call the login method
        self.login()  

        #  Wait for the login process to complete
        sleep(3)  

        # Navigate to the target profile
        self.driver.get(Data().url)  

        # Wait for the profile page to load
        sleep(5)  

    # Method for login
    def login(self):

        # Locate the username field and enter the username
        username_field = self.driver.find_element(by=By.NAME, value="username").send_keys(Data().username)
        
        # Locate the password field and enter the password
        password_field = self.driver.find_element(by=By.NAME, value="password").send_keys(Data().password)
        
        # Locate and click the login button to submit the form
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        
        # Confirmation message for successful Log in
        print("Logged in successfully.")  

        # Wait for the login process to complete
        sleep(3)  

    # Method to fetch the followers
    def fetch_followers_data(self):

        # Locate the followers count on the profile page
        followers_data = self.driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]/span')

        # Print the followers count
        print("GUVI Followers are:", followers_data.text)

        # Return the followers data
        return followers_data  

    # Method to fetch following data
    def fetch_following_data(self):

        # Locate the following count on the profile page
        following_data = self.driver.find_element(By.XPATH, '//a[contains(@href, "/following/")]/span')

        # Print the following count
        print("GUVI Followings are :", following_data.text)

        # Return the following data
        return following_data  

    # Method for closing browser and end the session
    def shutdown(self):

        # Close the browser and end the session
        self.driver.quit()

# GUVI_Instagram object to automation class and execute the methods
Guvi_Instagram = AutomateGuviInstagram()

# Start the automation process
Guvi_Instagram.start_automation()

# Fetch and print followers data
Guvi_Instagram.fetch_followers_data()  

# Fetch and print following data
Guvi_Instagram.fetch_following_data() 

# Close the browser
Guvi_Instagram.shutdown()  