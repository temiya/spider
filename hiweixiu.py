#brandPhone GET
import requests
import pandas
import json
from bs4 import BeautifulSoup
headers_root = {
'Host': 'api.shanxiuxia.com',
'Connection': 'keep-alive',
'Origin': 'http://www.weadoc.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Referer': 'http://www.weadoc.com/repairOrder.html',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
}

brandPhone_URL = 'http://www.hiweixiu.com/step?bid=24&fid=34&ref='
response = requests.get(brandPhone_URL)
soup = BeautifulSoup(response.text)
yy=soup.input
zz=yy['value']
z=json.loads(zz)
o=pandas.DataFrame(z)
o.ix["faluts"][0]
for k,v in z['95']['faluts'].items():
    for k1,v1 in v.items():
        for k2,v2 in v1.items():
            print(k2)

oo=pandas.DataFrame(index=['ColorId', 'ProductId','BrandId','MouldId','faulttype_id','faulttype_detail_id','Id','ColorName','Price','official_price','RepairTime','FaultTypeId','FaultType','FaultTypeDetailId','FaultTypeDetail','RepairType','remark','brand_home_visit_fee','brand_manual_fee','honai_brand_home_visit_fee','honai_brand_manual_fee','honai_Price'])
for k,v in z['95']['faluts'].items():
	for k1,v1 in v.items():
		n=pandas.Series(list(v1.values()), index=list(v1.keys()))
		x=pandas.DataFrame(n,columns=[z['95']['MouldName']])
		oo=pandas.concat([oo,x], axis=1)

		
		
kv=dict()
for k,v in z['95']['faluts'].items():
    for k1,v1 in v.items():
        for k2,v2 in v1.items():
            kv[k2]=v2


#soup.find_all("div", class_="h4_type")     #price             
#soup.find_all(attrs={"data-id": "1154"})    #phones   有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性:但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
#soup.find(attrs={"data-id": "1154"}).text.strip()   #phone 型号

brandPhone_URL = 'http://www.hiweixiu.com'
response = requests.get(brandPhone_URL)
soup = BeautifulSoup(response.text)
n=soup.find_all(href=re.compile("bid"))
Tails=n[0].get('href')
UU=brandPhone_URL+Tails


oo=pandas.DataFrame(index=['Id', 'MouldName', 'colors', 'faluts'])
for link in n:
	Tails=link.get('href')
	UU=brandPhone_URL+Tails
	response = requests.get(UU)
	soup = BeautifulSoup(response.text)
	yy=soup.input
	zz=yy['value']
	z=json.loads(zz)
	o=pandas.DataFrame(z)
	oo=pandas.concat([oo,o], axis=1)

oo.to_csv('hiweixiu_total20180317.csv',encoding='utf-8')

import re
import requests
import pandas
import json
from bs4 import BeautifulSoup
oo=pandas.DataFrame(index=['ColorId', 'ProductId','BrandId','MouldId','faulttype_id','faulttype_detail_id','Id','ColorName','Price','official_price','RepairTime','FaultTypeId','FaultType','FaultTypeDetailId','FaultTypeDetail','RepairType','remark','brand_home_visit_fee','brand_manual_fee','honai_brand_home_visit_fee','honai_brand_manual_fee','honai_Price'])
brandPhone_URL = 'http://www.hiweixiu.com'
response = requests.get(brandPhone_URL)
soup = BeautifulSoup(response.text)
n=soup.find_all(href=re.compile("bid"))
Tails=n[0].get('href')
UU=brandPhone_URL+Tails

for link in n:
	Tails=link.get('href')
	UU=brandPhone_URL+Tails
	response = requests.get(UU)
	soup = BeautifulSoup(response.text)
	yy=soup.input
	zz=yy['value']
	z=json.loads(zz)
	for breaknum in list(z.keys()):
		for k,v in z[breaknum]['faluts'].items():
			for k1,v1 in v.items():
				nn=pandas.Series(list(v1.values()), index=list(v1.keys()))
				x=pandas.DataFrame(nn,columns=[z[breaknum]['MouldName']])
				oo=pandas.concat([oo,x], axis=1)
	
oo.to_csv('hiweixiu_total20180323.csv')
