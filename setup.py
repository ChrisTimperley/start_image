import glob
import setuptools

setuptools.setup(
    name='start_image',
    version='0.0.1',
    description='Manages the Docker images used by START',
    author='Chris Timperley',
    author_email='christimperley@gmail.com',
    url='https://github.com/ChrisTimperley/start-image',
    install_requires=['docker'],
    include_package_data=True,
    packages=['start_image'],
    package_data={'': ['Dockerfile', 'Dockerfile.scenario']},
    entry_points = {
        'console_scripts': [ 'start-image = start_image.cli:main' ]
    }
)