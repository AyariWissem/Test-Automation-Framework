Setting up the Selenium and Appium Development environment 
==========================================================

Step 1: installing the software requirements:

- Python 3                              https://www.python.org/downloads/
- Pycharm Community Edition             https://www.jetbrains.com/fr-fr/pycharm/download/
- node.js                               https://nodejs.org/en/download/
- Appium Desktop		        https://github.com/appium/appium-desktop/releases/latest						
     
----------------------------------------------------------

Step 2: installing the packages/libraries through the CLI of your OS


 Library Name:             | Command for installing (To run on the CLI of your OS) 
                           | 
 selenium                  | pip install selenium
 Appium-Python-Client      | pip install Appium-Python-Client
 pytest                    | pip install pytest
 pytest-html               | pip install pytest-html
                           |
 Appium node module        | npm install -g appium

***  Dealing with proxies:  ***
 >using the Package Installer for Python (pip):
	Simply add the proxy argument to each command :
        "--proxy http://web-proxy.mydomain.com"
 Example: "pip install --proxy http://user:password@proxyserver:port LibraryName"
 
 >using the Node Package Manager (npm):
	You should run these two commands on the CLI : 
         "npm config set proxy http://<username>:<password>@<proxy-server-url>:<port>"
         "npm config set https-proxy http://<username>:<password>@<proxy-server-url>:<port>"
 
----------------------------------------------------------
When creating scripts in a new project:

Step 3: Pycharm:: Enable Pytest for your project﻿
1. Open the Settings/Preferences | Tools | Python Integrated Tools settings dialog as described in Choosing Your Testing Framework.
2. In the Default test runner field select pytest.
3. Click OK to save the settings.
4. create your python script using the pytest format. https://docs.pytest.org/en/latest/
5. right click on the opened script file and click on 'run pytest in ..'

----------------------------------------------------------

Other requirements:
- Selenium components drivers: download the drivers necessary for the target browser. 
(bottom of the page)          https://www.selenium.dev/downloads  
