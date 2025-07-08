
from setuptools import setup
APP = ['app.py']
DATA_FILES = []
OPTIONS = { 'argv_emulation': True, 'iconfile': 'icon.icns', 'packages': ["tkinter","psutil"],
    'plist': {
        'CFBundleName': 'Myapp', 'CFBundleDisplayName': 'Myapp',
        'CFBundleIdentifier': 'com.htmltoapk.myapp',
        'CFBundleVersion': '0.1.0', 'CFBundleShortVersionString': '0.1.0',
    }
}
setup(app=APP, data_files=DATA_FILES, options={'py2app': OPTIONS}, setup_requires=['py2app'])
