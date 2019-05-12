import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='Tower_defence_Golear_Karpenko',
    version='0.2.9',
    author="Golear_Karpenko",
    author_email="golyar.d@gmail.com",
    description="Simple tower defence game built on PyGame",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests']),
    package_dir={'': '.'},
    package_data={
        'Tower_defence_Golear_Karpenko': [
            'assets/towers/*',
            'assets/sounds/*',
            'assets/images/towers/*',
            'assets/images/*',
            'assets/images/buttons/*',
            'assets/worlds/*']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
    ],
    install_requires=['pygame'],
    entry_points={
        'console_scripts': [
            'tower_defence=Tower_defence_Golear_Karpenko.__main__:main'
        ]}
)
