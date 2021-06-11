from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 

def scrape_all_pages():
    # Set up Splinter
    # ADD IN THE OTHER CRAP HERE #
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # ADD IN THE OTHER CRAP HERE #
    news_title, news_paragraph = scrape_mars_news(browser)
    featured_image_url2 = scrape_mars_img(browser)
    mars_facts = scrape_mars_facts(browser)
    mars_hemi_image_urls = scrape_mars_hemi(browser)

    # ADD IN THE OTHER CRAP HERE #
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image_url2,
        "mars_facts" : mars_facts,
        "mars_hemi_image_urls" : mars_hemi_image_urls
    }

    browser.quit()
    return mars_data

################################################################## SCRAPE ######################################################################################

########################## MARS NEWS SECTION #############################################################
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
    news_paragraph = mars_news_soup.find('div' , class_='article_teaser_body').text

    # Return results
    return news_title, news_paragraph


######################### MARS CURRENT IMG SECTION #############################################################
def scrape_mars_img(browser):
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_img_url = "https://spaceimages-mars.com"
    browser.visit(mars_img_url)

    time.sleep(1)

    # Scrape page into Soup
    mars_img_html = browser.html
    mars_img_soup = bs(mars_img_html, 'html.parser')

    # Get the latest featured image
    thread = mars_img_soup.find('img' , class_='headerimage fade-in')
    featured_image_url = thread['src']
    featured_image_url2 = f'{mars_img_url}/{featured_image_url}'

    # Return results
    return featured_image_url2


################################ MARS FACTS SECTION ############################################################
def scrape_mars_facts(browser):
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_facts_url = "https://galaxyfacts-mars.com"
    tables = pd.read_html(mars_facts_url)

    time.sleep(1)

    # HERE IS YOUR CODE, DUMMY
    mars_df = tables[0]
    mars_df.columns = ["Mars-Earth Comparison", "Mars", "Earth"]
    mars_df = mars_df.iloc[1:]
    mars_df.set_index("Mars-Earth Comparison" , inplace=True)
    mars_facts = mars_df.to_html().replace('\n','')
    mars_facts 

    # Return results
    return mars_facts


################################ MARS HEMI IMAGES(4) SECTION ############################################################
def scrape_mars_hemi(browser):
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_hemi_url = 'https://marshemispheres.com'
    browser.visit(mars_hemi_url)

    time.sleep(1)

    # Scrape page into Soup
    mars_hemi_html = browser.html
    mars_hemi_soup = bs(mars_hemi_html, 'html.parser')

    # STEP ONE
    finder = mars_hemi_soup.find_all('div', class_='item')
    mars_hemi_url_list = []
    for x in finder:
        url = x.find('a')['href']
        mars_hemi_url_list.append(f'https://marshemispheres.com/{url}')
    mars_hemi_url_list

    # STEP TWO
    mars_hemi_image_urls=[]


    for x in mars_hemi_url_list:
        new_blank_dict={}
        browser.visit(x)
        mars_hemi2_html = browser.html
        mars_hemi2_soup = bs(mars_hemi2_html, 'html.parser')
        new_blank_dict["title"] =  mars_hemi2_soup.find('h2', class_='title').text.rsplit(' ' , 1)[0] 
        img_url1 = mars_hemi2_soup.find('img', class_='wide-image')['src']
        new_blank_dict['img_url'] = (f'https://marshemispheres.com/{img_url1}')
        mars_hemi_image_urls.append( new_blank_dict)
    mars_hemi_image_urls

    # Return results
    return mars_hemi_image_urls