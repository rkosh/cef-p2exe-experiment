import win32_ctypes
import win32_ui


win32_ctypes.RunWin32Gui()
print "Enumerating all windows..."
win32_ui.TestEnumWindows()
print "Testing drawing functions ..."
win32_ui.TestSetWorldTransform()
win32_ui.TestGradientFill()
print "All tests done!"