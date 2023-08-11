import os
print("1(Install App")
print("2(Uninstall App")
print("3(Install Deb Files")
print("4(Update System")
print("5(Upgrade System")
tool = input("Enter Tool Number:")
if tool == "1":
       appinstallname = input("Enter Command For Install:")
       os.system(appinstallname)
       print("Your App Was Installed.")
if tool == "2":
     appuninstallname = input("Enter Command For Uninstall App:")
     os.system(appuninstallname)
     print("Your App Was Deleted.")
if tool == "3":
    installdebfiles = input("Enter Command For Install Deb Files:")
    os.system(installdebfiles)
    print("Your Deb File Was Installed.")
if tool == "4":
       continueyn = input("continue<y n>?:")
       if continueyn == "y":
            os.system("sudo apt update")
       if continueyn == "n":
            os.system("clear; exit")
if tool == "5":
     continueyn2 = input("continue<y n>:")
     if continueyn2 == "y":
          os.system("sudo apt upgrade")
     if continueyn2 == "n":
          os.system("clear; exit")
