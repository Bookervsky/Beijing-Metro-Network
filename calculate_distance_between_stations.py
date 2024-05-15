import geopy
from geopy import distance
#1.两点间直线距离：根据经纬度计算两点geodesic distance，单位为m
def geodesic_distance(lat1, lon1, lat2, lon2):
    return distance.distance((lat1, lon1), (lat2, lon2)).m

#2.高德地图推荐距离
def Amap_distance(lat1, lon1, lat2, lon2):
    url = 'https://restapi.amap.com/v3/direction/transit/integrated?'

    param = {'key':'#此处输入你的key',
    'origin':str(lon1)+','+str(lat1),
    'destination':str(lon2)+','+str(lat2),
    'city':'北京',
    'strategy':'0',
    'nightflag':'0',
    'output':'json'
    }
    # 调用高德地图API计算两点地铁站间的公共交通换乘方案
    try:
        response = requests.get(url,params=param).json()
    #获得高德地图推荐路径的总距离
        Amap_distance = response['route']['transits'][0]['distance']
    except: 
        Amap_distance = 0
    return Amap_distance

#3.计算两点间的曼哈顿距离
def manhattan_distance(lat1, lon1, lat2, lon2):
    a = geopy.distance.distance((lat1, lon2), (lat1, lon1)).km
    b = geopy.distance.distance((lat1, lon2), (lat2, lon2)).km
    return a+b