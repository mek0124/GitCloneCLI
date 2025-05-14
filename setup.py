# setup.py
from setuptools import setup, find_packages

setup(
    name="git-clone",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click==8.2.0",
    ],
    entry_points={
        "console_scripts": [
            "git-clone=app.app:app",
        ],
    },
    python_requires=">=3.7",
)