from setuptools import setup, find_packages

setup(
    name='stream-cli',
    version='1.0.0',
    author='Raja Ravi',
    author_email='r.rajaravi@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    description="""
stream-cli
==========

https://getstream.io/

https://pypi.org/project/stream-cli/

CLI for activity feed APIs

Getting it
~~~~~~~~~~

To download, either fork this github repo or simply use Pypi via pip.

.. code:: sh

   $ pip install stream-cli

Using it
~~~~~~~~

::

   Usage: stream_cli.py [OPTIONS] COMMAND [ARGS]...

   Options:
     -k, --api-key TEXT     getstream.io api key  [required]
     -s, --secret-key TEXT  getstream.io secret key  [required]
     -l, --location TEXT    getstream.io hosted location
     --help                 Show this message and exit.

   Commands:
     delete-activity-from-feed
     delete-all-activity-from-feed
     get-activities-from-feed
     get-followers
     get-notification-by-id
     remove-activity
     update-mark-seen
    """,
    install_requires=[
        'Click',
        'stream-python'
    ],
    url='https://github.com/rrajaravi/stream-cli.git',
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
    ],
    entry_points={
        'console_scripts': [
            'stream-cli = stream_cli.stream_cli:cli',
        ],
    },
)