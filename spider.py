import cookielib
import mechanize
import json
import os
from bs4 import BeautifulSoup
from config import ACCOUNT
from urllib2 import urlopen, URLError, HTTPError


# Browser setup
cookiejar = cookielib.CookieJar()
browser = mechanize.Browser()
browser.set_cookiejar(cookiejar)

def login(username, password, browser=browser):
    BASE_URL = 'https://frontendmasters.com/login/'
    browser.open(BASE_URL)

    # Select the first form
    browser.select_form(nr=0)
    browser.form['rcp_user_login'] = username
    browser.form['rcp_user_pass'] = password
    browser.submit()
    return browser

def get_course_list(browser=browser):
    bs_course_page = BeautifulSoup(browser.response().read(), "html.parser")
    course_titles = bs_course_page.find_all('h2')
    course_links = []

    for title in course_titles:
        link = title.find('a')

        if link is not None:
            course = {
                'title': link.getText(),
                'url': link['href']
            }

            course_links.append(course)

    return course_links

def get_videos_data(videos_section_items):
    subsections = []

    for video in videos_section_items:
        # Course subsection data structure
        course_subsection = {
            'title': None,
            'url': None,
            'downloadable_url': None
        }

        course_subsection['url'] = video.find('a')['href']
        course_subsection['title'] = video.find('a').find('span', {'class', 'text'}).find('span', {'class', 'title'}).getText()

        subsections.append(course_subsection)

    return subsections

def get_section_data(sections_items):
    sections = []

    for item in sections_items:
        # Course section data structure
        course_section = {
            'title': None,
            'subsections': []
        }

        course_section['title'] = item.find('h4', {'class': 'video-nav-section-title'}).getText()

        videos_section = item.find('ul')
        videos_section_items = videos_section.find_all('li')

        videos_data = get_videos_data(videos_section_items)
        course_section['subsections'].extend(videos_data)

        sections.append(course_section)

    return sections

def get_detailed_course_list(course_list, browser=browser):
    detailed_course_list = []

    for course in course_list:
        # Course detail data structure
        course_detial = {
            'title': None,
            'url': None,
            'sections': []
        }

        course_detial['url'] = course['url']
        course_detial['title'] = course['title']

        browser.open(course_detial['url'])
        soup_page = BeautifulSoup(browser.response().read(), 'html.parser')

        # Find video nav list
        sections = soup_page.find('ul', {'class': 'video-nav-list'})
        sections_items = sections.find_all('li', {'class': 'video-nav-section'})

        sections = get_section_data(sections_items)
        course_detial['sections'].extend(sections)

        detailed_course_list.append(course_detial)

    return detailed_course_list

def download_file(url, path):
    try:
        buff = urlopen(url)
        print "Downloading: %s" % (path)

        # Open file for writing
        with open(path, 'wb') as local_file:
            local_file.write(buff.read())

    except HTTPError, e:
        print "Error: ", e.code, url
    except URLError, e:
        print "Error: ", e.code, url

# Browser with all login info.
browser = login(ACCOUNT['username'], ACCOUNT['password'])

# Save data to file
with open('DATA.json', 'w') as file:
    course_list = get_course_list()
    detailed_course_list = get_detailed_course_list(course_list)
    file.write(json.dumps(detailed_course_list))


