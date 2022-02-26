import sys
sys.path.append('/app')

from flask import Flask
from flask import render_template
import scraping_scripts.web_sraping_script as web_scraper
import resources.constants as constants

flask_app = Flask(__name__, template_folder='../web')

main_page = "<br><a href=\"/\">Comeback to main page</a>"

@flask_app.route('/')
def home():
    return render_template('index.html')

@flask_app.route('/first_filter')
def firstFilter():
    return web_scraper.first_filter(constants.URL) + main_page

@flask_app.route('/second_filter')
def secondFilter():
    return web_scraper.second_filter(constants.URL) + main_page

if __name__ == '__main__':
    flask_app.run(debug=False)