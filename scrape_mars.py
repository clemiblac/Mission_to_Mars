#!/usr/bin/env python
# coding: utf-8

# In[ ]:
def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"} # WINDOWS USERS!
    return Browser("chrome", **executable_path, headless=False)




# # NASA Mars News

# In[11]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser


# In[2]:


# URL of page to be scraped
url='https://mars.nasa.gov/news/'


# In[3]:


# Retrieve page with the requests module
response = requests.get(url)


# In[4]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[5]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[ ]:





# In[6]:


#Latest news title
news_title=soup.body.find('div',class_="content_title").text
news_title=news_title.strip('\n\n')
news_title


# In[7]:


#Paragraph text for latest news title
news_p=soup.body.find('div',class_="rollover_description_inner").text
news_p=news_p.strip('\n')
news_p


# In[ ]:


news=dict({'title':news_title,'text':news_p})


# In[20]:


def news_function():
    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    url='https://mars.nasa.gov/news/'
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_title=soup.body.find('div',class_="content_title").text
    news_title=news_title.strip('\n\n')
    news_p=soup.body.find('div',class_="rollover_description_inner").text
    news_p=news_p.strip('\n')
    news=dict({'title':news_title,'text':news_p})
    return news 


# In[22]:


news_function()


# ## JPL Mars Space Images - Featured Image

# In[34]:


#Setting up splinter for image scraping
from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[35]:


#Find featured Image url
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[36]:


#Find and click for featured image in gallery
gallery_button=browser.links.find_by_partial_text('FULL IMAGE')
gallery_button.click()


# In[37]:


browser.url


# In[38]:


# Find and click the image thumbnail
more_info=browser.links.find_by_partial_text('more info').first
more_info.click()


# In[39]:


url=browser.url


# In[40]:


from bs4 import BeautifulSoup
import requests


# In[41]:


image_response = requests.get(url)


# In[42]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(image_response.text, 'html.parser')


# In[43]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[44]:


image=soup.body.find('figure').a
image


# In[45]:


featured_image_url=image['href']
featured_image_url


# In[46]:


def featured_image_function():
    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    gallery_button=browser.links.find_by_partial_text('FULL IMAGE')
    gallery_button.click()
    browser.url
    more_info=browser.links.find_by_partial_text('more info').first
    more_info.click()
    url=browser.url
    from bs4 import BeautifulSoup
    import requests
    image_response = requests.get(url)
    soup = BeautifulSoup(image_response.text, 'html.parser')
    image=soup.body.find('figure').a
    featured_image_url=image['href']
    return featured_image_url
    
    


# In[47]:


featured_image_function()


# ## Mars Weather

# In[62]:


from bs4 import BeautifulSoup
import requests


# In[63]:


url='https://twitter.com/marswxreport?lang=en'


# In[64]:


#data = requests.get(url)


# In[66]:


#soup = BeautifulSoup(data.text, 'html.parser')


# In[67]:


#print(soup.prettify())


# In[ ]:


#mars_weather = soup.find("p", "tweet-text").get_text()


# In[ ]:





# In[ ]:


#mars_weather


# # Mars Facts

# In[ ]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[ ]:


url="https://space-facts.com/mars/"


# In[ ]:


facts = requests.get(url)


# In[ ]:


soup = BeautifulSoup(facts.content, 'lxml')


# In[ ]:


table = soup.find_all('table')[0] 
df = pd.read_html(str(table))
mars_facts=df[0].to_json(orient='records')
mars_facts


# In[48]:


def mars_facts_function():
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    url="https://space-facts.com/mars/"
    facts = requests.get(url)
    soup = BeautifulSoup(facts.content, 'lxml')
    table = soup.find_all('table')[0] 
    df = pd.read_html(str(table))
    mars_facts=df[0].to_json(orient='records')
    return mars_facts
    


# In[49]:


mars_facts_function()


# # Mars Hemisphere

# ### Ceberus

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

hemisphere=requests.get(url)

soup = BeautifulSoup(hemisphere.text, 'html.parser')


# In[3]:


print(soup.prettify())


# In[4]:


#Setting up splinter for image scraping
from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[5]:


browser.visit(url)


# In[6]:


#Find and click for featured image in gallery
c_button=browser.links.find_by_partial_text('Cerberus')
c_button.click()


# In[7]:


cerberus=browser.url
print(cerberus)


# In[8]:


response=requests.get(cerberus)
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())


# In[9]:


c_title=soup.body.find('h2',class_='title').text
c_title


# In[10]:


cerberus_img=soup.body.find('li').a['href']
cerberus_img


# In[12]:


cerberus=dict({"title":c_title,"img_url":cerberus_img})
cerberus


# In[50]:


def ceberus_function():
    from bs4 import BeautifulSoup
    import requests
    url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemisphere=requests.get(url)
    soup = BeautifulSoup(hemisphere.text, 'html.parser')
    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
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


# In[51]:


ceberus_function()


# ### Schiaparelli

# In[14]:


url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

hemisphere=requests.get(url)

soup = BeautifulSoup(hemisphere.text, 'html.parser')

browser.visit(url)


# In[15]:


s_button=browser.links.find_by_partial_text('Schiaparelli')
s_button.click()

Schiaparelli=browser.url
print(Schiaparelli)

response2=requests.get(Schiaparelli)
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response2.text, 'html.parser')


# In[16]:


s_title=soup.body.find('h2',class_='title').text
print(s_title)
Schiaparelli_img=soup.body.find('li').a['href']
print(Schiaparelli_img)


# In[17]:


Schiaparelli=dict({"title":s_title,"img_url":Schiaparelli_img})


# In[52]:


def schi_function():
    from bs4 import BeautifulSoup
    import requests
    url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemisphere=requests.get(url)
    soup = BeautifulSoup(hemisphere.text, 'html.parser')
    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
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

    


# In[53]:


schi_function()


# ### Syrtis

# In[18]:


#Go back to main page
url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

hemisphere=requests.get(url)

soup = BeautifulSoup(hemisphere.text, 'html.parser')

browser.visit(url)


# In[19]:


sy_button=browser.links.find_by_partial_text('Syrtis')
sy_button.click()

Syrtis=browser.url
print(Syrtis)

response3=requests.get(Syrtis)
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response3.text, 'html.parser')


# In[20]:


sy_title=soup.body.find('h2',class_='title').text
print(sy_title)
Syrtis_img=soup.body.find('li').a['href']
print(Syrtis_img)


# In[21]:


Syrtis=dict({"title":sy_title,"img_url":Syrtis_img})


# In[54]:


def syrtis_function():
    from bs4 import BeautifulSoup
    import requests
    url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemisphere=requests.get(url)
    soup = BeautifulSoup(hemisphere.text, 'html.parser')
    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
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


# In[55]:


syrtis_function()


# ### Valles

# In[22]:


#Go back to main page
url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

hemisphere=requests.get(url)

soup = BeautifulSoup(hemisphere.text, 'html.parser')

browser.visit(url)


# In[24]:


v_button=browser.links.find_by_partial_text('Valles')
v_button.click()

Valles=browser.url
print(Valles)

response4=requests.get(Valles)
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response4.text, 'html.parser')


# In[25]:


v_title=soup.body.find('h2',class_='title').text
print(v_title)
Valles_img=soup.body.find('li').a['href']
print(Valles_img)


# In[26]:


Valles=dict({"title":v_title,"img_url":Valles_img})


# In[56]:


def valles_function():
    from bs4 import BeautifulSoup
    import requests
    url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemisphere=requests.get(url)
    soup = BeautifulSoup(hemisphere.text, 'html.parser')
    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
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


# In[57]:


valles_function()


# #### Append dictionaries to list

# In[27]:


hemisphere_img_urls=[]


# In[28]:


hemisphere_img_urls=[cerberus,Schiaparelli,Syrtis,Valles]


# In[29]:


hemisphere_img_urls


# In[60]:


def hemispheres():
    hemisphere_img_urls=[]
    hemisphere_img_urls=[ceberus_function,schi_function,syrtis_function,valles_function]
    results = [f() for f in hemisphere_img_urls]
    return results


# In[61]:


hemispheres()


# In[ ]:

def scrape():
    mars_info = {}
    mars_info["news"]=news_function()
    mars_info["featured_image"]=featured_image_function()
    mars_info["facts"]=mars_facts_function()
    mars_info["hemispheres"]=hemispheres()
    return mars_info


