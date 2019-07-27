import pandas as pd

FILENAME = "LC_Bambenek_Domains_List.txt"

url="https://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt"
domains = pd.read_csv(url, skiprows=18, names=['domain','malware', 'date', 'url'], error_bad_lines=False, warn_bad_lines=False)
domains['source'] = 'bambenek'
domains = domains.drop_duplicates(subset='domain')
domains['meta'] = domains[['malware', 'date', 'source']].apply(lambda x: ' '.join(x), axis = 1)
domains.drop(columns=['url', 'malware', 'date'])
domains.to_csv(FILENAME, sep=':', encoding='utf-8', header=False, index=False, columns=['domain', 'meta'])