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


if __name__ == '__main__':
    urls = ['https://school-api.yangcong345.com/course/chapters-with-section/publisher/16/semester/17/subject/2/stage/2',
            'https://school-api.yangcong345.com/course/chapters-with-section/publisher/16/semester/18/subject/2/stage/2',
            'https://school-api.yangcong345.com/course/chapters-with-section/publisher/1/semester/17/subject/4/stage/2',
            'https://school-api.yangcong345.com/course/chapters-with-section/publisher/1/semester/44/subject/4/stage/2',
            'https://school-api.yangcong345.com/course/chapters-with-section/publisher/1/semester/17/subject/1/stage/2',
            'https://school-api.yangcong345.com/course/chapters-with-section/publisher/1/semester/18/subject/1/stage/2',
            'https://school-api.yangcong345.com/course/chapters-with-section/publisher/1/semester/33/subject/1/stage/2',
            'https://school-api.yangcong345.com/course/chapters-with-section/publisher/1/semester/34/subject/1/stage/2',
            ]
    print('''
    1.九上物理  2.九下物理  3.九上化学  4.中考复习化学
    5.九上数学  6.九下数学  7.中考一轮数学  8.中考二轮数学
    ''')
    choose = int(input('请输入要下载的序号：'))
    global url1
    url1 = urls[choose-1]
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

