# This Code is Written in Python to Shorten a URL.
# Created on: 23rd August 2021
# Created by: Aman Chourasia (www.amanchourasia.in)
# Copyright 2021 Aman Chourasia (www.amanchourasia.in)


# The Code Starts here.

import pyshorteners # Imported Pyshorteners

URL = "Paste your link here" # Making a variable, whichj will store the link.

short_URL = pyshorteners.Shortener() # Calling the function to do the work.

result = short_URL.tinyurl.short(URL) # Telling the function the location of the link.

print("Shortened URL: " + result) # Printing the output.