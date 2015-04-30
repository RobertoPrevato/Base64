# Scribe class
import io
import sys

isPython3 = sys.version_info >= (3, 0)

class Scribe:

	@staticmethod
	def readTextFile(path):
		with io.open(path, mode="rt", encoding="utf-8") as f:
			s = f.read()
			# go to beginning
			f.seek(0)
		return s
		
	@staticmethod
	def readBeginning(path, lines):
		with io.open(path, mode="rt", encoding="utf-8") as f:
			s = f.read(lines)
			# go to beginning
			f.seek(0)
		return s
	
	@staticmethod	
	def readTextFileLines(path):
		with io.open(path, mode="rt", encoding="utf-8") as f:
			content = f.readlines()
		return content
		
	@staticmethod
	def saveTextFile(contents, path):
		if isPython3:
			with open(path, mode="wt", encoding="utf-8") as f:
				# truncate previous contents
				f.truncate()
				f.write(contents)
		else:
			with io.open(path, mode="wt", encoding="utf-8") as f:
				# truncate previous contents
				f.truncate()
				f.write(contents.decode("utf8"))

	@staticmethod
	def saveTextFileLines(lines, path):
		if isPython3:
			with open(path, mode="wt", encoding="utf-8") as f:
				f.writelines(lines)
		else:
			with io.open(path, mode="wt") as f:
				for line in lines:
					f.writelines(line.decode("utf8"))

	@staticmethod
	def addContentToFile(contents, path):
		if isPython3:
			with open(path, mode="a", encoding="utf-8") as f:
				f.writelines(contents)
		else:
			with io.open(path, mode="a") as f:
				f.writelines(contents.decode("utf8"))