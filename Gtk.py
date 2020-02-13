#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:20:21 2019

@author: arslan
"""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk


class mainWin(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="منیم ایشله‌دیچی رابطلی یازیلیمیم")

        self.connect("delete_event", self.delete_event)
        self.connect("destroy", self.destroy)

        self.set_icon_from_file("./icon.png")
        self.set_border_width(10)
        self.set_default_size(500, 400)
        self.set_resizable(False)

        fixed = Gtk.Fixed()
        self.add(fixed)

        button = Gtk.Button.new_with_label("باس")
        button.connect("clicked", self.on_click)
        fixed.put(button, 100, 100)

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        Gtk.main_quit()

    def on_click(self, button):
        print("دوگمه باسیلدی!")


if __name__ == "__main__":
    win = mainWin()
    win.show_all()
    Gtk.main()