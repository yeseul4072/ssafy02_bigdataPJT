import requests
from bs4 import BeautifulSoup
import re

sido_url = 'http://www.childcare.go.kr/cpis2gi/nursery/NurserySlPL.jsp?programId=P0001PG00001909'
gugun_url = 'http://www.childcare.go.kr/common/util/AreaCodeSlL.jsp'
child_care_url = 'http://www.childcare.go.kr/cpis2gi/nursery/NurseryContentsSlL.jsp?programId=P0001PG00001909&flag=NSSlPL&areaType=1&dong=&crtype=&crspec=&crpub=&crcert=&cltype=&enclyn=&crname='
child_care_detail_url = 'http://info.childcare.go.kr/info/pnis/search/preview'

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

def get_summary(url):
    req = requests.get(url)    
    soup = BeautifulSoup(req.text, 'html.parser')
    table = soup.find('table',  {"class":"table_childcare2"})
    services = {
        '일반':'service_general',
        '영아전담':'service_infant',
        '장애아전문':'service_special_disable',
        '장애아통합':'service_integration_disable',
        '방과후 전담':'service_after',
        '방과후 통합':'service_integration_after',
        '야간연장':'service_night_extension',
        '휴일보육':'service_holiday_care',
        '24시간':'service_full_day',
        '시간제보육':'service_part_time'
    }
    class_columns = ['zero_class','one_class','two_class','three_class','four_class','five_class','zero_two_class','three_five_class','disable_class','total_class']
    child_columns = ['zero_child','one_child','two_child','three_child','four_child','five_child','zero_two_child','three_five_child','disable_child','total_child']

    result = {}
    for tr in table.find_all('tr'):
        header = tr.find('th').text.strip()
        column = {}
        if header == '기관명':
            column = {'organization_name' : tr.find('td').text.strip()}            
        elif header == '원장명':  
            column = {'director_name' : tr.find('td').text.strip()}                        
        elif header == '설립유형':
            column = {'establishment_type' : tr.find('td').text.strip()}
        elif header == '설립(개원)일':         
            column = {'jurisdiction' : tr.find('td').text.strip()}            
        elif header == '관할 행정기관':
            column = {'administrative_agency' : tr.find('td').text.strip()}
        elif header == '전화번호':            
            column = {'tel' : tr.find('td').text.strip()}
        elif header == '홈페이지':
            column = {'homepage' : tr.find('td').text.strip()}
        elif header == '운영시간':            
            column = {'operating_time' : tr.find('td').text.strip()}
        elif header == '주소':
            column = {'address' : tr.find('td').text.strip()}
        elif header == '제공서비스':      
            for li in tr.find_all('li'):
                if li.find('input', checked=True):
                    column.update({services[li.text.strip()]:True})
        elif header == '반수':
            
            for (idx, td) in enumerate(tr.find_all('td')):                
                column.update({class_columns[idx]:td.text.strip()})                
        elif header == '아동수':                     
            for (idx, td) in enumerate(tr.find_all('td')):                
                column.update({child_columns[idx]:td.text.strip()})
        elif header == '통학차량 운영':
            column = {'school_car' : tr.find('td').text.strip()}
        result.update(column)     
    return result

def get_basic(url):
    req = requests.get(url)    
    soup = BeautifulSoup(req.text, 'html.parser')
    area_table = soup.find_all('table',  {"class":"table_childcare2"})[1].find('tbody')
    area_column = ['nursery_room_count', 'nursery_room_area', 'playground_indoor_area', 'playground_outdoor_area', 'playground_rooftop_area', 'playground_nearby_area', 'health_room_area', 'kitchen_area', 'staffroom_area', 'other_space_area']

    result = {}
    for (idx,td) in enumerate(area_table.find_all('td')):
        result.update({area_column[idx]: td.text.strip()})

    building_table = soup.find_all('table',  {"class":"table_childcare2"})[2].find('tbody')
    building_column = ['building_year', 'building_floor' , 'building_type ', 'building_ownership_type' , 'building_only_area' , 'total_site_area', 'emergency_facility']
    for (idx,td) in enumerate(building_table.find_all('td')):
        result.update({building_column[idx]: td.text.strip()})

    cctv_table = soup.find_all('table',  {"class":"table_childcare2"})[3].find('tbody')
    cctv_column = ['cctv_type', 'cctv_total_count', 'cctv_nursery_room_count', 'cctv_playroom_count', 'cctv_playground_count', 'cctv_restaurant_count', 'cctv_auditorium_count', 'cctv_kitchen_count', 'cctv_hallway_count', 'cctv_office_count', 'cctv_health_room_count', 'cctv_building exterior_count', 'cctv_other_count','cctv_preservation_period', 'cctv_quality', 'cctv_installation_classification', 'cctv_installation_date', 'cctv_operation_method']
    
    for (idx,td) in enumerate(cctv_table.find_all('td')):
        result.update({cctv_column[idx]: td.text.strip()})
    return result

def get_staff(url):
    return {'1':1}

def get_curriculum(url):
    return {'1':1}

def get_health(url):
    return {'1':1}

def get_grade(url):
    return {'1':1}

def get_extension(url):
    return {'1':1}


def get_child_care_detail(code):
    base_url = child_care_detail_url
    categorys = [
        {'url':'/SummaryInfoSlPu.jsp?flag=YJ', 'get':get_summary},
        {'url':'/BasisPresentConditionSlPu.jsp?flag=GH','get':get_basic},
        {'url':'/ChildStaffSlPu.jsp?flag=BG','get':get_staff},
        {'url':'/ChildCareCurriculumSlPu.jsp?flag=BB','get':get_curriculum},
        {'url':'/HealthSafetySlPu.jsp?flag=GA','get':get_health},
        {'url':'/AppraisaAuthenticationGradeSlPu.jsp?flag=PI','get':get_grade},
        {'url':'/EtntctClassAdditionSlPu.jsp?flag=EN','get':get_extension}
    ]
    result = {}
    for category in categorys:
        result.update(category['get'](base_url + category['url'] + '&STCODE_POP={code}'.format(code=code)))
    return result

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
            print(get_child_care_detail(code))
            exit(0)
            
        offset+=10
        if offset >= total: break
    # exit(0)
    
    return req



sido_list = get_sido_code()
for sido in sido_list:
    for gugun in sido['gugun']:
        get_child_care_list(sido['sido_code'], gugun['gugun_code'])

