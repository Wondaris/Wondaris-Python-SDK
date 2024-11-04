from setuptools import setup

setup(
    name='wondaris_sdk',
    version='1.0.0',
    url='https://github.com/Wondaris/Wondaris-Python-SDK',
    license='MIT',
    author='Wondaris Team',
    install_requires=[
        'tuspy',
    ],
    author_email='support@wondaris_sdk.com',
    description='A Python SDK for the Wondaris Services',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=['wondaris_sdk'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: File Transfer Protocol (FTP)',
        'Topic :: Communications :: File Sharing',
    ],
    python_requires=">=3.5.3",
)