```python 
def download_province_nCov(province):

    #建立文件树
    os.chdir('d://')
    file_root_path = 'd://nCov'
    mkdir(file_root_path)

    #api地址
    api_url = 'https://lab.isaaclin.cn/nCoV/api/area'
    #从api获取数据
    params = {'latest':0,'province':province}
    r = requests.get(api_url,params)

    #数据处理
    require_data = r.json()
    if require_data['success']is True:
        city_data = require_data['results']
        Tmp = []
        i = 0 
        for times in city_data:#某个省份所有时序的所有数据
            #从按时间排序的数据中取出下属市区的数据，并且转化为DataFrame
            creat_time = times['updateTime']
            cities = times.pop('cities')
            cities = pd.DataFrame(cities)

            #因为最开始丁香园并没有统计下属市区的数据故而存在部分数据只有省份的现象
            if cities.empty:
                print(str(creat_time)+province+'is wrong')
                pass
            else:
                cityName = cities.pop('cityName')

                cities.insert(0,column='cityName',value=cityName)
                cities.insert(0,column='provinceName',value='安徽')
                cities.insert(0,column='updateTime',value = timestampMs2Date(creat_time))#把时间戳转化为标准时间

                cities = cities.set_index(['updateTime','provinceName','cityName'])
                Tmp.append(cities)
                i+=1 
        result = Tmp[0].append(Tmp[1:])

        #创建文件保存
        file_path = file_root_path+'//'+province+'.csv'
        if os.path.exists(file_path):
            pass
        else:
            result.to_csv(file_path)
    else:
        print('输入的省份或者直辖市有问题，请确认后重试')
```

## 更改一列的位置

```python
            # 取出要交换的一列
            cityName = cities.pop('cityName')
		   #插入到指定位置
            cities.insert(0,column='cityName',value=cityName)
```
## 设置多个index 

设置多个index之前

![image-20200218221434702](D:\data_of_tf\picture\image-20200218221434702.png)

```Python
cities = cities.set_index(['updateTime','provinceName','cityName'])
```

执行代码之后

![image-20200218221411595](D:\data_of_tf\picture\image-20200218221411595.png)

## 保存文件

使用以下代码以确认目标位置是否存在该文件，存在则

```python
    file_path = file_root_path+'//'+province+'.csv'
    if os.path.exists(file_path):
    	print('这里已经有这个文件啦！')
        pass
    else:
        result.to_csv(file_path)
```
## 时间戳

时间戳修改为标准时间

```python
def timestampMs2Date(timestamp):
    #转换成localtime
    timestamp = int(timestamp/1000)
    time_local=time.localtime(timestamp)
    #转换成时间格式：%Y_%m_%d %H:%M:%S
    dt=time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt 
```

