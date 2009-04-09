#!/usr/bin/env python

import gtk
import gtk.glade


class ChronoDom:
    def __init__(self):
        self.xml = gtk.glade.XML("chronodom.glade")
        self.w = self.xml.get_widget("window1")
        self.xml.signal_autoconnect(self)
        self.w.connect("delete_event", gtk.main_quit)
        self.w.show_all()

        self.chrono1_btn = self.xml.get_widget("chrono_button1")
        self.chrono2_btn = self.xml.get_widget("chrono_button1")

        gtk.main()

    def on_chrono_button1_clicked(self, widget):
        print "chrono1"

    def on_chrono_button2_clicked(self, widget):
        print "chrono2"

    def on_start_button1_clicked(self, widget):
        print "start1"

    def on_start_button2_clicked(self, widget):
        print "start2"

if __name__ == '__main__':
    ChronoDom()
