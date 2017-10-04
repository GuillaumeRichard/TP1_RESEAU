from httplib2 import Http
from bs4 import BeautifulSoup


class BeautifulSoupService:

    def get_form_list(self, url):
        http = Http('.cache')
        response, content = http.request(url)
        forms = BeautifulSoup(content, "html.parser").findAll('form')
        return forms
