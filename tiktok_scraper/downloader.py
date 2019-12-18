import requests

def download_mp4(name, url):
    name = name + ".mp4"
    r = requests.get(url)
    with open(name, 'wb') as f:
      for chunk in r.iter_content(chunk_size=255): 
        if chunk:
          f.write(chunk)
