import requests
from bs4 import BeautifulSoup
import re
import json
import itertools
import os

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
        },
    )
    soup = BeautifulSoup(req.text, 'html.parser')

    result = []
    for option in soup.find_all('option')[1:]:
        result.append({'gugun_name':option.text, 'gugun_code':option['value']})
    return result

def get_sido_code():
    req = requests.get(sido_url,timeout=5)    
    soup = BeautifulSoup(req.text, 'html.parser')
    sido = soup.find('select',  {"name":"ctprvn"})

    result = []
    for option in sido.find_all('option')[1:]:        
        result.append({'sido_name':option.text, 'sido_code':option['value'], 'gugun':get_gugun_code(option['value'])})
    return result

def get_summary(url):
    print('request')    
    req = requests.get(url,timeout=5)    
    print('response')    
    soup = BeautifulSoup(req.text, 'html.parser')
    table = soup.find('table',  {"class":"table_childcare2"})
    script = table.find('script')
    latlng = str(script).split('LatLng(')[1].split(')')[0]
    

    result = {'lat': latlng.split(', ')[0], 'lng': latlng.split(', ')[1]}
    for tr in table.find_all('tr'):
        header = tr.find('th').text.strip()        
        if header == '기관명':
            result.update({'organization_name' : tr.find('td').text.strip()})
        elif header == '원장명':  
            result.update({'director_name' : tr.find('td').text.strip()})                        
        elif header == '설립유형':
            result.update({'establishment_type' : tr.find('td').text.strip()})
        elif header == '설립(개원)일':         
            result.update({'created_date' : tr.find('td').text.strip()})            
        elif header == '관할 행정기관':
            result.update({'agency' : tr.find('td').text.strip()})
        elif header == '전화번호':            
            result.update({'tel' : tr.find('td').text.strip()})
        elif header == '홈페이지':
            result.update({'homepage' : tr.find('td').text.strip()})
        elif header == '운영시간':            
            result.update({'operating_time' : tr.find('td').text.strip()})
        elif header == '주소':
            result.update({'address' : tr.find('td').text.strip()})
        elif header == '제공서비스':      
            services_list = []
            for li in tr.find_all('li'):                
                if li.find('input', checked=True):
                    services_list.append(li.text.strip())
            result.update({'services' : services_list})
        elif header == '통학차량 운영':
            result.update({'school_bus' : tr.find('td').text.strip()})     
    return result

def get_basic(url):
    result = {}
    req = requests.get(url,timeout=5)    
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table',  {"class":"table_childcare2"})
    
    area_thead = tables[1].find('thead')
    area_tbody = tables[1].find('tbody')
    area_columns = [[],[]]
    area_info = []
    for (idx,tr) in enumerate(area_thead.find_all('tr')):
        for th in tr.find_all('th'):
            if 'colspan' in th.attrs: continue
            area_columns[idx].append(th.text.strip())
    
    for td in area_tbody.find_all('td'):
        area_info.append(td.text.strip())

    result.update({'area': {'columns': area_columns[1] + area_columns[0], 'info': area_info}})
    
    building_table = tables[2].find('tbody')
    building_columns = []
    building_info = []
    for th in building_table.find_all('th'):
        building_columns.append(th.text.strip())
    for td in building_table.find_all('td'):
        building_info.append(td.text.strip())

    result.update({'building': {'columns': building_columns, 'info': building_info}})


    cctv_table = tables[3].find('tbody')
    cctv_columns = []
    cctv_info = []

    for (idx,tr) in enumerate(cctv_table.find_all('tr')):
        cctv_columns.append([])        
        for th in tr.find_all('th'):
            if 'colspan' in th.attrs and th['colspan'] == '5': continue
            cctv_columns[idx].append(th.text.strip())
    
    for td in cctv_table.find_all('td'):
        cctv_info.append(td.text.strip())
    if len(cctv_table.find_all('tr')) > 3:
        result.update({'cctv': {'columns': cctv_columns[0] + cctv_columns[1][:1] + cctv_columns[2] + cctv_columns[1][1:] + list(itertools.chain.from_iterable(cctv_columns[3:])), 'info': cctv_info}})
    else:
        result.update({'cctv': {'columns': cctv_columns[0], 'info': cctv_info }})
    return result

def get_staff(url):
    result = {}
    req = requests.get(url,timeout=5)    
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table',  {"class":"table_childcare2"})

    age_thead = tables[0].find('thead')
    age_tbody = tables[0].find('tbody')
    age_columns = [[],[]]
    age_info = []
    for (idx,tr) in enumerate(age_thead.find_all('tr')):
        for th in tr.find_all('th'):
            if 'colspan' in th.attrs: continue
            age_columns[idx].append(th.text.strip())
    tmp = age_tbody.find_all('td', {'rowspan':'3'})

    for (idx,tr) in enumerate(age_tbody.find_all('tr')):
        age_info += [[tmp[0].text.strip(),tmp[1].text.strip()]]
        for td in tr.find_all('td'):
            if 'rowspan' in td.attrs: continue
            age_info[idx].append(td.text.strip())

    result.update({'age_by_class': {'columns': age_columns[0][:2] + age_columns[1] + age_columns[0][2:], 'info': age_info}})

    staff_thead = tables[1].find('thead')
    staff_tbody = tables[1].find('tbody')
    staff_columns = []
    staff_info = []
    for tr in staff_thead.find_all('tr'):
        for th in tr.find_all('th'):
            if 'colspan' in th.attrs: continue
            staff_columns.append(th.text.strip())

    for td in staff_tbody.find_all('td'):
        staff_info.append(td.text.strip())

    result.update({'staff': {'columns': staff_columns, 'info': staff_info}})
    
    continuous_years_thead = tables[2].find('thead')
    continuous_years_tbody = tables[2].find('tbody')
    continuous_years_columns = []
    continuous_years_info = []
    for th in continuous_years_thead.find_all('th'):        
        continuous_years_columns.append(th.text.strip())

    for tr in continuous_years_tbody.find_all('tr'):
        continuous_years_info.append([tr.find('th').text.strip()])
        for td in tr.find_all('td'):
            continuous_years_info[-1].append(td.text.strip())

    result.update({'continuous_years': {'columns': continuous_years_columns, 'info': continuous_years_info}})
    return result

def get_curriculum(url):
    result = {}
    req = requests.get(url,timeout=5)    
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table',  {"class":"table_childcare2"})

    fee_thead = tables[1].find('thead')
    fee_tbody = tables[1].find('tbody')
    fee_columns = []
    fee_info = []

    for th in fee_thead.find_all('th'):        
        fee_columns.append(th.text.strip())

    for tr in fee_tbody.find_all('tr'):
        fee_info.append(tr.find('th').text.strip())
        for td in tr.find_all('td'):
            fee_info.append(td.text.strip())
    result.update({'fee': {'columns': fee_columns, 'info': fee_info}})

    other_fee_thead = tables[2].find('thead')
    other_fee_tbody = tables[2].find('tbody')
    other_fee_columns = []
    other_fee_info = []

    for th in other_fee_thead.find_all('th'):        
        other_fee_columns.append(th.text.strip())

    for tr in other_fee_tbody.find_all('tr'):
        other_fee_info.append([])
        for td in tr.find_all('td'):
            other_fee_info[-1].append(td.text.strip())
    result.update({'other_fee': {'columns': other_fee_columns, 'info': other_fee_info}})
    
    special_activity_thead = tables[3].find('thead')
    special_activity_tbody = tables[3].find('tbody')
    special_activity_columns = []
    special_activity_info = []

    for th in special_activity_thead.find_all('th'):        
        special_activity_columns.append(th.text.strip())

    for tr in special_activity_tbody.find_all('tr'):
        if not tr.find('th'): break
        special_activity_info.append([tr.find('th').text.strip()])
        for td in tr.find_all('td'):
            special_activity_info[-1].append(td.text.strip())
    result.update({'special_activity': {'columns': special_activity_columns, 'info': special_activity_info}})
    
    return result

def get_health(url):
    result = {}
    req = requests.get(url,timeout=5)    
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table',  {"class":"table_childcare2"})

    poisoning_thead = tables[2].find('thead')
    poisoning_tbody = tables[2].find('tbody')
    poisoning_columns = []
    poisoning_info = []

    for th in poisoning_thead.find_all('th'):        
        poisoning_columns.append(th.text.strip())

    for tr in poisoning_tbody.find_all('tr'):
        poisoning_info.append([])
        for td in tr.find_all('td'):
            poisoning_info[-1].append(td.text.strip())
    result.update({'poisoning': {'columns': poisoning_columns, 'info': poisoning_info}})

    air_quality_thead = tables[3].find('thead')
    air_quality_tbody = tables[3].find('tbody')
    air_quality_columns = []
    air_quality_info = []

    for th in air_quality_thead.find_all('th'):        
        air_quality_columns.append(th.text.strip())

    for tr in air_quality_tbody.find_all('tr'):
        air_quality_info.append([])
        for td in tr.find_all('td'):
            air_quality_info[-1].append(td.text.strip())
    result.update({'air_quality': {'columns': air_quality_columns, 'info': air_quality_info}})

    disinfection_thead = tables[4].find('thead')
    disinfection_tbody = tables[4].find('tbody')
    disinfection_columns = []
    disinfection_info = []

    for th in disinfection_thead.find_all('th'):        
        disinfection_columns.append(th.text.strip())

    for tr in disinfection_tbody.find_all('tr'):
        disinfection_info.append([])
        for td in tr.find_all('td'):
            disinfection_info[-1].append(td.text.strip())
    result.update({'disinfection': {'columns': disinfection_columns, 'info': disinfection_info}})

    water_quality_tbody = tables[5].find('tbody')
    water_quality_columns = []
    water_quality_info = []

    for th in water_quality_tbody.find_all('th'):        
        water_quality_columns.append(th.text.strip())

    for tr in water_quality_tbody.find_all('tr'):
        for td in tr.find_all('td'):
            water_quality_info.append(td.text.strip())
    result.update({'water_quality': {'columns': water_quality_columns, 'info': water_quality_info}})
   
    return result

def get_grade(url):
    result = {}
    req = requests.get(url,timeout=5)    
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table',  {"class":"table_childcare2"})
    
    if not tables[0].find_all('th')[1].text.strip():
        url = url.replace('Grade', '')
        req = requests.get(url,timeout=5)    
        soup = BeautifulSoup(req.text, 'html.parser')
        tables = soup.find_all('table',  {"class":"table_childcare2"})

        result.update({'grade': tables[0].find('td').text.strip()})
    else:
        result.update({'grade': tables[0].find_all('th')[1].text.strip()})

    rating_certificate_tbody = tables[1].find('tbody')
    rating_certificate_columns = []
    rating_certificate_info = []

    for th in rating_certificate_tbody.find_all('th'):        
        rating_certificate_columns.append(th.text.strip())

    for tr in rating_certificate_tbody.find_all('tr'):
        for td in tr.find_all('td'):
            rating_certificate_info.append(td.text.strip())
    result.update({'rating_certificate': {'columns': rating_certificate_columns, 'info': rating_certificate_info}})
    
    rating_history_thead = tables[2].find('thead')
    rating_history_tbody = tables[2].find('tbody')
    rating_history_columns = []
    rating_history_info = []

    for th in rating_history_thead.find_all('th'):        
        rating_history_columns.append(th.text.strip())

    for tr in rating_history_tbody.find_all('tr'):
        rating_history_info.append([])
        for td in tr.find_all('td'):
            rating_history_info[-1].append(td.text.strip())
    result.update({'rating_history': {'columns': rating_history_columns, 'info': rating_history_info}})
    return result

def get_extension(url):
    result = {}
    req = requests.get(url, timeout=5)    
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table',  {"class":"table_childcare2"})
    
    extension_class_status_thead = tables[0].find('thead')
    extension_class_status_tbody = tables[0].find('tbody')
    extension_class_status_columns = []
    extension_class_status_info = []

    for th in extension_class_status_thead.find_all('th'):        
        extension_class_status_columns.append(th.text.strip())

    for tr in extension_class_status_tbody.find_all('tr'):
        extension_class_status_info.append([])
        for td in tr.find_all('td'):
            extension_class_status_info[-1].append(td.text.strip())
    result.update({'extension_class_status': {'columns': extension_class_status_columns, 'info': extension_class_status_info}})
    

    result.update({'extension_class_program': {'columns': tables[2].find('th').text.strip(),'info':tables[2].find('td').text.strip()}})   
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
    result = {'id': code}
    for category in categorys:
        print(category['url'] )
        result.update(category['get'](base_url + category['url'] + '&STCODE_POP={code}'.format(code=code)))
        
    return result

def get_child_care_list(sido_code, gugun_code):

    base_url = child_care_url
    offset = 0
    result = []
    while True:
        req = requests.get(base_url + '&ctprvn={sido_code}&signgu={gugun_code}&offset={offset}'.format(sido_code=sido_code, gugun_code=gugun_code,offset=offset))   
        soup = BeautifulSoup(req.text, 'html.parser')     
        total = int(soup.find('p', {'class':'sum'}).find('em').text)

        
        table = soup.find('div', {'class':'list_table'}).find('tbody')
        for ele in table.find_all('td', {'class':'lef'}):
            href = ele.find('a')['href']
            code = re.findall('[0-9]+', href)[0] 
            print(code)
            try:
                result.append(get_child_care_detail(code))
                print('success')
            except Exception as e: 
                print(code, ':', e)
                with open('./error.txt', "a") as errorfile:
                    errorfile.write(code + '\n')            
        offset+=10
        print(offset, total)
        if offset >= total: break
    return result

# file_path = './data.json'
# file_list = set([file_name.split('.')[0] for file_name in os.listdir('./') if len(file_name.split('.')) > 1 and file_name.split('.')[1] == 'json'])

# sido_list = get_sido_code()
# for sido in sido_list:
#     for gugun in sido['gugun']:
#         if gugun['gugun_code'] in file_list: continue
#         try:
#             print(gugun['gugun_code'])
#             data = get_child_care_list(sido['sido_code'], gugun['gugun_code'])            
#             with open("./{file_name}.json".format(file_name=gugun['gugun_code']), "w") as outfile:
#                 json.dump(data, outfile)
#         except Exception as e:    
#             print(e)
