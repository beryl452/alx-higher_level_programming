#!/usr/bin/python3
"""
    Fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
def get_status():
    """
        fetches https://alx-intranet.hbtn.io/status
    """
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        html_utf8 = html.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html_utf8))

if __name__ == "__main__":
    get_status()
