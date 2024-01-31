# Day 43
# Virtual Environment in python

# it is a tool to create a virtual environment so that you can use different versions and dependencies of python on the same machine.
# you can use different packages and many other different version of frameworks of python.
# What ever packages or any version of frameworks you install in your virtual environment it will not effect your main system.
# It is just you have a box with different shells and it is used for different works.


# To create a virtual environment.
# python -m venv 'filename'

# To activate the virtual environment in (linux, mac)
# source 'filename'/bin/activate

# To activate the virtual environment in windows
# 'filename'\scripts\activate.bat
# 'filename'\scripts\activate.ps1  in powershell.

# To close the virtual environment.
# deactivate

# let's suppose you want to send this virtual environment to your friends.
# Will you type or write the packages that you have installed in your virtual environment?
# No the simple way to do that is make a requirement.txt file.
# It will give you all the packages and its versions that you have installed in your virtual environment and your friends can easily install the required packages.

# To create requirement.txt
# pip freeze > requirement.txt

# To install the required packages.
# pip install -r requirement.txt