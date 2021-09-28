import os

def verify_env():

    requirements = open("requirements.txt", "r").read().splitlines()
    env_pkg = []
    is_pkgs_installed = True
    isPkgInstalled = False
    
    for aline in requirements:
        requiremnts = aline.strip()
        env_pkg.append(requiremnts)

    installed = []
    installed = os.popen('pip list').read().split()

    for package in env_pkg:
        if package in installed:
            isPkgInstalled = True
        else:
            is_pkgs_installed = False
            isPkgInstalled = False
        if isPkgInstalled is False:
            print(f"{package} is not installed!")
            
    assert(is_pkgs_installed == True)