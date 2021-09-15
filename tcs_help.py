import pyautogui
import time


def tcs_help_desk():
	#1850 966
	help_button_posx = 1770
	help_button_posy =1011

	#1700 1000
	submit_button_x =1700
	submit_button_y =1000

	# 1516 Y:  986
	write_padx =1516
	write_pady =986

	text ="""Today I have exam at 15 Sep , 9am so, I registered at 8 am and waited for launch button to activate. Then at 9:30 Am The launch button get activated and after clicking that it is showing the below information. Please Resolve my issue. This exam is very important to me.

	showing "Sorry for the inconvenience Note : You cannot launch this assessment now since you are trying to launch beyond the start time permitted."

	My Details: xxxxxx xxxxx xxxxxxx xxxxxxxxx

	"""

	pyautogui.keyDown('win')
	pyautogui.press('1')
	pyautogui.keyUp('win')
	pyautogui.click(x=help_button_posx, y=help_button_posy) 
	time.sleep(10)
	pyautogui.press('tab')
	pyautogui.write('karthik') 
	pyautogui.press('tab')
	pyautogui.write('krk0241@gmail.com') 
	pyautogui.press('tab')
	pyautogui.write('exam was not launching ,i am waiting from 8am for the launch button to get activated untill 9:30am button not activated.how will i attend at 9:10 am ?') 
	pyautogui.press('tab')
	pyautogui.click(x=submit_button_x, y=submit_button_y) 
	time.sleep(5)
	pyautogui.click(x=write_padx, y=write_pady) 

	pyautogui.write(text)
	pyautogui.press('enter')


for x in range(12):
	tcs_help_desk()
	time.sleep(300)

	
