from django.shortcuts import render
import requests
import xml.etree.ElementTree
from lxml import html, etree

# func to finding the elements before a slice and return slice before it
def before(value, a):
    # Find first part and return slice before it.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]
    
def ActivityDateType(request):
    return render(request, 'xmlapp/ActivityDateType.html')
    
def xmllist(request):
    xmlObj = []

    # scraping the file names from the repo
    url = ("https://github.com/IATI/IATI-Codelists/tree/version-2.03/xml")

    r = requests.get(url)
    data = r.text

    # xmlCount = data.count('.xml" id')
    nameList = []
    xmlFileNames = []

    dataSplits = data.split('open" title="')

    # delete first generated data split as it doesn't contain an xml list.
    del dataSplits[0]

    # trim trailing text from each in dataSplits and appending into nameList
    for i in dataSplits:
        try:
            nameList.append(before(i, '.xml" id='))
        except TypeError:
            nameList.append('no string found')

    # making a list the file names
    for name in nameList:
        xmlFileNames.append(name + ''.join('.xml'))

    ##### loop each file name to create urls and running them through the parser.
    for xmlFileName in xmlFileNames:
        xmlurl = ("https://raw.githubusercontent.com/IATI/IATI-Codelists/version-2.03/xml/" + ''.join(xmlFileName))

        # testurl = ("https://raw.githubusercontent.com/IATI/IATI-Codelists/version-2.03/xml/DocumentCategory.xml")

        # response = requests.get(xmlurl)
        response = requests.get(testurl)
        root = etree.fromstring(response.content)

        metaData = root.find("./metadata")
        codeListName = metaData.findtext("./name/narrative")
        codeListDesc = metaData.findtext("./description/narrative")

        codeListItems = root.find("./codelist-items")
        codeListItem = codeListItems.find("./codelist-item")

        ########

        # iterate over all item
        for codeListItem in codeListItems.findall('codelist-item'):

            # access element - name
            codeListItemName = codeListItem.findtext('./name/narrative')
            # print('list item : ', codeListItemName)

            # access element - description
            codeListItemDesc = codeListItem.findtext(
                './description/narrative')
            # print('item description : ', codeListItemDesc)

        myObj = {
            'codeListName': codeListName,
            'codeListDesc': codeListDesc,
            'codeListItemName': codeListItemName,
            'codeListItemDesc': codeListItemDesc,
            }

        xmlObj.append(myObj)

    return render(request, 'xmlapp/xmllist.html')

def index(request):
    return render(request, 'xmlapp/index.html')
