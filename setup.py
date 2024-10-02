from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cw-cli",
    version="0.1.0",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=[
        "requests==2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "cw=cw_cli.main:main",
        ],
    },
    python_requires='>=3.6',
    author="Kus Cámara",
    author_email="kcmr@users.noreply.github.com",
    description="Una herramienta CLI para comprobar cambios en sitios web",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kcmr/cw-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
