# coding: utf-8

from pynput.mouse import Button, Controller
import time
mouse = Controller()

num = raw_input("how much clicks ? >>> ")

def oFunction(num):
	for enum in range(1,int(num) + 1):
		time.sleep(0.1)
		print("[*] " + str(enum) + " clicks")

print("options = attack,build")
option = raw_input('choose option >>> ')
if option == "attack":
	time.sleep(5)
	mouse.click(Button.left, int(num))
	oFunction(num)

if option == "build":
	time.sleep(5)
	mouse.click(Button.right, int(num))
	oFunction(num)
