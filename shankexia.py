#brandPhone GET

brandPhone_URL = 'http://api.shanxiuxia.com/api/PhoneType/brandPhone'

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

response = requests.get(brandPhone_URL, headers=headers_root)
xx=response.text
brand=json.loads(xx)
yy=brand['data']


o=pandas.DataFrame(yy)
oo=o.drop(['img','mal_img'],axis=1)
brandPhone=oo
brandPhone[brandPhone['id']=='246'][:3]


#brand   GET
brand_URL = 'http://api.shanxiuxia.com/api/PhoneType/brand'

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

response = requests.get(brand_URL, headers=headers_root)
xx=response.text
brand=json.loads(xx)
yy=brand['data']


o=pandas.DataFrame(yy)
oo=o.drop(['image_url_click','url','url_click','wap_url','web_image_url'],axis=1)
brand=oo



#malclass POST
def create_data():
	data={'id':67}
	return data
ROOT_URL = 'http://api.shanxiuxia.com/api/PhoneType/malclass'

headers_root = {
'Host': 'api.shanxiuxia.com',
'Connection': 'keep-alive',
'Content-Length': '16',
'Origin': 'http://www.weadoc.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'http://www.weadoc.com/repairOrder.html',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
}
response = requests.post(ROOT_URL, data=create_data(), headers=headers_root)
xx=response.text
brand=json.loads(xx)
yy=brand['data']
zz=yy['malfunction']

o=pandas.DataFrame(zz)
oo=o.drop(['img'],axis=1)
malclass=oo



def create_data(phone):
	data={'id':phone}
	return data
import copy
nn=list(brandPhone['id'])
mal_total = pandas.DataFrame(columns=['id', 'name', 'type_id'])
for phone in nn:	
	response = requests.post(ROOT_URL, data=create_data(phone), headers=headers_root)
	xx=response.text
	brand=json.loads(xx)
	yy=brand['data']
	zz=yy['malfunction']
	if len(zz)==0: continue
	o=pandas.DataFrame(zz)
	oo=o.drop(['img'],axis=1)
	oo['type_id']=phone
	malclass=oo.copy()
	mal_total=mal_total.append(malclass)


response = requests.post(ROOT_URL, data=create_data(253), headers=headers_root)
xx=response.text
brand=json.loads(xx)
yy=brand['data']
zz=yy['malfunction']
o=pandas.DataFrame(zz)


#maldetails  POST
def create_data():
	data={'id':67,'type_id':16}
	return data
ROOT_URL = 'http://api.shanxiuxia.com/api/PhoneType/maldetails'

headers_root = {
'Host': 'api.shanxiuxia.com',
'Connection': 'keep-alive',
'Content-Length': '16',
'Origin': 'http://www.weadoc.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'http://www.weadoc.com/repairOrder.html',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
}
response = requests.post(ROOT_URL, data=create_data(), headers=headers_root)
xx=response.text
brand=json.loads(xx)
yy=brand['data']

o=pandas.DataFrame(yy)
oo=o.drop(['remark'],axis=1)
maldetails=oo



def create_data(phone,details):
	data={'id':phone,'type_id':details}
	return data

import copy
#nn=zip(list(mal_total['type_id'])[1:3],list(mal_total['id'])[1:3])
nn=zip(list(mal_total['type_id']),list(mal_total['id']))
maldetails_total = pandas.DataFrame(columns=['id', 'malfunction', 'price_reference', 'price_market', 'phone', 'details'])
for phone,details in nn:	
	response = requests.post(ROOT_URL, data=create_data(phone,details), headers=headers_root)
	xx=response.text
	brand=json.loads(xx)
	yy=brand['data']
	if len(yy)==0: continue
	o=pandas.DataFrame(yy)
	oo=o.drop(['remark'],axis=1)
	oo['phone']=phone
	oo['details']=details
	maldetails=oo.copy()
	maldetails_total=maldetails_total.append(maldetails)


response = requests.post(ROOT_URL, data=create_data(253), headers=headers_root)
xx=response.text
brand=json.loads(xx)
yy=brand['data']
zz=yy['malfunction']
o=pandas.DataFrame(zz)



mal_total.to_csv('mal_total20180317.csv')
maldetails_total.to_csv('maldetails_total20180317.csv')
brandPhone.to_csv('brandPhone20180317.csv')
