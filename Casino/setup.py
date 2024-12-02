from cx_Freeze import setup, Executable

setup(
    name="Casino",
    version="1.0",
    description="Program symulating a casino",
    executables=[Executable("main.py")]
)
