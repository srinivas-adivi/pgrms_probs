#!/home/ssrinivas/pyvenv/bin/python2.6

import os
import json
import urllib
import subprocess
from BeautifulSoup import BeautifulSoup

class Base(object):
    """This class that contains generic code for connecting to an API like Guardian, BBC etc."""
    def __init__(self, api_url):
        self.url = api_url
        self.base_json = self.open_url(api_url)
   
    def open_url(self, url):
        return urllib.urlopen(url).read()
         
    def get_response(self):
        response = json.loads(self.base_json)["response"]
        return response

    def parse_html(self, page):
        html_content = self.open_url(page)
        parsed_html = BeautifulSoup(html_content)
        
        return parsed_html
    
    def save_static_files(self, static_files, path_to_static_dir):
        if not os.path.exists(path_to_static_dir):
            os.makedirs(path_to_static_dir)

        old_cwd = os.getcwd()
        os.chdir(path_to_static_dir)
        for static_file_url in static_files:
            p = subprocess.Popen(["wget", "-c", static_file_url], stdout=subprocess.PIPE)
            output = p.stdout.readlines() 

        os.chdir(old_cwd)

class GuardianAPI(Base):
    """This class for Guardian API. """

    def __init__(self, url):
        """ 1. Call the Guardian REST endpoint and retrieve the data """
        super(GuardianAPI, self).__init__(url)
        self.response = self.get_response()
        self.results = self.response["results"]
    
    def get_images(self):
        """
        2. Iterate the objects 
        3. For each object call the contained url; 
            a. Parse the contents of the returned object and attempt to extract the image hrefs 
        """
        images = []
        for result in self.results:
            web_url = result["webUrl"]
            parsed_html = self.parse_html(web_url)
            content_div = parsed_html.body.find('div', {'id':'content'})
            images.append(content_div.find('img').get('src'))
            
        return images

if __name__ == "__main__":
    url = "http://content.guardianapis.com/search?q=obama&format=json"
    path_to_images_dir = 'images'

    g = GuardianAPI(url)
    images = g.get_images()
    #3(b). Request the images directly and save to a folder.
    #images are nothing but static files 
    g.save_static_files(images, path_to_images_dir)
