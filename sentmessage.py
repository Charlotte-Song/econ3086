import re
import time
import telepot
from telepot.loop import MessageLoop
import pandas as pd
import io

def search(name,size):
    website = ["knckff", "stockx"]
    df1 = pd.read_excel("/Users/songyijin/Desktop/data_KN.xlsx")

    df2 = pd.read_excel("/Users/songyijin/Desktop/data_SX.xlsx")

    df1 = df1.set_index('Unnamed: 0')
    df2 = df2.set_index('Unnamed: 0')
    price1 = []
    names = []

    for i in range(0, len(df1.index)):
        if name in df1.index[i]:
            price1.append(df1.loc[df1.index[i], size])
            names.append(df1.index[i])

    price2 = []
    for i in range(0, len(df2.index)):
        if name in df2.index[i]:
            price2.append(df2.loc[df2.index[i], size])

    pd1 = pd.DataFrame(price1, index=names, columns=[website[0]])
    pd2 = pd.DataFrame(price2, index=names, columns=[website[1]])

    inform = [pd1.T, pd2.T]
    output = pd.concat(inform)
    choose = ['-1'] * len(names)
    pd3 = pd.DataFrame(choose, index=names, columns=['choose'])
    pd3 = pd3.T
    # output.insert(output.shape[1], 'choose', 'both')
    output = pd.concat([output, pd3], axis=0)

    for i in range(0, len(names)):
        p1 = float("".join(filter(str.isdigit, output.loc[website[0], names[i]])))
        p2 = float("".join(filter(str.isdigit, output.loc[website[1], names[i]])))
        if p1 < p2:
            output.loc['choose', names[i]] = website[0]
        else:
            output.loc['choose', names[i]] = website[1]

    return output


token = '1638367235:AAGXDSEku5j3x7XO5ngcJZLZhpPhlWEHDyY'
bot = telepot.Bot(token)
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if msg['text'].isalnum:
        print(msg['text'])
        #name = "".join(filter(str.isalpha(),str(msg['text']))).upper()
        name = str(msg['text'])[1:6].upper()
        print(name)
        size =re.findall(r"\d+\.?\d*",str(msg['text']))[0]
        print(size)
        output = search(name,size)
        print(output)
        text = 'name: ' + output.columns[0] + ' ' +output.columns[1] + "\n" + 'knckff:    ' + output.loc['knckff'][0] +"                      "+ output.loc['knckff'][1] +"\n" + 'stockx:   ' +output.loc['stockx'][0]+"                      "+output.loc['stockx'][1] + "\n" + "choose:   "+output.loc['choose'][0] +"                      "+ output.loc['choose'][1]
        print(text)

        #towrite = io.BytesIO()
        #output.to_excel(towrite)  # write to BytesIO buffer
        #towrite.seek(0)
        #print(towrite)
        #b''
        #print(type(towrite))
        #_io.BytesIO
        bot.sendMessage(chat_id, text)


MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

while 1:
    time.sleep(10)