# Front-end Masters Video Downloader

This command-line tool requires a Front-end Masters subscription. Go to [Enroll Page](https://frontendmasters.com/enroll/) to subscribe (39USD/month).

> Front-end Masters is expert front-end training fro you to master building quality web interfaces.
> All video contents' Copyright belongs to MJG International.

Please open an new issue if you have problem to use this tool.

Note: This cli tool does NOT support Window OS yet.

### Usage

<img src="./img/screenshot.png" align="center">

<img src="./img/course_id.png" align="cetner">

To get help information,

```bash
python frontendmasters-dl.py --help

Usage: frontendmasters-dl.py [OPTIONS]

Options:
  --course TEXT    Course ID (e.g. `firebase-reac`)
  --id TEXT        Frontend Master Username
  --password TEXT  Frontend Master Password
  --help           Show this message and exit.
```

To start downloading course,

```bash
python frontendmasters-dl.py --id YOUR-USERNAME --password YOUR-PASSWORD --course COURSE-ID
```

Alternatively you can use interactive prompt by running the script directly,

```bash
python frontendmasters-dl.py
```

The default download path is `./Download` inside the repository directory.

**Requirements**

- Python 2.7
- Google Chrome

### Change Log

[01/04/2017] - Convert the existing script into command-line tool

### TODOs

- [ ] Support Window OS
- [ ] Support download all available courses
- [ ] Switching to `setuptools`

As always PR of any kind is always welcomed! :rocket:

### LICENSE

```
WWWWWW||WWWWWW
 W W W||W W W
      ||
    ( OO )__________
     /  |           \
    /o o|    MIT     \
    \___/||_||__||_|| *
         || ||  || ||
        _||_|| _||_||
       (__|__|(__|__|
```

The MIT License (MIT)

Copyright (c) 2017 Li Xinyang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
