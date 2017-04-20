import os
import subprocess

def download():
    if not os.path.exists('of.zip'):
        subprocess.call(['wget', 'http://openframeworks.cc/versions/v0.9.8/of_v0.9.8_osx_release.zip', '-O', 'of.zip'])
    else:
        print 'of.zip already exists'

def extract():
    subprocess.call(['unzip', 'of.zip'])
    subprocess.call(['cp', '-p', 'of_v0.9.8_osx_release/*', '.'])
    subprocess.call(['rm', '-rf', 'of_v0.9.8_osx_release'])


download()
extract()
