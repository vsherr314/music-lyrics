from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

# Get user input for the song to search for
search = input("Enter a song: ")
url = f'https://www.google.com/search?q={search}+lyrics'

# Open the page and get the lyrics
options = Options()
options.add_argument("--headless=new")  # for Chrome >= 109
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(1)
lyrics_div = driver.find_element(By.CLASS_NAME, "xaAUmb")
lyrics = lyrics_div.text
driver.quit()

# Reformat lyrics
lyrics = lyrics.lower().replace(',', '').replace("'", '').replace('"', '').replace('.', '').replace('?', '').replace(' ', '\n')

# Create a list with each word
word_list = lyrics.split('\n')

# Configure Jinja2 to load templates from the current directory
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("search.html")
rendered_content = template.render(word_list=word_list)
with open("word_list.html", "w", encoding="utf-8") as html_file:
    html_file.write(rendered_content)