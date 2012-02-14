#!/usr/bin/python
#
# main.py
# Copyright (C) Jorge Luis Hernandez 2012 <lesthack@gmail.com>
# 
# py-share is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# py-share is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

try:
    __file__
except NameError:
    pass
else:
    libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
    sys.path.insert(0, libdir)

from share import *

def main():
    app = GUI()
    app.window.show()
    gtk.gdk.threads_init()
    gtk.gdk.threads_enter()
    gtk.main()    
    gtk.gdk.threads_leave()
        
if __name__ == "__main__":
    sys.exit(main())
