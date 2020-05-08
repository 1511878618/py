# 完整代码
# 张子豪 2019-9-11
# Bilibili视频：同济子豪兄 https://space.bilibili.com/1900783
# 粉丝答疑QQ群：953712961


# 导入工具库
import urllib.request
import gzip

## 第一步：生成查询天气的url链接
city_name = input('请输入要查询的城市名称：')

# 将城市的中文名字编码成utf-8字符
urllib.parse.quote(city_name)
# 生成完整url链接
url = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)

## 第二步：访问url链接，解析服务器返回的json数据，变成python的字典数据
# 获取服务器返回的json字节串数据
weather_data = urllib.request.urlopen(url).read()
# 将字节串数据解码为unicode中的utf-8数据
weather_data = gzip.decompress(weather_data).decode('utf-8')
# 将json数据转为python的字典数据
weather_dict = eval(weather_data)
if weather_dict.get('desc') == 'invilad-citykey':
    print('您输入的城市未收录')
    
# 第三步：对字典进行索引，获取气温、风速、风向等天气信息
print('您查询的城市：',weather_dict['data']['city'])
print('--------------------------')
print('今天的天气')
print('温度',weather_dict['data']['wendu'])
print('感冒指数',weather_dict['data']['ganmao'])
print('--------------------------')
print('昨天的天气')
print('昨天：',weather_dict['data']['yesterday']['date'])
print('天气：',weather_dict['data']['yesterday']['type'])
print('最高气温：',weather_dict['data']['yesterday']['high'])
print('最低气温：',weather_dict['data']['yesterday']['low'])
print('风向：',weather_dict['data']['yesterday']['fx'])
print('风力：',weather_dict['data']['yesterday']['fl'][-5:-3])
print('--------------------------')
# 第四步：遍历forecast列表中的五个元素，打印天气信息
for each in weather_dict['data']['forecast']:
    print('日期',each['date'])
    print('天气',each['type'])
    print(each['high'])
    print(each['low'])
    print('风向',each['fengxiang'])
    print('风力：',each['fengli'][-5:-3])
    print('--------------------------')
