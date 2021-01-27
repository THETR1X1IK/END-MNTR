
import requests
import json
import time

s = requests.Session()

currentIDs = []
keywords = ['a']

useProxies = False
pages = 50
delay = 0.1

headers =  {
'Host': 'launches-api.endclothing.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:78.0) Gecko/20100101 Firefox/78.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Origin': 'https://www.endclothing.com',
'Connection': 'keep-alive',
'Referer': 'https://www.endclothing.com/sg/latest-products?brand=Nike%20Jordan&brand=Nike%20SB&brand=Adidas&department=Sneakers',
'Cache-Control': 'max-age=0'
}
ssss = ''
def scrape():
    global ssss
    offs = 0
    while offs<pages:
        print(offs)
        try:
            endpoint = f'https://launches-api.endclothing.com/api/products/offset/{str(offs)}'
            #if useProxies == True:
            #    random_proxy = proxy_manager.random_proxy()
            #    proxies = random_proxy.get_dict()
            #    response = s.get(endpoint, proxies=proxies)
            if useProxies == False:
                response = s.get(endpoint, headers=headers)
            #if offs != 0:
            #    print(response.text)
            responseJson = json.loads(response.text)
            for id in responseJson['products']:
                if id['id'] in currentIDs:
                    print('Product ID already found - {}'.format(id['id']))
                    continue
                if id['id'] not in currentIDs:
                    #print('New Product ID found - {}'.format(id['id']))
                    productName = '{} - {}'.format(id['name'], id['colour'])
                    for kw in keywords:
                        if kw.lower() in productName.lower():
                            productSKU = id['magentoSku']
                            productEngine = id['releaseMode']
                            productLauchDate = id['releaseDate']
                            if productEngine == 'prepaid-draw':
                                productEngine = 'Prepaid Draw'
                            productURL = 'https://launches.endclothing.com/product/{}.html'.format(id['urlKey'])
                            productImageURL = id['thumbnailUrl']
                            productPrice = id['productWebsites'][0]['price']
                            currentIDs.append(id['id'])
                            ssss += f", {id['id']}"
                            
                            #ss = requests.session()
                            #res = ss.post(webhook,json=message)
            offs += 1
            time.sleep(int(delay))
        except Exception as e:
            print('Error - {}'.format(e))
            time.sleep(int(delay)*2)
        print(ssss)

scrape()