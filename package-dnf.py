import os
print("1(Install App")
print("2(Uninstall App")
print("3(Install Rpm Files")
print("4(Update System")
print("5(Upgrade System")
tool = input("Enter Tool Number:")
if tool == "1":
    appinstall = input("Enter Command For Install:")
    os.system(appinstall)
    print("Your App Was Installed.")
if tool == "2":
    appuninstall = input("Enter Command For Uninstall:")
    os.system(appuninstall)
    print("Your App Was Uninstalled.")
if tool == "3":
    rpmfiles = input("Enter Command For Install Rpm Files:")
    os.system(rpmfiles)
    print("Your Rpm File Was Installed.")
if tool == "4":
           continueyn = input("continue<y n>?:")
           if continueyn == "y":
                os.system("sudo dnf update")
           if continueyn == "n":
                os.system("clear; exit")
if tool == "5":
     continueyn2 = input("continue<y n>:")
     if continueyn2 == "y":
          os.system("sudo dnf upgrade")
     if continueyn2 == "n":
          os.system("clear; exit")