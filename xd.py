
import requests, re, json, os, time, random, pytz, urllib.request, uuid
from bs4 import BeautifulSoup as bs
from datetime import datetime
from faker import Faker
from rich import print

Ok, Cp, Fail = 0,0,0

waktu = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%d-%m-%Y %H:%M:%S")

class CONFIG:
	
	def kode(self, a):
		for sleep in range(int(a), 0, -1):
			print(f' (+) Tunggu code verifikasi {sleep}{" "*10}', end='\r')
			time.sleep(1)
	
	@staticmethod
	def DefaultHeaders(Type: str) -> str:
		if Type == 'Post':
			return {
				'host': 'm.facebook.com',
				'content-length': '9444',
				'sec-ch-ua-platform': '"Android"',
				'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-prefers-color-scheme': 'light',
				'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A325M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
				'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
				'accept': '*/*',
				'origin': 'https://m.facebook.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://m.facebook.com/reg/',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
		else:
			return {
				'host': 'm.facebook.com',
                'cache-control': 'max-age=0',
                'dpr': '2.75',
                'viewport-width': '980',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-prefers-color-scheme': 'light',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A325M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
	
	@staticmethod
	def DefaultPayload(req):
		return {
			"__aaid": "0",
            "__user": "0",
            "__a": "1",
            "__req": "6",
            "__hs": re.search('"haste_session":"(.*?)"' , str(req)).group(1),
            "dpr": "1",
            "__ccg": "GOOD",
            "__rev": re.search('rev:(\d+)', str(req)).group(1),
            "__s": "",
            "__hsi": re.search('"hsi":"(\d+)"' , str(req)).group(1),
            "__dyn": "",
            "__csr": "",
            "fb_dtsg": re.search('{"dtsg":{"token":"(.*?)"', str(req)).group(1),
            "jazoest": re.search('"jazoest", "(.*?)"', str(req)).group(1),
            "lsd": re.search('"lsd":"(.*?)"', str(req)).group(1),
		}
	
	@staticmethod
	def DataGraphQL(req, id):
		return {
			'av': id,
			'__aaid': "0",
			'__user': id,
			'__a': "1",
			'__req': "x",
			'__hs': re.search('"haste_session":"(.*?)"', str(req)).group(1),
			'dpr': "3",
			'__ccg': "EXCELLENT",
			'__rev': re.search('"__spin_r":(.*?)', str(req)).group(1),
			'__s': "gj8z5g:6nupeb:1xcz9j",
			'__hsi': re.search(r'"hsi":"(.*?)"',str(req)).group(1),
			'__dyn': "",
			'__csr': "",
			'__comet_req': "15",
			'fb_dtsg': re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1),
			'jazoest': re.search(r'jazoest=(.*?)"',str(req)).group(1),
			'lsd': re.search('"LSD",\\[\\],{"token":"(.*?)"}', str(req)).group(1),
			'__spin_r': re.search('"__spin_r":(.*?)', str(req)).group(1),
			'__spin_b': "trunk",
			'__spin_t': re.search('"__spin_t":(.*?)', str(req)).group(1)
		}

class MAIN:
	 
	def banner(self):
		print(f""" 
   [bold grey37]___               _         ___  ___ 
  / __\ __ ___  __ _| |_ ___  / __\/ __\ 
 / / | '__/ _ \/ _` | __/ _ \/ _\ /__\/\ 
/ /__| | |  __/ (_| | ||  __/ /  / \\/  \\
[bold green]\\____/_|  \\___|\\__,_|\\__\\___\\/   \\_____/ [bold white]Version 0.1""")

	def menu(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.banner()
		print("""
 (01). CREATE FACEBOOK 
 (02). ADD FRIEND OTOMATIS
 (03). CEK AKUN
 (00). KELUAR
		""")
		choice = input(" (+) Choose option: ")
		if choice in ['1', '01']:self.create()
		
	
	def create(self):
		global web_email, total, delay, passwords
		print("""
 (01). TEMP-MAIL.IO
 (02). TEMPMAIL.PLUS
 (03). 10.MINUTE.MAIL
 (04). EMAIL MANUAL
		""")
		web_email = input("  ╰─/ (1/2/3/4) (skip=temp-mail.io): ") or '1'
		passwords = input("  ╰─/ Password (skip=akun123): ") or 'akun123'
		total = int(input('  ╰─/ Mau berapa akun yang di buat (default 5): ') or 5)
		delay = int(input("  ╰─/ Masukkan waktu delay antar requests (default 60 detik): ") or 60)
		print('')
		for i in range(total):
			AccountCreator()
			self.progres(i+1, total, delay)
		time.sleep(1.5)
		self.results()
		
	def progres(self, current, total, delay):
		for sleep in range(int(delay), 0, -1):
			print(f' (+) Progress: {current}/{total} success: [bold green]{Ok}[bold white] failed: [bold red]{Fail}[bold white] check: [bold yellow]{Cp}[bold white] Next: {sleep}s', end='\r')
			time.sleep(1)
			if current == total:
				break
	
	def results(self):
		print(f"""
 [bold white]Final Results
 ╰─/ Success: [bold green]{Ok}[/]
 ╰─/ Failed: [bold red]{Fail}[/]
 ╰─/ Checkpoint: [bold yellow]{Cp}[/]

Hasil disimpan ke Folder Results""")

class AccountCreator:
	def __init__(self):
		self.config = CONFIG()
		self.ses = requests.Session()
		self.data_collection()
		self.create_account()
		
	def data_collection(self):
		self.nama_depan, self.nama_belakang = self.generate_username()
		if web_email == '01' or web_email == '1': self.email = self.get_email_temp_mail()
		elif web_email == '02' or web_email == '2': self.email = self.get_temp_plus()
		elif web_email == '03' or web_email == '3': self.email = self.get_email_10minutemail()
		elif web_email == '04' or web_email == '4':
			print(f" {' ' *65}", end = '\r')
			time.sleep(000.11)
			self.email = input(' (+) email: ')
		else:
			console.print(" [bold yellow]Pilihan email tidak valid, menggunakan temp-mail.io.")
			self.email = self.get_email_temp_mail()
		self.tgl_lahir = self.generate_birthday()
		self.password = passwords
	
	def generate_username(self):
		fake = Faker("id_ID")
		first_name = fake.first_name_female()
		last_name = fake.last_name_female()
		name = f"{first_name} {last_name}"
		return first_name, last_name
	
	def generate_birthday(self):
		year = random.randint(1980, 2003)
		month = random.randint(1, 12)
		day = random.randint(1, 28)
		return str(f'{day:02d}-{month:02d}-{year}')
		
	def get_temp_plus(self):
		nama = self.nama_depan.lower().replace(' ','')
		jam = str(datetime.now().strftime("%X")).replace(':','')
		domain = random.choice(['fexbox.org','fexpost.com','fextemp.com','chitthi.in'])
		email = f'{nama}.{jam}.{str(random.randrange(1000,10000))}@{domain}'
		return email
	
	def get_code_temp_plus(self, email):
		mail = requests.Session()
		headers = {}
		headers.update({'cookie': f'email={email}'})
		response = mail.get(f'https://tempmail.plus/api/mails', headers=headers)
		print(response.json())
		if response.status_code == 200:
			req = response.json()
			mail_list = req.get("mail_list", [])
			if mail_list:
				subject = mail_list[0].get('subject', '')
				kode = re.search(r'(\d+)', subject)
				code = kode.group(1) if kode else 'Kode tidak ditemukan'
				return code
			return 'Mail list kosong'
		return False
	
	def get_email_10minutemail(self):
		mail = requests.Session()
		req = mail.get('https://10minutemail.net/m/?lang=id').text
		self.ses_email = re.search('sessionid="(.*?)"', str(req)).group(1)
		self.tim_email = str(time.time()).replace('.', '')[:13]
		dat = {'new': '1', 'sessionid': self.ses_email, '_': self.tim_email}
		pos = mail.post('https://10minutemail.net/address.api.php', data=dat, allow_redirects=True).json()
		email = pos['mail_get_mail']
		self.cookie_email = '; '.join([f"{x}={y}" for x, y in mail.cookies.get_dict().items()])
		return email
	
	def get_code_10minutemail(self):
		mail = requests.Session()
		dat = {'new':'0','sessionid':self.ses_email,'_':self.tim_email}
		pos = mail.post('https://10minutemail.net/address.api.php',data=dat,cookies={'cookie':self.cookie_email},allow_redirects=True).json()
		print(pos)
		subject = pos.get('mail_list', [])[0].get('subject', '')
		kode = re.search(r'(\d+)', subject).group(1)
		return(kode)
		
	def get_email_temp_mail(self):
		try:
			mail = requests.Session()
			headers = {
				'User-Agent':'Temp%20Mail/30 CFNetwork/1220.1 Darwin/20.3.0',
				'Content-Type':'application/json',
				'Connection-type': 'wifi'
			}
			payload = json.dumps({"min_name_length": 10,"max_name_length": 10})
			response = mail.post('https://api.internal.temp-mail.io/api/v3/email/new', data=payload, headers=headers)
			return response.json()['email']
		except Exception as e: return None
	
	def get_code_temp_mail(self, email):
		mail = requests.Session()
		headers = {
			'User-Agent':'Temp%20Mail/30 CFNetwork/1220.1 Darwin/20.3.0',
			'Content-Type':'application/json',
			'Connection-type': 'wifi'
		}
		response = mail.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages', headers=headers)
		if response.status_code == 200:
			req = response.json()
			if req and isinstance(req, list):
				subject = req[0].get('subject', '')
				kode = re.search(r'(\d+)', subject)
				code = kode.group(1) if kode else 'Kode tidak ditemukan'
				return code
			else:
				return 'Respon tidak valid'
		return None
	
	def create_account(self):
		try:
			response = self.ses.get('https://m.facebook.com/reg/', headers = self.config.DefaultHeaders('Get')).text
			version = re.search('\\["WebBloksVersioningID",\\[\\],{versioningID:"(.*?)"}', response)
			self.versioningID = version.group(1) if version else 'b187aeb6992d725d2f0fee8885c98f6b6f26079006a06093954f6628d1977a9a'
			self.data = self.config.DefaultPayload(response)
			self.headers = self.config.DefaultHeaders('Post')
			self.cok = ';'.join([str(x)+"="+str(y) for x,y in self.ses.cookies.get_dict().items()])
			self.enpas = '#PWD_BROWSER:0:{}:{}'.format(int(time.time()), self.password)
			self.name_signup()
			self.birthday()
			self.gender()
			self.email_signup()
			self.password_reg()
			self.credentials()
			self.setujui_ketentuan()
			self.next_create()
		except Exception as e:
			raise e
			return False
	
	def name_signup(self):
		self.data.update({"params":"{\"server_params\":{\"event_request_id\":\"70ff79f5-b12b-4ecf-b8db-ea0d55619efe\",\"reg_info\":\"{\\\"first_name\\\":null,\\\"last_name\\\":null,\\\"full_name\\\":null,\\\"contactpoint\\\":null,\\\"ar_contactpoint\\\":null,\\\"contactpoint_type\\\":null,\\\"is_using_unified_cp\\\":null,\\\"unified_cp_screen_variant\\\":null,\\\"is_cp_auto_confirmed\\\":false,\\\"is_cp_auto_confirmable\\\":false,\\\"confirmation_code\\\":null,\\\"birthday\\\":null,\\\"did_use_age\\\":null,\\\"gender\\\":null,\\\"use_custom_gender\\\":false,\\\"custom_gender\\\":null,\\\"encrypted_password\\\":null,\\\"username\\\":null,\\\"username_prefill\\\":null,\\\"fb_conf_source\\\":null,\\\"device_id\\\":null,\\\"ig4a_qe_device_id\\\":null,\\\"family_device_id\\\":null,\\\"nta_eligibility_reason\\\":null,\\\"ig_nta_test_group\\\":null,\\\"user_id\\\":null,\\\"safetynet_token\\\":null,\\\"safetynet_response\\\":null,\\\"machine_id\\\":null,\\\"profile_photo\\\":null,\\\"profile_photo_id\\\":null,\\\"profile_photo_upload_id\\\":null,\\\"avatar\\\":null,\\\"email_oauth_token_no_contact_perm\\\":null,\\\"email_oauth_token\\\":null,\\\"email_oauth_tokens\\\":null,\\\"should_skip_two_step_conf\\\":null,\\\"openid_tokens_for_testing\\\":null,\\\"encrypted_msisdn\\\":null,\\\"encrypted_msisdn_for_safetynet\\\":null,\\\"cached_headers_safetynet_info\\\":null,\\\"should_skip_headers_safetynet\\\":null,\\\"headers_last_infra_flow_id\\\":null,\\\"headers_last_infra_flow_id_safetynet\\\":null,\\\"headers_flow_id\\\":null,\\\"was_headers_prefill_available\\\":null,\\\"sso_enabled\\\":null,\\\"existing_accounts\\\":null,\\\"used_ig_birthday\\\":null,\\\"sync_info\\\":null,\\\"create_new_to_app_account\\\":null,\\\"skip_session_info\\\":null,\\\"ck_error\\\":null,\\\"ck_id\\\":null,\\\"ck_nonce\\\":null,\\\"should_save_password\\\":null,\\\"horizon_synced_username\\\":null,\\\"fb_access_token\\\":null,\\\"horizon_synced_profile_pic\\\":null,\\\"is_identity_synced\\\":false,\\\"is_msplit_reg\\\":null,\\\"user_id_of_msplit_creator\\\":null,\\\"dma_data_combination_consent_given\\\":null,\\\"xapp_accounts\\\":null,\\\"fb_device_id\\\":null,\\\"fb_machine_id\\\":null,\\\"ig_device_id\\\":null,\\\"ig_machine_id\\\":null,\\\"should_skip_nta_upsell\\\":null,\\\"big_blue_token\\\":null,\\\"skip_sync_step_nta\\\":null,\\\"caa_reg_flow_source\\\":null,\\\"ig_authorization_token\\\":null,\\\"full_sheet_flow\\\":false,\\\"crypted_user_id\\\":null,\\\"is_caa_perf_enabled\\\":false,\\\"is_preform\\\":true,\\\"ignore_suma_check\\\":false,\\\"ignore_existing_login\\\":false,\\\"ignore_existing_login_from_suma\\\":false,\\\"ignore_existing_login_after_errors\\\":false,\\\"suggested_first_name\\\":null,\\\"suggested_last_name\\\":null,\\\"suggested_full_name\\\":null,\\\"replace_id_sync_variant\\\":null,\\\"is_redirect_from_nta_replace_id_sync_variant\\\":false,\\\"frl_authorization_token\\\":null,\\\"post_form_errors\\\":null,\\\"skip_step_without_errors\\\":false,\\\"existing_account_exact_match_checked\\\":false,\\\"existing_account_fuzzy_match_checked\\\":false,\\\"email_oauth_exists\\\":false,\\\"confirmation_code_send_error\\\":null,\\\"is_too_young\\\":false,\\\"source_account_type\\\":null,\\\"whatsapp_installed_on_client\\\":false,\\\"confirmation_medium\\\":null,\\\"source_credentials_type\\\":null,\\\"source_cuid\\\":null,\\\"source_account_reg_info\\\":null,\\\"soap_creation_source\\\":null,\\\"source_account_type_to_reg_info\\\":null,\\\"registration_flow_id\\\":\\\"\\\",\\\"should_skip_youth_tos\\\":false,\\\"is_youth_regulation_flow_complete\\\":false,\\\"is_on_cold_start\\\":false,\\\"email_prefilled\\\":false,\\\"cp_confirmed_by_auto_conf\\\":false,\\\"auto_conf_info\\\":null,\\\"in_sowa_experiment\\\":false,\\\"youth_regulation_config\\\":null,\\\"conf_allow_back_nav_after_change_cp\\\":null,\\\"conf_bouncing_cliff_screen_type\\\":null,\\\"conf_show_bouncing_cliff\\\":null,\\\"eligible_to_flash_call_in_ig4a\\\":false,\\\"flash_call_permissions_status\\\":null,\\\"attestation_result\\\":null,\\\"request_data_and_challenge_nonce_string\\\":null,\\\"confirmed_cp_and_code\\\":null,\\\"notification_callback_id\\\":null,\\\"reg_suma_state\\\":0,\\\"is_msplit_neutral_choice\\\":false,\\\"msg_previous_cp\\\":null,\\\"ntp_import_source_info\\\":null,\\\"youth_consent_decision_time\\\":null,\\\"reduced_tos_test_group\\\":\\\"control\\\",\\\"should_show_spi_before_conf\\\":true,\\\"google_oauth_account\\\":null,\\\"is_reg_request_from_ig_suma\\\":false,\\\"is_igios_spc_reg\\\":false,\\\"device_emails\\\":null,\\\"is_toa_reg\\\":false,\\\"is_threads_public\\\":false,\\\"spc_import_flow\\\":false,\\\"caa_play_integrity_attestation_result\\\":null,\\\"flash_call_provider\\\":null,\\\"spc_birthday_input\\\":false,\\\"failed_birthday_year_count\\\":null,\\\"user_presented_medium_source\\\":null,\\\"user_opted_out_of_ntp\\\":null,\\\"is_from_registration_reminder\\\":false,\\\"show_youth_reg_in_ig_spc\\\":false,\\\"fb_suma_combined_landing_candidate_variant\\\":\\\"control\\\",\\\"fb_suma_is_high_confidence\\\":null,\\\"screen_visited\\\":[\\\"CAA_REG_WELCOME_SCREEN\\\"],\\\"fb_email_login_upsell_skip_suma_post_tos\\\":false,\\\"fb_suma_is_from_email_login_upsell\\\":false,\\\"fb_suma_login_upsell_skipped_warmup\\\":false,\\\"fb_suma_login_upsell_show_list_cell_link\\\":false}\",\"flow_info\":\"{\\\"flow_name\\\":\\\"new_to_family_fb_default\\\",\\\"flow_type\\\":\\\"ntf\\\"}\",\"current_step\":1,\"INTERNAL__latency_qpl_marker_id\":36707139,\"INTERNAL__latency_qpl_instance_id\":\"22748591700052\",\"device_id\":null,\"family_device_id\":null,\"waterfall_id\":\"5c633b1c-7418-491f-81ad-c26d16b6f427\",\"offline_experiment_group\":null,\"layered_homepage_experiment_group\":null,\"is_platform_login\":0,\"is_from_logged_in_switcher\":0,\"is_from_logged_out\":0,\"access_flow_version\":\"F2_FLOW\",\"INTERNAL_INFRA_THEME\":\"default\"},\"client_input_params\":{\"firstname\":\""+self.nama_depan+"\",\"lastname\":\""+self.nama_belakang+"\",\"lois_settings\":{\"lois_token\":\"\",\"lara_override\":\"\"}}}"})
		self.headers.update({'content-length': str(len(self.data)), 'cookie': self.cok})
		post = self.ses.post(f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.name.async&type=action&__bkv={self.versioningID}', data=self.data, headers = self.headers, cookies={'cookie': self.cok})
	
	def birthday(self):
		self.data.update({"params":"{\"server_params\":{\"reg_info\":\"{\\\"first_name\\\":\\\""+self.nama_depan+"\\\",\\\"last_name\\\":\\\""+self.nama_belakang+"\\\",\\\"full_name\\\":\\\""+self.nama_depan+"\\\",\\\"contactpoint\\\":null,\\\"ar_contactpoint\\\":null,\\\"contactpoint_type\\\":null,\\\"is_using_unified_cp\\\":null,\\\"unified_cp_screen_variant\\\":null,\\\"is_cp_auto_confirmed\\\":false,\\\"is_cp_auto_confirmable\\\":false,\\\"confirmation_code\\\":null,\\\"birthday\\\":null,\\\"did_use_age\\\":false,\\\"gender\\\":null,\\\"use_custom_gender\\\":false,\\\"custom_gender\\\":null,\\\"encrypted_password\\\":null,\\\"username\\\":null,\\\"username_prefill\\\":null,\\\"fb_conf_source\\\":null,\\\"device_id\\\":null,\\\"ig4a_qe_device_id\\\":null,\\\"family_device_id\\\":null,\\\"nta_eligibility_reason\\\":null,\\\"ig_nta_test_group\\\":null,\\\"user_id\\\":null,\\\"safetynet_token\\\":null,\\\"safetynet_response\\\":null,\\\"machine_id\\\":null,\\\"profile_photo\\\":null,\\\"profile_photo_id\\\":null,\\\"profile_photo_upload_id\\\":null,\\\"avatar\\\":null,\\\"email_oauth_token_no_contact_perm\\\":null,\\\"email_oauth_token\\\":null,\\\"email_oauth_tokens\\\":null,\\\"should_skip_two_step_conf\\\":null,\\\"openid_tokens_for_testing\\\":null,\\\"encrypted_msisdn\\\":null,\\\"encrypted_msisdn_for_safetynet\\\":null,\\\"cached_headers_safetynet_info\\\":null,\\\"should_skip_headers_safetynet\\\":null,\\\"headers_last_infra_flow_id\\\":null,\\\"headers_last_infra_flow_id_safetynet\\\":null,\\\"headers_flow_id\\\":null,\\\"was_headers_prefill_available\\\":null,\\\"sso_enabled\\\":null,\\\"existing_accounts\\\":null,\\\"used_ig_birthday\\\":null,\\\"sync_info\\\":null,\\\"create_new_to_app_account\\\":null,\\\"skip_session_info\\\":null,\\\"ck_error\\\":null,\\\"ck_id\\\":null,\\\"ck_nonce\\\":null,\\\"should_save_password\\\":null,\\\"horizon_synced_username\\\":null,\\\"fb_access_token\\\":null,\\\"horizon_synced_profile_pic\\\":null,\\\"is_identity_synced\\\":false,\\\"is_msplit_reg\\\":null,\\\"user_id_of_msplit_creator\\\":null,\\\"dma_data_combination_consent_given\\\":null,\\\"xapp_accounts\\\":null,\\\"fb_device_id\\\":null,\\\"fb_machine_id\\\":null,\\\"ig_device_id\\\":null,\\\"ig_machine_id\\\":null,\\\"should_skip_nta_upsell\\\":null,\\\"big_blue_token\\\":null,\\\"skip_sync_step_nta\\\":null,\\\"caa_reg_flow_source\\\":null,\\\"ig_authorization_token\\\":null,\\\"full_sheet_flow\\\":false,\\\"crypted_user_id\\\":null,\\\"is_caa_perf_enabled\\\":false,\\\"is_preform\\\":true,\\\"ignore_suma_check\\\":false,\\\"ignore_existing_login\\\":false,\\\"ignore_existing_login_from_suma\\\":false,\\\"ignore_existing_login_after_errors\\\":false,\\\"suggested_first_name\\\":null,\\\"suggested_last_name\\\":null,\\\"suggested_full_name\\\":null,\\\"replace_id_sync_variant\\\":null,\\\"is_redirect_from_nta_replace_id_sync_variant\\\":false,\\\"frl_authorization_token\\\":null,\\\"post_form_errors\\\":null,\\\"skip_step_without_errors\\\":false,\\\"existing_account_exact_match_checked\\\":false,\\\"existing_account_fuzzy_match_checked\\\":false,\\\"email_oauth_exists\\\":false,\\\"confirmation_code_send_error\\\":null,\\\"is_too_young\\\":false,\\\"source_account_type\\\":null,\\\"whatsapp_installed_on_client\\\":false,\\\"confirmation_medium\\\":null,\\\"source_credentials_type\\\":null,\\\"source_cuid\\\":null,\\\"source_account_reg_info\\\":null,\\\"soap_creation_source\\\":null,\\\"source_account_type_to_reg_info\\\":null,\\\"registration_flow_id\\\":\\\"\\\",\\\"should_skip_youth_tos\\\":false,\\\"is_youth_regulation_flow_complete\\\":false,\\\"is_on_cold_start\\\":false,\\\"email_prefilled\\\":false,\\\"cp_confirmed_by_auto_conf\\\":false,\\\"auto_conf_info\\\":null,\\\"in_sowa_experiment\\\":false,\\\"youth_regulation_config\\\":null,\\\"conf_allow_back_nav_after_change_cp\\\":null,\\\"conf_bouncing_cliff_screen_type\\\":null,\\\"conf_show_bouncing_cliff\\\":null,\\\"eligible_to_flash_call_in_ig4a\\\":false,\\\"flash_call_permissions_status\\\":null,\\\"attestation_result\\\":null,\\\"request_data_and_challenge_nonce_string\\\":null,\\\"confirmed_cp_and_code\\\":null,\\\"notification_callback_id\\\":null,\\\"reg_suma_state\\\":0,\\\"is_msplit_neutral_choice\\\":false,\\\"msg_previous_cp\\\":null,\\\"ntp_import_source_info\\\":null,\\\"youth_consent_decision_time\\\":null,\\\"reduced_tos_test_group\\\":\\\"control\\\",\\\"should_show_spi_before_conf\\\":true,\\\"google_oauth_account\\\":null,\\\"is_reg_request_from_ig_suma\\\":false,\\\"is_igios_spc_reg\\\":false,\\\"device_emails\\\":null,\\\"is_toa_reg\\\":false,\\\"is_threads_public\\\":false,\\\"spc_import_flow\\\":false,\\\"caa_play_integrity_attestation_result\\\":null,\\\"flash_call_provider\\\":null,\\\"spc_birthday_input\\\":false,\\\"failed_birthday_year_count\\\":null,\\\"user_presented_medium_source\\\":null,\\\"user_opted_out_of_ntp\\\":null,\\\"is_from_registration_reminder\\\":false,\\\"show_youth_reg_in_ig_spc\\\":false,\\\"fb_suma_combined_landing_candidate_variant\\\":\\\"control\\\",\\\"fb_suma_is_high_confidence\\\":null,\\\"screen_visited\\\":[\\\"CAA_REG_WELCOME_SCREEN\\\",\\\"bloks.caa.reg.birthday\\\"],\\\"fb_email_login_upsell_skip_suma_post_tos\\\":false,\\\"fb_suma_is_from_email_login_upsell\\\":false,\\\"fb_suma_login_upsell_skipped_warmup\\\":false,\\\"fb_suma_login_upsell_show_list_cell_link\\\":false}\",\"flow_info\":\"{\\\"flow_name\\\":\\\"new_to_family_fb_default\\\",\\\"flow_type\\\":\\\"ntf\\\"}\",\"current_step\":2,\"INTERNAL__latency_qpl_marker_id\":36707139,\"INTERNAL__latency_qpl_instance_id\":\"22777075200139\",\"device_id\":null,\"family_device_id\":null,\"waterfall_id\":\"5c633b1c-7418-491f-81ad-c26d16b6f427\",\"offline_experiment_group\":null,\"layered_homepage_experiment_group\":null,\"is_platform_login\":0,\"is_from_logged_in_switcher\":0,\"is_from_logged_out\":0,\"access_flow_version\":\"F2_FLOW\",\"INTERNAL_INFRA_THEME\":\"default\"},\"client_input_params\":{\"birthday_timestamp\":"+str(int(time.time()))+",\"should_skip_youth_tos\":0,\"is_youth_regulation_flow_complete\":0,\"lois_settings\":{\"lois_token\":\"\",\"lara_override\":\"\"}}}"})
		cok  = ';'.join([str(x)+"="+str(y) for x,y in self.ses.cookies.get_dict().items()])
		self.headers.update({'content-length': str(len(self.data)), 'cookie': cok})
		post = self.ses.post(f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.birthday.async&type=action&__bkv={self.versioningID}', data=self.data, headers = self.headers, cookies={'cookie': cok})
	
	def gender(self):
		self.data.update({"params":"{\"server_params\":{\"reg_info\":\"{\\\"first_name\\\":\\\""+self.nama_depan+"\\\",\\\"last_name\\\":\\\""+self.nama_belakang+"\\\",\\\"full_name\\\":\\\""+self.nama_depan+"\\\",\\\"contactpoint\\\":null,\\\"ar_contactpoint\\\":null,\\\"contactpoint_type\\\":null,\\\"is_using_unified_cp\\\":null,\\\"unified_cp_screen_variant\\\":null,\\\"is_cp_auto_confirmed\\\":false,\\\"is_cp_auto_confirmable\\\":false,\\\"confirmation_code\\\":null,\\\"birthday\\\":\\\""+self.tgl_lahir+"\\\",\\\"did_use_age\\\":false,\\\"gender\\\":null,\\\"use_custom_gender\\\":false,\\\"custom_gender\\\":null,\\\"encrypted_password\\\":null,\\\"username\\\":null,\\\"username_prefill\\\":null,\\\"fb_conf_source\\\":null,\\\"device_id\\\":null,\\\"ig4a_qe_device_id\\\":null,\\\"family_device_id\\\":null,\\\"nta_eligibility_reason\\\":null,\\\"ig_nta_test_group\\\":null,\\\"user_id\\\":null,\\\"safetynet_token\\\":null,\\\"safetynet_response\\\":null,\\\"machine_id\\\":null,\\\"profile_photo\\\":null,\\\"profile_photo_id\\\":null,\\\"profile_photo_upload_id\\\":null,\\\"avatar\\\":null,\\\"email_oauth_token_no_contact_perm\\\":null,\\\"email_oauth_token\\\":null,\\\"email_oauth_tokens\\\":null,\\\"should_skip_two_step_conf\\\":null,\\\"openid_tokens_for_testing\\\":null,\\\"encrypted_msisdn\\\":null,\\\"encrypted_msisdn_for_safetynet\\\":null,\\\"cached_headers_safetynet_info\\\":null,\\\"should_skip_headers_safetynet\\\":null,\\\"headers_last_infra_flow_id\\\":null,\\\"headers_last_infra_flow_id_safetynet\\\":null,\\\"headers_flow_id\\\":null,\\\"was_headers_prefill_available\\\":null,\\\"sso_enabled\\\":null,\\\"existing_accounts\\\":null,\\\"used_ig_birthday\\\":null,\\\"sync_info\\\":null,\\\"create_new_to_app_account\\\":null,\\\"skip_session_info\\\":null,\\\"ck_error\\\":null,\\\"ck_id\\\":null,\\\"ck_nonce\\\":null,\\\"should_save_password\\\":null,\\\"horizon_synced_username\\\":null,\\\"fb_access_token\\\":null,\\\"horizon_synced_profile_pic\\\":null,\\\"is_identity_synced\\\":false,\\\"is_msplit_reg\\\":null,\\\"user_id_of_msplit_creator\\\":null,\\\"dma_data_combination_consent_given\\\":null,\\\"xapp_accounts\\\":null,\\\"fb_device_id\\\":null,\\\"fb_machine_id\\\":null,\\\"ig_device_id\\\":null,\\\"ig_machine_id\\\":null,\\\"should_skip_nta_upsell\\\":null,\\\"big_blue_token\\\":null,\\\"skip_sync_step_nta\\\":null,\\\"caa_reg_flow_source\\\":null,\\\"ig_authorization_token\\\":null,\\\"full_sheet_flow\\\":false,\\\"crypted_user_id\\\":null,\\\"is_caa_perf_enabled\\\":false,\\\"is_preform\\\":true,\\\"ignore_suma_check\\\":false,\\\"ignore_existing_login\\\":false,\\\"ignore_existing_login_from_suma\\\":false,\\\"ignore_existing_login_after_errors\\\":false,\\\"suggested_first_name\\\":null,\\\"suggested_last_name\\\":null,\\\"suggested_full_name\\\":null,\\\"replace_id_sync_variant\\\":null,\\\"is_redirect_from_nta_replace_id_sync_variant\\\":false,\\\"frl_authorization_token\\\":null,\\\"post_form_errors\\\":null,\\\"skip_step_without_errors\\\":false,\\\"existing_account_exact_match_checked\\\":false,\\\"existing_account_fuzzy_match_checked\\\":false,\\\"email_oauth_exists\\\":false,\\\"confirmation_code_send_error\\\":null,\\\"is_too_young\\\":false,\\\"source_account_type\\\":null,\\\"whatsapp_installed_on_client\\\":false,\\\"confirmation_medium\\\":null,\\\"source_credentials_type\\\":null,\\\"source_cuid\\\":null,\\\"source_account_reg_info\\\":null,\\\"soap_creation_source\\\":null,\\\"source_account_type_to_reg_info\\\":null,\\\"registration_flow_id\\\":\\\"\\\",\\\"should_skip_youth_tos\\\":false,\\\"is_youth_regulation_flow_complete\\\":false,\\\"is_on_cold_start\\\":false,\\\"email_prefilled\\\":false,\\\"cp_confirmed_by_auto_conf\\\":false,\\\"auto_conf_info\\\":null,\\\"in_sowa_experiment\\\":false,\\\"youth_regulation_config\\\":null,\\\"conf_allow_back_nav_after_change_cp\\\":null,\\\"conf_bouncing_cliff_screen_type\\\":null,\\\"conf_show_bouncing_cliff\\\":null,\\\"eligible_to_flash_call_in_ig4a\\\":false,\\\"flash_call_permissions_status\\\":null,\\\"attestation_result\\\":null,\\\"request_data_and_challenge_nonce_string\\\":null,\\\"confirmed_cp_and_code\\\":null,\\\"notification_callback_id\\\":null,\\\"reg_suma_state\\\":0,\\\"is_msplit_neutral_choice\\\":false,\\\"msg_previous_cp\\\":null,\\\"ntp_import_source_info\\\":null,\\\"youth_consent_decision_time\\\":null,\\\"reduced_tos_test_group\\\":\\\"control\\\",\\\"should_show_spi_before_conf\\\":true,\\\"google_oauth_account\\\":null,\\\"is_reg_request_from_ig_suma\\\":false,\\\"is_igios_spc_reg\\\":false,\\\"device_emails\\\":null,\\\"is_toa_reg\\\":false,\\\"is_threads_public\\\":false,\\\"spc_import_flow\\\":false,\\\"caa_play_integrity_attestation_result\\\":null,\\\"flash_call_provider\\\":null,\\\"spc_birthday_input\\\":false,\\\"failed_birthday_year_count\\\":null,\\\"user_presented_medium_source\\\":null,\\\"user_opted_out_of_ntp\\\":null,\\\"is_from_registration_reminder\\\":false,\\\"show_youth_reg_in_ig_spc\\\":false,\\\"fb_suma_combined_landing_candidate_variant\\\":\\\"control\\\",\\\"fb_suma_is_high_confidence\\\":null,\\\"screen_visited\\\":[\\\"CAA_REG_WELCOME_SCREEN\\\",\\\"bloks.caa.reg.birthday\\\"],\\\"fb_email_login_upsell_skip_suma_post_tos\\\":false,\\\"fb_suma_is_from_email_login_upsell\\\":false,\\\"fb_suma_login_upsell_skipped_warmup\\\":false,\\\"fb_suma_login_upsell_show_list_cell_link\\\":false}\",\"flow_info\":\"{\\\"flow_name\\\":\\\"new_to_family_fb_default\\\",\\\"flow_type\\\":\\\"ntf\\\"}\",\"current_step\":3,\"INTERNAL__latency_qpl_marker_id\":36707139,\"INTERNAL__latency_qpl_instance_id\":\"22812938400120\",\"device_id\":null,\"family_device_id\":null,\"waterfall_id\":\"5c633b1c-7418-491f-81ad-c26d16b6f427\",\"offline_experiment_group\":null,\"layered_homepage_experiment_group\":null,\"is_platform_login\":0,\"is_from_logged_in_switcher\":0,\"is_from_logged_out\":0,\"access_flow_version\":\"F2_FLOW\",\"INTERNAL_INFRA_THEME\":\"default\"},\"client_input_params\":{\"gender\":1,\"pronoun\":0,\"custom_gender\":\"\",\"device_phone_numbers\":[],\"lois_settings\":{\"lois_token\":\"\",\"lara_override\":\"\"}}}"})
		cok  = ';'.join([str(x)+"="+str(y) for x,y in self.ses.cookies.get_dict().items()])
		self.headers.update({'content-length': str(len(self.data)), 'cookie': cok})
		post = self.ses.post(f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.gender.async&type=action&__bkv={self.versioningID}', data=self.data, headers = self.headers, cookies={'cookie': cok})
	
	def email_signup(self):
		self.data.update({"params":"{\"server_params\":{\"event_request_id\":\"6b00699c-c2e0-4a88-b264-efa7bf033133\",\"cp_funnel\":0,\"cp_source\":0,\"text_input_id\":\"22826788100065\",\"reg_info\":\"{\\\"first_name\\\":\\\""+self.nama_depan+"\\\",\\\"last_name\\\":\\\""+self.nama_belakang+"\\\",\\\"full_name\\\":\\\""+self.nama_depan+"\\\",\\\"contactpoint\\\":null,\\\"ar_contactpoint\\\":null,\\\"contactpoint_type\\\":null,\\\"is_using_unified_cp\\\":null,\\\"unified_cp_screen_variant\\\":null,\\\"is_cp_auto_confirmed\\\":false,\\\"is_cp_auto_confirmable\\\":false,\\\"confirmation_code\\\":null,\\\"birthday\\\":\\\""+self.tgl_lahir+"\\\",\\\"did_use_age\\\":false,\\\"gender\\\":1,\\\"use_custom_gender\\\":false,\\\"custom_gender\\\":null,\\\"encrypted_password\\\":null,\\\"username\\\":null,\\\"username_prefill\\\":null,\\\"fb_conf_source\\\":null,\\\"device_id\\\":null,\\\"ig4a_qe_device_id\\\":null,\\\"family_device_id\\\":null,\\\"nta_eligibility_reason\\\":null,\\\"ig_nta_test_group\\\":null,\\\"user_id\\\":null,\\\"safetynet_token\\\":null,\\\"safetynet_response\\\":null,\\\"machine_id\\\":null,\\\"profile_photo\\\":null,\\\"profile_photo_id\\\":null,\\\"profile_photo_upload_id\\\":null,\\\"avatar\\\":null,\\\"email_oauth_token_no_contact_perm\\\":null,\\\"email_oauth_token\\\":null,\\\"email_oauth_tokens\\\":null,\\\"should_skip_two_step_conf\\\":null,\\\"openid_tokens_for_testing\\\":null,\\\"encrypted_msisdn\\\":null,\\\"encrypted_msisdn_for_safetynet\\\":null,\\\"cached_headers_safetynet_info\\\":null,\\\"should_skip_headers_safetynet\\\":null,\\\"headers_last_infra_flow_id\\\":null,\\\"headers_last_infra_flow_id_safetynet\\\":null,\\\"headers_flow_id\\\":null,\\\"was_headers_prefill_available\\\":null,\\\"sso_enabled\\\":null,\\\"existing_accounts\\\":null,\\\"used_ig_birthday\\\":null,\\\"sync_info\\\":null,\\\"create_new_to_app_account\\\":null,\\\"skip_session_info\\\":null,\\\"ck_error\\\":null,\\\"ck_id\\\":null,\\\"ck_nonce\\\":null,\\\"should_save_password\\\":null,\\\"horizon_synced_username\\\":null,\\\"fb_access_token\\\":null,\\\"horizon_synced_profile_pic\\\":null,\\\"is_identity_synced\\\":false,\\\"is_msplit_reg\\\":null,\\\"user_id_of_msplit_creator\\\":null,\\\"dma_data_combination_consent_given\\\":null,\\\"xapp_accounts\\\":null,\\\"fb_device_id\\\":null,\\\"fb_machine_id\\\":null,\\\"ig_device_id\\\":null,\\\"ig_machine_id\\\":null,\\\"should_skip_nta_upsell\\\":null,\\\"big_blue_token\\\":null,\\\"skip_sync_step_nta\\\":null,\\\"caa_reg_flow_source\\\":null,\\\"ig_authorization_token\\\":null,\\\"full_sheet_flow\\\":false,\\\"crypted_user_id\\\":null,\\\"is_caa_perf_enabled\\\":false,\\\"is_preform\\\":true,\\\"ignore_suma_check\\\":false,\\\"ignore_existing_login\\\":false,\\\"ignore_existing_login_from_suma\\\":false,\\\"ignore_existing_login_after_errors\\\":false,\\\"suggested_first_name\\\":null,\\\"suggested_last_name\\\":null,\\\"suggested_full_name\\\":null,\\\"replace_id_sync_variant\\\":null,\\\"is_redirect_from_nta_replace_id_sync_variant\\\":false,\\\"frl_authorization_token\\\":null,\\\"post_form_errors\\\":null,\\\"skip_step_without_errors\\\":false,\\\"existing_account_exact_match_checked\\\":false,\\\"existing_account_fuzzy_match_checked\\\":false,\\\"email_oauth_exists\\\":false,\\\"confirmation_code_send_error\\\":null,\\\"is_too_young\\\":false,\\\"source_account_type\\\":null,\\\"whatsapp_installed_on_client\\\":false,\\\"confirmation_medium\\\":null,\\\"source_credentials_type\\\":null,\\\"source_cuid\\\":null,\\\"source_account_reg_info\\\":null,\\\"soap_creation_source\\\":null,\\\"source_account_type_to_reg_info\\\":null,\\\"registration_flow_id\\\":\\\"\\\",\\\"should_skip_youth_tos\\\":false,\\\"is_youth_regulation_flow_complete\\\":false,\\\"is_on_cold_start\\\":false,\\\"email_prefilled\\\":false,\\\"cp_confirmed_by_auto_conf\\\":false,\\\"auto_conf_info\\\":null,\\\"in_sowa_experiment\\\":false,\\\"youth_regulation_config\\\":null,\\\"conf_allow_back_nav_after_change_cp\\\":null,\\\"conf_bouncing_cliff_screen_type\\\":null,\\\"conf_show_bouncing_cliff\\\":null,\\\"eligible_to_flash_call_in_ig4a\\\":false,\\\"flash_call_permissions_status\\\":null,\\\"attestation_result\\\":null,\\\"request_data_and_challenge_nonce_string\\\":null,\\\"confirmed_cp_and_code\\\":null,\\\"notification_callback_id\\\":null,\\\"reg_suma_state\\\":0,\\\"is_msplit_neutral_choice\\\":false,\\\"msg_previous_cp\\\":null,\\\"ntp_import_source_info\\\":null,\\\"youth_consent_decision_time\\\":null,\\\"reduced_tos_test_group\\\":\\\"control\\\",\\\"should_show_spi_before_conf\\\":true,\\\"google_oauth_account\\\":null,\\\"is_reg_request_from_ig_suma\\\":false,\\\"is_igios_spc_reg\\\":false,\\\"device_emails\\\":null,\\\"is_toa_reg\\\":false,\\\"is_threads_public\\\":false,\\\"spc_import_flow\\\":false,\\\"caa_play_integrity_attestation_result\\\":null,\\\"flash_call_provider\\\":null,\\\"spc_birthday_input\\\":false,\\\"failed_birthday_year_count\\\":null,\\\"user_presented_medium_source\\\":null,\\\"user_opted_out_of_ntp\\\":null,\\\"is_from_registration_reminder\\\":false,\\\"show_youth_reg_in_ig_spc\\\":false,\\\"fb_suma_combined_landing_candidate_variant\\\":\\\"control\\\",\\\"fb_suma_is_high_confidence\\\":null,\\\"screen_visited\\\":[\\\"CAA_REG_WELCOME_SCREEN\\\",\\\"bloks.caa.reg.birthday\\\",\\\"CAA_REG_CONTACT_POINT_PHONE\\\",\\\"CAA_REG_CONTACT_POINT_EMAIL\\\"],\\\"fb_email_login_upsell_skip_suma_post_tos\\\":false,\\\"fb_suma_is_from_email_login_upsell\\\":false,\\\"fb_suma_login_upsell_skipped_warmup\\\":false,\\\"fb_suma_login_upsell_show_list_cell_link\\\":false}\",\"flow_info\":\"{\\\"flow_name\\\":\\\"new_to_family_fb_default\\\",\\\"flow_type\\\":\\\"ntf\\\"}\",\"current_step\":4,\"INTERNAL__latency_qpl_marker_id\":36707139,\"INTERNAL__latency_qpl_instance_id\":\"22826788100102\",\"device_id\":null,\"family_device_id\":null,\"waterfall_id\":\"5c633b1c-7418-491f-81ad-c26d16b6f427\",\"offline_experiment_group\":null,\"layered_homepage_experiment_group\":null,\"is_platform_login\":0,\"is_from_logged_in_switcher\":0,\"is_from_logged_out\":0,\"access_flow_version\":\"F2_FLOW\",\"INTERNAL_INFRA_THEME\":\"default\"},\"client_input_params\":{\"device_id\":\"\",\"family_device_id\":\"\",\"email\":\""+self.email+"\",\"email_prefilled\":0,\"accounts_list\":[],\"fb_ig_device_id\":[],\"confirmed_cp_and_code\":{},\"is_from_device_emails\":0,\"msg_previous_cp\":\"\",\"switch_cp_first_time_loading\":1,\"switch_cp_have_seen_suma\":0,\"lois_settings\":{\"lois_token\":\"\",\"lara_override\":\"\"}}}"})
		cok  = ';'.join([str(x)+"="+str(y) for x,y in self.ses.cookies.get_dict().items()])
		self.headers.update({'content-length': str(len(self.data)), 'cookie': cok})
		post = self.ses.post(f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.async.contactpoint_email.async&type=action&__bkv={self.versioningID}', data=self.data, headers = self.headers, cookies={'cookie': cok})
	
	def password_reg(self):
		self.data.update({"params":"{\"server_params\":{\"event_request_id\":\"5e7ab4f5-1e85-4478-9dbf-4273340d82c3\",\"reg_info\":\"{\\\"first_name\\\":\\\""+self.nama_depan+"\\\",\\\"last_name\\\":\\\""+self.nama_belakang+"\\\",\\\"full_name\\\":\\\""+self.nama_depan+"\\\",\\\"contactpoint\\\":\\\""+self.email+"\\\",\\\"ar_contactpoint\\\":null,\\\"contactpoint_type\\\":\\\"email\\\",\\\"is_using_unified_cp\\\":false,\\\"unified_cp_screen_variant\\\":null,\\\"is_cp_auto_confirmed\\\":false,\\\"is_cp_auto_confirmable\\\":false,\\\"confirmation_code\\\":null,\\\"birthday\\\":\\\""+self.tgl_lahir+"\\\",\\\"did_use_age\\\":false,\\\"gender\\\":1,\\\"use_custom_gender\\\":false,\\\"custom_gender\\\":null,\\\"encrypted_password\\\":null,\\\"username\\\":null,\\\"username_prefill\\\":null,\\\"fb_conf_source\\\":null,\\\"device_id\\\":null,\\\"ig4a_qe_device_id\\\":null,\\\"family_device_id\\\":null,\\\"nta_eligibility_reason\\\":null,\\\"ig_nta_test_group\\\":null,\\\"user_id\\\":null,\\\"safetynet_token\\\":null,\\\"safetynet_response\\\":null,\\\"machine_id\\\":null,\\\"profile_photo\\\":null,\\\"profile_photo_id\\\":null,\\\"profile_photo_upload_id\\\":null,\\\"avatar\\\":null,\\\"email_oauth_token_no_contact_perm\\\":null,\\\"email_oauth_token\\\":null,\\\"email_oauth_tokens\\\":null,\\\"should_skip_two_step_conf\\\":null,\\\"openid_tokens_for_testing\\\":null,\\\"encrypted_msisdn\\\":null,\\\"encrypted_msisdn_for_safetynet\\\":null,\\\"cached_headers_safetynet_info\\\":null,\\\"should_skip_headers_safetynet\\\":null,\\\"headers_last_infra_flow_id\\\":null,\\\"headers_last_infra_flow_id_safetynet\\\":null,\\\"headers_flow_id\\\":null,\\\"was_headers_prefill_available\\\":null,\\\"sso_enabled\\\":null,\\\"existing_accounts\\\":null,\\\"used_ig_birthday\\\":null,\\\"sync_info\\\":null,\\\"create_new_to_app_account\\\":null,\\\"skip_session_info\\\":null,\\\"ck_error\\\":null,\\\"ck_id\\\":null,\\\"ck_nonce\\\":null,\\\"should_save_password\\\":null,\\\"horizon_synced_username\\\":null,\\\"fb_access_token\\\":null,\\\"horizon_synced_profile_pic\\\":null,\\\"is_identity_synced\\\":false,\\\"is_msplit_reg\\\":null,\\\"user_id_of_msplit_creator\\\":null,\\\"dma_data_combination_consent_given\\\":null,\\\"xapp_accounts\\\":null,\\\"fb_device_id\\\":null,\\\"fb_machine_id\\\":null,\\\"ig_device_id\\\":null,\\\"ig_machine_id\\\":null,\\\"should_skip_nta_upsell\\\":null,\\\"big_blue_token\\\":null,\\\"skip_sync_step_nta\\\":null,\\\"caa_reg_flow_source\\\":null,\\\"ig_authorization_token\\\":null,\\\"full_sheet_flow\\\":false,\\\"crypted_user_id\\\":null,\\\"is_caa_perf_enabled\\\":false,\\\"is_preform\\\":true,\\\"ignore_suma_check\\\":false,\\\"ignore_existing_login\\\":false,\\\"ignore_existing_login_from_suma\\\":false,\\\"ignore_existing_login_after_errors\\\":false,\\\"suggested_first_name\\\":null,\\\"suggested_last_name\\\":null,\\\"suggested_full_name\\\":null,\\\"replace_id_sync_variant\\\":null,\\\"is_redirect_from_nta_replace_id_sync_variant\\\":false,\\\"frl_authorization_token\\\":null,\\\"post_form_errors\\\":null,\\\"skip_step_without_errors\\\":false,\\\"existing_account_exact_match_checked\\\":false,\\\"existing_account_fuzzy_match_checked\\\":false,\\\"email_oauth_exists\\\":false,\\\"confirmation_code_send_error\\\":null,\\\"is_too_young\\\":false,\\\"source_account_type\\\":null,\\\"whatsapp_installed_on_client\\\":false,\\\"confirmation_medium\\\":null,\\\"source_credentials_type\\\":null,\\\"source_cuid\\\":null,\\\"source_account_reg_info\\\":null,\\\"soap_creation_source\\\":null,\\\"source_account_type_to_reg_info\\\":null,\\\"registration_flow_id\\\":\\\"\\\",\\\"should_skip_youth_tos\\\":false,\\\"is_youth_regulation_flow_complete\\\":false,\\\"is_on_cold_start\\\":false,\\\"email_prefilled\\\":false,\\\"cp_confirmed_by_auto_conf\\\":false,\\\"auto_conf_info\\\":null,\\\"in_sowa_experiment\\\":false,\\\"youth_regulation_config\\\":null,\\\"conf_allow_back_nav_after_change_cp\\\":null,\\\"conf_bouncing_cliff_screen_type\\\":null,\\\"conf_show_bouncing_cliff\\\":null,\\\"eligible_to_flash_call_in_ig4a\\\":false,\\\"flash_call_permissions_status\\\":null,\\\"attestation_result\\\":null,\\\"request_data_and_challenge_nonce_string\\\":null,\\\"confirmed_cp_and_code\\\":null,\\\"notification_callback_id\\\":null,\\\"reg_suma_state\\\":0,\\\"is_msplit_neutral_choice\\\":false,\\\"msg_previous_cp\\\":null,\\\"ntp_import_source_info\\\":null,\\\"youth_consent_decision_time\\\":null,\\\"reduced_tos_test_group\\\":\\\"control\\\",\\\"should_show_spi_before_conf\\\":true,\\\"google_oauth_account\\\":null,\\\"is_reg_request_from_ig_suma\\\":false,\\\"is_igios_spc_reg\\\":false,\\\"device_emails\\\":null,\\\"is_toa_reg\\\":false,\\\"is_threads_public\\\":false,\\\"spc_import_flow\\\":false,\\\"caa_play_integrity_attestation_result\\\":null,\\\"flash_call_provider\\\":null,\\\"spc_birthday_input\\\":false,\\\"failed_birthday_year_count\\\":null,\\\"user_presented_medium_source\\\":null,\\\"user_opted_out_of_ntp\\\":null,\\\"is_from_registration_reminder\\\":false,\\\"show_youth_reg_in_ig_spc\\\":false,\\\"fb_suma_combined_landing_candidate_variant\\\":\\\"control\\\",\\\"fb_suma_is_high_confidence\\\":null,\\\"screen_visited\\\":[\\\"CAA_REG_WELCOME_SCREEN\\\",\\\"bloks.caa.reg.birthday\\\",\\\"CAA_REG_CONTACT_POINT_PHONE\\\",\\\"CAA_REG_CONTACT_POINT_EMAIL\\\",\\\"CAA_REG_PASSWORD\\\"],\\\"fb_email_login_upsell_skip_suma_post_tos\\\":false,\\\"fb_suma_is_from_email_login_upsell\\\":false,\\\"fb_suma_login_upsell_skipped_warmup\\\":false,\\\"fb_suma_login_upsell_show_list_cell_link\\\":false}\",\"flow_info\":\"{\\\"flow_name\\\":\\\"new_to_family_fb_default\\\",\\\"flow_type\\\":\\\"ntf\\\"}\",\"current_step\":5,\"INTERNAL__latency_qpl_marker_id\":36707139,\"INTERNAL__latency_qpl_instance_id\":\"22836411700211\",\"device_id\":null,\"family_device_id\":null,\"waterfall_id\":\"5c633b1c-7418-491f-81ad-c26d16b6f427\",\"offline_experiment_group\":null,\"layered_homepage_experiment_group\":null,\"is_platform_login\":0,\"is_from_logged_in_switcher\":0,\"is_from_logged_out\":0,\"access_flow_version\":\"F2_FLOW\",\"INTERNAL_INFRA_THEME\":\"default\"},\"client_input_params\":{\"machine_id\":\"\",\"encrypted_password\":\""+self.enpas+"\",\"safetynet_token\":\"\",\"safetynet_response\":\"\",\"email_oauth_token_map\":{},\"whatsapp_installed_on_client\":0,\"encrypted_msisdn_for_safetynet\":\"\",\"headers_last_infra_flow_id_safetynet\":\"\",\"fb_ig_device_id\":[],\"caa_play_integrity_attestation_result\":\"\",\"lois_settings\":{\"lois_token\":\"\",\"lara_override\":\"\"}}}"})
		cok  = ';'.join([str(x)+"="+str(y) for x,y in self.ses.cookies.get_dict().items()])
		self.headers.update({'content-length': str(len(self.data)), 'cookie': cok})
		post = self.ses.post(f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.save-credentials&type=app&__bkv={self.versioningID}', data=self.data,headers = self.headers, cookies={'cookie': cok})
	
	def credentials(self):
		self.data.update({"params":"{\"server_params\":{\"waterfall_id\":\"5c633b1c-7418-491f-81ad-c26d16b6f427\",\"is_platform_login\":0,\"is_from_logged_out\":0,\"access_flow_version\":\"F2_FLOW\",\"reg_info\":\"{\\\"first_name\\\":\\\""+self.nama_depan+"\\\",\\\"last_name\\\":\\\""+self.nama_belakang+"\\\",\\\"full_name\\\":\\\""+self.nama_depan+"\\\",\\\"contactpoint\\\":\\\""+self.email+"\\\",\\\"ar_contactpoint\\\":null,\\\"contactpoint_type\\\":\\\"email\\\",\\\"is_using_unified_cp\\\":false,\\\"unified_cp_screen_variant\\\":null,\\\"is_cp_auto_confirmed\\\":false,\\\"is_cp_auto_confirmable\\\":false,\\\"confirmation_code\\\":null,\\\"birthday\\\":\\\""+self.tgl_lahir+"\\\",\\\"did_use_age\\\":false,\\\"gender\\\":1,\\\"use_custom_gender\\\":false,\\\"custom_gender\\\":null,\\\"encrypted_password\\\":\\\""+self.password+"\\\",\\\"username\\\":null,\\\"username_prefill\\\":null,\\\"fb_conf_source\\\":null,\\\"device_id\\\":null,\\\"ig4a_qe_device_id\\\":null,\\\"family_device_id\\\":null,\\\"nta_eligibility_reason\\\":null,\\\"ig_nta_test_group\\\":null,\\\"user_id\\\":null,\\\"safetynet_token\\\":null,\\\"safetynet_response\\\":null,\\\"machine_id\\\":null,\\\"profile_photo\\\":null,\\\"profile_photo_id\\\":null,\\\"profile_photo_upload_id\\\":null,\\\"avatar\\\":null,\\\"email_oauth_token_no_contact_perm\\\":null,\\\"email_oauth_token\\\":null,\\\"email_oauth_tokens\\\":[],\\\"should_skip_two_step_conf\\\":null,\\\"openid_tokens_for_testing\\\":null,\\\"encrypted_msisdn\\\":null,\\\"encrypted_msisdn_for_safetynet\\\":null,\\\"cached_headers_safetynet_info\\\":null,\\\"should_skip_headers_safetynet\\\":null,\\\"headers_last_infra_flow_id\\\":null,\\\"headers_last_infra_flow_id_safetynet\\\":null,\\\"headers_flow_id\\\":null,\\\"was_headers_prefill_available\\\":null,\\\"sso_enabled\\\":null,\\\"existing_accounts\\\":null,\\\"used_ig_birthday\\\":null,\\\"sync_info\\\":null,\\\"create_new_to_app_account\\\":null,\\\"skip_session_info\\\":null,\\\"ck_error\\\":null,\\\"ck_id\\\":null,\\\"ck_nonce\\\":null,\\\"should_save_password\\\":null,\\\"horizon_synced_username\\\":null,\\\"fb_access_token\\\":null,\\\"horizon_synced_profile_pic\\\":null,\\\"is_identity_synced\\\":false,\\\"is_msplit_reg\\\":null,\\\"user_id_of_msplit_creator\\\":null,\\\"dma_data_combination_consent_given\\\":null,\\\"xapp_accounts\\\":null,\\\"fb_device_id\\\":null,\\\"fb_machine_id\\\":null,\\\"ig_device_id\\\":null,\\\"ig_machine_id\\\":null,\\\"should_skip_nta_upsell\\\":null,\\\"big_blue_token\\\":null,\\\"skip_sync_step_nta\\\":null,\\\"caa_reg_flow_source\\\":null,\\\"ig_authorization_token\\\":null,\\\"full_sheet_flow\\\":false,\\\"crypted_user_id\\\":null,\\\"is_caa_perf_enabled\\\":false,\\\"is_preform\\\":true,\\\"ignore_suma_check\\\":false,\\\"ignore_existing_login\\\":false,\\\"ignore_existing_login_from_suma\\\":false,\\\"ignore_existing_login_after_errors\\\":false,\\\"suggested_first_name\\\":null,\\\"suggested_last_name\\\":null,\\\"suggested_full_name\\\":null,\\\"replace_id_sync_variant\\\":null,\\\"is_redirect_from_nta_replace_id_sync_variant\\\":false,\\\"frl_authorization_token\\\":null,\\\"post_form_errors\\\":null,\\\"skip_step_without_errors\\\":false,\\\"existing_account_exact_match_checked\\\":false,\\\"existing_account_fuzzy_match_checked\\\":false,\\\"email_oauth_exists\\\":false,\\\"confirmation_code_send_error\\\":null,\\\"is_too_young\\\":false,\\\"source_account_type\\\":null,\\\"whatsapp_installed_on_client\\\":false,\\\"confirmation_medium\\\":null,\\\"source_credentials_type\\\":null,\\\"source_cuid\\\":null,\\\"source_account_reg_info\\\":null,\\\"soap_creation_source\\\":null,\\\"source_account_type_to_reg_info\\\":null,\\\"registration_flow_id\\\":\\\"\\\",\\\"should_skip_youth_tos\\\":false,\\\"is_youth_regulation_flow_complete\\\":false,\\\"is_on_cold_start\\\":false,\\\"email_prefilled\\\":false,\\\"cp_confirmed_by_auto_conf\\\":false,\\\"auto_conf_info\\\":null,\\\"in_sowa_experiment\\\":false,\\\"youth_regulation_config\\\":null,\\\"conf_allow_back_nav_after_change_cp\\\":null,\\\"conf_bouncing_cliff_screen_type\\\":null,\\\"conf_show_bouncing_cliff\\\":null,\\\"eligible_to_flash_call_in_ig4a\\\":false,\\\"flash_call_permissions_status\\\":null,\\\"attestation_result\\\":null,\\\"request_data_and_challenge_nonce_string\\\":null,\\\"confirmed_cp_and_code\\\":null,\\\"notification_callback_id\\\":null,\\\"reg_suma_state\\\":0,\\\"is_msplit_neutral_choice\\\":false,\\\"msg_previous_cp\\\":null,\\\"ntp_import_source_info\\\":null,\\\"youth_consent_decision_time\\\":null,\\\"reduced_tos_test_group\\\":\\\"control\\\",\\\"should_show_spi_before_conf\\\":true,\\\"google_oauth_account\\\":null,\\\"is_reg_request_from_ig_suma\\\":false,\\\"is_igios_spc_reg\\\":false,\\\"device_emails\\\":[],\\\"is_toa_reg\\\":false,\\\"is_threads_public\\\":false,\\\"spc_import_flow\\\":false,\\\"caa_play_integrity_attestation_result\\\":null,\\\"flash_call_provider\\\":null,\\\"spc_birthday_input\\\":false,\\\"failed_birthday_year_count\\\":null,\\\"user_presented_medium_source\\\":null,\\\"user_opted_out_of_ntp\\\":null,\\\"is_from_registration_reminder\\\":false,\\\"show_youth_reg_in_ig_spc\\\":false,\\\"fb_suma_combined_landing_candidate_variant\\\":\\\"control\\\",\\\"fb_suma_is_high_confidence\\\":null,\\\"screen_visited\\\":[\\\"CAA_REG_WELCOME_SCREEN\\\",\\\"bloks.caa.reg.birthday\\\",\\\"CAA_REG_CONTACT_POINT_PHONE\\\",\\\"CAA_REG_CONTACT_POINT_EMAIL\\\",\\\"CAA_REG_PASSWORD\\\"],\\\"fb_email_login_upsell_skip_suma_post_tos\\\":false,\\\"fb_suma_is_from_email_login_upsell\\\":false,\\\"fb_suma_login_upsell_skipped_warmup\\\":false,\\\"fb_suma_login_upsell_show_list_cell_link\\\":false}\",\"flow_info\":\"{\\\"flow_name\\\":\\\"new_to_family_fb_default\\\",\\\"flow_type\\\":\\\"ntf\\\"}\",\"current_step\":6,\"INTERNAL_INFRA_screen_id\":\"CAA_REG_SAVE_PASSWORD_CREDENTIALS\"},\"client_input_params\":{\"lois_settings\":{\"lois_token\":\"\",\"lara_override\":\"\"}}}"})
		cok  = ';'.join([str(x)+"="+str(y) for x,y in self.ses.cookies.get_dict().items()])
		self.headers.update({'content-length': str(len(self.data)), 'cookie': cok})
		post = self.ses.post(f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.save-credentials&type=app&__bkv={self.versioningID}', data=self.data,headers = self.headers, cookies={'cookie': cok})
	
	def setujui_ketentuan(self):
		self.data.update({"params":"{\"server_params\":{\"waterfall_id\":\"5c633b1c-7418-491f-81ad-c26d16b6f427\",\"is_platform_login\":0,\"is_from_logged_out\":0,\"access_flow_version\":\"F2_FLOW\",\"tos_type\":\"standard\",\"reg_info\":\"{\\\"first_name\\\":\\\""+self.nama_depan+"\\\",\\\"last_name\\\":\\\""+self.nama_belakang+"\\\",\\\"full_name\\\":\\\""+self.nama_depan+"\\\",\\\"contactpoint\\\":\\\""+self.email+"\\\",\\\"ar_contactpoint\\\":null,\\\"contactpoint_type\\\":\\\"email\\\",\\\"is_using_unified_cp\\\":false,\\\"unified_cp_screen_variant\\\":null,\\\"is_cp_auto_confirmed\\\":false,\\\"is_cp_auto_confirmable\\\":false,\\\"confirmation_code\\\":null,\\\"birthday\\\":\\\""+self.tgl_lahir+"\\\",\\\"did_use_age\\\":false,\\\"gender\\\":1,\\\"use_custom_gender\\\":false,\\\"custom_gender\\\":null,\\\"encrypted_password\\\":\\\""+self.enpas+"\\\",\\\"username\\\":null,\\\"username_prefill\\\":null,\\\"fb_conf_source\\\":null,\\\"device_id\\\":null,\\\"ig4a_qe_device_id\\\":null,\\\"family_device_id\\\":null,\\\"nta_eligibility_reason\\\":null,\\\"ig_nta_test_group\\\":null,\\\"user_id\\\":null,\\\"safetynet_token\\\":null,\\\"safetynet_response\\\":null,\\\"machine_id\\\":null,\\\"profile_photo\\\":null,\\\"profile_photo_id\\\":null,\\\"profile_photo_upload_id\\\":null,\\\"avatar\\\":null,\\\"email_oauth_token_no_contact_perm\\\":null,\\\"email_oauth_token\\\":null,\\\"email_oauth_tokens\\\":[],\\\"should_skip_two_step_conf\\\":null,\\\"openid_tokens_for_testing\\\":null,\\\"encrypted_msisdn\\\":null,\\\"encrypted_msisdn_for_safetynet\\\":null,\\\"cached_headers_safetynet_info\\\":null,\\\"should_skip_headers_safetynet\\\":null,\\\"headers_last_infra_flow_id\\\":null,\\\"headers_last_infra_flow_id_safetynet\\\":null,\\\"headers_flow_id\\\":null,\\\"was_headers_prefill_available\\\":null,\\\"sso_enabled\\\":null,\\\"existing_accounts\\\":null,\\\"used_ig_birthday\\\":null,\\\"sync_info\\\":null,\\\"create_new_to_app_account\\\":null,\\\"skip_session_info\\\":null,\\\"ck_error\\\":null,\\\"ck_id\\\":null,\\\"ck_nonce\\\":null,\\\"should_save_password\\\":true,\\\"horizon_synced_username\\\":null,\\\"fb_access_token\\\":null,\\\"horizon_synced_profile_pic\\\":null,\\\"is_identity_synced\\\":false,\\\"is_msplit_reg\\\":null,\\\"user_id_of_msplit_creator\\\":null,\\\"dma_data_combination_consent_given\\\":null,\\\"xapp_accounts\\\":null,\\\"fb_device_id\\\":null,\\\"fb_machine_id\\\":null,\\\"ig_device_id\\\":null,\\\"ig_machine_id\\\":null,\\\"should_skip_nta_upsell\\\":null,\\\"big_blue_token\\\":null,\\\"skip_sync_step_nta\\\":null,\\\"caa_reg_flow_source\\\":null,\\\"ig_authorization_token\\\":null,\\\"full_sheet_flow\\\":false,\\\"crypted_user_id\\\":null,\\\"is_caa_perf_enabled\\\":false,\\\"is_preform\\\":true,\\\"ignore_suma_check\\\":false,\\\"ignore_existing_login\\\":false,\\\"ignore_existing_login_from_suma\\\":false,\\\"ignore_existing_login_after_errors\\\":false,\\\"suggested_first_name\\\":null,\\\"suggested_last_name\\\":null,\\\"suggested_full_name\\\":null,\\\"replace_id_sync_variant\\\":null,\\\"is_redirect_from_nta_replace_id_sync_variant\\\":false,\\\"frl_authorization_token\\\":null,\\\"post_form_errors\\\":null,\\\"skip_step_without_errors\\\":false,\\\"existing_account_exact_match_checked\\\":false,\\\"existing_account_fuzzy_match_checked\\\":false,\\\"email_oauth_exists\\\":false,\\\"confirmation_code_send_error\\\":null,\\\"is_too_young\\\":false,\\\"source_account_type\\\":null,\\\"whatsapp_installed_on_client\\\":false,\\\"confirmation_medium\\\":null,\\\"source_credentials_type\\\":null,\\\"source_cuid\\\":null,\\\"source_account_reg_info\\\":null,\\\"soap_creation_source\\\":null,\\\"source_account_type_to_reg_info\\\":null,\\\"registration_flow_id\\\":\\\"\\\",\\\"should_skip_youth_tos\\\":false,\\\"is_youth_regulation_flow_complete\\\":false,\\\"is_on_cold_start\\\":false,\\\"email_prefilled\\\":false,\\\"cp_confirmed_by_auto_conf\\\":false,\\\"auto_conf_info\\\":null,\\\"in_sowa_experiment\\\":false,\\\"youth_regulation_config\\\":null,\\\"conf_allow_back_nav_after_change_cp\\\":null,\\\"conf_bouncing_cliff_screen_type\\\":null,\\\"conf_show_bouncing_cliff\\\":null,\\\"eligible_to_flash_call_in_ig4a\\\":false,\\\"flash_call_permissions_status\\\":null,\\\"attestation_result\\\":null,\\\"request_data_and_challenge_nonce_string\\\":null,\\\"confirmed_cp_and_code\\\":null,\\\"notification_callback_id\\\":null,\\\"reg_suma_state\\\":0,\\\"is_msplit_neutral_choice\\\":false,\\\"msg_previous_cp\\\":null,\\\"ntp_import_source_info\\\":null,\\\"youth_consent_decision_time\\\":null,\\\"reduced_tos_test_group\\\":\\\"control\\\",\\\"should_show_spi_before_conf\\\":true,\\\"google_oauth_account\\\":null,\\\"is_reg_request_from_ig_suma\\\":false,\\\"is_igios_spc_reg\\\":false,\\\"device_emails\\\":[],\\\"is_toa_reg\\\":false,\\\"is_threads_public\\\":false,\\\"spc_import_flow\\\":false,\\\"caa_play_integrity_attestation_result\\\":null,\\\"flash_call_provider\\\":null,\\\"spc_birthday_input\\\":false,\\\"failed_birthday_year_count\\\":null,\\\"user_presented_medium_source\\\":null,\\\"user_opted_out_of_ntp\\\":null,\\\"is_from_registration_reminder\\\":false,\\\"show_youth_reg_in_ig_spc\\\":false,\\\"fb_suma_combined_landing_candidate_variant\\\":\\\"control\\\",\\\"fb_suma_is_high_confidence\\\":null,\\\"screen_visited\\\":[\\\"CAA_REG_WELCOME_SCREEN\\\",\\\"bloks.caa.reg.birthday\\\",\\\"CAA_REG_CONTACT_POINT_PHONE\\\",\\\"CAA_REG_CONTACT_POINT_EMAIL\\\",\\\"CAA_REG_PASSWORD\\\",\\\"CAA_REG_SAVE_PASSWORD_CREDENTIALS\\\"],\\\"fb_email_login_upsell_skip_suma_post_tos\\\":false,\\\"fb_suma_is_from_email_login_upsell\\\":false,\\\"fb_suma_login_upsell_skipped_warmup\\\":false,\\\"fb_suma_login_upsell_show_list_cell_link\\\":false}\",\"flow_info\":\"{\\\"flow_name\\\":\\\"new_to_family_fb_default\\\",\\\"flow_type\\\":\\\"ntf\\\"}\",\"current_step\":8,\"INTERNAL_INFRA_screen_id\":\"CAA_REG_TERMS_OF_SERVICE\"},\"client_input_params\":{\"lois_settings\":{\"lois_token\":\"\",\"lara_override\":\"\"}}}"})
		cok  = ';'.join([str(x)+"="+str(y) for x,y in self.ses.cookies.get_dict().items()])
		self.headers.update({'content-length': str(len(self.data)), 'cookie': cok})
		post = self.ses.post(f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.tos&type=app&__bkv={self.versioningID}', data=self.data, headers = self.headers, cookies={'cookie': cok})
	
	def next_create(self):
		global Ok, Cp, Fail
		self.data.update({"params":"{\"server_params\":{\"event_request_id\":\"fee78509-e222-412e-9a79-1a33e56fb347\",\"app_id\":0,\"reg_info\":\"{\\\"first_name\\\":\\\""+self.nama_depan+"\\\",\\\"last_name\\\":\\\""+self.nama_belakang+"\\\",\\\"full_name\\\":\\\""+self.nama_depan+"\\\",\\\"contactpoint\\\":\\\""+self.email+"\\\",\\\"ar_contactpoint\\\":null,\\\"contactpoint_type\\\":\\\"email\\\",\\\"is_using_unified_cp\\\":false,\\\"unified_cp_screen_variant\\\":null,\\\"is_cp_auto_confirmed\\\":false,\\\"is_cp_auto_confirmable\\\":false,\\\"confirmation_code\\\":null,\\\"birthday\\\":\\\""+self.tgl_lahir+"\\\",\\\"did_use_age\\\":false,\\\"gender\\\":1,\\\"use_custom_gender\\\":false,\\\"custom_gender\\\":null,\\\"encrypted_password\\\":\\\""+self.enpas+"\\\",\\\"username\\\":null,\\\"username_prefill\\\":null,\\\"fb_conf_source\\\":null,\\\"device_id\\\":null,\\\"ig4a_qe_device_id\\\":null,\\\"family_device_id\\\":null,\\\"nta_eligibility_reason\\\":null,\\\"ig_nta_test_group\\\":null,\\\"user_id\\\":null,\\\"safetynet_token\\\":null,\\\"safetynet_response\\\":null,\\\"machine_id\\\":null,\\\"profile_photo\\\":null,\\\"profile_photo_id\\\":null,\\\"profile_photo_upload_id\\\":null,\\\"avatar\\\":null,\\\"email_oauth_token_no_contact_perm\\\":null,\\\"email_oauth_token\\\":null,\\\"email_oauth_tokens\\\":[],\\\"should_skip_two_step_conf\\\":null,\\\"openid_tokens_for_testing\\\":null,\\\"encrypted_msisdn\\\":null,\\\"encrypted_msisdn_for_safetynet\\\":null,\\\"cached_headers_safetynet_info\\\":null,\\\"should_skip_headers_safetynet\\\":null,\\\"headers_last_infra_flow_id\\\":null,\\\"headers_last_infra_flow_id_safetynet\\\":null,\\\"headers_flow_id\\\":null,\\\"was_headers_prefill_available\\\":null,\\\"sso_enabled\\\":null,\\\"existing_accounts\\\":null,\\\"used_ig_birthday\\\":null,\\\"sync_info\\\":null,\\\"create_new_to_app_account\\\":null,\\\"skip_session_info\\\":null,\\\"ck_error\\\":null,\\\"ck_id\\\":null,\\\"ck_nonce\\\":null,\\\"should_save_password\\\":true,\\\"horizon_synced_username\\\":null,\\\"fb_access_token\\\":null,\\\"horizon_synced_profile_pic\\\":null,\\\"is_identity_synced\\\":false,\\\"is_msplit_reg\\\":null,\\\"user_id_of_msplit_creator\\\":null,\\\"dma_data_combination_consent_given\\\":null,\\\"xapp_accounts\\\":null,\\\"fb_device_id\\\":null,\\\"fb_machine_id\\\":null,\\\"ig_device_id\\\":null,\\\"ig_machine_id\\\":null,\\\"should_skip_nta_upsell\\\":null,\\\"big_blue_token\\\":null,\\\"skip_sync_step_nta\\\":null,\\\"caa_reg_flow_source\\\":null,\\\"ig_authorization_token\\\":null,\\\"full_sheet_flow\\\":false,\\\"crypted_user_id\\\":null,\\\"is_caa_perf_enabled\\\":false,\\\"is_preform\\\":true,\\\"ignore_suma_check\\\":false,\\\"ignore_existing_login\\\":false,\\\"ignore_existing_login_from_suma\\\":false,\\\"ignore_existing_login_after_errors\\\":false,\\\"suggested_first_name\\\":null,\\\"suggested_last_name\\\":null,\\\"suggested_full_name\\\":null,\\\"replace_id_sync_variant\\\":null,\\\"is_redirect_from_nta_replace_id_sync_variant\\\":false,\\\"frl_authorization_token\\\":null,\\\"post_form_errors\\\":null,\\\"skip_step_without_errors\\\":false,\\\"existing_account_exact_match_checked\\\":false,\\\"existing_account_fuzzy_match_checked\\\":false,\\\"email_oauth_exists\\\":false,\\\"confirmation_code_send_error\\\":null,\\\"is_too_young\\\":false,\\\"source_account_type\\\":null,\\\"whatsapp_installed_on_client\\\":false,\\\"confirmation_medium\\\":null,\\\"source_credentials_type\\\":null,\\\"source_cuid\\\":null,\\\"source_account_reg_info\\\":null,\\\"soap_creation_source\\\":null,\\\"source_account_type_to_reg_info\\\":null,\\\"registration_flow_id\\\":\\\"\\\",\\\"should_skip_youth_tos\\\":false,\\\"is_youth_regulation_flow_complete\\\":false,\\\"is_on_cold_start\\\":false,\\\"email_prefilled\\\":false,\\\"cp_confirmed_by_auto_conf\\\":false,\\\"auto_conf_info\\\":null,\\\"in_sowa_experiment\\\":false,\\\"youth_regulation_config\\\":null,\\\"conf_allow_back_nav_after_change_cp\\\":null,\\\"conf_bouncing_cliff_screen_type\\\":null,\\\"conf_show_bouncing_cliff\\\":null,\\\"eligible_to_flash_call_in_ig4a\\\":false,\\\"flash_call_permissions_status\\\":null,\\\"attestation_result\\\":null,\\\"request_data_and_challenge_nonce_string\\\":null,\\\"confirmed_cp_and_code\\\":null,\\\"notification_callback_id\\\":null,\\\"reg_suma_state\\\":0,\\\"is_msplit_neutral_choice\\\":false,\\\"msg_previous_cp\\\":null,\\\"ntp_import_source_info\\\":null,\\\"youth_consent_decision_time\\\":null,\\\"reduced_tos_test_group\\\":\\\"control\\\",\\\"should_show_spi_before_conf\\\":true,\\\"google_oauth_account\\\":null,\\\"is_reg_request_from_ig_suma\\\":false,\\\"is_igios_spc_reg\\\":false,\\\"device_emails\\\":[],\\\"is_toa_reg\\\":false,\\\"is_threads_public\\\":false,\\\"spc_import_flow\\\":false,\\\"caa_play_integrity_attestation_result\\\":null,\\\"flash_call_provider\\\":null,\\\"spc_birthday_input\\\":false,\\\"failed_birthday_year_count\\\":null,\\\"user_presented_medium_source\\\":null,\\\"user_opted_out_of_ntp\\\":null,\\\"is_from_registration_reminder\\\":false,\\\"show_youth_reg_in_ig_spc\\\":false,\\\"fb_suma_combined_landing_candidate_variant\\\":\\\"control\\\",\\\"fb_suma_is_high_confidence\\\":null,\\\"screen_visited\\\":[\\\"CAA_REG_WELCOME_SCREEN\\\",\\\"bloks.caa.reg.birthday\\\",\\\"CAA_REG_CONTACT_POINT_PHONE\\\",\\\"CAA_REG_CONTACT_POINT_EMAIL\\\",\\\"CAA_REG_PASSWORD\\\",\\\"CAA_REG_SAVE_PASSWORD_CREDENTIALS\\\"],\\\"fb_email_login_upsell_skip_suma_post_tos\\\":false,\\\"fb_suma_is_from_email_login_upsell\\\":false,\\\"fb_suma_login_upsell_skipped_warmup\\\":false,\\\"fb_suma_login_upsell_show_list_cell_link\\\":false}\",\"flow_info\":\"{\\\"flow_name\\\":\\\"new_to_family_fb_default\\\",\\\"flow_type\\\":\\\"ntf\\\"}\",\"current_step\":8,\"INTERNAL__latency_qpl_marker_id\":36707139,\"INTERNAL__latency_qpl_instance_id\":\"22873194000041\",\"device_id\":null,\"family_device_id\":null,\"waterfall_id\":\"5c633b1c-7418-491f-81ad-c26d16b6f427\",\"offline_experiment_group\":null,\"layered_homepage_experiment_group\":null,\"is_platform_login\":0,\"is_from_logged_in_switcher\":0,\"is_from_logged_out\":0,\"access_flow_version\":\"F2_FLOW\",\"INTERNAL_INFRA_THEME\":\"default\"},\"client_input_params\":{\"device_id\":\"\",\"waterfall_id\":\"5c633b1c-7418-491f-81ad-c26d16b6f427\",\"machine_id\":\"\",\"ck_error\":\"\",\"ck_id\":\"\",\"ck_nonce\":\"\",\"should_ignore_existing_login\":0,\"encrypted_msisdn\":\"\",\"headers_last_infra_flow_id\":\"\",\"reached_from_tos_screen\":1,\"no_contact_perm_email_oauth_token\":\"\",\"failed_birthday_year_count\":\"{}\",\"lois_settings\":{\"lois_token\":\"\",\"lara_override\":\"\"}}}"})
		cok  = ';'.join([str(x)+"="+str(y) for x,y in self.ses.cookies.get_dict().items()])
		self.headers.update({'content-length': str(len(self.data)), 'cookie': cok})
		post = self.ses.post(f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.create.account.async&type=action&__bkv={self.versioningID}', data=self.data, headers = self.headers, cookies={'cookie': cok}).text
		if "session_key" in str(post):
			self.userID = re.search('"uid":(\d+)', post.replace('\\','')).group(1)
			self.config.kode(5)
			if web_email == '1': self.code = self.get_code_temp_mail(self.email)
			elif web_email == '2': self.code = self.get_code_temp_plus(self.email)
			elif web_email == '3': self.code = self.get_code_10minutemail()
			elif web_email == '4':
				print(f" {' ' *65}", end = '\r')
				time.sleep(000.11)
				self.code = input(' (+) code: ')
			else:self.code = self.get_code_temp_mail(self.email)
			self.konfirmasi()
		elif "Nama pengguna atau kata sandi tidak valid" in post.replace('\\', ''):
			cookie = ';'.join([str(x)+"="+str(y) for x,y in self.ses.cookies.get_dict().items()])
			self.userID = re.search('c_user=(\\d+)', str(cookie)).group(1)
			self.config.kode(5)
			if web_email == '1': self.code = self.get_code_temp_mail(self.email)
			elif web_email == '2': self.code = self.get_code_temp_plus(self.email)
			elif web_email == '3': self.code = self.get_code_10minutemail()
			elif web_email == '4':
				print(f" {' ' *65}", end = '\r')
				time.sleep(000.11)
				self.code = input(' (+) code: ')
			else:self.code = self.get_code_temp_mail(self.email)
			self.konfirmasi()
		else:
			print(f"""\r{' ' * 76}
 INFO ACCOUNT

 STATUS     : [bold red]Failed[bold white]
 TIMESTAMP  : [bold red]{waktu}[bold white]
 NAME       : [bold red]{self.nama_depan} {self.nama_belakang}[bold white]
 EMAIL      : [bold red]{self.email}[bold white]
 PASSWORD   : [bold red]{self.password}[bold white]
 BIRTHDAY   : [bold red]{self.tgl_lahir}[bold white]
			""")
			Fail+=1
	
	def konfirmasi(self):
		global Ok, Cp, Fail
		print(f" (+) verification code > {self.code}{' ' *20}", end = '\r')
		time.sleep(1.5)
		header = {
			'authority': 'm.facebook.com',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'dpr': '2',
			'referer': 'https://m.facebook.com/login/save-device/',
			'sec-ch-prefers-color-scheme': 'light',
			'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-model': '"vivo 1820"',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': '"8.1.0"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A325M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
			'viewport-width': '980',
		}
		params = {
			'next': 'https://m.facebook.com/?deoia=1',
			'soft': 'hjk',
		}
		respon = self.ses.get('https://m.facebook.com/confirmemail.php', params=params, headers=header).text    
		headers = {
			'authority': 'm.facebook.com',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'dpr': '2',
			'origin': 'https://m.facebook.com',
			'referer': 'https://m.facebook.com/confirmemail.php',
			'sec-ch-prefers-color-scheme': 'light',
			'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-model': '"vivo 1820"',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': '"8.1.0"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A325M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
			'viewport-width': '980',
		}
		params1 = {
			'contact': '{}'.format(self.email),
			'type': 'submit',
			'is_soft_cliff': 'false',
			'medium': 'email',
			'code': '{}'.format(self.code),
		}
		data = {
			'fb_dtsg': re.search('"dtsg":{"token":"(.*?)"',str(respon)).group(1),
			'jazoest': re.search(r'"\d+"', respon).group().strip('"'),
			'lsd': re.search('"LSD",\[\],{"token":"([^"]+)"}',str(respon)).group(1),
			'__dyn': '',
			'__csr': '',
			'__req': '4',
			'__fmt': '1',
			'__a': '',
			'__user': f'{self.userID}',
		}
		response = self.ses.post('https://m.facebook.com/confirmation_cliff/', params=params1, headers=headers, data=data)
		if "home.php?confirmed_account" in str(response.text):
			self.cookie = ';'.join([str(x)+"="+str(y) for x,y in self.ses.cookies.get_dict().items()])
		#	profil = self.postFotoProfile(self.cookie)
			#self.Aktifkan()
			print(f"""\r{' ' * 76}
 INFO ACCOUNT

 STATUS     : [bold green]Success[bold white]
 TIMESTAMP  : [bold green]{waktu}[bold white]
 NAME       : [bold green]{self.nama_depan} {self.nama_belakang}[bold white]
 USERID     : [bold green]{self.userID}[bold white]
 EMAIL      : [bold green]{self.email}[bold white]
 PASSWORD   : [bold green]{self.password}[bold white]
 BIRTHDAY   : [bold green]{self.tgl_lahir}[bold white]
 [bold green]{self.cookie}[bold white]
			""")
			Ok+=1
			with open(f"/sdcard/neraka.txt","a") as wr:
				wr.write(f"{self.userID}\n")
			wr.close()
		elif "errorSummary" in response.text:
			print(f"""\r{' ' * 76}
 INFO ACCOUNT

 Status     : [bold red]errorSummary[bold white]
 Timestamp  : [bold red]{waktu}[bold white]
 Name       : [bold red]{self.nama_depan} {self.nama_belakang}[bold white]
 UserID     : [bold red]{self.userID}[bold white]
 Email      : [bold red]{self.email}[bold white]
 Password   : [bold red]{self.password}[bold white]
 Birthday   : [bold red]{self.tgl_lahir}[bold white]
			""")
			Cp+=1
		else:
			print(f"""\r{' ' * 76}
 INFO ACCOUNT

 Status     : [bold red]Failed[bold white]
 Timestamp  : [bold red]{waktu}[bold white]
 Name       : [bold red]{self.nama_depan} {self.nama_belakang}[bold white]
 UserID     : [bold red]{self.userID}[bold white]
 Email      : [bold red]{self.email}[bold white]
 Password   : [bold red]{self.password}[bold white]
 Birthday   : [bold red]{self.tgl_lahir}[bold white]
			""")
			Cp+=1
			
	def postFotoProfile(self, cookie):
		img = open('/sdcard/JOS/src/foto2/1735492187997.jpg', 'r').read().splitlines()
		image_url = random.choice(img)
		try:
			with requests.Session() as r:
				id = re.search('c_user=(\\d+)', str(cookie)).group(1)
				req = r.get(f'https://web.facebook.com/profile.php?id={id}', cookies={'cookie': cookie}).text
				params = self.config.DataGraphQL(req, id)
				params.update({
					'profile_id': id,
					'photo_source': "57",
				})
				files = {'file':('image.jpg',urllib.request.urlopen(image_url).read())}
				pos = r.post("https://web.facebook.com/profile/picture/upload/", cookies={'cookie': cookie}, params=params,  files=files).text
				fbid = re.search('"fbid":"(\d+)"', str(pos)).group(1)
				data = self.config.DataGraphQL(req, id)
				data.update({
					"fb_api_caller_class": "RelayModern",
					"fb_api_req_friendly_name": "ProfileCometProfilePictureSetMutation",
					"variables": json.dumps({"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1729674295794,691444,190055527696468,,","caption":"","existing_photo_id":fbid,"expiration_time":None,"profile_id":id,"profile_pic_method":"EXISTING","profile_pic_source":"TIMELINE","scaled_crop_rect":{"height":1,"width":1,"x":0,"y":0},"skip_cropping": True,"actor_id":id,"client_mutation_id":"2"},"isPage":False,"isProfile":True,"sectionToken":"UNKNOWN","collectionToken":"UNKNOWN","scale":3,"__relay_internal__pv__ProfileGeminiIsCoinFlipEnabledrelayprovider":False}),
					"server_timestamps": "true",
					"doc_id": "28132579203008372"
				})
				post = r.post('https://web.facebook.com/api/graphql/', data=data, cookies = {'cookie':cookie})
				if 'profilePhoto' in post.text:
					return f"[bold green]Berhasil memperbarui foto profil[bold white]"
				else:
					return f"[bold red]Gagal memperbarui foto profil[bold white]"
					
		except Exception as e:
			return f"[bold red]Gagal memperbarui foto profil[bold red]"

if __name__ == '__main__':
	main = MAIN()
	main.menu()
	
	
