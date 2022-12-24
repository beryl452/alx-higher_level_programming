#!/usr/bin/python3

"""
    Module containing a script that sends a POST request to a given URL with an email
    as a parameter and displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.parse

def main():
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email})
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)

if __name__ == "__main__":
    main()

