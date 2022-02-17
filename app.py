from selenium import webdriver
from selenium.common.exceptions import *
import datetime
import logging
import time
import sys

import gmailcreds

# create logger
log = logging.getLogger(__file__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)d   %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

email = sys.argv[1]
dayofweek = sys.argv[2].lower()
refresh = 1
if len(sys.argv) > 3:
    refresh = sys.argv[3]
url = "https://reservation.frontdesksuite.ca/rcfs/richcraftkanata/Home/Index?Culture=en&PageId=b3b9b36f-8401-466d-b4c4-19eb5547b43a&ButtonId=00000000-0000-0000-0000-000000000000"

# setup email functionality
import smtplib, ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = gmailcreds.user
sender_password = gmailcreds.password
receiver_email = email
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
# to test email
#with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#    server.login(sender_email, sender_password)
#    server.sendmail(sender_email, receiver_email, message)

log.debug("trying {}".format(url))
driver = webdriver.Chrome('./chromedriverv98.exe')
driver.get(url)
log.debug(driver.title)

# find basketball
basketball = driver.find_elements_by_xpath('//div[contains(text(), "Basketball")]')
driver.execute_script("arguments[0].click();", basketball[0]) # perform JS click

# wait for the page to load
time.sleep(1)

while True:
    available = False
    log.debug("looking for a date with no warning")
    dates = driver.find_elements_by_class_name('date-text')
    for d in dates:
        if dayofweek != "any":
            # match day of week
            day = d.find_elements_by_xpath('//span[contains(text(), "' + dayofweek.capitalize() + '")]')
            if len(day) == 0:
                continue;
        warn = []
        warn = d.find_elements_by_xpath('//div[contains(@class, "warning")]')
        if len(warn) == 0:
            available = True
            break

    if available:
        # send an email
        log.debug("found a time with open slot(s)")
        message = "Subject: basketball opening on " + dayofweek + "\nThis message is sent from pyton."
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
        email_sent = True
    else:
        log.debug("no slots found - waiting to refresh...")
    driver.refresh()
    time.sleep(int(refresh))
