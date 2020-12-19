import os
import requests
import re
Base_dir="F:/高中英语听力/results"
dir=""
phone_dir=""
def main():
    global dir,phone_dir
    #路径关系表
    tables={'1':"一",'2':"二",'3':"三"}
    template="http://ting.xiai123.com/src/js/2019rjbyy-gaozhong-d%sc.js"
    for i in ('2','3'):
        #设置电脑目录和手机目录
        dir="第%s册/" % tables[i]
        dir=os.path.join(Base_dir,dir)
        phone_dir="/sdcard/高中英语听力/第%s册/" % tables[i]
        #配置url
        url=template % i
        # print(tables[i])
        #获取资源
        jsons=get_src_json(url,i)
        #下载资源
        for json in jsons:
            download_json(json)

def download_json(json):
    url=json[0]
    filename=get_clear_filename(json[1])
    #电脑路径
    save_path=dir+filename
    #下载资源
    rep=requests.get(url)
    save_response(rep,save_path)
    #手机路径
    phone_save_path=phone_dir+filename
    #上传到手机
    push_to(save_path,phone_save_path)
    print(filename+" 下载完成")

def get_clear_filename(filename):
    filename=filename.strip()
    if filename[0]==".":
        filename=filename[1:]
    return filename
def get_src_json(url,i):
    jsons=[]
    rep=requests.get(url)
    html=rep.text
    pat_str="src {4}: '(http://ting.xiai123.com/mp3/kewen/2019rjbyy-gaozhong-d%sc/\d{2}(.+?mp3))'" % i
    pat=re.compile(pat_str)
    # pat=re.compile("src.+?mp3")
    for src in pat.findall(html):
        if src is not None:
            jsons.append(src)
    return jsons

def save_response(rep,save_dir):
    with open(save_dir,"wb") as f:
        f.write(rep.content)

def push_to(file,dir):
    os.system('adb push "{}" "{}"'.format(file,dir))

if __name__ == '__main__':
    main()