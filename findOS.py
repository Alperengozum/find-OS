import platform

""" Just give 1 if you want this information.
    
"""


def get(system=1, release=0):
    if system == 1 and release == 1:
        if platform.system()=="Darwin":
            system_name="MacOS"
        else :
            system_name=platform.system()
        info = system_name + platform.release()
    elif system == 1 and release == 0:
        if platform.system()=="Darwin":
            system_name="MacOS"
        else :
            system_name=platform.system()
        info = system_name
    elif system == 0 and release == 1:
        info = platform.release()

    return info



""" Please write what you want
    like windowsxp / MacOS19.6.0 / macos / windows / linux
    returns True or Error message"""
def control(want="linux"):

    want=want.lower()
    if want=="linux" or want=="windows" or want=="macos":
        system_name=get(1,0)
        print(system_name)
        system=system_name.lower()
        if system==want:
            return True
        else:
            return "This program just usable in: "+want+ "\nYou are using: " + system
    else:
        system_name=get(1,1)
        system = system_name.lower()

        if system == want:
            return True
        else:
            return "This program just usable in: " + want + "\nYou are using: " + system



