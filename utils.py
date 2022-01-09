import os
import re
import requests
import settings
import pathlib
from uuid import uuid4
from xml.etree import ElementTree
from http.cookies import SimpleCookie



# https://stackoverflow.com/questions/32281041/converting-cookie-string-into-python-dict
def cookieStr_to_dict(cookie_str):
  cookie = SimpleCookie()
  cookie.load(cookie_str)
  cookies = {}
  for key, morsel in cookie.items():
    cookies[key] = morsel.value
  return cookies

def getfilename(headers):
  d = headers['content-disposition']
  fname = re.findall("filename=(.+)", d)
  if fname:
    return fname[0]
  return

def download(url, save_path=None):
  cookies = cookieStr_to_dict(settings.COOKIE_STR)
  r = requests.get(url, cookies=cookies)
  if save_path:
    with open(save_path, 'wb') as f:
      f.write(r.content)
  else:
    return r.content

def getFilenameAndSave(url, output_dir):
  cookies = cookieStr_to_dict(settings.COOKIE_STR)
  r = requests.get(url, cookies=cookies)
  filename = getfilename(r.headers)
  if filename:
    ext = pathlib.Path(filename).suffix
    filename = f'{str(uuid4())}{ext}'
  else:
    filename = str(uuid4())
  dest_path = os.path.join(output_dir, filename)
  with open(dest_path, 'wb') as f:
    f.write(r.content)
  return filename

def parse_xml(file_path):
  tree = ElementTree.parse(file_path)
  return tree