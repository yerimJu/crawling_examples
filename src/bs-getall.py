from bs4 import BeautifulSoup
import urllib.request as request
import urllib.parse as parse
from os import makedirs
import os.path, time, re

'''
Example for downloading all the files (css, js, html ...) in the URL
'''
# store if the file is checked
proc_files = {}


def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")
    result = []

    for a in links:
        href = a.attrs['href']
        url = parse.urljoin(base, href)
        result.append(url)

    return result

def download_file(url):
    o = parse.urlparse(url)
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$", savepath):
        savepath += "index.html"
    savedir = os.path.dirname(savepath)

    # check all the links are downloaded
    if os.path.exists(savepath): return savepath
    # create a directory to save the downloaded files
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)
    
    # download files
    try:
        print("download=", url)
        request.urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print("Failed to download.")
        return None

def analyze_html(url, root_url):
    savepath = download_file(url)

    if savepath is None: return
    if savepath in proc_files: return

    proc_files[savepath] = True
    print("analyze_html=", url)

    # extract links
    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)

    for link_url in links:
        # ignore if link is out of root URL
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url): continue
        # if HTML, analyze file recursively
        if re.search(r".(html|htm)$", link_url):
            analyze_html(link_url, root_url)
            continue
        download_file(link_url)

if __name__ == "__main__":
    # url = "https://docs.python.org/3.5/library"
    url = input("Enter a URL: ")
    analyze_html(url, url)