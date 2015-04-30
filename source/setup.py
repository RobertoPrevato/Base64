import sys
from cx_Freeze import setup, Executable

# run like this:
#
# Linux:
# sudo python setup.py build
#
# Windows: (with right Python version inside the path)
# C:\Python34\python setup.py build
#
build_exe_options = {"packages": ["os", "core", "lib"] }

# NB: change executable to have the right path for you!
executablePath = "C:\\Root\\Projects\\Base64\\source\\base64-pics.py"

setup(
	name = "Base64Pics",
	version = "1.0",
	description = "Pictures to base64 encoded bulk converter. Converts pictures into css properties containing the Base64 encoded string.",
	options = {"build_exe": build_exe_options},
	executables = [Executable(executablePath)]
)
