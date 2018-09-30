import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tmx2dataframe',
    version='0.1',
    description='Converting tmx translation files to pandas dataframe',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/jaderabbit/tmx2dataframe',
    author='Jade Abbott',
    author_email='jade.zoe.abbott@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])
