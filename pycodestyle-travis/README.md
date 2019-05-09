[![Build Status](https://img.shields.io/travis/TravisToolbox/pycodestyle-travis/master.svg)](https://travis-ci.org/TravisToolbox/pycodestyle-travis)
[![Software License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)
[![Release](https://img.shields.io/github/release/TravisToolbox/pycodestyle-travis.svg)](https://github.com/TravisToolbox/pycodestyle-travis/releases/latest)
[![Github commits (since latest release)](https://img.shields.io/github/commits-since/TravisToolbox/pycodestyle-travis/latest.svg)](https://github.com/TravisToolbox/pycodestyle-travis/commits)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/TravisToolbox/pycodestyle-travis.svg)](https://github.com/TravisToolbox/pycodestyle-travis)
[![GitHub contributors](https://img.shields.io/github/contributors/TravisToolbox/pycodestyle-travis.svg)](https://github.com/TravisToolbox/pycodestyle-travis)

Pycodestyle for Travis 
==================

A tool to run pycodestyle against your python code within travis.ci pipelines.

## Scripts

- The `install.sh` script will install pycodestyle (and any other requirements).
- The `scan.sh` will scan all python files with pycodestyle. Python files are 'identifed' as files with a .py suffix.

## Usage

Making use of this tool as simple just add the following to your .travis.yml file. This will clone
the latest version of the code each time the pipeline runs.

```yml
    before_install:
      - git clone https://github.com/TravisToolbox/pycodestyle-travis.git
    install:
      - ./pycodestyle-travis/install.sh
    script:
      - ./pycodestyle-travis/scan.sh
```

## Advanced Usage

If you are writing django or flask based code then you may well not want to add a script interpreter line to the top of the file. It is possible to tell the scanner to skip this check.

```yml
    env: SKIP_INTERPRETER=true

    before_install:
      - git clone https://github.com/TravisToolbox/pycodestyle-travis.git
    install:
      - ./pycodestyle-travis/install.sh
    script:
      - ./pycodestyle-travis/scan.sh
```

## Example output

```
Linting all *.py files
We will test to ensure the script interpreter is set to python
 [ Info ] Linting tests/test.py (executable)
 [  OK  ] Linting successful for tests/test.py
```

The scanner will tell you if it is testing or skipping the script interpreter or not (see line 2 of the output), it will also tell if you a script has the exxecute permission
set or not.

## Deprecated

Using the travis toolbox scripts but adding them as git submodules is now no longer the recommended method.
