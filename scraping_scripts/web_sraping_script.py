import sys
sys.path.append('/app')

import time
import itertools
import scraping_scripts.models.entry as entry
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Fetch all the information needed from the website
# URL -> Url of the website 
def scrape_site(URL):
    criteria = webdriver.ChromeOptions()
    criteria.headless = True
    criteria.add_argument("window_size=1920x1080")
    criteria.add_argument('--no-sandbox')
    criteria.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=criteria)
    driver.get(URL)

    time.sleep(5)

    titles = driver.find_elements_by_class_name('titlelink')
    ranks = driver.find_elements_by_class_name('rank')
    scores = driver.find_elements_by_class_name('score')
    comments = driver.find_elements_by_partial_link_text('comments')

    # delete first comments link appearance
    del comments[0]

    entry_array = []

    for (title, rank, comment, score) in itertools.zip_longest(titles, ranks, comments, scores):
        if title is not None and rank is not None and comment is not None and score is not None: 
            entry_element = entry.entry(title.text, rank.text, comment.text, score.text)
            entry_array.append(entry_element)

    driver.close()

    return entry_array

def order_by_comments(list_entries):
    hashmap_comments = {}
    for entry in list_entries:
        comment = entry.comment.split()
        number_comments = int(comment[0])
        hashmap_comments[number_comments] = entry
        
    return sorted(hashmap_comments.items())

def order_by_points(list_entries):
    hashmap_score = {}
    for entry in list_entries:
        score = entry.score.split()
        number_score = int(score[0])
        hashmap_score[number_score] = entry
    return sorted(hashmap_score.items())

def print_web(list_entries):
    final_web = ""
    for key, entry in list_entries:
        final_web += entry.print_entry() + "<br>"

    return final_web

def first_filter(URL):
    list_entries = scrape_site(URL)
    filter_entries = filter(lambda c: len(c.title.split()) > 5, list_entries)
    sorted_entries = order_by_comments(filter_entries)
    return print_web(sorted_entries)

    
def second_filter(URL):
    list_entries = scrape_site(URL)
    filter_entries = filter(lambda c: len(c.title.split()) <= 5, list_entries)
    sorted_entries = order_by_points(filter_entries)
    return print_web(sorted_entries)

