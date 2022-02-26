import sys
sys.path.append('/app')

import time
import numpy as np
import itertools
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import scraping_scripts.models.entry as entry


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

    #delete first comments link appearance
    del comments[0]

    final_web = ""


    for (title, rank, comment, score) in itertools.zip_longest(titles, ranks, scores, comments):
        if title is not None and rank is not None and comment is not None and score is not None: 
            final_web += rank.text + " | " + title.text + " | " + score.text + " | " + comment.text + "<br>"

    driver.close()

    return final_web


