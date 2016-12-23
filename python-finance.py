import tkinter
from tkinter import *
from modules import share_data
import time
import urllib
# Define variables
share_names = []


# Main function
def main():
	# Write your code here
	data = share_data.share_update
	time.sleep(10)
	yahoo = data.return_share_price('YHOO')
	print(yahoo[1])
	# gui_module()

#############################################
# Graphical User Interface module
# def gui_module():
# 	top = tkinter.Tk()
# 	#Code to add widgets will go here...
# 	text = Text(top)
# 	text.insert(INSERT,"Yahoo: \n")
# 	text.insert(END,"BYE...")
# 	text.pack()
# 	top.mainloop()



##############################################
if __name__ == "__main__":
	# execute only if run as a script
	try:
		while (1):
			main()



	except KeyboardInterrupt:
		print("Program Stopped Here")
	except urllib.error.HTTPError:
		print("HTTP Error! Bad Request!")
