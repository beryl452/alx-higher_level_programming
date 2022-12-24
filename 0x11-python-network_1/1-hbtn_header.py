#!/usr/bin/python3
"""
    Module containing a script that sends a request to a given URL and displays the
    value of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request

def main():
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header["X-Request-Id"])

if __name__ == "__main__":
    main()

