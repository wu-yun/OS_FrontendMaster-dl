from bs4                             import BeautifulSoup
from selenium                        import webdriver
from selenium.webdriver.common.keys  import Keys
from urllib2                         import urlopen, URLError, HTTPError
from helper                          import *

import httplib
import cookielib
import json
import mechanize
import os
import time

# Constants
DATA_COURSE_LIST              = './DATA_COURSE_LIST.json'
DATA_COURSE_DETAILED_LIST_CDN = './DATA_COURSE_DETAILED_LIST_CDN.json'
URL_LOG_IN                    = 'https://frontendmasters.com/login/'
URL_COURSE_LIST               = 'https://frontendmasters.com/courses/'

class Spider(object):
    def __init__(self):
        self.browser = webdriver.Chrome()

    def login(self, id, password):
        self.browser.get(URL_LOG_IN)
        time.sleep(2)

        username_field = self.browser.find_element_by_id('rcp_user_login')
        password_field = self.browser.find_element_by_id('rcp_user_pass')

        username_field.send_keys(id)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    def download(self, course):
        # Get detailed course list
        course_detailed_list = self._get_detailed_course_list(course)

        # Get downloadable CDN
        course_downloadbale = self._get_downloadable_links(course_detailed_list)

        

        # Download course videos
        self.download_course(course_downloadbale)

        # self.browser.close()


    def _get_detailed_course_list(self, course):
        course_link = URL_COURSE_LIST + course + '/'
        course_detial = {
            'title': course,
            'url': course_link,
            'sections': []
        }

        self.browser.get(course_link)
        self.browser.implicitly_wait(2)
        soup_page = BeautifulSoup(self.browser.page_source, 'html.parser')

        # Find video nav list
        sections = soup_page.find('ul', {'class': 'video-nav-list'})
        sections_items = sections.find_all(
            'li', {'class': 'video-nav-section'}
        )

        sections = self._get_section_data(sections_items)
        course_detial['sections'].extend(sections)

        return course_detial

    def _get_section_data(self, sections_items):
        sections = []
        for item in sections_items:
            # Course section data structure
            course_section = {
                'title': None,
                'subsections': []
            }

            course_section['title'] = item.find(
                'h4', {'class': 'video-nav-section-title'}
            ).getText()

            videos_section = item.find('ul')
            videos_section_items = videos_section.find_all('li')

            videos_data = self._get_videos_data(videos_section_items)
            course_section['subsections'].extend(videos_data)

            sections.append(course_section)

        return sections

    def _get_videos_data(self, videos_section_items):
        subsections = []

        for video in videos_section_items:
            # Course subsection data structure
            course_subsection = {
                'title': None,
                'url': None,
                'downloadable_url': None
            }

            course_subsection['url'] = video.find('a')['href']
            title = video.find('a').find(
                'span', {'class', 'text'}
            ).find(
                'span', {'class', 'title'}
            ).getText()

            course_subsection['title'] = format_filename(title)
            subsections.append(course_subsection)

        return subsections

    def _get_downloadable_links(self, course):
        # course data structure
        # {
        #     'title': course,
        #     'url': course_link,
        #     'sections': []
        # }

        url = course['url']

        for section in course['sections']:
            for subsection in section['subsections']:
                if subsection['downloadable_url'] is None:

                    print("Retriving: {0}/{1}/{2}".format(
                        format_filename(course['title']),
                        format_filename(section['title']),
                        format_filename(subsection['title'])))

                    video_url = url + subsection['url']
                    self.browser.get(video_url)
                    time.sleep(8)

                    url_str = self._get_video_source()
                    print("Video URL: {0}".format(url_str))
                    subsection['downloadable_url'] = url_str

        return course

    def _get_video_source(self):
        try:
            video_tag = self.browser.find_element_by_tag_name('video')
            source_link = video_tag.get_attribute('src')
            return source_link
        except:
            return "http://placehold.it/500x500"

    def download_course(self, course):
        # Create download directory
        create_path('./Download')
        title = course['title']

        # Create course directory
        course_path = './Download/{0}'.format(title)
        create_path(course_path)

        for i1, section in enumerate(course['sections']):
            section_title = section['title']

            for i2, subsection in enumerate(section['subsections']):
                subsection_title = subsection['title']
                print("Downloading: {0}".format(
                    format_filename(subsection_title)))

                filename = str(i1) + '-' + str(i2) + format_filename(
                    section_title) + '|' + format_filename(
                        subsection_title) + '.mp4'

                file_path = course_path + '/' + format_filename(filename)

                download_file(subsection['downloadable_url'], file_path, self)