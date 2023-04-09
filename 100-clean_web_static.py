#!/usr/bin/python3
""" Cleans old and outdated files """

from fabric.api import *
import os
from datetime import datetime
import tarfile


env.hosts = ["54.236.12.160", "100.26.158.11"]
env.user = "ubuntu"


def do_clean(number=0):
	"""" Removes all but the wanted number of archives """
	number = int(number)
	if number < 2:
		number = 1
	number += 1
	number = str(number)
	with lcd("versions"):
		local("ls -lt | grep web_static_.*\.tgz | tail -n +" +
		        number + " | xargs -I {} rm -- {}")
	with cd("/data/web_static/releases"):
		run("ls -lt | grep web_static_ | tail -n +" +
		     number + " | xargs -I {} rm -rf -- {}")	
