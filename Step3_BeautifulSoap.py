from BeautifulSoup import *
import re
import urllib

params = "keyword=&selectedCriteria=E&dateRange=All&searchType=Basic&Signature+ID=false&Signature+Name=false&Latest+Release+Date=false&Alarm+Severity=false&Release=false&Original+Release=true&Release+Date=true&Default+Enabled=true&Default+Retired=true&Fidelity=true&itemsPerPage=100&currentPage=1&pageSize=100&sortOrder=d&lastUpSortOrder=d&sortType=date&PAGE_START=#"
html = urllib.urlopen("https://tools.cisco.com/security/center/ipshome.x", params).read()


soap = BeautifulSOAP(html)

tags = soap('a')

for tag in tags:
#    print tag.get("href", None)
    print tag
"""
for sections in shandle:
    data = sections.strip()
    if re.search("var myData", data):
        result = re.findall("\[\"([0-9]+)/[0-9]+\",", data)
        print "The number is signatures: "+ str(len(result))
        print result
        break

"""





