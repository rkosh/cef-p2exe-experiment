import platform
import sys
import urllib
import json
import os

from cefpython3 import cefpython as cef

def main():
	root_path = os.getcwd()
	appSettings = dict()
	appSettings["locales_dir_path"] = os.path.join(root_path, "lib")
	appSettings["resources_dir_path"] = appSettings["locales_dir_path"]
	appSettings["log_file"] = os.path.join(root_path, "cef_out.txt")
	appSettings["browser_subprocess_path"] = os.path.join(root_path, "lib", "subprocess.exe")

	sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
	cef.Initialize(appSettings)
	cef.CreateBrowserSync(url="https://www.google.com/", window_title="Hello World!")
	cef.MessageLoop()
	cef.Shutdown()

if __name__ == "__main__":
	main()
