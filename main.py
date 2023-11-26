import flet
from flet import *
import keyboard
import random
import string
import socket



#Variables
password = 'JD-3425'

sufler_text = ''



#DEFs
#Getting local ip-address
def get_ip():
	hostname = socket.gethostname()
	local_ip = socket.gethostbyname(hostname)
	return local_ip

#SignIn flet page
def flet_sign_in(page: Page):
	if page.client_ip == '127.0.0.1':
		page.add(Text('Loading admin interface...'))
		admin(page)
	else:
		#DEFs#2
		#Password check
		def passwd_check(e):
			if signin_passwd_enter.value == password:
				user(page)

		#Generate interface
		signin_passwd_enter = TextField(label="Password", capitalization=TextCapitalization.CHARACTERS)
		signin_passwd_btn = FilledButton("Login", on_click=passwd_check)
		signin_passwd_enter_container = Container(content=signin_passwd_enter, alignment=alignment.center)
		signin_passwd_btn_container = Container(content=signin_passwd_btn, alignment = alignment.center)
		page.views.append(View("/signin", [Column([signin_passwd_enter_container, signin_passwd_btn_container])], vertical_alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER))
		page.update()


#User's flet page
def user(page: Page):

	#DEFs#2
	#Navigation bar checking
	def chek_navigationBar(e):

		#Reload
		if user_navigation_bar.selected_index == 0:
			keyboard.press('left')
			keyboard.release('left')
		elif user_navigation_bar.selected_index == 1:
			keyboard.press('F5')
			keyboard.release('F5')
		elif user_navigation_bar.selected_index == 2:
			user_sufler.value = sufler_text
			page.update()
		elif user_navigation_bar.selected_index == 3:
			keyboard.press('b')
			keyboard.release('b')
		elif user_navigation_bar.selected_index == 4:
			keyboard.press('right')
			keyboard.release('right')

	user_sufler = Text(sufler_text, selectable=True)
	user_navigation_bar = NavigationBar(destinations=[NavigationDestination(icon=icons.ARROW_BACK, label="Back"), NavigationDestination(icon=icons.SMART_DISPLAY, label='Play'), NavigationDestination(icon=icons.KEYBOARD_DOUBLE_ARROW_DOWN, label="Reload"), NavigationDestination(icon=icons.CROP_SQUARE, label='Hide'), NavigationDestination(icon=icons.ARROW_FORWARD, label='Next')], on_change=chek_navigationBar)
	page.views.append(View("/user", [user_sufler, user_navigation_bar]))
	page.update()


#Main desktop page
def admin(page: Page):
	global sufler_text

	#DEFs#2
	def send_sufler(e):
		global sufler_text
		sufler_text = admin_sufler_text.value

	def regen_password(e):
		pass_gen()
		admin_noname0.value = password
		page.update()

	#Generate interface
	admin_sufler_text = TextField(label="Суфлёрский текст", min_lines=23, max_lines=23, multiline=True, hint_text='Введите сюда текст, отображаемый у выступающего', on_change=send_sufler)
	admin_sufler_text_container = Container(content=admin_sufler_text, width=700)
	admin_noname0 = TextField(disabled=True, value=password)
	admin_password_row = Row([Text('Password: ', style='titleLarge'), admin_noname0, TextButton('Regenerate', on_click=regen_password)])
	page.views.append(View("/admin", [Row([Column([admin_sufler_text_container, ]), Column([Text(value="Connection", italic=False, selectable=True, style='displayMedium'), Text(value='Address: http://'+get_ip()+':1111/', italic=False, selectable=True, style='titleLarge'), admin_password_row, Text('Подсказка: Для подключения компьютер и телефон должны находиться в одной WiFi-сети,\nна телефоне перейдите в браузер и введите адрес, указанный выше, а псоел пароль\n-----\nHint: To connect, the computer and phone must be on the same WiFi network; on the phone,\ngo to the browser and enter the address indicated above, and enter the password')])])]))
	page.update()


#Password generator
def pass_gen():
	global password
	password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + '-' + str(random.randint(1000, 9999))



#Run the app
pass_gen()
app(target=flet_sign_in, view=WEB_BROWSER, port=1111)