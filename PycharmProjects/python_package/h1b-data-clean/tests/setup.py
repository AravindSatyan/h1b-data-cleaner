
from setuptools import setup, find_packages

setup(
    name='data_cleaner',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'data_cleaner=data_cleaner.data_clean:main',
        ],
    },
    author='Aravind Satyanarayanan',
    author_email='aravind.bedean@gmail.com',
    description='A package for cleaning data frames.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/data_cleaner',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
