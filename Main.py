raktazodis="A1 Vilnius-Kaunas-Klaipėda ruožo nuo 10,000 iki 95,000 km rekonstravimas"
import requests
r=requests.get("https://cvpp.eviesiejipirkimai.lt/?Query=vilnius%E2%80%93kaunas%E2%80%93klaip%C4%97da&OrderingType=0&OrderingDirection=0&TypeContractId=&ProcedureSearchTypeId=&NoticeType=&PublicationType=&SectorSearchTypeId=&IncludeExpired=false&Cpvs=&TenderId=&DeadlineFromDate=&DeadlineToDate=&PublishedFromDate=2018-04-01&PublishedToDate=")
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')
results= soup.find_all("div", class_='notice-search-item-header')
for result in results:
    result=result.find_all("a", href=True)
    if len(result) == 2:
        print(result[1])
    elif len(result)==1:
        print(result[0])
        elementas = result[1]
    elif len(result)==1:
        elementas = result[0]
    pavadinimas=elementas.text
    adresas=elementas["href"]
    if raktazodis in pavadinimas:
        print("Rastas projektas pagal raktazodi")
        print(elementas.text)
        print(elementas["href"])
        projektas=puslapis+adresas
        print(projektas)
projekto=requests.get(projektas)
soup = BeautifulSoup(projekto.content, 'html.parser')
page=soup.find_all("div", class_="details-view-action-box") 
documents=soup.find_all("a", href=True)
for documents in page:
    if len(documents) == 2:
        element = result[1]
        elif len(documents)==1:
        element = result[0]
    grafa=element.text
    graf_adresas=element["href"]
    print(element.text)