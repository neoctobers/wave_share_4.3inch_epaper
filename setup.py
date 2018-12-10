# coding:utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wave_share_4d3inch_epaper",
    version="1.0.3",
    author="@neoctobers",
    author_email="neoctobers@gmail.com",
    description="For WaveShare 4.3inch e-paper UART module.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neoctobers/wave_share_4.3inch_epaper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
