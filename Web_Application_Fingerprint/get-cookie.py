#!/usr/bin/env python3

# script name:  Web Application Fingerprinting tool pary 1 of 3
# author:       ben_podawiltz
# revision:     10.18.21
#
######################################
# Libraries
import os
import requests
from requests.cookies import get_cookie_header
import webbrowser
####################################### T
# The below Python script shows one possible method to return the cookie from a site that supports cookies.
# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

    for cookie in response.cookies:
       print('cookie domain = ' + cookie.domain)
       print('cookie name = ' + cookie.name)
       print('cookie value = ' + cookie.value)
       print('*************************************')

#def send_cookie():

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:
# > Send the cookie back to the site and receive a HTTP response
# > Generate a .html file to capture the contents of the HTTP response
# > Open it with Firefox
#
# Stretch Goal
# - Give Cookie Monster hands

send = requests.get(targetsite, cookies=cookie)
# "Python requests are generally used to fetch the content from a particular resource URI" This returns a response object and saves to a variable
print("_" * 8 + "URL CODE" + "_" * 8)
print(response.url)
print("")
print("_" * 8 + "Status CODE" + "_" * 8)
print(response.status_code)
print("")

with open("/home/kali/Desktop/get_cookie.html", "wb") as file:
  file.write(send.content)
# Full path passed to open and write contents of HTTP response object

webbrowser.open_new_tab("/home/kali/Desktop/get_cookie.html")
# Display url in new tab using the default browser

###############################################
#
# Resource: https://zetcode.com/python/requests/
#           https://www.geeksforgeeks.org/response-content-python-requests/

# End