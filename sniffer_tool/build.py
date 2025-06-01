import PyInstaller.__main__
import sys
import os

def build_windows():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--name=NetworkSniffer-Windows',
        '--icon=resources/sniffer.ico',
        '--uac-admin',
        '--add-binary=npcap-sdk/wpcap.dll;.',
        '--add-binary=npcap-sdk/packet.dll;.',
        '--clean'
    ])

def build_linux():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--name=NetworkSniffer-Linux',
        '--icon=resources/sniffer.ico',
        '--clean'
    ])

def build_mac():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--name=NetworkSniffer-Mac',
        '--icon=resources/sniffer.icns',  # Note: Mac uses .icns format
        '--clean'
    ])

def build_all():
    print("Building for Windows...")
    build_windows()
    
    print("Building for Linux...")
    build_linux()
    
    print("Building for Mac...")
    build_mac()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        platform = sys.argv[1].lower()
        if platform == "windows":
            build_windows()
        elif platform == "linux":
            build_linux()
        elif platform == "mac":
            build_mac()
        else:
            print("Invalid platform. Use: windows, linux, or mac")
    else:
        build_all()