from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['dbm']}
setup(name='PyChat Server Wizard',
      version='1.0',
      options = {"build_exe": build_exe_options},
      description='The configuration wizard for PyChat Server',
      executables = [Executable("PyChat-Server-Wizard.py")])
