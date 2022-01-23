import urllib.request
import bs4
import ssl
import pandas as pd

def replaceSpace(s): #鞋子名字格式改成yeezy-slide-pure类
    newss = []
    for si in s:
        if(si == ' '):
            si = '-'
            newss.append(si)
        else:
            newss.append(si)
    Newstr = ''
    for i in newss:
        Newstr += i
    return Newstr

def replaceComma(s): #鞋子名字格式改成yeezy-slide-pure类
    newss = []
    for si in s:
        if(si == ','):
            si = ''
            newss.append(si)
        else:
            newss.append(si)
    Newstr = ''
    for i in newss:
        Newstr += i
    return Newstr

def getData(url): #读取网页所有yeezy的信息
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    text = response.read().decode()
    html = bs4.BeautifulSoup(text, 'html.parser')
    shoes = html.find_all("h2", attrs={"class":"shoes-title"})
    data = html.find_all("div", attrs={"class":"field-item even"})
    n = 0
    for price in data:
        n += 1
        if n%4==0:
            output = price.text.strip("NT$")
            money = float(replaceComma(output))*0.2803 #新台币与港币汇率
            output = "HK$" + str(int(money))
            prices.append(output)
    for shoe in shoes:
        url_name = shoe.text
        urlName = replaceSpace(url_name).lower()
        url_names.append(urlName) #urlnames 用来储存接入具体鞋款网址的名字
        name = shoe.text.replace(" ", "") #names 用来储存大写无空格名字
        name = "ADIDAS"+name
        names.append(name)

def getName(): #输入获取名字并处理
    try:
        namee = input("Shoes name: ")
        inputName = namee.replace(' ', '').upper()
        return(inputName)
    except ValueError:
        print("unexpected input name, please try again")
        getName()

def getSize(): #输入获取码数并处理
    try:
        g = input("Shoes size: ")
        a = str(g).split('.')
        b = float(g)
        c = ''.join(a)
        d = float(c)
        if b == d:
            inputSize = str(int(g))
        else:
            inputSize = str(float(g))
        return(inputSize)
    except ValueError:
        print("unexpected input size, please try again")
        getSize()


#正文
names = []
url_names = []
prices = []
url = 'https://www.knckff.com/adidas/yeezy' #因为第一页读不了所以特别分类出来读一遍
getData(url) #读取第一页鞋名字
urls = ['https://www.knckff.com/adidas/yeezy?page={}'.format(i)
        for i in range(1, 8)]
for url in urls: #循环读2-7页的鞋名字
    getData(url)
sizes = ["us All"]
for y in range(4, 19):
    Y = str(int(y))
    sizes.append(Y)
    u = y + 0.5
    if u <= 18:
        U = str(u)
        sizes.append(U)
information = []
for i in range(0,len(names)):
    price = [prices[i]]*len(sizes)
    df = pd.DataFrame(price, index=sizes, columns=[names[i]])
    information.append(df.T)
all_data1 = pd.concat(information)

all_data1.to_excel('/Users/songyijin/Desktop/data_KN.xlsx')
#这里输入name和size，其中name会自动转化为符合格式的全大写，size会自动转化成符合格式的字符串
inputName = getName()
inputSize = getSize()













