# How to Create URL Shortener in Python?

![How to Create URL Shortener in Python?](https://blogger.googleusercontent.com/img/a/AVvXsEgzKQPZGCq-iWBIRwqskNta2oaKivuPF4IdiQehvzOi5NApgPjSA-Sjo9nh4kDNJvQDP3GhN0zIp5Km3ocljnw8aMw0KjmVa8OunHJLHFz3Sz3UA2VmPxYhajOKVnqH4tQW2baXdKO-dg4zKQtaicctHt1zpV_bjibpv5wnAphs_UIL0FzZ0w3iIZXN "How to Create URL Shortener in Python?")

Hello Readers! So, you would have seen short URLs being used in various places (social media, websites, messaging platforms, etc.). Short URLs are easy to remember or type so they are very popular. 

No one loves long URLs and so the need to shorten lengthy URLs often comes to us.

We can write a program in Python language for our needs. Then we can give a long URL as the input and get short URLs as output, too in very few lines of code. Is not it exciting? The use of various APIs does it very easily without having to dig into complex topics.

We're going to use a library named [PyShorteners](https://pypi.org/project/pyshorteners/), which i think is the best library to shorten your URLs in Python. Let's begin the journey.

## What is a URL Shortener?
A URL shortener is a simple tool that takes a long URL and turns it into a short url which can be easily, remembered by an individual.

## What is PyShorteners?
PyShorteners is a Python library to help you short urls, it is the most . You just have to install the lib and you're good to proceed.

You can install the lib using the command given below.

```python
pip install pyshortners
```

After installing the PyShortener library let's start the Implementation part.

## Implementation

Here we have to import the PyShorteners Library before using it, if you have used python before you should can relate to it, but those who don't know about what we are talking about let's know that first.

In the first line of our code we have to import the library which we installed before, in order to use it's features.

Import the PyShorteners library using the code given below.

```python
import pyshorteners
```

Once you have imported pyshorteners. Our next step is to create a variable named "URL" which is basically a variable, going to store our link which is going to be shortened. The link will be in double quotes as it is a string.

```python
URL = "Paste your link here"
```

Next we're going to create another variable named "short_URL" which will call pyshorteners library, to shorten the url.

```python
short_URL = pyshorteners.Shortener()
```

In this step we're going to do the main step, we are going to make a variable named "result" and then we are telling pyshorteners to shorten the link which is in a variable named "URL", which we created earlier. Here "tinyurl" in the code is the website which is going to shorten the URL.

```python
result = short_URL.tinyurl.short(URL)
```

We have almost completed all the steps, in this last step we are going to print the URL which is shortened.

```python
print("Shortened URL: " + result)
```

All complete here, is our final code.

```python
import pyshorteners # Imported Pyshorteners

URL = "Paste your link here" # Making a variable, whichj will store the link.

short_URL = pyshorteners.Shortener() # Calling the function to do the work.

result = short_URL.tinyurl.short(URL) # Telling the function the location of the link.

print("Shortened URL: " + result) # Printing the output.
```

Now, here is our output.

![Output - How to Create URL Shortener in Python?](https://1.bp.blogspot.com/-bCoM5wFgSEQ/YKk0O5-btTI/AAAAAAAABjU/0bXTFkq5WYUf3ZR9UfnyJqk5EZuDjgWBwCLcBGAsYHQ/s16000/Output.png "Output - How to Create URL Shortener in Python?")

Peace ✌️

----