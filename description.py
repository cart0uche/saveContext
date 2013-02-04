#!/usr/bin/python
# -*- coding: utf-8 -*-
# saveContext

import time
from Tkinter import END
import Tkinter

DESCRIPTION_TEMP_FILE = 'desc.txt'

class Description(Tkinter.Tk):


	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()

		self.message = Tkinter.Message(self,text="The application just crashs, please describe what's just happend.",width=700)
		self.message.grid(padx=10,pady=10,column=0,row=0,sticky='W')

		self.text = Tkinter.Text(self,insertborderwidth=1)
		self.text.grid(padx=10,pady=10,column=0,row=1,sticky='WENS')

		buttonSave = Tkinter.Button(self,text=u"Save !",command=self.OnButtonClick)
		buttonSave.grid(column=0,row=2)

		buttonNoComment = Tkinter.Button(self,text=u"No comment..",command=self.closeWindows)
		buttonNoComment.grid(padx=10,pady=10,column=0,row=3)

		self.title("saveContext : what's append ?")
		self.protocol("WM_DELETE_WINDOW", self.closeWindows)
		self.mainloop()

	def OnButtonClick(self):
		fileDescription = open(DESCRIPTION_TEMP_FILE,'w+')
		fileDescription.write(time.strftime('%c',time.localtime())+'\n')
		fileDescription.write(self.text.get(1.0, END).encode('utf-8'))
		fileDescription.close()
		self.destroy()

	def closeWindows(self):
		self.destroy()


def main():
	app = Description(None)
	return

if __name__ == '__main__':
	main()
