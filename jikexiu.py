#jikexiu  POST
import requests
import pandas
import json
import copy

brand_URL = 'https://tuiguang.jikexiu.com/order/quick/getBrand'
headers_brand = {
'Host': 'tuiguang.jikexiu.com',
'Connection': 'keep-alive',
'Content-Length': '0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Content-Type': 'text/plain;charset=UTF-8',
'Accept': '*/*',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'https://tuiguang.jikexiu.com/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
}

response = requests.post(brand_URL, headers=headers_brand)
xx=response.text
brand=json.loads(xx)
yy=brand['brandList']
o=pandas.DataFrame(yy)
oo=o.drop(['checkFlag','pic','status'],axis=1)
brand=oo


ROOT_URL = 'https://tuiguang.jikexiu.com/order/quick/deviceMalfunction'
headers_root = {
'Host': 'tuiguang.jikexiu.com',
'Connection': 'keep-alive',
'Content-Length': '21',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Accept': '*/*',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'https://tuiguang.jikexiu.com/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
}

solutionDF0 = pandas.DataFrame(columns=['id', 'malfunctionFid', 'malfunctionId', 'malfunctionName', 'method', 'officialPrice', 'price', 'solutionOwnerType', 'brandId', 'deviceId', 'model'])
deviceLiDF0 = pandas.DataFrame(columns=['id', 'model'])
for ibrand in brand['id']:
	def create_data():
		data={'deviceId':-1,'brandId':ibrand}
		return data
	response = requests.post(ROOT_URL, data=create_data(), headers=headers_root)
	xx=response.text
	brandxx=json.loads(xx)
	solution=brandxx['solutionMalfunctionList']
	if len(solution)==0: continue
	deviceLi=brandxx['deviceList']
	if len(deviceLi)==0: continue
	solutionDF=pandas.DataFrame(solution)
	deviceLiDF=pandas.DataFrame(deviceLi)
	solutionDF['brandId'] = ibrand
	solutionDF['deviceId'] = deviceLiDF.loc[0,'id']
	solutionDF['model'] = deviceLiDF.loc[0,'model']
	solutionDF0=solutionDF0.append(solutionDF)
	deviceLiDF0=deviceLiDF0.append(deviceLiDF)
	x=0
	for i in list(deviceLiDF['id'])[1:]:
		def create_data1():
			data={'deviceId':i,'brandId':-1}
			return data
		response = requests.post(ROOT_URL, data=create_data1(), headers=headers_root)
		xx=response.text
		brandxx=json.loads(xx)
		solution=brandxx['solutionMalfunctionList']
		if len(solution)==0: continue
		solutionDF=pandas.DataFrame(solution)
		x=x+1
		solutionDF['brandId'] = ibrand
		solutionDF['deviceId'] = deviceLiDF.loc[x,'id']
		solutionDF['model'] = deviceLiDF.loc[x,'model']
		solutionDF0=solutionDF0.append(solutionDF)


mal_total.to_csv('mal_total20180317.csv')
maldetails_total.to_csv('maldetails_total20180317.csv')
brandPhone.to_csv('brandPhone20180317.csv')
