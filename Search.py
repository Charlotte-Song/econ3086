import pandas as pd
import re

def getName(): #输入获取名字并处理
    try:
        namee = input("Shoes name: ")
        inputName = "".join(filter(str.isalnum, namee)).upper()
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


# load data
website = ["knckff","stockx"]
df1 = pd.read_excel("/Users/songyijin/Desktop/data_KN.xlsx")

df2 = pd.read_excel("/Users/songyijin/Desktop/data_SX.xlsx")

df1 = df1.set_index('Unnamed: 0')
df2 = df2.set_index('Unnamed: 0')

name = getName()
size = getSize()

price1 = []
names = []

for i in range(0,len(df1.index)):
    if name in df1.index[i]:
        price1.append(df1.loc[df1.index[i], size])
        names.append(df1.index[i])

price2 = []
for i in range(0,len(df2.index)):
    if name in df2.index[i]:
        price2.append(df2.loc[df2.index[i], size])

pd1 = pd.DataFrame(price1,index=names,columns=[website[0]])
pd2 = pd.DataFrame(price2,index=names,columns=[website[1]])

inform = [pd1.T,pd2.T]
output = pd.concat(inform)
choose = ['-1']*len(names)
pd3 = pd.DataFrame(choose,index=names,columns=['choose'])
pd3 = pd3.T
#output.insert(output.shape[1], 'choose', 'both')
output = pd.concat([output,pd3],axis=0)

for i in range(0,len(names)):
    p1 = int("".join(filter(str.isdigit, output.loc[website[0],names[i]])))
    p2 = int("".join(filter(str.isdigit, output.loc[website[1],names[i]])))
    if p1<p2:
        output.loc['choose',names[i]] = website[0]
    else:
        output.loc['choose', names[i]] = website[1]

print(output)



