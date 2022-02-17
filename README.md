# bballalert
send email alerts when spots become available

1. download python (should include pip3)
https://www.python.org/

2. download chrome
https://www.google.ca/google_chrome/install

3. download chromedriver (used with selenium)
copy into this folder - rename chromedriver.exe
https://chromedriver.chromium.org/downloads

4. uses a gmail account with an app-specific generated password (gmailcreds.py)
generate app-specific password for a gmail account and use that

usage:
app.py <email to notify> <day of week to check> <delay for page refresh in seconds>
example) check for friday opening, 10 minute refresh
app.py bob@hotmail.com friday 600

example) check for any opening, 1 minute refresh
app.py bob@hotmail.com any 60
