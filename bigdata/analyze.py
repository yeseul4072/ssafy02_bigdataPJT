import json
import pandas as pd
from collections import Counter

with open('./data.json', encoding="utf-8") as f:
    datas = json.loads(f.read())

services = {
    '일반' :'general',
    '영아전담': 'infants',
    '장애아전문': 'disabled',
    '장애아통합': 'disabled_integration',
    '방과후 전담': 'after_school',
    '방과후 통합': 'after-school_inclusion',
    '야간연장': 'extension',
    '휴일보육': 'holiday',
    '24시간': 'all_day',
    '시간제보육': 'part_time'
}

for data in datas:
    t = data['operating_time'].split(':')
    data['start_time'] = int(t[1]) * 60 + int(t[2][:2])
    data['finish_time'] = int(t[2][-2:]) * 60 + int(t[3])
    
    for service in services.values():
        data[service] = 0
    for service in data['services']:
        data[services[service]] = 1

    data['school_bus'] = 1 if data['school_bus'] == '운영' else 0

    if 48 <= ord(data['grade'][0]) <= 57:
        data['score'] = float(data['grade'])
        if data['score'] >= 95: data['grade'] = 1
        elif data['score'] >= 85: data['grade'] = 2
        elif data['score'] >= 75: data['grade'] = 3
        else: data['grade'] = 4        
    else:
        try:
            data['grade'] = ['A','B','C','D'].index(data['grade']) + 1
        except ValueError as e: 
            data['grade'] = 0            
        data['score'] = 0

    data['area_columns'] = ','.join(data['area']['columns'])
    data['area_info'] = ','.join(data['area']['info'])
    data['building_columns'] = ','.join(data['building']['columns'])
    data['building_info'] = ','.join(data['building']['info'])
    data['cctv_columns'] = ','.join(data['cctv']['columns'])
    data['cctv_info'] = ','.join(data['cctv']['info'])
    
    cctv_count = int(data['cctv']['info'][1]) if len(data['cctv']['info']) > 1 else 0
    area = float(data['area']['info'][1][:-2])    

    try:
        data['cctv_per_area'] = cctv_count / area
    except ZeroDivisionError as e: 
        data['cctv_per_area'] = cctv_count

    
    data['age_by_class_columns'] = ','.join(data['age_by_class']['columns'])
    data['age_by_class_info'] = '|'.join([','.join(info) for info in data['age_by_class']['info']])    
    data['staff_columns'] = ','.join(data['staff']['columns'])
    data['staff_info'] = ','.join(data['staff']['info'])
    data['continuous_columns'] = ','.join(data['continuous_years']['columns'])
    data['continuous_info'] = ','.join(data['continuous_years']['info'][0])
    try:
        data['child_per_staff'] = int(data['age_by_class']['info'][0][1]) / int(data['staff']['info'][0])
    except ZeroDivisionError as e: 
        data['child_per_staff'] = int(data['age_by_class']['info'][0][1])

    data['fee_columns'] = ','.join(data['fee']['columns'])
    data['fee_info'] = ','.join(data['fee']['info'])
    data['other_fee_columns'] = ','.join(data['other_fee']['columns'])
    data['other_fee_info'] = '|'.join([','.join(info) for info in data['other_fee']['info']])    
    data['special_activity_columns'] = ','.join(data['special_activity']['columns'])
    data['special_activity_info'] = '|'.join([','.join(info) for info in data['special_activity']['info']])    
    fee = [0]*6
    other_fee = 0
    for (idx,info) in enumerate(data['fee']['info'][1:]):
        fee[idx] = int(info.replace('-', '0').replace(',', '').replace('원', ''))
    
    for info in data['other_fee']['info']:
        if info[-1] == '연단위':
            other_fee += int(info[-2])/12
        elif info[-1] == '분기':
            other_fee += int(info[-2])/4
        elif info[-1] == '월단위':
            other_fee += int(info[-2])
        elif info[-1] == '일단위':
            other_fee += int(info[-2])*20
    data['monthly_fee'] = ','.join([str(int(round(i + other_fee,-1))) for i in fee])

    data['poisoning_columns'] = ','.join(data['poisoning']['columns'])
    data['poisoning_info'] = '|'.join([','.join(info) for info in data['poisoning']['info']])    
    data['air_quality_columns'] = ','.join(data['air_quality']['columns'])
    data['air_quality_info'] = '|'.join([','.join(info) for info in data['air_quality']['info']])    
    data['disinfection_columns'] = ','.join(data['disinfection']['columns'])
    data['disinfection_info'] = '|'.join([','.join(info) for info in data['disinfection']['info']])    
    
    data['water_quality_columns'] = ','.join(data['water_quality']['columns'])
    data['water_quality_info'] = ','.join(data['water_quality']['info'])

    data['rating_certificate_columns'] = ','.join(data['rating_certificate']['columns'])
    data['rating_certificate_info'] = ','.join(data['rating_certificate']['info'])
    data['rating_history_columns'] = ','.join(data['rating_history']['columns'])
    data['rating_history_info'] = '|'.join([','.join(info) for info in data['rating_history']['info']])    
    data['extension_class_status_columns'] = ','.join(data['extension_class_status']['columns'])
    data['extension_class_status_info'] = '|'.join([','.join(info) for info in data['extension_class_status']['info']])    

    data['extension_class_program_columns'] = data['extension_class_program']['columns']
    data['extension_class_program_info'] = data['extension_class_program']['info']
    
    data['has_extension_class'] = 1 if len(data['extension_class_status_info']) != 0 else 0

    del data['operating_time']
    del data['services']
    del data['area']
    del data['building']
    del data['cctv']
    del data['age_by_class']
    del data['staff']
    del data['continuous_years']
    del data['fee']
    del data['other_fee']
    del data['special_activity']

    del data['poisoning']
    del data['air_quality']
    del data['disinfection']
    del data['water_quality']
    del data['rating_certificate']
    del data['rating_history']
    del data['extension_class_status']
    del data['extension_class_program']

with open("./data2.json", "w") as outfile:
    json.dump(datas, outfile)

