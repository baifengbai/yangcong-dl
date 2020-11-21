import requests
import json
import download


def getkey(dic,value_list):
    res = []
    for value in list(value_list):
        res.append(list(dic.keys())[list(dic.values()).index(str(value))])
    return res


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
    global semester, choice_sub
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
        '苏教版': '15',
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
        '中考一轮':'33',
        '中考二轮':'34',
        '必修一':'19',
        '必修二': '20',
        '必修三': '21',
        '必修四': '22',
        '必修五': '23',
        '选修2-1(理科)': '29',
        '选修2-2(理科)': '36',
        '选修1-1(文科)':'41',
        '选修1-2(文科)': '42',
    }
    for i in range(len(list(subjects.keys()))):
        print(str(i)+'.'+list(subjects.keys())[i]+'  ',end='')
    print('\n')
    while True:
        try:
            choice_sub = int(input('请输入要下载的学科的序号:'))
            subject = subjects[list(subjects.keys())[choice_sub]]
            break
        except Exception or ValueError:
            continue
    if list(subjects.keys())[choice_sub] == '小学数学':
        for i in [1,2,5,6,10]:print(str(i)+'.'+list(publishers.keys())[i-1]+'  ',end='')
    elif list(subjects.keys())[choice_sub] == '初中数学':
        for i in range(1,14):print(str(i)+'.'+list(publishers.keys())[i-1]+'  ',end='')
    elif list(subjects.keys())[choice_sub] == '高中数学':
        for i in [1,2,4,15,18,19,20,21,22]:print(str(i)+'.'+list(publishers.keys())[i-1]+'  ',end='')
    while True:
        try:
            choice = int(input('\n请输入版本的序号:'))
            publisher = publishers[list(publishers.keys())[choice]]
            break
        except Exception or ValueError:
            continue
    if list(subjects.keys())[choice_sub] == '小学数学':
        for i in range(1,9): print(str(i) + '.' + list(semesters.keys())[i - 1] + '  ', end='')
    elif list(subjects.keys())[choice_sub] == '初中数学':
        for i in range(9,17): print(str(i) + '.' + list(semesters.keys())[i - 1] + '  ', end='')
    elif list(subjects.keys())[choice_sub] == '高中数学':
        for i in range(17,26): print(str(i) + '.' + list(semesters.keys())[i - 1] + '  ', end='')
    while True:
        try:
            choice = int(input('\n请输入年级的序号:'))
            semester = int(semesters[list(semesters.keys())[choice-1]])
            if list(subjects.keys())[choice_sub] == '小学数学' and choice in range(1, 9):
                break
            elif list(subjects.keys())[choice_sub] == '初中数学' and choice in range(9, 17):
                break
            elif list(subjects.keys())[choice_sub] == '高中数学' and choice in range(17, 26):
                break
            else:
                continue
        except Exception or ValueError:
            continue
    print('正在爬取')
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
    print('用户登录(怕就直接回车吧，我要你账号也没啥用...)')
    username = input('用户名(手机号):')
    pw = input('密码:')
    if username == '' or pw == '':
        username = '17727171396'
        pw = 'ABcd1234'
    url1 = chooce()
    themes_ids = []
    list1 = get_themesid(login(username, pw))
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

