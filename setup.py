import setuptools

setuptools.setup( 
    name='testservice',
    version='0.0.1',
    author='Timo Thans',
    author_email='t.thans@primevision.com',
    description='cx test service',
    url='https://primevision.com',
    packages=['testservice'],
    zip_safe=True,
    architecture='amd64',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'sanic',
        'jinja2'
    ],
    license='Proprietary',
)