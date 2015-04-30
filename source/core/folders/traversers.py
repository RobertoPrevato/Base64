import os
import re
from os import listdir
from os.path import isfile, join, isdir

class Traverser:
	#__init__ is an initializer, not a constructor
	def __init__(this, ext):
		#if ext[:1] == ".":
		#	ext = ext[1:]
		this.ext = ext
		
	def includeFile(this, f):
		p = re.compile("\.{}$".format(this.ext), re.IGNORECASE)
		return p.search(f) is not None
		
	def getFiles(this, path):
		#if path[:1] == os.sep:
		#	path = path[1:]
		a = [ path + os.sep + f for f in listdir(path) if (isfile(join(path, f)) and this.includeFile(f))]
		dr = [ f for f in listdir(path) if isdir(join(path, f)) ]
		for b in dr:
			a = a + this.getFiles(path + os.sep + b)
		return a
		
class JsTraverser(Traverser):
	def __init__(this):
		this.ext = "js"
		
	def includeFile(this, f):
		p = re.compile("\.{}$".format(this.ext), re.IGNORECASE)
		return p.search(f) is not None and not "main.built.js" in f.lower()
		
class TxtTraverser(Traverser):
	def __init__(this):
		this.ext = "txt"
		
	def includeFile(this, f):
		p = re.compile("\.txt$", re.IGNORECASE)
		return p.search(f) is not None
		
class CsvTraverser(Traverser):
	def __init__(this):
		this.ext = "csv"
		
	def includeFile(this, f):
		p = re.compile("\.csv$", re.IGNORECASE)
		return p.search(f) is not None
		
class HtmlTraverser(Traverser):
	def __init__(this):
		this.ext = "html"
		
	def includeFile(this, f):
		p = re.compile("\.html$|\.htm$", re.IGNORECASE)
		return p.search(f) is not None

class HbsTraverser(Traverser):
	def __init__(this):
		this.ext = "hbs"

	def includeFile(this, f):
		p = re.compile("\.hbs", re.IGNORECASE)
		return p.search(f) is not None

class PicsTraverser(Traverser):
	def __init__(this):
		this.ext = ";".join(['jpg', 'jpeg', 'jpe', 'png'])
		
	def includeFile(this, f):
		p = re.compile("\.jpg$|\.jpeg$|\.jpe$|\.png$|\.gif$", re.IGNORECASE)
		return p.search(f) is not None
