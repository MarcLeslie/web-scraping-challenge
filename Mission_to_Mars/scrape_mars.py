from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all_pages():
    # Set up Splinter
    # ADD IN THE OTHER CRAP HERE #
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # ADD IN THE OTHER CRAP HERE #
    news_title, p_text = scrape_mars_news(browser)

    # ADD IN THE OTHER CRAP HERE #
    mars_data = {
        "news_title": news_title,
        "news_paragraph": p_text
    }

    browser.quit()
    return mars_data

#################### SCRAPE ###############################

# MARS NEWS SECTION #
def scrape_mars_news(browser):
    
    mars_news_url = "https://redplanetscience.com"
    browser.visit(mars_news_url)

    time.sleep(1)

    # Scrape page into Soup
    mars_news_html = browser.html
    mars_news_soup = bs(mars_news_html, 'html.parser')

    # Get the latest news title
    news_title = mars_news_soup.find('div' , class_='content_title').text

    # Get the latest news paragraph
    p_text = mars_news_soup.find('div' , class_='article_teaser_body').text

    # # Store data in a dictionary
    # mars_data = {
    #     "news_title": news_title,
    #     "news_paragraph": p_text
    # }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return news_title, p_text


###  DO THE NEXT SECTION HERE ######