from setuptools import setup, find_packages

setup(
    name="network-sniffer",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'scapy>=2.5.0',
        'colorama>=0.4.6',
        'PyInstaller>=5.13.0'
    ],
    author="Your Team Name",
    author_email="team@example.com",
    description="A powerful network packet sniffer for network analysis and monitoring",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/network-sniffer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Topic :: System :: Networking :: Monitoring",
    ],
    entry_points={
        'console_scripts': [
            'network-sniffer=sniffer_tool.main:main',
        ],
    },
    python_requires='>=3.7',
)