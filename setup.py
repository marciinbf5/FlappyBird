from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["pygame", "neat"], "include_files": [("imgs/transferir.png", "imgs/transferir.png"), ("config.txt", ".")]}

setup(
    name="Flappy bird IA",
    version="0.1",
    description="Flappy Bird IA",
    options={"build_exe": build_exe_options},
    executables=[Executable("flappybird.py.", base="Win32GUI")]
)
