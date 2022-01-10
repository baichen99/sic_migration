import requests
from http.cookies import SimpleCookie

# https://stackoverflow.com/questions/32281041/converting-cookie-string-into-python-dict
def cookieStr_to_dict(cookie_str):
  cookie = SimpleCookie()
  cookie.load(cookie_str)
  cookies = {}
  for key, morsel in cookie.items():
    cookies[key] = morsel.value
  return cookies

def upload(file_path, name):
  headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMyIsImV4cCI6MTY0MjM4MTQ5NCwiaWF0IjoxNjQxNzc2Njk0fQ.ROHrvD7wwNaLzfdeeGrR98TmUaklz667JVPCmVbtad8BZnctJUHN-jc_ca710mUYsGmGPabVrT96M2OfjIbhng',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
  }

  cookie_str = 'token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMyIsImV4cCI6MTY0MjM4MTQ5NCwiaWF0IjoxNjQxNzc2Njk0fQ.ROHrvD7wwNaLzfdeeGrR98TmUaklz667JVPCmVbtad8BZnctJUHN-jc_ca710mUYsGmGPabVrT96M2OfjIbhng'
  cookies = cookieStr_to_dict(cookie_str)

  form = {
    'name': name,
    'templateEditionId': '135',
    'teamId': '13',
  }
  url = 'http://172.16.0.74/api/data/upload'
  r = requests.post(url, data=form, files={'file': open(file_path, 'rb')}, headers=headers, cookies=cookies)
  return r

# for i in range(188):
#   res = upload(f'/Users/chenbai/Projects/mgi_data_migration/sic/output/data{i}/data.zip', f'data{i}')
#   print(f'data{i} 上传完成,   状态码{res.status_code}, {res.text}')
#   break