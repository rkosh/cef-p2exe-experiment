import os
from distutils.core import setup
from glob import glob

import py2exe  # noqa

tmp_dist_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dist")


class Target(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # For the version info resources.
        self.name = "Some name"
        self.company_name = "Lame"


data_files = []
data_files.append(
    (
        "lib",
        glob(
            r"C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*"
        ),
    )
)
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
]

module = __import__("cefpython3")
cef_data_files_paths = [
    os.path.join(module.__path__[0], cef_file) for cef_file in cef_data_files
]
data_files.append(("lib", cef_data_files_paths))
options = dict(
    dist_dir=tmp_dist_dir,
    optimize=2,
    bundle_files=3,
    dll_excludes=[
        "w9xpopen.exe",
        "msvcp100.dll",
        "msvcp140.dll",
        "msvcr100.dll",
        "msvcr140.dll",
        "msvcr71.dll",
        "python34.dll",
        "python35.dll",
        "python36.dll",
        "python37.dll",
        "vcruntime140.dll",
        "api-ms-win-core-io-l1-1-0.dll",
        "api-ms-win-core-heap-l2-1-0.dll",
        "api-ms-win-core-registry-l1-1-0.dll",
        "api-ms-win-service-management-l1-1-0.dll",
        "api-ms-win-security-base-l1-1-0.dll",
        "api-ms-win-core-crt-l2-1-0.dll",
        "api-ms-win-core-delayload-l1-1-0.dll",
        "api-ms-win-core-crt-l1-1-0.dll",
        "api-ms-win-core-heap-obsolete-l1-1-0.dll",
        "api-ms-win-core-delayload-l1-1-1.dll",
        "api-ms-win-core-libraryloader-l1-2-0.dll",
        "api-ms-win-core-shlwapi-legacy-l1-1-0.dll",
        "api-ms-win-core-psapi-l1-1-0.dll",
        "api-ms-win-core-string-obsolete-l1-1-0.dll",
        "api-ms-win-core-kernel32-legacy-l1-1-0.dll",
        "api-ms-win-core-libraryloader-l1-2-1.dll",
        "api-ms-win-core-datetime-l1-1-1.dll",
        "api-ms-win-core-windowserrorreporting-l1-1-0.dll",
        "api-ms-win-core-localization-l1-2-2.dll",
        "api-ms-win-core-apiquery-l1-1-0.dll",
    ],
)

main_exe = Target(
    description="Some Name",
    version="1.2.3.4",
    script="main.py",
    icon_resources=[(0, "app.ico")],
    dest_base="main",
)

setup(
    zipfile="lib/modules.zip",
    data_files=data_files,
    options=dict(py2exe=options),
    windows=[main_exe],
)
