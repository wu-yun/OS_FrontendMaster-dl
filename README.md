# Front-end Master Video Downloader

The default behavior of the script is to fetch and download **all** available courses. It is a time consuming process (about 30 minutes) since it use GUI browser to do the crawling. 

You can optionally download the individual course you want after you have the `DATA_COURSEDETAILED_LIST_CDN.json` file.

NOTE: 

This assumes you have got a Frontend Master account with subscription

Please do NOT spread the downloadable links to others. Please keep you subscription to continue supporting [FrontendMaster](https://frontendmasters.com/) and getting updates from them.

## Usage

**Requirements**

- Python 2.7
- Google Chrome

```python
# Step 0: Install Google Chromedriver
# The latest version can be found at 
# https://sites.google.com/a/chromium.org/chromedriver/downloads

# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Edit account info. in config.sample.py
# Step 3: Rename config.sample.py -> config.py

# Step 4: Run script
python run.py

# Step 5: Happy hacking!
# Find all the courses videos inside `Download` folder inside project directory
```

## Special Thanks

Thanks [@andreiglingeanu](https://github.com/andreiglingeanu) for his kindness.
