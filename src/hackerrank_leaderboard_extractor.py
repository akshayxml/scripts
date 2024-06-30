from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from ctypes import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\SeleniumDrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
MAXPAGES = 100
outfile = 'leaderboard2.csv'
leaderboardEntries = []
MAXSCORE = 900
ok = windll.user32.BlockInput(True)

try:
    for i in range(1,MAXPAGES):
        driver.get("https://www.hackerrank.com/contests/2021-dsa-lab-2/leaderboard/"+str(i))
        leaderboard = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "leaders"))
        )

        entries = leaderboard.find_elements_by_class_name("leaderboard-list-view")

        if(len(entries) == 0):
            break

        for entry in entries:
            values = entry.text.split()
            name = values[1]
            score = values[2]
            time = values[3]
            leaderboardEntries.append([name, score, time, name[:10], round(10*(float(score)/MAXSCORE),2)])

        print("Page {} fetched.".format(i))

finally:
    with open(outfile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Username', 'Score', 'Time', 'Roll Number', 'Marks'])
        writer.writerows(leaderboardEntries)
    driver.quit()
