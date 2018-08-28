import time
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

R_Day = "00"
R_S_Time = "0:00 PM"
R_E_Time = "0:00 PM"
R_ReservationDescription = "Autoweb"

R_Sleep = 0

time.sleep(R_Sleep)




#Don't change this delay
delay = 3

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option(name="useAutomationExtension", value=False)

driver = webdriver.Chrome(
    executable_path="C:\\bin\\chromedriver.exe",
    chrome_options=chrome_options)

# driver = webdriver.Ie(
#     executable_path="C:\\bin\\IEDriverServer.exe")

#browser.get("http://www.google.com")
#driver.implicitlyWait(10)
driver.get("http://fontanamarkhamresidents.buildinglink.com/V2/Tenant/Home/DefaultNew.aspx")

elemUserName = driver.find_element_by_id("ctl00_Login1_UserName")
elemPassword = driver.find_element_by_id("ctl00_Login1_Password")
elemLoginButton = driver.find_element_by_id("LoginButton")

elemUserName.send_keys("xxxxxxxxxx")
elemPassword.send_keys("yyyyyyyyyy")

elemLoginButton.click()

while True:
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, "ctl00_body"))
        )
        print("Page is ready!")
        break # it will break from the loop once the specific element will be present.
    except TimeoutException:
        print("Loading took too much time!-Try again")


driver.get("http://fontanamarkhamresidents.buildinglink.com/V2/Tenant/Amenities/CalendarView.aspx")

while True:
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, "ctl00_body"))
        )
        print("Page is ready!")
        break # it will break from the loop once the specific element will be present.
    except TimeoutException:
        print("Loading took too much time!-Try again")

elemNewReservatrion = driver.find_element_by_id("ctl00_ContentPlaceHolder1_NewReservatrionButton")
elemNewReservatrion.click()

while True:
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, "ctl00_body"))
        )
        print("Page is ready!")
        break # it will break from the loop once the specific element will be present.
    except TimeoutException:
        print("Loading took too much time!-Try again")

elemAmenitiesContainer = driver.find_element_by_id("amenitiesContainer")

driver.execute_script("javascript:__doPostBack('ctl00$ContentPlaceHolder1$AmenitiesDataList$ctl04$SelectAmenityLink','');", elemAmenitiesContainer)

while True:
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_StartDatePicker"))
        )
        print("Page is ready!")
        break # it will break from the loop once the specific element will be present.
    except TimeoutException:
        print("Loading took too much time!-Try again")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(2)

elemDateWidget = driver.find_element_by_id("ctl00_ContentPlaceHolder1_StartDatePicker")
elemDateWidgetRows = elemDateWidget.find_elements(By.TAG_NAME, "tr")

try:
    isFound = False
    for row in elemDateWidgetRows:
        elemColumns = row.find_elements(By.TAG_NAME, "td")
        for col in elemColumns:
            if col.text == R_Day:
                col.click()
                time.sleep(3)
                break
        if isFound:
            break
except StaleElementReferenceException:
    pass

time.sleep(2)

elemStartTimePicker = driver.find_element_by_id("ctl00_ContentPlaceHolder1_StartTimePicker_dateInput")
elemStartTimePicker.click()

while True:
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_StartTimePicker_timeView_tdl"))
        )
        print("Page is ready!")
        break # it will break from the loop once the specific element will be present.
    except TimeoutException:
        print("Loading took too much time!-Try again")

time.sleep(2)

elemDateStartTimePicker = driver.find_element_by_id("ctl00_ContentPlaceHolder1_StartTimePicker_timeView_tdl")
elemDateStartTimePickerRows = elemDateStartTimePicker.find_elements(By.TAG_NAME, "tr")

try:
    isFound = False
    for row_S in elemDateStartTimePickerRows:
        elemColumns_S = row_S.find_elements(By.TAG_NAME, "td")
        for col_S in elemColumns_S:
            if col_S.text == R_S_Time:
                col_S.click()
                isFound = True
                time.sleep(3)
                break
        if isFound:
            break
except StaleElementReferenceException:
    pass


while True:
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_EndTimePicker_dateInput"))
        )
        print("Page is ready!")
        break # it will break from the loop once the specific element will be present.
    except TimeoutException:
        print("Loading took too much time!-Try again")

elemEndTimePicker = driver.find_element_by_id("ctl00_ContentPlaceHolder1_EndTimePicker_dateInput")
elemEndTimePicker.click()

time.sleep(2)

while True:
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_EndTimePicker_timeView_tdl"))
        )
        print("Page is ready!")
        break # it will break from the loop once the specific element will be present.
    except TimeoutException:
        print("Loading took too much time!-Try again")

elemDateEndTimePicker = driver.find_element_by_id("ctl00_ContentPlaceHolder1_EndTimePicker_timeView_tdl")
elemDDateEndTimePickerRows = elemDateEndTimePicker.find_elements(By.TAG_NAME, "tr")

try:
    isFound = False
    for row in elemDDateEndTimePickerRows:
        elemColumns = row.find_elements(By.TAG_NAME, "td")
        for col in elemColumns:
            if col.text == R_E_Time:
                col.click()
                time.sleep(3)
                isFound = True
                break
            if isFound:
                break
except StaleElementReferenceException:
    pass

elemReservationDescription = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ReservationDescription")
elemReservationDescription.send_keys(R_ReservationDescription)

elemWaiverAgreeCheckbox = driver.find_element_by_id("ctl00_ContentPlaceHolder1_liabilityWaiverAgreeCheckbox")
elemWaiverAgreeCheckbox.click()

time.sleep(3)

elemFooterSaveButton = driver.find_element_by_id("ctl00_ContentPlaceHolder1_FooterSaveButton")
elemFooterSaveButton.click()
