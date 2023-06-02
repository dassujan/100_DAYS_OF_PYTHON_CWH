import shutil
import os

# shutil.copy("main.py", "main2.py")
# shutil.copy2("main.py", "main2.py")
# shutil.copytree("tutorial", "mytutorial")
shutil.move("tutorial/file.file", "file.file")
# shutil.rmtree("mytutorial")
os.remove("file.file")

# shutil.make_archive("mytutorial", "zip", "tutorial")
# shutil.unpack_archive("mytutorial.zip", "mytutorial")