
def _get_course_list():
    BASE_URL = URL_COURSE_LIST
    browser.get(BASE_URL)
    bs_course_page = BeautifulSoup(browser.page_source, "html.parser")
    course_titles = bs_course_page.select('h2.title')
    course_links = []

    for title in course_titles:
        link = title.find('a')

        if link is not None:
            title = link.getText()
            course = {'title': title, 'url': link['href']}
            course_links.append(course)

    return course_links

def save_course_list():
    with open(DATA_COURSE_LIST, 'w') as file:
        file.write(json.dumps(_get_course_list()))

def retrive_course_list():
    with open(DATA_COURSE_LIST, 'r') as file:
        return json.load(file)

def save_course_detailed_list(course_list):
    with open(DATA_COURSE_DETAILED_LIST_CDN, 'w') as file:
        file.write(json.dumps(_get_detailed_course_list(course_list)))

def retrive_course_detailed_list():
    with open(DATA_COURSE_DETAILED_LIST_CDN, 'r') as file:
        return json.load(file)

def _write_downloadable_data(courses_data):
    with open(DATA_COURSE_DETAILED_LIST_CDN, 'w') as file:
        file.write(json.dumps(courses_data))

def retrive_downloadable_links():
    with open(DATA_COURSE_DETAILED_LIST_CDN, 'r') as file:
        return json.load(file)

# Func(PASSED): Download resources via CDN
