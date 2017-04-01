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

### Special Thanks

- Thanks [@andreiglingeanu](https://github.com/andreiglingeanu) for his kindness.
