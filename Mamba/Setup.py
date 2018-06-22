import cx_Freeze
executables=[cx_Freeze.Executable("PyProject.py")]
cx_Freeze.setup(name="Mamba",options={"build_exe":{"packages":["pygame"],"include_files":["food.png","mamba.png","gm.jpg","gm1.jpg","oops.jpg","pause.png","head.png","startscreen.jpg"]}},description="Mamba Game",executables=executables)
