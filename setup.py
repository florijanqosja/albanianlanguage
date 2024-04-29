from setuptools import setup, find_packages

setup(
    name='albanianlanguage',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        # none so fas
    ],
    author='Florijan Qosja',
    package_data={'albanianlanguage': ['words.csv']},
    author_email='florijanqosja@gmail.com',
    description='A package with a few functionalities for the albanian language.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/florijanqosja/albanianlanguage',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
