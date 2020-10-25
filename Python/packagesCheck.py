import subprocess
import sys

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
counter = 0
for package in installed_packages:
    print(f'Package #{counter} - {package}')
    counter += 1
