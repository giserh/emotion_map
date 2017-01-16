#coding:utf-8
import flickrapi
import time

# Information of Flickr API
def flickrAPI():
    api_key=u'382e669299b2ea33fa2288fd7180326a'
    api_secret=u'b556d443c16be15e'
    flickr = flickrapi.FlickrAPI(api_key, api_secret,cache=True)
    return flickr

#Get URL by location which contains the latitude and the longitude of the center point with radius of searching round
def getUrlFromLocation(latitude,longitude,datemin,datemax,R=5):
    flickr=flickrAPI()
    file=open(str(locationName)+r'.txt','a')
    file.write(str(datemin)+"\n")
    file.close()
    try:
        photos = flickr.walk(lat=latitude,lon=longitude,radius=R,extras='url_c',min_taken_date=datemin,max_taken_date=datemax,per_page=500)
        print("搜索中心:经度"+str(latitude)+"  纬度"+str(longitude)+"  搜索半径:"+str(R)+"km")
        print(datemin)
    except e:
        print('error!')

    url=getUrl(photos)
    return url

#Get URL exactly
def getUrl(photos):
    #遍历集合中的所有照片并获取URL
    file=open(str(locationName)+r'.txt','a')
    count=0
    for photo in photos:
        url=photo.get('url_c')
        if url is not None:
            count+=1
            file.write(url+"\n")
            photoSet.add(url)
            print(str(count)+"."+str(url))
        else:
            print('url none')
    file.write("Count:"+str(count)+"photos\n")
    file.close()

def timeRange():
    month={m:d for(m,d)in zip(list(range(1,13)),[31,28,31,30,31,30,31,31,30,31,30,31])}
    datemin=[];datemax=[]
    year=list(range(startYear,2017))
    for y in year:
        for m in month:
            datey=y
            datem=m
            dated=month[m]
            if y==2016 and m>=7:break
            datemax.append(str(datey)+"-"+str(datem)+"-"+str(dated))
            datemin.append(str(datey)+"-"+str(datem)+"-01")
    return datemax,datemin

#Set information here!
print('Start Downloading!')
# Input information
locationName0=['5NiagaraFalls','5NiagaraFallsCana','28GreatWallOfChina','35OceanParkHongKong']
latitude0=[43.0828,43.0962,40.4319,22.4346]
longitude0=[-79.0742,-79.0377,116.5704,114.1722]

startYear=2012#起始时间（年份）
searchRadius=0.5
# Other information
num=0
for locationName in locationName0:
    latitude=latitude0[num]
    longitude=longitude0[num]
    num+=1
    photoSet=set()
    number=0
    datemax,datemin=timeRange()
    for maxd in datemax:
        mind=datemin[number]
        number+=1
        getUrlFromLocation(latitude,longitude,mind,maxd,searchRadius)
        time.sleep(5)
    file=open(str(locationName)+r'Set.txt','a')
    for photo in photoSet:
        file.write(photo+"\n")
    file.close()