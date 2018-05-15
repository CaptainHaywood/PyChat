from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['dbm']}
setup(name='PyChat Client',
      version='1.0',
      options = {"build_exe": build_exe_options},
      description='The client for PyChat.',
      executables = [Executable("PyChat-Client.pyw")])
