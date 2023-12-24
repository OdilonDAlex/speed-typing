# ----------------------------------------- #
# Module who create the app executable file #
# ----------------------------------------- #
import os
import sys

from cx_Freeze import setup, Executable

files = ["speedTyping.ico"]

target = Executable(
    script="app.py",
    base="Win32GUI",
    icon="speedTyping.ico"
)

setup(
    name="SpeedTyping",
    version="0.0.0.1",
    description = "nothing special...",
    author="NOMENJANAHARY Odilon D'Alex",
    options={'build_exe' : {'include_files' : files}},
    executables = [target]
)