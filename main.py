import win32_ctypes
import win32_ui
import cef_ui


win32_ctypes.RunWin32Gui()
print "Enumerating all windows..."
win32_ui.TestEnumWindows()
print "Testing drawing functions ..."
win32_ui.TestSetWorldTransform()
win32_ui.TestGradientFill()
print "All tests done!"
cef_ui.main() # py2exe fails during getting the dependencies
print "Everything went fine!"