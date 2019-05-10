import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name='serverpath',

    version='0.1.2',

    author="Luke DeLuccia",

    author_email="deluccial@gmail.com",

    description="Platform-independent server-share path discovery.",

    long_description=long_description,

    long_description_content_type="text/markdown",

    py_modules=['serverpath'],

    packages=setuptools.find_packages(),

    url="https://github.com/deluccial/serverpath.git",

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

)
