import sys
from cx_Freeze import setup, Executable

path = sys.path
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "pygame", "pytest", ],
                     "include_files": ["structures", "pictures", "maps", "test"],
                     "excludes": ["tkinter"],
                     "path": path, "optimize": 2}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
icone = None
if sys.platform == "win32":
    icone = "icone.ico"
    base = "Win32GUI"

setup(name="game.py",
      version="0.1",
      description="Mac gyver rules",
      options={"build_exe": build_exe_options},
      executables=[Executable("game.py", base=base, icon=icone)]
      )
