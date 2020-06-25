from setuptools import setup

with open("distributions/README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sse-distributions-42", # Replace with your own username
    version="0.2.1",
    author="Sudhakar",
    author_email="sudhakar@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)