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
            sessionid = rl.cookies.get_dict()['sessionid']
            userid = rl.cookies.get_dict()['ds_user_id']
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
        while True:
            root = tkinter.Tk()
            root.withdraw()
            try:
                if 'https://www.instagram.com/p/' in root.clipboard_get():
                    url =  root.clipboard_get()
                    try:
                        url = search(r"https://www.instagram.com/p/(.*?)/.*", str(url)).group(1)
                        url = f"https://www.instagram.com/p/{url}/"
                    except:pass
                    break
            except:
                pass
        return main(url)

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
            urllib.request.urlretrieve(video_url, file_name, reporthook)
        clearClip()
        print(Fore.GREEN+"[+] Done Download")
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
                                    urllib.request.urlretrieve(side_url, file_name, reporthook)
            clearClip()
            print(Fore.GREEN+"[+] Done Download")
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
            urllib.request.urlretrieve(pic_url, file_name, reporthook)
        clearClip()
        print(Fore.GREEN+"[+] Done Download")
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

#:P 270