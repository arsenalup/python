# -*- coding: utf-8 -*-
import  os
import random
import subprocess

video_=['avi','mkv','mp4','wmv','jpg']

def rand_walk(root_dir):
    all_videos=[]
    for root,dir,files in os.walk(root_dir):
        for file_ in files :
            if 'xuexi' in root or 'guangtouqiang' in file_:
                continue
            extster=file_.split('.')[-1].lower()
            if extster in video_:
                all_videos.append(os.path.join(root,file_))
    return all_videos

if __name__ == '__main__':
    all_videos=rand_walk('e:\\')
    print all_videos
    for i in range(random.randint(1,5)):
        video=random.choice(all_videos)

    os.startfile(video)