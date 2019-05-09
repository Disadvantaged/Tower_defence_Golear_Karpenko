import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Tower_defence_Golear_Karpenko',
    version='0.2',
    author="Golear_Karpenko",
    author_email="golyar.d@gmail.com",
    description="Simple tower defence game built on PyGame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests']),
    package_dir={'': '.'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
    ],
    install_requires=['pygame'],
    entry_points={
        'console_scripts':[
        'main=Tower_defence_Golear_Karpenko.__main__:main'
        ]}
)
