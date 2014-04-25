from setuptools import setup

setup(
    name='sphinxapi',
    version='2.1.7-release',
    description='Sphinx search official client',
    long_description=open('README.md').read(),
    author='Sphinx Technologies Inc',
    url='http://github.com/Romamo/sphinxapi',
    license='GPL',
    packages=('sphinxapi',),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
