import os
import json
import shutil
import requests
from tqdm import tqdm
from utils import download, parse_xml, getFilenameAndSave

def replaceUrlWithImport(tree):
  output_dir = '/Users/chenbai/Projects/mgi_data_migration/sic/output_files'
  root = tree.getroot()
  all_nodes = []
  for elem in root.iter():
    all_nodes.append(elem)
  for node in all_nodes:
    if node.tag == 'url' and node.text:
      download_url = 'http://matdata.shu.edu.cn' + node.text
      filename = getFilenameAndSave(download_url, output_dir)
      node.text = f'import:{filename}'
  return tree

# recreate output_files dir
shutil.rmtree('/Users/chenbai/Projects/mgi_data_migration/sic/output_files')
os.mkdir('/Users/chenbai/Projects/mgi_data_migration/sic/output_files')

with open('/Users/chenbai/Projects/mgi_data_migration/sic/data.json', 'r') as f:
  json_obj = json.load(f)
data = json_obj['data']['data']

ids = []
for d in data:
  ids.append(d['_id'])
print(f'共{len(ids)}个记录')

for id in tqdm(ids):
  url = f'http://matdata.shu.edu.cn/api/xml?id={id}&lang=zh'
  # downlaod xml
  download(url, save_path='/Users/chenbai/Projects/mgi_data_migration/sic/xml_example.xml')
  tree = parse_xml('/Users/chenbai/Projects/mgi_data_migration/sic/xml_example.xml')
  tree = replaceUrlWithImport(tree)
  tree.write('/Users/chenbai/Projects/mgi_data_migration/sic/xml_example_output.xml')
  
