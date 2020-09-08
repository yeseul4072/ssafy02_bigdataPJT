import requests
from bs4 import BeautifulSoup
import re

def get_gugun_code(code):    
    req = requests.post(gugun_url,
        data={
            'subArea': 'signgu',
            'ctprvn': code,
            'alltype': 'A'
        }
    )
    soup = BeautifulSoup(req.text, 'html.parser')

    result = []
    for option in soup.find_all('option')[1:]:
        result.append({'gugun_name':option.text, 'gugun_code':option['value']})
    return result

def get_sido_code():
    req = requests.get(sido_url)    
    soup = BeautifulSoup(req.text, 'html.parser')
    sido = soup.find('select',  {"name":"ctprvn"})

    result = []
    for option in sido.find_all('option')[1:]:        
        result.append({'sido_name':option.text, 'sido_code':option['value'], 'gugun':get_gugun_code(option['value'])})
    return result

def get_child_care_detail(code):
    base_url = child_care_detail_url
    categorys = [
        {'url':'/SummaryInfoSlPu.jsp?flag=YJ', 'name':'summary'},
        {'url':'/BasisPresentConditionSlPu.jsp?flag=GH','name':'basic'},
        {'url':'/ChildStaffSlPu.jsp?flag=BG','name':'staff'},
        {'url':'/ChildCareCurriculumSlPu.jsp?flag=BB','name':'curriculum'},
        {'url':'/HealthSafetySlPu.jsp?flag=GA','name':'health'},
        {'url':'/AppraisaAuthenticationGradeSlPu.jsp?flag=PI','name':'grade'},
        {'url':'/EtntctClassAdditionSlPu.jsp?flag=EN','name':'extension'}
    ]

    for category in categorys:
        print(category)

def get_child_care_list(sido_code, gugun_code):
    base_url = child_care_url
    offset = 0
    while True:
        req = requests.get(base_url + '&ctprvn={sido_code}&signgu={gugun_code}&offset={offset}'.format(sido_code=sido_code, gugun_code=gugun_code,offset=offset))   
        soup = BeautifulSoup(req.text, 'html.parser')     
        total = int(soup.find('p', {'class':'sum'}).find('em').text)

        
        table = soup.find('div', {'class':'list_table'}).find('tbody')
        for ele in table.find_all('td', {'class':'lef'}):
            href = ele.find('a')['href']
            code = re.findall('[0-9]+', href)[0] 
            get_child_care_detail(code,)
            exit(0)
            
        offset+=10
        if offset >= total: break
    # exit(0)
    
    return req




sido_url = 'http://www.childcare.go.kr/cpis2gi/nursery/NurserySlPL.jsp?programId=P0001PG00001909'
gugun_url = 'http://www.childcare.go.kr/common/util/AreaCodeSlL.jsp'
child_care_url = 'http://www.childcare.go.kr/cpis2gi/nursery/NurseryContentsSlL.jsp?programId=P0001PG00001909&flag=NSSlPL&areaType=1&dong=&crtype=&crspec=&crpub=&crcert=&cltype=&enclyn=&crname='
child_care_detail_url = 'http://info.childcare.go.kr/info/pnis/search/preview'

sido_list = get_sido_code()
for sido in sido_list:
    for gugun in sido['gugun']:
        get_child_care_list(sido['sido_code'], gugun['gugun_code'])