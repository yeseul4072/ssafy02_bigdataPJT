import requests
from bs4 import BeautifulSoup
import re
import json

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
    tables = soup.find_all('table',  {"class":"table_childcare2"})
    area_table = tables[1].find('tbody')
    area_column = ['nursery_room_count', 'nursery_room_area', 'playground_indoor_area', 'playground_outdoor_area', 'playground_rooftop_area', 'playground_nearby_area', 'health_room_area', 'kitchen_area', 'staffroom_area', 'other_space_area']

    result = {}
    for (idx,td) in enumerate(area_table.find_all('td')):
        result.update({area_column[idx]: td.text.strip()})

    building_table = tables[2].find('tbody')
    building_column = ['building_year', 'building_floor' , 'building_type ', 'building_ownership_type' , 'building_only_area' , 'total_site_area', 'emergency_facility']
    for (idx,td) in enumerate(building_table.find_all('td')):
        result.update({building_column[idx]: td.text.strip()})

    cctv_table = tables[3].find('tbody')
    cctv_column = ['cctv_type', 'cctv_total_count', 'cctv_nursery_room_count', 'cctv_playroom_count', 'cctv_playground_count', 'cctv_restaurant_count', 'cctv_auditorium_count', 'cctv_kitchen_count', 'cctv_hallway_count', 'cctv_office_count', 'cctv_health_room_count', 'cctv_building exterior_count', 'cctv_other_count','cctv_preservation_period', 'cctv_quality', 'cctv_installation_classification', 'cctv_installation_date', 'cctv_operation_method']
    
    for (idx,td) in enumerate(cctv_table.find_all('td')):
        result.update({cctv_column[idx]: td.text.strip()})
    return result

def get_staff(url):
    result = {}
    req = requests.get(url)    
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table',  {"class":"table_childcare2"})

    age_table = tables[0].find('tbody')
    age_column = ['age_total_fixed_number', 'age_total_current_number'] + ['tmp']*13 + ['fixed_zero_child','fixed_one_child','fixed_two_child','fixed_three_child','fixed_four_child','fixed_five_child','fixed_zero_two_child','fixed_three_five_child','fixed_disable_child'] + ['tmp']*14
    for (idx,td) in enumerate(age_table.find_all('td')):
        result.update({age_column[idx]: td.text.strip()})

    staff_table = tables[1].find('tbody')
    staff_column = ['total_staff', 'director_count', 'nursery_teacher_count', 'special_teacher_count', 'therapist_count', 'nutritionist_count', 'nurse_count', 'cook_count', 'clerk_count', 'first_grade_staff_count', 'second_grade_staff_count', 'Third_grade_staff_count']
    for (idx,td) in enumerate(staff_table.find_all('td')):
        result.update({staff_column[idx]: td.text.strip()})
    
    year_table = tables[2].find('tbody')
    year_column = ['continuous_service_year_zero_one', 'continuous_service_year_one_two', 'continuous_service_year_two_four', 'continuous_service_year_four_six', 'continuous_service_year_six'] + ['tmp']*5
    for (idx,td) in enumerate(year_table.find_all('td')):    
        result.update({year_column[idx]: td.text.strip()})

    return result

def get_curriculum(url):
    result = {}
    req = requests.get(url)    
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table',  {"class":"table_childcare2"})

    fee_table = tables[1].find('tbody')
    fee_column = ['fee_zero_child','fee_one_child','fee_two_child','fee_three_child','fee_four_child','fee_five_child']
    for (idx,td) in enumerate(fee_table.find_all('td')):    
        result.update({fee_column[idx]: td.text.strip()})

    other_fee_table = tables[2].find('tbody')
    other_fee_column = ['item', 'defail_item', 'cost', 'cycle']
    other_fee_list = []
    for tr in other_fee_table.find_all('tr'):    
        other_fee = {}
        for (idx,td) in enumerate(tr.find_all('td')):                
            other_fee.update({other_fee_column[idx]: td.text.strip()})
        other_fee_list.append(other_fee)
    result.update({'other_fee': other_fee_list})

    activities_table = tables[3].find('tbody')
    activities_column = ['category', 'program', 'company', 'per_week', 'operating_time', 'cost']
    activities_list = []
    for tr in activities_table.find_all('tr'):    
        activities = {'age':tr.find('th').text.strip()}
        for (idx,td) in enumerate(tr.find_all('td')):                
            activities.update({activities_column[idx]: td.text.strip()})
        activities_list.append(activities)
    result.update({'activities': activities_list})

    return result

def get_health(url):
    result = {}
    req = requests.get(url)    
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table',  {"class":"table_childcare2"})

    poisoning_table = tables[2].find('tbody')
    poisoning_column = ['date', 'total_child', 'occur_child', 'contents']
    poisoning_list = []
    for tr in poisoning_table.find_all('tr'):    
        poisoning = {}
        for (idx,td) in enumerate(tr.find_all('td')):                
            poisoning.update({poisoning_column[idx]: td.text.strip()})
        poisoning_list.append(poisoning)
    result.update({'poisoning': poisoning_list})

    air_quality_table = tables[3].find('tbody')
    air_quality_column = ['target', 'date', 'result']
    air_quality_list = []
    for tr in air_quality_table.find_all('tr'):    
        air_quality = {}
        for (idx,td) in enumerate(tr.find_all('td')):                
            air_quality.update({air_quality_column[idx]: td.text.strip()})
        air_quality_list.append(air_quality)
    result.update({'air_quality': air_quality_list})

    disinfection_table = tables[4].find('tbody')
    disinfection_column = ['target', 'date', 'result']
    disinfection_list = []
    for tr in disinfection_table.find_all('tr'):    
        disinfection = {}
        for (idx,td) in enumerate(tr.find_all('td')):                
            disinfection.update({disinfection_column[idx]: td.text.strip()})
        disinfection_list.append(disinfection)
    result.update({'disinfection': disinfection_list})

    water_quality_table = tables[5].find('tbody')
    water_quality_column = ['water_type','target','date','result']
    water_quality = {}
    for (idx,td) in enumerate(water_quality_table.find_all('td')):    
        water_quality.update({water_quality_column[idx]: td.text.strip()})
    result.update({'water_quality' : water_quality})

    return result

def get_grade(url):
    result = {}
    req = requests.get(url)    
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table',  {"class":"table_childcare2"})

    rating_table = tables[0].find('tbody')
    rating_column = ['interaction','safety','management','staff']
    rating = {'grade': rating_table.find_all('th')[1].text.strip()}
    for (idx,td) in enumerate(rating_table.find_all('td')):    
        if idx % 2 == 0: continue
        rating.update({rating_column[idx//2]: td.text.strip()})
    result.update({'rating' : rating})

    rating_info_table = tables[1].find('tbody')
    rating_info_column = ['type','date','Validity']
    rating_info = {}
    for (idx,td) in enumerate(rating_info_table.find_all('td')):    
        rating_info.update({rating_info_column[idx]: td.text.strip()})
    result.update({'rating_info' : rating_info})

    rating_history_table = tables[2].find('tbody')
    rating_history_column = ['date', 'type']
    rating_history_list = []
    for tr in rating_history_table.find_all('tr'):    
        rating_history = {}
        for (idx,td) in enumerate(tr.find_all('td')):                
            rating_history.update({rating_history_column[idx]: td.text.strip()})
        rating_history_list.append(rating_history)
    result.update({'rating_history': rating_history_list})
    return result

def get_extension(url):
    result = {}
    req = requests.get(url)    
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table',  {"class":"table_childcare2"})

    extension_class_status_table = tables[0].find('tbody')
    extension_class_status_column = ['class_name', 'class_type', 'total_number', 'current_number', 'concurrent', 'staff']
    extension_class_status_list = []
    for tr in extension_class_status_table.find_all('tr'):    
        extension_class_status = {}
        for (idx,td) in enumerate(tr.find_all('td')):                
            extension_class_status.update({extension_class_status_column[idx]: td.text.strip()})
        extension_class_status_list.append(extension_class_status)
    result.update({'extension_class_status': extension_class_status_list})
    
    result.update({'extension_class_program': tables[2].find('tbody').find('td').text.strip()})
    return result


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
        try:
            result.update(category['get'](base_url + category['url'] + '&STCODE_POP={code}'.format(code=code)))
        except Exception as e: 
            raise Exception(category['url'])
    return result

def get_child_care_list(sido_code, gugun_code):
    result = []

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
            result.append(get_child_care_detail(code))
            print(code, )
            if code == '11140000104':
                raise Exception('예외 발생')
            
        offset+=10
        if offset >= total: break
    return result

file_path = './data.json'
error_path = './error.json'
data = []

sido_list = get_sido_code()
for sido in sido_list:
    for gugun in sido['gugun']:
        try:
            data.append(get_child_care_list(sido['sido_code'], gugun['gugun_code']))
        except Exception as e:    
            print(e)
            with open(file_path, 'w') as outfile:
                json.dump(data, outfile)
            with open(error_path, 'w') as outfile:
                json.dump({'sido':sido['sido_code'], 'gugun': gugun['gugun_code']}, outfile)
            exit(0)


with open(file_path, 'w') as outfile:
    json.dump(data, outfile)