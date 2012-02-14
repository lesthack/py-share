## Process this file with automake to produce Makefile.in
## Created by Anjuta

uidir = $(datadir)/py_share/ui
ui_DATA = ../data/py_share.ui

## The main script
bin_SCRIPTS = py_share.py

## Directory where .class files will be installed
py_sharedir = $(pythondir)/py_share

EXTRA_DIST = $(ui_DATA)

py_share_PYTHON = \
	py_share.py

# Remove ui directory on uninstall
uninstall-local:
	-rm -r $(uidir)
	-rm -r $(datadir)/py_share
