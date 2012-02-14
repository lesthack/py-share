## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src 

py_sharedocdir = ${prefix}/doc/py_share
py_sharedoc_DATA = \
	README\
	COPYING\
	AUTHORS\
	ChangeLog\
	INSTALL\
	NEWS


EXTRA_DIST = $(py_sharedoc_DATA)


# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(py_sharedocdir)
