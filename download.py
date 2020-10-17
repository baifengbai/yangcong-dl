import os
import time


def download(urls,names):
    for i in range(0, len(urls)):
        urls[i] = urls[i].replace('\n', '')
    dic = chuli(urls,names)
    for i in range(0, len(urls)):
        print('\r进度:%d/%d' % (i + 1, len(urls)), end='')
        name = dic[urls[i].split('_')[1].split('.')[0]]
        vbs = '''
        set ws=createobject("wscript.shell")
        ws.run "1.bat",0
        wscript.quit
        '''
        order = 'N_m3u8DL-CLI_v2.7.2.exe ' + urls[i] + ' --saveName "'+str(i)+name+'" --enableDelAfterDone' +'\nexit'
        with open('1.bat', 'w') as f:
            f.write(order)
            f.close()
        with open('1.vbs', 'w') as f:
            f.write(vbs)
            f.close()
        os.system('start 1.vbs')
        time.sleep(3.0)
    time.sleep(1.0)
    print('\n下载完成')


def chuli(urls,names):
    dic = {}
    res = []
    for i in urls:
        i = i.split('_')[1].split('.')
        del i[-1]
        res.append(''.join(i))
    for i in range(0, len(res)):
        dic[res[i]] = names[i]
    return dic