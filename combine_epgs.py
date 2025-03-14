import requests
from xml.etree import ElementTree as ET

# List of EPG URLs to merge
epg_urls = [
    "https://github.com/pigzillaaaaa/iptv-scraper/raw/refs/heads/main/epgs/tvpass-epg.xml.gz",
    "https://github.com/pigzillaaaaa/iptv-scraper/raw/refs/heads/main/epgs/moveonjoy-epg.xml.gz",
    "https://github.com/pigzillaaaaa/iptv-scraper/raw/refs/heads/main/epgs/daddylive-epg.xml.gz",
    "https://raw.githubusercontent.com/acidjesuz/EPGTalk/master/guide.xml",
    "https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_US_LOCALS2.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_US1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_DUMMY_CHANNELS.xml.gz"
]

# Output file
output_file = "combined_epg.xml"

def fetch_and_parse_epg(url):
    print(f"Fetching EPG from: {url}")
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return ET.fromstring(response.content)

def merge_epgs(epg_urls):
    # Create root element for the new combined EPG
    combined_tv = ET.Element("tv")

    for url in epg_urls:
        try:
            epg_tree = fetch_and_parse_epg(url)
            for element in epg_tree:
                combined_tv.append(element)
            print(f"✅ Merged EPG from {url}")
        except Exception as e:
            print(f"❌ Failed to fetch/parse {url}: {e}")

    # Save the combined EPG
    tree = ET.ElementTree(combined_tv)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"\n✅ Combined EPG saved as '{output_file}'")

if __name__ == "__main__":
    merge_epgs(epg_urls)
