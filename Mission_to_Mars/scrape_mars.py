from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_mars_news():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    mars_news_browser = Browser('chrome', **executable_path, headless=False)

    # Visit visitcostarica.herokuapp.com
    mars_news_url = "https://redplanetscience.com"
    mars_news_browser.visit(mars_news_url)

    time.sleep(1)

    # Scrape page into Soup
    mars_news_html = mars_news_browser.html
    mars_news_soup = bs(mars_news_html, 'html.parser')

    # Get the latest news title
    news_title = mars_news_soup.find('div' , class_='content_title').text

    # Get the latest news paragraph
    p_text = mars_news_soup.find('div' , class_='article_teaser_body').text

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_paragraph": p_text
    }

    # Close the browser after scraping
    mars_news_browser.quit()

    # Return results
    return mars_data
