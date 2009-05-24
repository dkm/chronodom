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
        self.start_date = datetime.datetime.today()

        while self.please_loop:
            now = datetime.datetime.today()
            delta = now - self.start_date
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
        self.chrono1 = None

        self.sw = self.xml.get_widget("scrolledwindow1")

        self.start_btn = self.xml.get_widget("start_button1")

        self.treestore = gtk.TreeStore(str)
        self.tree = self.xml.get_widget("treeview1")
        self.tree.set_model(self.treestore)

        self.tree.set_headers_visible(True)
        renderer = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Temps",renderer, text=0)
        column.set_resizable(True)
        self.tree.append_column(column)

        self.fc = self.xml.get_widget("filechooserdialog1")
        gtk.main()

    def insert_row(self, col, parent=None):
        myiter = self.treestore.prepend(None)
        self.treestore.set_value(myiter, 0, col)
        return myiter

    def on_start_button1_clicked(self, widget):
        print "chrono1"
        if self.chrono1 == None:
            self.chrono1 = Chrono(None, btn=self.chrono1_btn)
            self.chrono1.start()
            self.start_btn.set_label("STOP")
        else:
            self.chrono1.please_loop = False
            self.chrono1 = None
            self.start_btn.set_label("START")

    
    def on_save_button_clicked(self, widget):
        chooser = gtk.FileChooserDialog(
            title="Save Output",action=gtk.FILE_CHOOSER_ACTION_SAVE,
            buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,
                     gtk.STOCK_SAVE,gtk.RESPONSE_OK))
        response = chooser.run()
        filename = chooser.get_filename()

        chooser.destroy()
        print filename

        treeiter = self.treestore.get_iter_first()
        if treeiter == None:
            return

        fout = open(filename, "w")

        while treeiter != None:
            value = self.treestore.get_value(treeiter, 0)
            print >>fout, value, ","
            treeiter = self.treestore.iter_next(treeiter)
        fout.close()


    def on_chrono_button1_clicked(self, widget):
        print "start1"

        if self.chrono1 == None:
            return

        now = datetime.datetime.today()
        delta = now - self.chrono1.start_date

        self.insert_row(str(delta))

        # adj = self.sw.get_vadjustment()
        # print "b", adj.get_value()

        # p = adj.lower
        # adj.set_value(p)
        # print "a", adj.get_value()


if __name__ == '__main__':
    gtk.gdk.threads_init()
    ChronoDom()
