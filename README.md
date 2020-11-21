# Automated quarantine attestation filling

Python script triggered by Google Assistant voice command which automatically fills a Covid-19 attestation to go out during quarantine (official attestation only valid in France, available at https://media.interieur.gouv.fr/deplacement-covid-19/).


## Requirements : 

This program was written on MacOS Catalina 10.15.1 with Visual Studio Code, using Python 3.7.6 and tested on a Lenovo Smart Clock with Google Assistant. To check your current version of Python, run `python --version` in your terminal. If pip is not already installed, run : `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` (for more information, see https://pypi.org/).

Then : 
```
pip install selenium
```
`email` and `smtplib` packages are already in Python standard library. 

To install the latest version of Homebrew if not already done, run : `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`, and install chromedriver with `brew cask install chromedriver`.



