
#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: XSS Vulnerability Scanner 
# Date:        10.25.21
# Modified by: Ben Podawiltz

### Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
### Function that gets all content from html forms from a url #
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
### Creates an empty array to load details and attributes from html forms parsed into {actions, methods, and inputs} ###
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
### This function inputs details from previous function to submit or 'POST' to target_url or 'GET' determined by the method identified in form_details ###
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
### This function takes all the html content gather from the intial function and inputs javascript to test for vulnerability. Then prints detected vulnerability to STDOUT ###
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>THISISNOTADRILL('Vulnerability Detected!!')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### In your own words, describe the purpose of this main as it relates to the overall objectives of the script ###
### User inputs URL for testing vulnerability scanner and the results are printed to the screen ###
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### DONE: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### DONE: Test this script against one XSS-positive target and one XSS-negative target
### DONE: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection
# Cool resource: https://pentest-tools.com/website-vulnerability-scanning/xss-scanner-online

### Positive detection: 
# Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
# [+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
# [+] XSS Detected on https://xss-game.appspot.com/level1/frame
# [*] Form details:
# {'action': '',
# 'inputs': [{'name': 'query',
#            'type': 'text',
#             'value': "<Script>THISISNOTADRILL('Vulnerability "
#                      "Detected!!')</script>"},
#            {'name': None, 'type': 'submit'}],
# 'method': 'get'}
#True

### Negative Detection:
# dojo@dojo-VirtualBox:~/Desktop/class-37$ python3 challenge.py 
# Enter a URL to test for XSS:http://scanme.nmap.org/
# [+] Detected 1 forms on http://scanme.nmap.org/.
# False

# End