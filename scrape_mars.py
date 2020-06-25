#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # NASA Mars News

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


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


# In[8]:


news=dict({'title':news_title,'text':news_p})


# In[10]:


def news_function():
    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url='https://mars.nasa.gov/news/'
    browser.visit(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_title=soup.body.find('div',class_="content_title").text
    news_title=news_title.strip('\n\n')
    news_p=soup.body.find('div',class_="rollover_description_inner").text
    news_p=news_p.strip('\n')
    news=dict({'title':news_title,'text':news_p})
    return news 


# In[11]:


news_function()


# ## JPL Mars Space Images - Featured Image

# In[12]:


from bs4 import BeautifulSoup
import requests
from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[13]:


#Find featured Image url
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[14]:


#Find and click for featured image in gallery
gallery_button=browser.links.find_by_partial_text('FULL IMAGE')
gallery_button.click()


# In[15]:


browser.url


# In[16]:


# Find and click the image thumbnail
more_info=browser.links.find_by_partial_text('more info').first
more_info.click()


# In[17]:


url=browser.url


# In[18]:


image_response = requests.get(url)


# In[19]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(image_response.text, 'html.parser')


# In[20]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[21]:


image=soup.body.find('figure').a
image


# In[22]:


featured_image_url=image['href']
featured_image_url


# In[23]:


def featured_image_function():
    from bs4 import BeautifulSoup
    import requests
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
    image_response = requests.get(url)
    soup = BeautifulSoup(image_response.text, 'html.parser')
    image=soup.body.find('figure').a
    featured_image_url=image['href']
    return featured_image_url
    
    


# In[24]:


featured_image_function()


# ## Mars Weather

# In[ ]:


#from bs4 import BeautifulSoup
#import requests
#from splinter import Browser
#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


#url='https://twitter.com/marswxreport?lang=en'


# In[ ]:





# In[ ]:


#data = requests.get(url)


# In[ ]:


#soup = BeautifulSoup(data.text, 'html.parser')


# In[ ]:


#print(soup.prettify())


# In[ ]:


#mars_weather = soup.find("p", "tweet-text").get_text()


# In[ ]:





# In[ ]:


#mars_weather


# # Mars Facts

# In[25]:


from bs4 import BeautifulSoup
import requests
from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
import pandas as pd


# In[26]:


url="https://space-facts.com/mars/"
browser.visit(url)


# In[27]:


facts = requests.get(url)


# In[28]:


soup = BeautifulSoup(facts.content, 'lxml')


# In[29]:


table = soup.find_all('table')[0] 
df = pd.read_html(str(table))
mars_facts=df[0].to_json(orient='records')
mars_facts


# In[30]:


def mars_facts_function():
    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    import pandas as pd
    url="https://space-facts.com/mars/"
    browser.visit(url)
    facts = requests.get(url)
    soup = BeautifulSoup(facts.content, 'lxml')
    table = soup.find_all('table')[0] 
    df = pd.read_html(str(table))
    mars_facts=df[0].to_json(orient='records')
    return mars_facts
    


# In[31]:


mars_facts_function()


# # Mars Hemisphere

# ### Cerberus

# In[32]:


from bs4 import BeautifulSoup
import requests
from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[33]:


url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


# In[34]:


hemisphere=requests.get(url)

soup = BeautifulSoup(hemisphere.text, 'html.parser')


# In[35]:


print(soup.prettify())


# In[36]:


browser.visit(url)


# In[37]:


#Find and click for featured image in gallery
c_button=browser.links.find_by_partial_text('Cerberus')
c_button.click()


# In[38]:


cerberus=browser.url
print(cerberus)


# In[39]:


response=requests.get(cerberus)
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())


# In[40]:


c_title=soup.body.find('h2',class_='title').text
c_title


# In[41]:


cerberus_img=soup.body.find('li').a['href']
cerberus_img


# In[42]:


cerberus=dict({"title":c_title,"img_url":cerberus_img})
cerberus


# In[43]:


def cerberus_function():
    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
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


# In[44]:


cerberus_function()


# ### Schiaparelli

# In[45]:


from bs4 import BeautifulSoup
import requests
from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[46]:


url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

hemisphere=requests.get(url)

soup = BeautifulSoup(hemisphere.text, 'html.parser')

browser.visit(url)


# In[47]:


s_button=browser.links.find_by_partial_text('Schiaparelli')
s_button.click()

Schiaparelli=browser.url
print(Schiaparelli)

response2=requests.get(Schiaparelli)
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response2.text, 'html.parser')


# In[48]:


s_title=soup.body.find('h2',class_='title').text
print(s_title)
Schiaparelli_img=soup.body.find('li').a['href']
print(Schiaparelli_img)


# In[49]:


Schiaparelli=dict({"title":s_title,"img_url":Schiaparelli_img})


# In[50]:


def schi_function():
    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    
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

    


# In[51]:


schi_function()


# ### Syrtis

# In[52]:


from bs4 import BeautifulSoup
import requests
from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[53]:


#Go back to main page
url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

hemisphere=requests.get(url)

soup = BeautifulSoup(hemisphere.text, 'html.parser')

browser.visit(url)


# In[54]:


sy_button=browser.links.find_by_partial_text('Syrtis')
sy_button.click()

Syrtis=browser.url
print(Syrtis)

response3=requests.get(Syrtis)
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response3.text, 'html.parser')


# In[55]:


sy_title=soup.body.find('h2',class_='title').text
print(sy_title)
Syrtis_img=soup.body.find('li').a['href']
print(Syrtis_img)


# In[56]:


Syrtis=dict({"title":sy_title,"img_url":Syrtis_img})


# In[57]:


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


# In[58]:


syrtis_function()


# ### Valles

# In[59]:


from bs4 import BeautifulSoup
import requests
from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[60]:


#Go back to main page

url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

hemisphere=requests.get(url)

soup = BeautifulSoup(hemisphere.text, 'html.parser')

browser.visit(url)


# In[61]:


v_button=browser.links.find_by_partial_text('Valles')
v_button.click()

Valles=browser.url
print(Valles)

response4=requests.get(Valles)
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response4.text, 'html.parser')


# In[62]:


v_title=soup.body.find('h2',class_='title').text
print(v_title)
Valles_img=soup.body.find('li').a['href']
print(Valles_img)


# In[63]:


Valles=dict({"title":v_title,"img_url":Valles_img})


# In[64]:


def valles_function():
    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
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


# In[65]:


valles_function()


# #### Append dictionaries to list

# In[71]:


hemisphere_img_urls=[]


# In[72]:


hemisphere_img_urls=[cerberus,Schiaparelli,Syrtis,Valles]


# In[73]:


#Returning dictionaries saved in the hemisphere names in the list above
hemisphere_img_urls


# In[74]:


def hemispheres():
    hemisphere_img_urls=[]
    hemisphere_img_urls=[cerberus,Schiaparelli,Syrtis,Valles]
    return hemisphere_img_urls


# In[75]:


hemispheres()


# ### final scrape function

# In[76]:


def scrape():
    mars_info = {
        'news':news_function(),
        'featured_image':featured_image_function(),
        'mars facts':mars_facts_function(),
        'hemispheres':hemispheres()
    }
    return mars_info


# In[77]:


scrape()


# In[ ]:





# In[ ]:




