import re

class Text:

	@staticmethod
	def condensate(txt):
		"""
			Returns a condensed version of the given string, trimming, removing line breaks and multiple spaces
		"""
		s = txt.strip()
		s = Text.removeLineBreaks(s)
		s = Text.removeMultipleSpaces(s)
		return s
		
	@staticmethod
	def removeLineBreaks(txt):
		return txt.replace('\n', ' ').replace('\r', '')
		
	@staticmethod
	def removeMultipleSpaces(txt):
		return re.sub("[\s]+", " ", txt)

	@staticmethod
	def repeat(txt, times):
		return "".join(txt for a in range(times))