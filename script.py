from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)

driver.get("https://www.reddit.com/r/LaptopDeals/new/")
#get title
#print(driver.title)
#searching something
#search=driver.find_element(by=By.NAME,value='q')
#search.send_keys("test")
#search.send_keys(Keys.RETURN)
#sleep(5)

search=driver.find_element(by=By.TAG_NAME,value='body')
for i in range(1,200):
    search.send_keys(Keys.DOWN)

try:
    data = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))

    )
except:
    driver.quit()

data=driver.find_elements(by=By.TAG_NAME,value='h3')
#links=driver.find_element(by=By.LINK_TEXT,value='outbound-link')
links=driver.find_elements(by=By.TAG_NAME,value='a')

#links=driver.find_element_by_xpath("//div[@class='into']/div[contains(text(), 'noopener nofollow ugc')]").click()

#links=driver.find_element(by=By.XPATH,value='"//div[@class='into']/div[contains(text(), 'noopener nofollow ugc')]"')
i=0
j=0
list=['Scraped Laptops']
link=['corresponding lists']
for a in data:
    temp=data[i].text
    temp.lower()
    if temp.find('[')==0 :

      #if temp.find('asus') >= 0 or temp.find('lenovo') >= 0 or temp.find('dell') >= 0 or temp.find('acer') >= 0 or temp.find('msi') >= 0 or temp.find('gigabyte')>= 0 or temp.find('hp')>= 0:
        list.append(data[i].text)

   # print (data[i].text)
    i=i+1
i=0
for b in links:
    temp=links[i].get_attribute('href')
    #temp.__str__()
    temp.lower()
    if temp.find('asus') >= 0 or temp.find('lenovo')>= 0 or temp.find('dell')>= 0 or temp.find('acer')>= 0 or temp.find('msi')>= 0 or temp.find('gigabyte') >= 0 or temp.find('omen')>= 0:
        asusfil=open('asus.txt',mode='w')
        if(temp.find('asus')>=0):
            asusfil.write(links[i].get_attribute('href'))
        asusfil.close()
        msifil = open('msi.txt', mode='w')
        if (temp.find('msi') >= 0):
            msifil.write(links[i].get_attribute('href'))
        msifil.close()
        gigfil = open('gigabyte.txt', mode='w')
        if (temp.find('gigabyte') >= 0):
            gigfil.write(links[i].get_attribute('href'))
        gigfil.close()
        link.append(links[i].get_attribute('href'))
    i=i+1
print(list)
print(link)
