#!/usr/bin/env python

import psutil
import sys
import os
import pygtk
pygtk.require('2.0')
import gtk

class MainClass:

	def __init__(self):
		self.window = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Task Manager")

		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(250, 400)
		self.window.set_tooltip_text("This is the task manager")


		self.button1=gtk.Button("\t Close Application \t")
		self.button1.connect("clicked", self.destroy)

		self.button2=gtk.Button("\t List of All Processes \t")
		self.button2.connect("clicked", self.process)

		self.label1=gtk.Label("Enter PID of the process")
		self.textbox = gtk.Entry()

		self.button3=gtk.Button("\t Terminate a Process \t")
		self.button3.connect("clicked", self.terminate)

		self.button4=gtk.Button("\t Active Processes \t")
		self.button4.connect("clicked", self.active)

		self.button5=gtk.Button("\t Memory Status \t")
		self.button5.connect("clicked", self.mem)
		
		self.button6=gtk.Button("\t CPU Utilization Graph \t")
		self.button6.connect("clicked", self.cpu_graph)

		self.box1 = gtk.VBox()
		self.box1.pack_start(self.button2)
		self.box1.pack_start(self.label1)
		self.box1.pack_start(self.textbox)
		self.box1.pack_start(self.button3)
		self.box1.pack_start(self.button4)
		self.box1.pack_start(self.button5)
		self.box1.pack_start(self.button6)
		self.box1.pack_start(self.button1)

		self.window.add(self.box1)
		self.window.show_all()
		self.window.connect("destroy", self.destroy)

	def destroy(self, widget, data=None):
		gtk.main_quit()

	def main(self):
		gtk.main()

	def terminate(self, widget, data=None):
		port = self.textbox.get_text()
		pid=int(port)
		if psutil.pid_exists(pid) == True:
			p=psutil.Process(pid)
			p.kill()
			print 'Pid: %d terminated' % pid
		elif psutil.pid_exists(pid) == False:
			em= gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "This PID does not exist")
			em.run()
			em.destroy()

	def process(self, widget, data=None):
		self.window1 = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
		self.window1.set_title("Processes")
		print 'All Running Processes : '
		print psutil.test()

	def mem(self, widget, data=None) :
		print "\nDETAILS OF SYSTEM MEMORY USAGE\n"
		print psutil.virtual_memory()
	
	def cpu_graph(self, widget, data=None) :
		import graph

	def active(self, widget, data=None) :
		print 'PIDs of All Actively Running Processes: '
		print psutil.pids()

if __name__ =="__main__":
	bse = MainClass()
	bse.main()
