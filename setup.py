from setuptools import setup

APP = ['neoos.pyw']
DATA_FILES = ['nube.png']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'NeoOS',
        'CFBundleDisplayName': 'NeoOS Alpha',
        'CFBundleIdentifier': 'com.neoos.alpha',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)