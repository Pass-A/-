from bs4 import BeautifulSoup
import requests
import re
newsurl="https://ks.wjx.top/m/17074032.aspx"
res=requests.get(newsurl)
res.encoding='UTF-8'
soup=BeautifulSoup(res.text,'html.parser')
#soup.select('.field-label')[0].text
List =[]
soup.select('.qtypetip')
#for cc in soup.select('.field-label'):
#    print (cc.text)

#for aa in soup.select('.label'): 
#    List.append(aa.text)
#print(List)
Str=''
a_list = soup.findAll('div',attrs={'topic':True})
Str+="----------------------------------------------------------------------------"+'\n' 
numid='#div{}'
x=0
Str+=soup.select("#divCut1")[0].text+'\n'  #判断题
for num in range(1,22):    
    for aa in soup.select(numid.format(num)): 
        Str+=a_list[x].get("topic")+'\n'   #topic值 1，c1
        x+=1
        Str+=aa.text+'\n' #基本信息
Str+=a_list[x].get("topic")+'\n' 
Str+="----------------------------------------------------------------------------"+'\n' 
x2=x
Str+=soup.select("#divCut2")[0].text+'\n' 
for num in range(128,168):    
    for aa in soup.select(numid.format(num)): 
        Str+=a_list[x2+1].get("topic")+'\n' 
        x2+=1
        Str+=aa.text+'\n' 
Str+=a_list[x2+1].get("topic")+'\n' 
Str+="----------------------------------------------------------------------------"+'\n' 
x3=x2
Str+=soup.select("#divCut3")[0].text+'\n' 
for num in range(501,511):    
    for aa in soup.select(numid.format(num)): 
        Str+=a_list[x3+2].get("topic")+'\n' 
        x3+=1
        Str+=aa.text+'\n' 
Str+=a_list[x3+2].get("topic")+'\n' 
Str+="***********************************************************************"+'\n' 
print(Str)
f = open("C:/Users/Morris/Desktop/interest7.txt", 'w+',encoding='UTF-8')
f.write(Str)
#print(Str,file=f)
# a_list = soup.findAll('div',attrs={'topic':True})
# for a in a_list:
#     print(a.get("topic"))
