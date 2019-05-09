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
