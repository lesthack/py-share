#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import sys
import os
import threading
import time
import webbrowser
from ipaddress import *

try:
    import gtk    
except ImportError:
    sys.exit("pygtk not found.")

UI_FILE = "data/py_share.ui"
INTERFACE = "wlan0"

def handle_server(port, obj, sec):        
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    port_busy = True
    
    try:        
        httpd = SocketServer.TCPServer(("", port), handler)
        port_busy = False
        
        url = "http://%s:%s" % (obj.ip, port)
        obj.lb_status.set_label("Status: %s %s" % ("Start Server", url))        
        webbrowser.open(url)
        
        while obj.isActive:
            try:
                httpd.handle_request()
            except:
                obj.lb_status.set_label("Status: Ups we're  problems")
                        
        obj.lb_status.set_label("Status: Off")
        obj.bt_start.set_sensitive(True)        
        
    except:
        for i in range(sec):
            if obj.isBreake: break
            obj.lb_status.set_label("Status: Port busy... wating %s seconds" % (sec - i) )
            time.sleep(1)
        
        if not obj.isBreake:
            handle_server(port, obj, sec + 5)            
        else:
            obj.lb_status.set_label("Status: Off") 
            obj.bt_start.set_sensitive(True)           
        
        
class GUI:        
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.window = self.builder.get_object("winshare")
        self.fc_path = self.builder.get_object("fc_path")
        self.bt_start = self.builder.get_object("bt_start")
        self.ad_port = self.builder.get_object("ad_port")
        self.lb_status = self.builder.get_object("lb_status")
        
        self.port = 8000
        self.isActive = False        
        self.isBreake = False
        self.ip = get_ip_address(INTERFACE)        
        
        self.window.connect("destroy", self.exit)
        self.bt_start.connect("clicked", self.start)
        self.ad_port.set_value(self.port)
        
    def start(self, widget=None):        
        
        if self.isActive == False:
            self.port = int(self.ad_port.get_value())
            self.isActive = True
            
            path_select = self.fc_path.get_current_folder()        
            os.chdir(path_select)
            
            threadserver = threading.Thread(target=handle_server, args=(self.port, self, 10, ))
            threadserver.start()
                
            self.bt_start.set_label("Stop")
            self.isBreake = False
        else:            
            self.isActive = False            
            self.isBreake = True
            self.bt_start.set_label("Start")
            self.lb_status.set_label("Status: %s" % ("Stopping Server..."))            
            self.bt_start.set_sensitive(False)
            webbrowser.open("http://127.0.0.1:%s" % self.port)

    def exit(self, widget=None):                        
        self.isActive = False
        gtk.main_quit()
        

