from setuptools import setup, find_packages

setup(
    name='my-database-package',
    version='1.0.0',
    description='A package for simple database management with implementations for MySQL and MariaDB',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my-database-package',
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python',
        'mariadb',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)