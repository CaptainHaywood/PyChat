from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['dbm']}
setup(name='PyChat Server',
      version='1.0',
      options = {"build_exe": build_exe_options},
      description='The server for PyChat.',
      executables = [Executable("PyChat-Server.py")])
