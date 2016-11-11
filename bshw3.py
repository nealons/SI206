# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re 

f_out = open('output.html', 'w')
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")


text_word_soup = soup.prettify()

y = text_word_soup.replace('logo2.png', 'media/logo.png')
x = y.replace("https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg", 'media/picture2.png')
text_word_soup2 = re.sub("student", "AMAZING student", x)

f_out.write(x)
f_out.close()

