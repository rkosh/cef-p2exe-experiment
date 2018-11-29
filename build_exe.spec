# -*- mode: python -*-
import os

block_cipher = None
cef_data_files = [
    "cef.pak",
    "cef_100_percent.pak",
    "cef_200_percent.pak",
    "cef_extensions.pak",
    "locales\\en-US.pak",
    "icudtl.dat",
    "natives_blob.bin",
    "snapshot_blob.bin",
    "subprocess.exe",
    "cefpython_py27.pyd",
    "chrome_elf.dll",
    "libcef.dll"

]

module = __import__("cefpython3")
cef_data_files_paths = [
    (os.path.join(module.__path__[0], cef_file), "lib") for cef_file in cef_data_files
]

a = Analysis(['main.py'],
             pathex=['.\\'],
             binaries=[],
             datas=cef_data_files_paths,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
