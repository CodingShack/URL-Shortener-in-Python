import pyshorteners

URL = "Paste your link here"

short_URL = pyshorteners.Shortener()
result = short_URL.tinyurl.short(URL)
print("Shortened URL: " + result)
