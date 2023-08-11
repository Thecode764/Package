import os
use = input("Use Redhat Linux?:")
if use == "yes":
    os.system("sudo dnf install pip")
    pip = input("Enter Command from pip:")
    os.system(pip) 
if use == "no":
    os.system("sudo apt-get install pip")
    pip = input("Enter Command from pip:")
    os.system(pip) 