from cx_Freeze import setup, Executable

setup(
    name="Casino",
    version="2.2-2",
    description="Version that should work",
    executables=[Executable("main.py")]
)
