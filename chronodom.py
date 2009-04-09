#!/usr/bin/env python

import gtk
import gtk.glade
import gobject
from threading import Thread
import time
import datetime

class Chrono(Thread):
    def __init__(self, args, btn, delta=0.1):
        self.btn_widget = btn
        self.delta = delta
        Thread.__init__(self)
        print "created a chrono"
        self.please_loop = True
        self.start_date = None

    def run(self):
        start_date = datetime.datetime.today()

        while self.please_loop:
            now = datetime.datetime.today()
            delta = now - start_date
            gobject.idle_add(self.btn_widget.set_label, str(delta))
            time.sleep(self.delta)

class ChronoDom:
    def __init__(self):
        self.xml = gtk.glade.XML("chronodom.glade")
        self.w = self.xml.get_widget("window1")
        self.xml.signal_autoconnect(self)
        self.w.connect("delete_event", gtk.main_quit)
        self.w.show_all()

        self.chrono1_btn = self.xml.get_widget("chrono_button1")
        self.chrono2_btn = self.xml.get_widget("chrono_button2")
        
        self.chrono1 = None
        self.chrono2 = None

        gtk.main()

    def on_start_button1_clicked(self, widget):
        print "chrono1"
        if self.chrono1 == None:
            self.chrono1 = Chrono(None, btn=self.chrono1_btn)
            self.chrono1.start()
        else:
            self.chrono1.please_loop = False
            self.chrono1 = None

    def on_start_button2_clicked(self, widget):
        print "chrono2"
        if self.chrono2 == None:
            self.chrono2 = Chrono(None, btn=self.chrono2_btn)
            self.chrono2.start()
        else:
            self.chrono2.please_loop = False
            self.chrono2 = None

    def on_chrono_button1_clicked(self, widget):
        print "start1"

    def on_chrono_button2_clicked(self, widget):
        print "start2"

if __name__ == '__main__':
    gtk.gdk.threads_init()
    ChronoDom()
