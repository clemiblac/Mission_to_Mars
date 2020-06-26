
# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser

def scrape_info():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)


    def news_function():
        url='https://mars.nasa.gov/news/'
        browser.visit(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        news_title=soup.body.find('div',class_="content_title").text
        news_title=news_title.strip('\n\n')
        news_p=soup.body.find('div',class_="rollover_description_inner").text
        news_p=news_p.strip('\n')
        news={'title':news_title,'text':news_p}
        return news 

    
    # ## JPL Mars Space Images - Featured Image
    def featured_image_function():
        url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url)
        gallery_button=browser.links.find_by_partial_text('FULL IMAGE')
        gallery_button.click()
        browser.url
        more_info=browser.links.find_by_partial_text('more info').first
        more_info.click()
        url=browser.url
        image_response = requests.get(url)
        soup = BeautifulSoup(image_response.text, 'html.parser')
        image=soup.body.find('figure').a
        featured_image_url='https://www.jpl.nasa.gov'+image['href']
        return featured_image_url
    
        

   
    # ## Mars Weather
    #def mars_weather_function():

        #url='https://twitter.com/marswxreport?lang=en'

        #data = requests.get(url)
        #soup = BeautifulSoup(data.text, 'html.parser')
        #mars_weather = soup.find("p", "tweet-text").get_text()
        #mars_weather

    
    # # Mars Facts
    def mars_facts_function():
        import pandas as pd
        url="https://space-facts.com/mars/"
        browser.visit(url)
        facts = requests.get(url)
        soup = BeautifulSoup(facts.content, 'html')
        table = soup.find_all('table')[0] 
        df = pd.read_html(str(table))
        mars_facts=df[0]
        mars_facts=df[0].to_json(orient='records')
        return mars_facts
        
    """

    # # Mars Hemisphere

    # ### Cerberus
    def cerberus_function():
        
        url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        
        hemisphere=requests.get(url)
        soup = BeautifulSoup(hemisphere.text, 'html.parser')
        browser.visit(url)
        c_button=browser.links.find_by_partial_text('Cerberus')
        c_button.click()
        cerberus=browser.url
        response=requests.get(cerberus)
        soup = BeautifulSoup(response.text, 'html.parser')
        c_title=soup.body.find('h2',class_='title').text
        cerberus_img=soup.body.find('li').a['href']
        cerberus=dict({"title":c_title,"img_url":cerberus_img})
        return cerberus



    def schi_function():
        
        url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        hemisphere=requests.get(url)
        soup = BeautifulSoup(hemisphere.text, 'html.parser')
        
        browser.visit(url)
        s_button=browser.links.find_by_partial_text('Schiaparelli')
        s_button.click()
        Schiaparelli=browser.url
        response2=requests.get(Schiaparelli)
        soup = BeautifulSoup(response2.text, 'html.parser')
        s_title=soup.body.find('h2',class_='title').text
        Schiaparelli_img=soup.body.find('li').a['href']
        Schiaparelli=dict({"title":s_title,"img_url":Schiaparelli_img})
        return Schiaparelli

        

    def syrtis_function():
        from bs4 import BeautifulSoup
        import requests
        from splinter import Browser
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)
        
        url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        hemisphere=requests.get(url)
        soup = BeautifulSoup(hemisphere.text, 'html.parser')
        
        browser.visit(url)
        sy_button=browser.links.find_by_partial_text('Syrtis')
        sy_button.click()
        Syrtis=browser.url
        response3=requests.get(Syrtis)
        soup = BeautifulSoup(response3.text, 'html.parser')
        sy_title=soup.body.find('h2',class_='title').text
        Syrtis_img=soup.body.find('li').a['href']
        Syrtis=dict({"title":sy_title,"img_url":Syrtis_img})
        return Syrtis


    def valles_function():
        
        url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        hemisphere=requests.get(url)
        soup = BeautifulSoup(hemisphere.text, 'html.parser')

        
        browser.visit(url)
        v_button=browser.links.find_by_partial_text('Valles')
        v_button.click()
        Valles=browser.url
        response4=requests.get(Valles)
        soup = BeautifulSoup(response4.text, 'html.parser')
        v_title=soup.body.find('h2',class_='title').text
        Valles_img=soup.body.find('li').a['href']
        Valles=dict({"title":v_title,"img_url":Valles_img})
        return Valles


    # #### Append dictionaries to list
    def hemispheres():
        hemisphere_img_urls=[]
        hemisphere_img_urls=[cerberus_function(),schi_function(),syrtis_function(),valles_function()]
        return hemisphere_img_urls
        """

    mars_info = {
    'news':news_function(),
    'featured_image':featured_image_function(),
    #'mars_weather':mars_weather_function()
    'mars_facts':mars_facts_function()
    #,
    #'hemispheres':hemispheres()
    }
    return mars_info


if __name__ == "__main__":
    print(scrape_info())





