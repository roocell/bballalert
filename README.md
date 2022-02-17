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
app.py <email> <dayofweek> <refresh>
where
  email - email to notify
  dayofweek - if you want an alert for a specific day (use 'any' to search all future days)
  refresh   - time to wait before checking again

example) check for friday opening, 10 minute refresh
app.py bob@hotmail.com friday 600

example) check for any opening, 1 minute refresh
app.py bob@hotmail.com any 60
