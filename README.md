# Heroku Config
This python script helps you set all your heroku config vars directly from a .env file, instead of having to load them in one by one.
This script works especially for laravel, but can be used for any other environment, all you just need do is to have a `.env` file, and have your variables set like APP_NAME=your_app_name

### Requirements
* python runtime (2.7+)
* heroku toolbelt (CLI)
* A project already connected to heroku

### Installation and Usage
* Clone or download this repo, then copy the `heroku-config.py` file into the root directory of your project (or wherever your .env file is located)
* Or download the `heroku-config.py` directly from git into the same location as your .env file
- From the cmd, `cd` into the location of your .env file e.g ``cd C:/projects/your heroku project``
- Run `python heroku-config.py` . You should see your config vars getting set on after the other
- That's all

### Now you can spend your time saving the world instead of setting Config Vars.
