python related:
    python version 3.6.1
    
    use pip install -r requirements.txt to install related package
    
    !report use https://github.com/TesterlifeRaymond/BeautifulReport, can not use pip to install package

1. test web reqiure

    for test it need to download Fixfox(Chrome, etc) Browser and
    related driver like resource/web_driver/firefox/geckodriver-v0.24.0-linux64.tar.gz

    can see detail in https://www.seleniumhq.org/download/

    use python /bin/web.py to run test and get report

2. test app require

    android sdk (8.0 and 9.0), need set the env variable
    
    jdk(1.8.0_201), need set the env variable
    
    node https://nodejs.org/en/ (v10.6.0 or higher)
    
    chooce one(appium or appium-destop)
        1. appium, https://pypi.org/project/Appium-Python-Client/#files
        2. appium-destop, https://github.com/appium/appium-desktop/releases/tag/v1.12.0

    for test it need to run `appium` in a new terminal

    use python /bin/app.py to run test and get report


project structure introduce

```
.
├── bin                     -- run test(app, web) shell
├── devices_info.json       -- the test device info(name, password)
├── page                    -- page with some element and logic
├── plex                    -- public method etc
├── report                  -- report output(include log image, etc)
├── requirements.txt        -- pip install file
├── resource                -- put some driver and app package on it
├── settings.py             -- base setting file
├── test                    -- test code
├── users_info.json         -- the test user info(name, password)
```
