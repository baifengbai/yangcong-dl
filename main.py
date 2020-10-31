import requests
import json
import download


def login(username,pw):
    data = '{"name":"%s","password":"%s"}' % (username,pw)
    header = {
        'Content-Type':'application/json'
    }
    res = requests.post('https://school-api.yangcong345.com/public/login',data=data,headers=header).headers
    return res['authorization']


def get_themesid(authorization):
    global header
    header = {
        'Authorization': authorization
    }
    res1 = requests.get(url1, headers=header).text
    themes_ids,res = [],[]
    for a in range(0, 10):
        try:
            themes_ids.append(json.loads(res1)[a]['sections'][0]['subsections'][0]['themes'][0]['id'])
        except Exception:
            continue
        for b in range(0, 10):
            try:
                themes_ids.append(json.loads(res1)[a]['sections'][b]['subsections'][0]['themes'][0]['id'])
            except Exception:
                continue
            for c in range(0, 10):
                try:
                    themes_ids.append(json.loads(res1)[a]['sections'][b]['subsections'][c]['themes'][0]['id'])
                    themes_ids.append(json.loads(res1)[a]['sections'][b]['subsections'][c]['themes'][1]['id'])
                except Exception:
                    continue
    for id in themes_ids:
        if id not in res:
            res.append(id)
    return res


def get_names(authorization):
    global header
    header = {
        'Authorization': authorization
    }
    res1 = requests.get(url1, headers=header).text
    names, res = [], []
    for a in range(0, 10):
        try:
            names.append(json.loads(res1)[a]['name'])
        except Exception:
            continue
        for b in range(0, 10):
            try:
                names.append(json.loads(res1)[a]['sections'][b]['name'])
            except Exception:
                continue
            for c in range(0, 10):
                try:
                    names.append(json.loads(res1)[a]['sections'][b]['subsections'][c]['name'])
                except Exception:
                    continue
                for d in range(0, 10):
                    try:
                        names.append(json.loads(res1)[a]['sections'][b]['subsections'][c]['themes'][d]['name'])
                    except Exception:
                        continue
    for id in names:
        if id not in res:
            res.append(id)
    return res


def get_m3u8_url(themes_id):
    url2 = 'https://school-api.yangcong345.com/course/course-tree/themes/' + themes_id
    res2 = requests.get(url2, headers=header).text
    m3u8_urls,names = [],[]
    for i in range(0, 10):
        try:
            m3u8_url = json.loads(res2)['topics'][i]['video']['addresses'][0]['url']
            m3u8_urls.append(m3u8_url)
            #print(m3u8_url)
        except Exception:
            continue
        try:
            name = json.loads(res2)['topics'][i]['name']
            names.append(name)
            #print(m3u8_url)
        except Exception:
            continue
    return m3u8_urls,names


def chooce():
    global semester
    subject,publisher = '',''
    subjects = {
        '小学数学':'1',
        '初中数学':'1',
        '高中数学':'1',
        '初中物理':'2',
        '初中化学':'4',
    }
    publishers = {
        '人教版':'1',
        '北师大版':'2',
        '华师大版':'3',
        '湘教版':'4',
        '冀教版':'5',
        '苏科版':'6',
        '鲁教版':'7',
        '沪科版':'8',
        '沪教版':'9',
        '青岛版':'10',
        '浙教版': '11',
        '北京课改版': '12',
        '通用版': '13',
        '鲁科版': '14',
        '粤沪版': '16',
        '教科版': '17',
        '人教A': '18',
        '人教B':'19',
        '湘教旧版':'20',
        '人教新课标A':'21',
        '人教新课标B':'24',
    }
    semesters = {
        '三年级上册':'5',
        '三年级下册':'6',
        '四年级上册':'7',
        '四年级下册':'8',
        '五年级上册':'9',
        '五年级下册':'10',
        '六年级上册':'11',
        '六年级下册':'12',
        '七年级上册':'13',
        '七年级下册':'14',
        '八年级上册':'15',
        '八年级下册':'16',
        '九年级上册':'17',
        '九年级下册':'18',
        '中考一轮':'19',
        '中考二轮':'20',
    }
    for i in range(len(list(subjects.keys()))):
        print(str(i)+'.'+list(subjects.keys())[i]+'  ',end='')
    print('\n')
    while True:
        try:
            choice = int(input('请输入要下载的学科的序号:'))
            subject = subjects[list(subjects.keys())[choice]]
            break
        except Exception or ValueError:
            continue
    for i in range(len(list(publishers.keys()))):print(str(i)+'.'+list(publishers.keys())[i]+'  ',end='\n')
    while True:
        try:
            choice = int(input('请输入版本的序号:'))
            publisher = publishers[list(publishers.keys())[choice]]
            break
        except Exception or ValueError:
            continue
    for i in range(len(list(semesters.keys()))):print(str(i)+'.'+list(semesters.keys())[i]+'  ',end='\n')
    while True:
        try:
            choice = int(input('请输入年级的序号:'))
            semester = int(semesters[list(semesters.keys())[choice]])
            break
        except Exception or ValueError:
            continue
    if semester <= 12:
        stage = '1'
    elif 18 >= semester > 12:
        stage = '2'
    else:
        stage = '3'
    url = 'https://school-api.yangcong345.com/course/chapters-with-section/publisher/%s/semester/%s/subject/%s/stage/%s'%(publisher,semester,subject,stage)
    print(url)
    return url


if __name__ == '__main__':
    url1 = chooce()
    themes_ids = []
    list1 = get_themesid(login('17727171396', 'ABcd1234'))
    [themes_ids.append(i) for i in list1 if i not in themes_ids]
    m3u8_urls, video_names = [], []
    for i in range(0,len(themes_ids)):
        print('\r进度:%d/%d'%(i+1,len(themes_ids)),end='')
        a,b = get_m3u8_url(themes_ids[i])
        m3u8_urls.append(a)
        video_names.append(b)
    print('\n爬取完成')
    m3u8_urls = [i for j in m3u8_urls for i in j]
    video_names = [i for j in video_names for i in j]
    for i in range(0,len(m3u8_urls)):
        print(video_names[i],m3u8_urls[i])
    print('开始下载')
    download.download(m3u8_urls, video_names)

