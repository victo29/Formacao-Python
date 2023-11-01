from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()
    
with open('requeriments.txt', 'r') as f:
    requeriments = f.read().splitlines()

setup(
    name='image_processing',
    version='0.0.1',
    long_description=page_description ,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires =requeriments,
    python_requires='>=3.8'
    
)