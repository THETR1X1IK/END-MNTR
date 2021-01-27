############## BOT COMMANDS ##############
# !run (optional) [] example: !run end
# !endal (optional) [] example: !endal https://sdsdsd.ss/
# !endrl (optional) [] example: !endrl https://sdsdsd.ss/
# !stop (optinal) [] example: !stop end
# 
#
#
#
#
##########################################

import requests
import json
from bs4 import BeautifulSoup as Soup
import discord_webhooks 
from discord_webhooks import DiscordWebhooks
import discord
import time
import asyncio
from urllib3 import ProxyManager, make_headers
from discord.ext import commands

s = requests.Session()

bot = commands.Bot(command_prefix='?')

IsRunned = False
################# BOT SETTINGS #################

bot_cid = '729431862505898035'
bot_token = 'NzI5NDMxODYyNTA1ODk4MDM1.XwI2cw.1AHwVAV936GdduUNlglb9WEF7I0'

################################################

########### MONITOR DEFAULT SETTINGS ###########
sysWEBHOOK = 'https://discordapp.com/api/webhooks/729430604008914978/bgLuO0KCFSsZDtl1YIcgLXi3aAFhmTebeFOaa4mC7Rb2GDwBrRf1nay3o2Ao9Gt5x2fQ'
WEBHOOK = 'https://discordapp.com/api/webhooks/729430492553936936/br9QA1_wzKx42QRJJ1dnifYNRdkSQabkfTqlBPFhfJ9ujuOzqo5fIKYl6Ho2KpN_NGG5'
db_PATH = '/Users/MagixPE/Desktop/Pasichniy Private/endproducts.json'
################################################


sizs = {}


init = 1
currentIDs = []
restockList = []
producSizes = []

try:
    with open(db_PATH) as json_file:
        currentIDs = json.load(json_file)
except Exception as e:
    print(e)
    with open(db_PATH, 'w') as outfile:
        json.dump(currentIDs, outfile)

keywords = ['yeezy', 'jordan 1', 'dunk', 'sacai', 'travis scott', 'a']

useProxies = False
pages = 50
delay = 0.5

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

endpoint = f'https://launches-api.endclothing.com/api/products/offset/0'
import ast
async def RestockHandler():
    pass

async def UploadHandler():
    pass

async def UpdateLinks(newdict):
    global sizs
    dct = '{'
    if str(sizs) != '{}':
        for name, value in sizs.items():
            dct += f'{name}:{value},'
        for name, value in newdict.items():
            dct += f'{name}:{value}' + '}'
    else:
        for name, value in newdict.items():
            dct = '{' + f'{name}:{value}' + '}'
    sizs = ast.literal_eval(dct)
    return sizs

async def RemoveLink(name):
    try:
        id = sizs[name]
    except KeyError:
        return 'KeyError'
    return id

@bot.event
async def on_message(message):
    command = message.content.split(' ')[0]
    print(command)
    if True:#'!' in message.content[0]:
        #if '!run' in command:
        #    IsRunned = True
        #    await message.channel.send('Стартуем...\nКак только монитор будет запущен, в системный канал поступит сообщение.')
        #    return await run()
        if '!endal' in command:
            link = message.content.split(' ')[1]
            txt = await findId(link)
            print('TXT '+txt)
            return await message.channel.send(txt)
        if '!endrl' in command:
            id = await RemoveLink(message.content.split(' ')[1])
            currentIDs.remove(id)
            return await message.channel.send('Ссылка успешна удалена!')
        #if '!run' in command:
        #    IsRunned = False
        #    await message.channel.send('Останавливаю монитор...\nОн будет выключен, когда закончит цикл проверки товаров.')

async def findId(link):
    #sess = requests.Session()
    headers =  {
'Host': 'launches.endclothing.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:78.0) Gecko/20100101 Firefox/78.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'If-None-Match': "19b79-zx+1eKiqZ6C9n9UNQgBrDgkoGgc",
'Cache-Control': 'max-age=0'
}
    isstop = 0
    offs = 1
    while (isstop < 1) or (offs < 65):
        try:
            endpointtt = f'https://launches.endclothing.com/?page={str(offs)}'
            #if useProxies == True:
            #    random_proxy = proxy_manager.random_proxy()
            #    proxies = random_proxy.get_dict()
            #    response = s.get(endpoint, proxies=proxies)
            if useProxies == False:
                response = requests.get(endpointtt, headers=headers)
            #if offs != 0:
            #    print(response.text)
            soup = Soup(response.text)
            products = soup.findAll("div", attrs={"class":"ProductCardSC-ut9ty8-0 gIdUYp"})
            #print(products)
            #responseJson = json.loads(response.text)
            for id in products:
                soup2 = Soup(str(id))
                href = soup2.find("a", attrs={"class":"InnerLink-sc-1tkrc89-0 dGdHfu"})["href"].split('product/')[1]
                print(f'Checking offset - {str(offs)} [{href}]')
                if id['id'].split('plp-item-')[1] not in currentIDs:
                    #print('New Product ID found - {}'.format(id['id']))
                    if str(href) in str(link):
                        currentIDs.append(id['id'].split('plp-item-')[1])
                        isstop = 1
                        #await UpdateLinks({link:id['id']})
                        print(str(f"Продукт с ID {id['id'].split('plp-item-')[1]} найден на {offs} странице."))
                        return str(f"Продукт с ID {id['id'].split('plp-item-')[1]} найден на {offs} странице.")
        except Exception as e:
            print('Error - {}, offset - {}'.format(e, offs))
        time.sleep(0.01)
        offs += 1
    return 'Продукт не найден в списке.\n Пробую загрузить продукт в список без ID.'

#async def RaffleHandler():
#    pass



async def GetProductInfo(productName, urlkey, thumbnail, sku, url, price):
    headers =  {
'Host': 'www.endclothing.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:78.0) Gecko/20100101 Firefox/78.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'If-None-Match': "19b79-zx+1eKiqZ6C9n9UNQgBrDgkoGgc",
'Cache-Control': 'max-age=0'
}
    link = f'https://www.endclothing.com/ru/{urlkey}.html'
    ########      curl -U "zuvrbj:xvTndXTaBd" -vx "45.89.62.84:24531" -H "Cache-Control: max-age=0" -H "Upgrade-Insecure-Requests: 1" -H "Connection: keep-alive" -H "Host: api2.endclothing.com" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:78.0) Gecko/20100101 Firefox/78.0" -H "Cookie: rxVisitor=1592436835933CI7VOU8MIMEV6J186OG7AQB35CCV1NV2; _gcl_au=1.1.822826295.1592436840; _ga=GA1.1.179666916.1592436841; _ga_BZDVJYZJVX=GS1.1.1593280141.7.1.1593280168.0; DG_IID=90D75181-BF41-33B5-BD46-3AD850F4EEF7; DG_UID=2F78832D-BA5E-3172-8DE2-7D9A01F3A4BC; DG_ZID=521BEFDD-256B-32E0-97B4-B7724F869B98; DG_ZUID=0BFCCBD9-1C0F-3864-B8D5-E81DFEB77155; DG_HID=E1781909-F195-38F5-A6AC-E0839A10B7D1; DG_SID=37.204.133.6:jlHjVMnepWMn+On7eec4GOoiGtMAeJ+kk421lyH1W4g; __zlcmid=ykjDZbqCeGhcg5; _fbp=fb.1.1592436843095.289571638; dtPC=2$269320296_492h-vKQDFMHNUJWFFURHIGASGKPKGCSKUUMHR-0e0; rxvt=1593276879922|1593275025233; dtSa=-; dtLatC=88; end_country=US; _gid=GA1.2.1604448578.1593262261; _uetsid=fd9528b0-e263-2276-47c1-4d911ff2648d; _uetvid=0c3ee3fc-f80b-1eca-b4bd-ad432e3b735d; dtCookie=v_4_srv_2_sn_6K6K8C8AMPUTJB6QO00D67ASB0LH9D5F_app-3A6abe796a369c80f6_1_app-3A063974da2eae43d3_1_ol_0_perc_100000_mul_1; reese84=3:d3XLSvTW5CeVvbeO1CrIjg==:elEgkng6TzUMA6hYULpt8Oh/PiQKMyvA86rUjVVXSD08jgfPutn214te8QMfch21qGzns250Nw8+pNCnGzpi+D9ukmY3xN44/+SDs/SM89Ry3kzgx+JKEpDawUvZ5Q32g0x++8zJqyip2cz4zFOSufbxTtp33wKoXfbSgHMol9NxfMTtI4YijHpBmIaoKCLH/1+1DAlHMHtL/rrz80nJoR8MwNmhJii+6Duq6lj1NKzdRL9jUDFPT3mSoV8KIrf+NDTYoO/0QviQXzNCMknsXh//2H48iuYFnbrHerJqwI79WU6vc4ypPU1UQ0M9bJ8DVNEwLHY2j1/zfzC0tNvSGcGSdFkw2YKST1EmDdK+AnBw1j96m/ErxgPgmZWTwG4zngyEbZbzfx2KQsSnwMyYl4sqOWuo72c+Xuq5WG26Dxs=:jcoWRO30Ms1ltgTjYpv0k7WSmkvREH4fAkbFq9be6No=" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br" "https://api2.endclothing.com/ru/rest/V1/end/catalog/link?link=%252Fus%252Fconverse-x-pop-trading-company-jack-purcell-pro-hi-169006c.html"
    r = requests.get(link, headers=headers)
    if r.status_code == 404:
        return print('Product not loaded')
    if 'Access To Website Blocked' in str(r.text):
        return print('Proxy Error')
    soup = Soup(r.content, 'html.parser')
    f = soup.find("script", attrs={'id':'__NEXT_DATA__'})
    to_p = str(f).split('<script id="__NEXT_DATA__" type="application/json">')[1].split('</script>')[0]
    try:
        sizes = json.loads(to_p)['props']['initialProps']['pageProps']['product']['configurable_product_options'][0]['values']
    except KeyError:
        print('SoldOut')
        if sku not in restockList:
            restockList.append(sku)
        for i in producSizes:
            if sku in str(i):
                if i[sku] != '':
                    producSizes.remove(i)
                    producSizes.append({sku:''})
                    return print('continue')
        return print('continue')
    if str(sizes) == '[]':
        return False # Sizes not defined
    r_sizes = ''
    stock = 0
    for i in sizes:
        r_sizes += f'{i["label"]}\n'
        stock += 1
    if sku not in restockList:
        restockList.append(sku)
        if init != 1:
            return await MessageSend(productName, url, r_sizes, price, thumbnail, sku, stock, False)
        else:
            return True
    for i in producSizes:
        if sku in str(i):
            print('i[sku]\n' + i[sku])
            print('r_sizes\n' + r_sizes)
            if r_sizes not in str(i[sku]):
                print('r_sizes not in i[sku]')
                producSizes.remove(i)
                producSizes.append({sku:r_sizes})
                if init != 1:
                    return await MessageSend(productName, url, r_sizes, price, thumbnail, sku, stock, True)
                else:
                    return True
    producSizes.append({sku:r_sizes})
    return True

    #soup_size = Soup(sizes, 'html.parser')

#async def RestockInit():
#    for pid in currentIDs:
#        sess = requests.Session()
#        endpoint = f'https://launches-api.endclothing.com/api/products/{pid}'
#        response = sess.get(endpoint, headers=headers)
#        id = json.loads(response.text)
#        sku = id['magentoSku']
#        productName = '{} - {}'.format(id['name'], id['colour'])
#        productURL = 'https://launches.endclothing.com/product/{}.html'.format(id['urlKey'])
#        tmb = id['thumbnailUrl']
#        price = str(id['productWebsites'][14]['price']) + ' RUB'
#        sess.close()
#        await GetProductInfo(productName, id['urlKey'], tmb, sku, productURL, price)
async def RestockInit():
    pass
async def SendSystem(message):
    embed_obj = DiscordWebhooks(sysWEBHOOK)
    embed_obj.description = message
    embed_obj.send()

async def MessageSend(name, p_url, sizes, price, tmURL, sku, stock, IsRestock):
    embed_obj = DiscordWebhooks(WEBHOOK)
    embed_obj.title = name
    embed_obj.url = p_url
    embed_obj.set_thumbnail(url=tmURL)
    embed_obj.add_field(name='**SKU**', value=sku)
    if IsRestock == True:
        embed_obj.add_field(name='**Type**', value='Restock')
    else:
        embed_obj.add_field(name='**Type**', value='New Item')
    #embed_obj.add_field(name='Stock', value=f'{stock}+')
    embed_obj.add_field(name='**Price**', value=price)
    embed_obj.add_field(name='**Sizes**', value=sizes)
    embed_obj.add_field(name='**Links**', value='[Checkout](https://www.endclothing.com/us/checkout/)\n[Login](https://www.endclothing.com/us/customer/account/login/)')
    embed_obj.set_footer(text='Pasichniy Private | ' + time.ctime(), url='https://sun9-22.userapi.com/c858036/v858036349/13a5b3/9Cxwya8brno.jpg')
    embed_obj.send()

import traceback

async def run():
    global init
    global IsRunned
    print('Starting...')
    await RestockInit()
    while IsRunned:
        try:
            #if useProxies == True:
            #    random_proxy = proxy_manager.random_proxy()
            #    proxies = random_proxy.get_dict()
            #    response = s.get(endpoint, proxies=proxies)
            if useProxies == False:
                response = s.get(endpoint, headers=headers)
            try:
                responseJson = json.loads(response.text)
            except Exception as e:
                if 'Expecting value' in str(e):
                    await asyncio.sleep(2)
                    continue
            for id in responseJson['products']:
                productName = '{} - {}'.format(id['name'], id['colour'])
                productSKU = id['magentoSku']
                productURL = 'https://www.endclothing.com/ru/{}.html'.format(id['urlKey'])
                productImageURL = id['thumbnailUrl']
                priceRU = str(id['productWebsites'][14]['price']) + ' RUB'
                for kw in keywords:
                    if kw.lower() in productName.lower():
                        if id['id'] in currentIDs:
                            print('Product ID already found - {}'.format(id['id']))
                            await GetProductInfo(productName, id['urlKey'], productImageURL, productSKU, productURL, priceRU)
                            time.sleep(0.01)
                            continue
                        if id['id'] not in currentIDs:
                            print('New Product ID found - {}'.format(id['id']))
                            #productEngine = id['releaseMode']
                            #productLauchDate = id['releaseDate']
                            #if productEngine == 'prepaid-draw':
                            #    productEngine = 'Prepaid Draw'
                            #productPrice = id['productWebsites'][0]['price']
                            await GetProductInfo(productName, id['urlKey'], productImageURL, productSKU, productURL, priceRU)
                            currentIDs.append(id['id'])
                            with open(db_PATH, 'w') as outfile:
                                json.dump(currentIDs, outfile)
                            time.sleep(0.01)
                            #ss = requests.session()
                            #res = ss.post(webhook,json=message)
            for id in currentIDs:
                endpointt = f'https://launches-api.endclothing.com/api/products/{id}'
                response = s.get(endpointt, headers=headers)
                try:
                    pid = json.loads(response.text)
                except Exception as e:
                    if 'Expecting value' in str(e):
                        continue
                sku = pid['magentoSku']
                productName = '{} - {}'.format(pid['name'], pid['colour'])
                productURL = 'https://www.endclothing.com/ru/{}.html'.format(pid['urlKey'])
                productImageURL = pid['thumbnailUrl']
                priceRU = str(pid['productWebsites'][14]['price']) + ' RUB'
                if init == 1:
                    await GetProductInfo(productName, pid['urlKey'], productImageURL, sku, productURL, priceRU)
                for rsku in restockList:
                    if sku == rsku:
                        if init != 1:
                            await GetProductInfo(productName, pid['urlKey'], productImageURL, sku, productURL, priceRU)
            if init == 1:
                init = 0
                await SendSystem('Initialization completed!')
            time.sleep(int(delay))
        except Exception as e:
            print('Error - {}'.format(e))
            if 'list index out of range' in str(e):
                time.sleep(5)
            else:
                await SendSystem(traceback.format_exc())
bot.loop.create_task(run())
#asyncio.get_event_loop().run_until_complete(run())
bot.run(bot_token)
#asyncio.get_event_loop().run_until_complete(run())
#MessageSend('Test Embed', 'https://www.endclothing.com/ru/adidas-response-hoverturf-fx4152.html','UK 0\nUK -1\nUK 1+1', '1000000$', 'https://media.endclothing.com/media/catalog/product/A/d/Adidas-Response-Hoverturf---White_-Yellow-_-Black---_FX4152_m1_1.jpg', 'YY0002', '3+')