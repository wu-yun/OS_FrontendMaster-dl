import click
from extractor.spider import Spider

@click.command()
@click.option('--course', prompt='Course ID', help='Course ID (e.g. `firebase-react`)')
@click.option('--id', prompt='Username', help='Frontend Master Username')
@click.option('--password', prompt='Password', help='Frontend Master Password')
def downloader(id, password, course):
    spider = Spider()
    click.secho('>>> Login with your credential', fg='green')
    spider.login(id, password)

    click.secho('>>> Downloading course: ' + course, fg='green')
    spider.download(course)

    click.secho('>>> Download Completed! Thanks for using frontendmasters-dl', fg='green')

# TODO: (Xinyang) Switching to setuptools
#   http://click.pocoo.org/5/quickstart/#switching-to-setuptools
if __name__ == '__main__':
    downloader()
