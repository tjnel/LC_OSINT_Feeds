from urllib.parse import urlparse
import pandas as pd

FILENAME = "LC_URLHAUS_Domains_List.txt"

url="https://urlhaus.abuse.ch/downloads/text/"
domains = pd.read_csv(url, skiprows=9, names=['url'], error_bad_lines=False, warn_bad_lines=False)
domains['source'] = ' urlhaus'
domains['url'] = domains['url'].apply(lambda url: urlparse(url).netloc.split(':')[0])
domains = domains.drop_duplicates(subset='url')
domains.to_csv(FILENAME, sep=':', encoding='utf-8', header=False, index=False)