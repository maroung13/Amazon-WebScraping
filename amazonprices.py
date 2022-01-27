from bs4 import BeautifulSoup
import pandas as pd
import requests

def getRequest(url):
    HEADERS = ({'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'})
    return requests.get(url,headers=HEADERS)

#return urls in an array
def readFile(path):
    with open(path,'r') as f :
        url = f.readlines()
    return url 

def saveToExcel(output):
    df = pd.DataFrame(data=output)
    df = df.T
    df.to_excel('dict1.xlsx')

if __name__ == "__main__" :
    array_urls = readFile("<path of the file containing urls>")
    result = {}
    for url in array_urls :
        response = getRequest(url)
        response_content = response.content
        response_code = response.status_code
        title=''
        lower_price=''
        higher_price='' 

        if response_code != 200:
            pass
        else :
            try:
                soup = BeautifulSoup(response_content,'html.parser')
                title=soup.find('span',{'id':'productTitle'}).text
                price_tag = soup.find('td',{'class':'a-color-secondary a-size-base a-text-right a-nowrap'})
                prices = soup.find_all('span',{'class':'a-price a-text-price a-size-medium apexPriceToPay'})
                lower_price = prices[0].find('span',{'class':'a-offscreen'}).text
                if(len(prices)>1):
                    higher_price = prices[1].find('span',{'class':'a-offscreen'}).text

            except:
                lower_price=''
                higher_price=''
        details = {"URL Status code": response_code,"title":title,"Lower Price":lower_price,"Higher Price":higher_price}
        result[url]=details
    saveToExcel(result)

    
    
        
            





