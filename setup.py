# GitPullBot Dependencies   

import subprocess

# List of modules to be installed
modules_to_install = [
    'colorama',
    'PyGithub',
    'openai'
]

def install_modules():
    for module in modules_to_install:
        try:
            subprocess.run(['pip', 'install', module])
        except:
            subprocess.run(['pip3', 'install', module])


if __name__ == "__main__":
    install_modules()
