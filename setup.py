#!/usr/bin/python

# This file is part of sendxmppy.
# Author: Denis Klimov

__author__ = "Denis Klimov"
__version__ = "0.4.1"
__date__ = "Mon Jan 25 11:34:38 YEKT 2010"
__copyright__ = "Copyright (c) 2009 Denis Klimov"
__license__ = "BSD"

from distutils.core import setup
from os.path import isfile, join, isdir
from sys import argv
from glob import glob

longdesc = '''XMPP message sender from CLI'''

setup(
	name = "sendxmppy", 
	version = __version__, 
	description = "XMPP message sender from CLI",
	long_description = longdesc, 
	author = __author__, 
	author_email = "zver@altlinux.org", 
	url = "http://git.altlinux.org/people/zver/packages/sendxmppy.git", 
	license = __license__, 
	platforms = "Posix", 
	scripts =	[
					'sendxmppy', 
				], 
)

