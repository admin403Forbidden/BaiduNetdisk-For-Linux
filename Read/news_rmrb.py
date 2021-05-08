import requests

import datetime,time,os

from bs4 import *

def get_PAGE(date=None):
    
    url = "http://paper.people.com.cn/rmrb/html/%s/nbs.D110000renmrb_01.htm"%date

    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
    
    r = requests.get(url,headers=headers)
    
    r.raise_for_status()
    
    r.encoding = r.apparent_encoding

    print("> HTML DOWNLOAD FROM",url)
    
    return r.text

def get_LINK(day):
    
    #print(day)
    
    bs=BeautifulSoup(get_PAGE(day),'html.parser')

    tmp = bs.find('div',attrs = {"id" : "pageList"})
    
    if tmp:
        
        pageList = tmp.ul.find_all('div', attrs = {'class': 'right_title-name'})

    else:
        
        pageList = bs.find('div', attrs = {'class': 'swiper-container'}).find_all('div', attrs = {'class': 'swiper-slide'})

    #print(pageList)
    
    pages=[]
    
    for i in pageList:
        
        nurl = 'http://paper.people.com.cn/rmrb/html/'+day+"/"+i.a["href"]
         
        #print(nurl)

        pages.append(nurl)

        print("=> GETTING LINKS",nurl)
    
    return pages

def Final_Link(Link=None,day=None):

    url = Link
    
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
    
    r = requests.get(url,headers=headers)
    
    r.raise_for_status()
    
    r.encoding = r.apparent_encoding
    
    html = r.text
    
    bs = BeautifulSoup(html,"html.parser")

    tmp = bs.find('div', attrs = {'id': 'titleList'})

    if tmp:
        
        tlist = tmp.ul.find_all("li")
        
    else:
        
        tlist = bs.find("ul",attrs = {"class":"news-list"}).find_all('li')
        
    #print(tlist)
    
    Link_list=[]
    
    for i in tlist:
        
        for j in i.find_all("a"):
            
            Link = j["href"]
            
            if "D110000renmrb" in Link:
                
                Link_list.append('http://paper.people.com.cn/rmrb/html/'+day+"/"+Link)

                print("==> GETTING FINAL LINK",'http://paper.people.com.cn/rmrb/html/'+day+"/"+Link)

    return Link_list
    
def URL_FINAL(day):
    
    gotten_link = get_LINK(day)
    
    Final_URL=[]
    
    for i in gotten_link:
        
        for j in Final_Link(i,day):
            
            Final_URL.append(j)

    print("-> SUCCESSFULLY GOTTEN ALL THE LINKS")

    return Final_URL

def Get_Artical(url):

    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
    
    r = requests.get(url,headers=headers)
    
    r.raise_for_status()
    
    r.encoding = r.apparent_encoding

    html = r.text

    bs = BeautifulSoup(html,"html.parser")

    title = bs.h3.text + "\n" + bs.h1.text + "\n" + bs.h2.text + "\n"

    #print(title)

    artical_ = bs.find("div",attrs={"id":"ozoom"}).find_all("p")

    artical = ""

    for i in artical_:
        
        artical += i.text + "\n"

    final = title + artical

    #print(final)

    print("--> SUCCESSFULLY TURNED PART OF AN ARTICAL INTO ONE.")

    return [final,title.replace('\n',"")]

def save(path = ".\\Data\\",day = None , day2= None):

    try:

        os.mkdir(path + day2)

    except:
        
        print("[Error] Unable to make the path, please check if the path is already there.")

    Dir = path + day2
    
    for i in URL_FINAL(day):

        Art = Get_Artical(i)
        try:
            
            file = open(Dir + "\\" + Art[1] + ".txt","w",encoding='utf-8')

            file.write(Art[0])

            file.close()

            print('---> SUCCESSFULLY WROTE A FILE.')

        except FileNotFoundError:

            print("[Error]Couldn't save the file.Program is going to exit.")

            break
        
    print("====== DOWNLOAD FINISHED. ======")

def main():
    
    day = time.strftime('%Y-%m/%d' , time.localtime())

    print("Today is",day)

    print("====== DOWNLOAD STARTS ======\n\n")
    
    save(day = day ,day2 = time.strftime('%Y%m%d' , time.localtime()))

if __name__ == "__main__":

    main()

    input("\n\nPRESS ENTER TO EXIT THE APP.")
    
