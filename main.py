from download_lib import install
install()
from re import search
import tkinter
import requests
import os
import urllib.request
import sys
from colorama import Fore
from time import sleep, time
from os import system
system("title " + "Devil is Here - instagram:@0xdevil")
try:
    def banner():
        print(Fore.LIGHTBLUE_EX+'''
          .    .
          |\   |\
       _..;|;__;|;
     ,'   ';` \';`-.
     7;-..     :   )
.--._)|   `;==,|,=='
 `\`@; \_ `<`G," G).
   `\/-;,(  )  .>. )
       < ,-;'-.__.;'
        `\_ `-,__,'
   DV      `-..,;,>
              `;;;;

                ``AutoDownloader v1 By @0xdevil $(web)`` 
        ''')
    def clear():import os;os.system('cls' if os.name=='nt' else 'clear')#instagram : @0xdevil
    def start():     
        clear()
        banner()
        try:
            print()
            input(Fore.LIGHTCYAN_EX+"Press Enter To Start...")
            print(Fore.RED+"Press CTRL+C To Stop !")
            sleep(2)
        except KeyboardInterrupt:
            import signal
            os.kill(os.getpid(), signal.SIGINT)
    start()
    def login():
        global sessionid, userid
        data = {}
        ts = int(time())
        headers = {}#instagram : @0xdevil
        headers['accept']          = '*/*'#instagram : @0xdevil
        headers['user-agent']      = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        headers['x-csrftoken']     = 'if4LWnYUFrwE8x7eGc6Sqe8P8E3MUBP4'#instagram : @0xdevil
        headers['x-requested-with']= 'XMLHttpRequest' #instagram : @0xdevil
        user = input(Fore.YELLOW + "[+] Username:")
        passw = input(Fore.YELLOW + "[+] Password:")
        data['username'] = f'{user}'
        data['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:0:{ts}:{passw}'
        rl = requests.post("https://www.instagram.com/accounts/login/ajax/",
        data=data,
        headers=headers)
        if rl.status_code != 429:
            try:
                sessionid = rl.cookies.get_dict()['sessionid']
                userid = rl.cookies.get_dict()['ds_user_id']
            except:
                input(Fore.RED+"SomeThing Went Wrong in login!")
                exit(1)
        else:
            input(Fore.RED+"You Get Blocked Press Enter")
            exit(1)
    login()
    def clearClip():
        from ctypes import windll
        if windll.user32.OpenClipboard(None):
            windll.user32.EmptyClipboard()
            windll.user32.CloseClipboard()
    def getClip():
        clear()
        try:
            clearClip()
        except:
            pass
        root = tkinter.Tk()
        root.withdraw()
        while True:
            try:
                if 'https://www.instagram.com/p/' in root.clipboard_get():
                    url =  root.clipboard_get()
                    try:
                        url = search(r"https://www.instagram.com/p/(.*?)/.*", str(url)).group(1)
                        url = f"https://www.instagram.com/p/{url}/"
                        return main(url)
                    except:return getClip()  
                elif 'https://www.instagram.com/stories/' in root.clipboard_get():
                    url = root.clipboard_get()
                    try:
                        url_user = search(r'https://www.instagram.com/stories/(.*?)/(.*?)/', str(url))
                        id_story = url_user.group(2)
                        url = f"https://www.instagram.com/{url_user.group(1)}/?__a=1"
                        r = requests.get(url,headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'cookie': f'ig_did=BA986F43-2024-41AB-8C92-0C1D2EE021F4; ig_nrcb=1; mid=YGLS9wALAAFmkgUh9_H2-55YnsOx; shbid=5749; rur=RVA; shbts=1618591091.331925; csrftoken=Is7aXNh5dLawmwrBw9C1z0bhqc4Kx07b; ds_user_id={userid}; sessionid={sessionid}'
        })              
                        ids = r.json()['graphql']['user']['id']
                        user= r.json()['graphql']['user']['username']
                        get_this_story(id_story, ids, user)
                    except:return getClip()

                elif 'https://www.instagram.com/' in root.clipboard_get():
                    url =  root.clipboard_get()
                    try:
                        url = search(r"https://www.instagram.com/(.*?)/.*", str(url)).group(1)
                        url = f"https://www.instagram.com/{url}/?__a=1"
                        r = requests.get(url,headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'cookie': f'ig_did=BA986F43-2024-41AB-8C92-0C1D2EE021F4; ig_nrcb=1; mid=YGLS9wALAAFmkgUh9_H2-55YnsOx; shbid=5749; rur=RVA; shbts=1618591091.331925; csrftoken=Is7aXNh5dLawmwrBw9C1z0bhqc4Kx07b; ds_user_id={userid}; sessionid={sessionid}'
        })              
                        ids = r.json()['graphql']['user']['id']
                        user= r.json()['graphql']['user']['username']
                        return story_grab(ids, user)
                    except:return getClip()
            except:
                pass
        

    def video(r):
        video_url = r.json()['graphql']['shortcode_media']['video_url']
        video_name = r.json()['graphql']['shortcode_media']['id']
        owner_user = r.json()['graphql']['shortcode_media']['owner']['username']
        local_path = os.getcwd() + f'\\{owner_user}'
        if os.path.exists(local_path):
            pass
        else:
            os.mkdir(local_path)
        file_name = local_path + '\\' +str(video_name)+'.mp4'
        if os.path.exists(file_name):
            print(Fore.RED+"video Already Downloaded !")
            pass
        else:
            print(Fore.YELLOW)
            urllib.request.urlretrieve(video_url, file_name, reporthook)
        clearClip()
        print(Fore.GREEN+"[+] Done")
        sleep(3)
        return getClip()
    def reporthook(blocknum, blocksize, totalsize):    
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 1e2 / totalsize
            s = "\r%5.1f%% %*d / %d" % (
                percent, len(str(totalsize)), readsofar, totalsize)
            sys.stderr.write(s)
            if readsofar >= totalsize: 
                sys.stderr.write("\n")
        else:
            sys.stderr.write("read %d\n" % (readsofar,))

    def get_this_story(id_story, id_user, owner):
        url = 'https://www.instagram.com/graphql/query/?query_hash=303a4ae99711322310f25250d988f3b7&variables={"reel_ids":["'+id_user+'"],"tag_names":[],"location_ids":[],"highlight_reel_ids":[],"precomposed_overlay":false,"show_story_viewer_list":true,"story_viewer_fetch_count":50}'
        r = requests.get(url, headers={
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
                'cookie': f'ig_did=BA986F43-2024-41AB-8C92-0C1D2EE021F4; ig_nrcb=1; mid=YGLS9wALAAFmkgUh9_H2-55YnsOx; shbid=5749; rur=RVA; shbts=1618591091.331925; csrftoken=Is7aXNh5dLawmwrBw9C1z0bhqc4Kx07b; ds_user_id={userid}; sessionid={sessionid}'
                })
        _json = r.json()['data']['reels_media'][0]['items']
        for __json in _json:
            if __json['id'] == id_story:
                    vid = __json['is_video']
                    if vid:
                        vid_name= id_story
                        local_path = os.getcwd() + f'\\{owner}'
                        if os.path.exists(local_path):
                                    pass
                        else:
                                os.mkdir(local_path)
                        file_name = local_path + '\\' + str(vid_name) + ".mp4"
                        if os.path.exists(file_name):
                                    print(Fore.RED+"Video Already Downloaded !")
                                    pass
                        else:  
                                for url in __json['video_resources']:
                                    url = url['src']
                                    print(Fore.YELLOW)
                                    urllib.request.urlretrieve(url, file_name, reporthook)
                                    break
                    else:
                        url = __json['display_url']
                        pic_name = __json['id']
                        local_path = os.getcwd() + f'\\{owner}'
                        if os.path.exists(local_path):
                            pass
                        else:
                            os.mkdir(local_path)
                        file_name = local_path + '\\' + str(pic_name) + ".jpg"
                        if os.path.exists(file_name):
                                print(Fore.RED+"Pic Already Downloaded !")
                                pass
                        else:  
                            print(Fore.YELLOW)
                            urllib.request.urlretrieve(url, file_name, reporthook)
        clearClip()
        print(Fore.GREEN+"[+] Done")
        sleep(3)
        return getClip()
    def story_grab(ids , owner):
        def download_all(ids, owner):
                url = 'https://www.instagram.com/graphql/query/?query_hash=303a4ae99711322310f25250d988f3b7&variables={"reel_ids":["'+ids+'"],"tag_names":[],"location_ids":[],"highlight_reel_ids":[],"precomposed_overlay":false,"show_story_viewer_list":true,"story_viewer_fetch_count":50}'
                r = requests.get(url, headers={
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
                'cookie': f'ig_did=BA986F43-2024-41AB-8C92-0C1D2EE021F4; ig_nrcb=1; mid=YGLS9wALAAFmkgUh9_H2-55YnsOx; shbid=5749; rur=RVA; shbts=1618591091.331925; csrftoken=Is7aXNh5dLawmwrBw9C1z0bhqc4Kx07b; ds_user_id={userid}; sessionid={sessionid}'

                })
                _json = r.json()['data']['reels_media'][0]['items']
                for __json in _json:
                    vid = __json['is_video']
                    if vid:
                        vid_name= __json['id']
                        local_path = os.getcwd() + f'\\{owner}'
                        if os.path.exists(local_path):
                                pass
                        else:
                            os.mkdir(local_path)
                        file_name = local_path + '\\' + str(vid_name) + ".mp4"
                        if os.path.exists(file_name):
                                print(Fore.RED+"Video Already Downloaded !")
                                pass
                        else:  
                            for url in __json['video_resources']:
                                url = url['src']
                                print(Fore.YELLOW)
                                urllib.request.urlretrieve(url, file_name, reporthook)
                                break
                    else:
                        url = __json['display_url']
                        pic_name = __json['id']
                        local_path = os.getcwd() + f'\\{owner}'
                        if os.path.exists(local_path):
                                pass
                        else:
                            os.mkdir(local_path)
                        file_name = local_path + '\\' + str(pic_name) + ".jpg"
                        if os.path.exists(file_name):
                                print(Fore.RED+"Pic Already Downloaded !")
                                pass
                        else:  
                            print(Fore.YELLOW)
                            urllib.request.urlretrieve(url, file_name, reporthook)
                
        i = 0
        picnvid = []
        urls = []
        vid_dict = {}
        pic_dict = {}
        url = 'https://www.instagram.com/graphql/query/?query_hash=303a4ae99711322310f25250d988f3b7&variables={"reel_ids":["'+ids+'"],"tag_names":[],"location_ids":[],"highlight_reel_ids":[],"precomposed_overlay":false,"show_story_viewer_list":true,"story_viewer_fetch_count":50}'
        r = requests.get(url, headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'cookie': f'ig_did=BA986F43-2024-41AB-8C92-0C1D2EE021F4; ig_nrcb=1; mid=YGLS9wALAAFmkgUh9_H2-55YnsOx; shbid=5749; rur=RVA; shbts=1618591091.331925; csrftoken=Is7aXNh5dLawmwrBw9C1z0bhqc4Kx07b; ds_user_id={userid}; sessionid={sessionid}'

        })
        _json = r.json()['data']['reels_media'][0]['items']
        print('Do You Want To Download :')
        for __json in _json:
            vid = __json['is_video']
            if vid:
                
                for url in __json['video_resources']:
                    url = url['src']
                    i += 1
                    picnvid.append(i)
                    urls.append(url)
                    vid_dict[i] = url 
                    print(f"{i}'s- Video")
                    break
            else:
                url = __json['display_url']
                i +=1
                picnvid.append(i)
                urls.append(url)
                pic_dict[i] = url
                print(f"{i}'s- Pic")
        print('[0] Download All')
        mod = int(input("Choose:"))
        if mod == 0:
            download_all(ids, owner)
        else:
            for _ in picnvid:
                if mod == _:
                    try:
                                url = vid_dict[mod]
                                _name = __json['id']
                                local_path = os.getcwd() + f'\\{owner}'
                                if os.path.exists(local_path):
                                    pass
                                else:
                                    os.mkdir(local_path)
                                file_name = local_path + '\\' +str(_name)+'.mp4'
                                if os.path.exists(file_name):
                                    print(Fore.RED+"video Already Downloaded !")
                                    pass
                                else:
                                    print(Fore.YELLOW)
                                    urllib.request.urlretrieve(url, file_name, reporthook)
                    except:
                                url = pic_dict[mod]
                                _name = __json['id']
                                local_path = os.getcwd() + f'\\{owner}'
                                if os.path.exists(local_path):
                                    pass
                                else:
                                    os.mkdir(local_path)
                                file_name = local_path + '\\' +str(_name)+'.jpg'
                                if os.path.exists(file_name):
                                    print(Fore.RED+"pic Already Downloaded !")
                                    pass
                                else:
                                    print(Fore.YELLOW)
                                    urllib.request.urlretrieve(url, file_name, reporthook)
        clearClip()
        print(Fore.GREEN+"[+] Done")
        sleep(3)
        return getClip()
    def side_bar(r):
            def download_all(r):
                    side_ = r.json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']
                    owner_user = r.json()['graphql']['shortcode_media']['owner']['username']
                    for side_ in side_:  
                        is_video = side_['node']['is_video']
                        if is_video :    
                            side_url = side_['node']['video_url']
                            side_name = side_['node']['id']
                            local_path = os.getcwd() + f'\\{owner_user}'
                            if os.path.exists(local_path):
                                pass
                            else:
                                os.mkdir(local_path)
                            file_name = local_path + '\\' +str(side_name)+'.mp4'
                            if os.path.exists(file_name):
                                print(Fore.RED+"video Already Downloaded !")
                                pass
                            else:
                                print(Fore.YELLOW)
                                urllib.request.urlretrieve(side_url, file_name, reporthook)
                        else:
                            side_url = side_['node']['display_url']
                            side_name = side_['node']['id']
                            local_path = os.getcwd() + f'\\{owner_user}'
                            if os.path.exists(local_path):
                                pass
                            else:
                                os.mkdir(local_path)
                            file_name = local_path + '\\' +str(side_name)+'.jpg'
                            if os.path.exists(file_name):
                                print(Fore.RED+"pic Already Downloaded !")
                                pass
                            else:
                                print(Fore.YELLOW)
                                urllib.request.urlretrieve(side_url, file_name, reporthook)
            i = 0
            picnvid = []
            vid_dict = {}
            pic_dict = {}
            side_ = r.json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']
            owner_user = r.json()['graphql']['shortcode_media']['owner']['username']
            print('Do You Want To Download :')
            print()
            for side_ in side_:  
                is_video = side_['node']['is_video']
                if is_video :    
                    side_url = side_['node']['video_url']
                    i +=1
                    picnvid.append(i) 
                    vid_dict[i] = side_url 
                    print(f"{i}'s- Video")
                else:
                    side_url = side_['node']['display_url']
                    i +=1
                    picnvid.append(i)
                    pic_dict[i] = side_url
                    print(f"{i}'s- Pic")
            
            
            print('[0] Download All')
            print('[99] Exit')
            mod = int(input('Choose :'))
            if mod == 0:
                    download_all(r)
            elif mod == 99:
                    pass
            else:
                    for _ in picnvid:
                        if mod == _:
                            try:
                                url = vid_dict[mod]
                                side_name = side_['node']['id']
                                local_path = os.getcwd() + f'\\{owner_user}'
                                if os.path.exists(local_path):
                                    pass
                                else:
                                    os.mkdir(local_path)
                                file_name = local_path + '\\' +str(side_name)+'.mp4'
                                if os.path.exists(file_name):
                                    print(Fore.RED+"video Already Downloaded !")
                                    pass
                                else:
                                    print(Fore.YELLOW)
                                    urllib.request.urlretrieve(url, file_name, reporthook)
                            except:
                                url = pic_dict[mod]
                                side_name = side_['node']['id']
                                local_path = os.getcwd() + f'\\{owner_user}'
                                if os.path.exists(local_path):
                                    pass
                                else:
                                    os.mkdir(local_path)
                                file_name = local_path + '\\' +str(side_name)+'.jpg'
                                if os.path.exists(file_name):
                                    print(Fore.RED+"pic Already Downloaded !")
                                    pass
                                else:
                                    print(Fore.YELLOW)
                                    urllib.request.urlretrieve(side_url, file_name, reporthook)
            clearClip()
            print(Fore.GREEN+"[+] Done")
            sleep(3)
            return getClip()
    def pic(r):
        pic_url = r.json()['graphql']['shortcode_media']['display_url']
        pic_name = r.json()['graphql']['shortcode_media']['id']
        owner_user = r.json()['graphql']['shortcode_media']['owner']['username'] 
        local_path = os.getcwd() + f'\\{owner_user}'   
        if os.path.exists(local_path):
            pass
        else:
            os.mkdir(local_path)
        file_name = local_path + '\\' +str(pic_name)+'.jpg'
        if os.path.exists(file_name):
            print(Fore.RED+"pic Already Downloaded !")
            pass
        else:
            print(Fore.YELLOW)
            urllib.request.urlretrieve(pic_url, file_name, reporthook)
        clearClip()
        print(Fore.GREEN+"[+] Done")
        sleep(3)
        return getClip()
    def main(url):
        r = requests.get(url+'?__a=1', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'cookie': f'ig_did=BA986F43-2024-41AB-8C92-0C1D2EE021F4; ig_nrcb=1; mid=YGLS9wALAAFmkgUh9_H2-55YnsOx; shbid=5749; rur=RVA; shbts=1618591091.331925; csrftoken=Is7aXNh5dLawmwrBw9C1z0bhqc4Kx07b; ds_user_id={userid}; sessionid={sessionid}'

        })
        vOpOs = r.json()['graphql']['shortcode_media']['__typename']
        if vOpOs == "GraphVideo":
                video(r)
        elif vOpOs == "GraphSidecar":
                side_bar(r)
        elif vOpOs == "GraphImage":
                pic(r)
        else:
                print("You Copy Something Not Supported")
                return getClip()
    def stop():
        clear()
        try:
            print("Done Stop !")
            input("Press Enter To Start Again !")
            clear()
            return getClip()
        except KeyboardInterrupt:
                return stop()

    if __name__ == '__main__':
            getClip()
except KeyboardInterrupt:
   stop()