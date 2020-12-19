import os

#将列表切割成多份指定长度的列表
def slice_elements(elements, size):
    all_elements = []
    length = len(elements)
    start = 0
    while True:
        end = start + size
        if end > length:
            end = length
        all_elements.append(elements[start:end])
        start += size
        if start >= length:
            break
    return all_elements



#将range()按指定长度切割成多份
def slice_range(start,end,size):
    all_nums=slice_elements(list(range(start,end)),size)
    for nums in all_nums:
        yield nums

def merge_dir(path,src_mp4="p.mp4",src_mp3=".mp3",outPut_mp4=".mp4",limit=1000):
    commands=[]
    gap=" && "
    removes=[]
    for i in range(1,limit+1):
        mp4=os.path.join(path,str(i)+src_mp4)
        mp3=os.path.join(path,str(i)+src_mp3)
        if os.path.exists(mp4) and os.path.exists(mp3):
            final_path=os.path.join(path,str(i)+outPut_mp4)
            if os.path.exists(final_path):
                removes.extend([mp3,mp4])
                continue
            else:
                command=merge(mp3,mp4,final_path)
                commands.append(command)
                removes.extend([mp3,mp4])
        else:
            continue
    command=gap.join(commands)
    os.system(command)
    for remove in removes:
        os.remove(remove)

def merge(mp3_path,mp4_path,final_path):
    return 'ffmpeg -i "{}" -i "{}" -c:v copy -strict experimental "{}"'.format(mp4_path,mp3_path,final_path)
# for nums in slice_indexs(5,100,13):
def rename_dir(path,src_type,out_put_type):
    files=os.listdir(path)
    for file in files:
        name,type=file.split(".")
        if type==src_type:
            src=os.path.join(path,file)
            out_put=os.path.join(path,name+"."+out_put_type)
            os.rename(src,out_put)

def scan_all_files(path):
    listdir=os.listdir(path)
    for subpath in listdir:
        abs_path=os.path.join(path,subpath)
        if os.path.isdir(abs_path):
            for file in scan_all_files(abs_path):
                yield file
        else:
            yield abs_path



#     print(nums)
if __name__ == '__main__':
    # merge_dir("F:/videos/十课精通onenote ")
    for file in scan_all_files("e:/c#"):
        print(file)