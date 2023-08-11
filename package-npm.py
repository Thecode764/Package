import os
use = input("Use Redhat Linux:")
if use == "yes":
    os.system("sudo dnf install npm")
    npm = input("Enter Command From npm:")
    os.system(npm)
    if use == "no":
        npm = input("Enter Command From npm:")
        os.system(npm)