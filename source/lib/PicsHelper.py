import os
import re
import base64
from core.folders import traversers as Traversers
from core.literature.scribe import Scribe

def generateBase64File(path, filename, mode):
	if mode is None:
		mode = "css"
	else:
		mode = mode.lower()
	#declare pics traverser
	t = Traversers.PicsTraverser()

	allPics = t.getFiles(path)
	l = len(allPics)
	if (l == 0):
		print("*" * 70)
		print("!!! no pictures found inside {}".format(path))
		print("*" * 70)
		return
	f = []
	
	for p in allPics:
		# get extension
		ext = os.path.splitext(p)[1]
		name = os.path.basename(p)
		print("...processing picture {}".format(name))
		
		if mode == "css":
			f.append("/* picture: {} */".format(name))
			f.append(".{} {}".format(name.replace(".", "-"), "{"))
			
			# picture:
			with open(p, "rb") as image_file:
				b = base64.b64encode(image_file.read())
				# decode b to utf-8 to obtain a string from bytes
				f.append("\tbackground-image: url(\"data:{0};base64,{1}\");".format(getDescriptorByExtension(ext), b.decode("utf-8")))
			
			f.append("}")
		elif mode == "csv":
			with open(p, "rb") as image_file:
				b = base64.b64encode(image_file.read())
				# decode b to utf-8 to obtain a string from bytes
				f.append("{},{}".format(name, b.decode("utf-8")))
		
	#save css file
	code = "\n".join(f)
	outputPath = os.path.join(path, filename) + "." + mode
	print("...saving file to {}".format(outputPath))
	Scribe.saveTextFile(code, outputPath)
			
def getDescriptorByExtension(ext):
	options = {
	".jpg" : "image/jpeg",
	".jpeg" : "image/jpeg",
	".jpe" : "image/jpeg",
	".jif" : "image/jpeg",
	".jfif" : "image/jpeg",
	".jfi" : "image/jpeg",
	".png" : "image/png",
	".gif" : "image/gif",
	}
	k = options.get(ext.lower())
	if k is None:
		raise Exception("Only Jpeg, Png and Gif images are supported.")
	return k
