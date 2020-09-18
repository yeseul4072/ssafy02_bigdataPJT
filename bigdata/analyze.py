import json
import pandas as pd
from collections import Counter
from bisect import bisect_right

with open('./data.json', encoding="utf-8") as f:
    datas = json.loads(f.read())

service_list = {
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
establishment_type_list = {
    '직장': 'office', 
    '국공립': 'public', 
    '민간': 'private', 
    '가정': 'family', 
    '법인·단체등': 'corporate', 
    '협동': 'cooperation', 
    '사회복지법인': 'welfare'
}

program_list = {
    '언어': 'language', 
    '문화/예술': 'culture', 
    '체육': 'sport',
    '과학/창의': 'science', 
    '': 'other'    
}

age_list = ['zero_year_old', 'one_year_old', 'two_year_old', 'three_year_old', 'four_year_old', 'five_year_old']

area_per_cctv_list = []
child_per_staff_list = []

for data in datas:
    t = data['operating_time'].split(':')
    data['start_time'] = int(t[1]) * 60 + int(t[2][:2])
    data['finish_time'] = int(t[2][-2:]) * 60 + int(t[3])
    
    for service in service_list.values():
        data[service] = 0
    for service in data['services']:
        data[service_list[service]] = 1

    for establishment_type in establishment_type_list.values():
        data[establishment_type] = 0
    
    data[establishment_type_list[data['establishment_type']]] = 1

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
            data['grade'] = 5            
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
        data['area_per_cctv'] = area / cctv_count
    except ZeroDivisionError as e: 
        data['area_per_cctv'] = area
    area_per_cctv_list.append(data['area_per_cctv'])    
    
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
    child_per_staff_list.append(data['child_per_staff'])

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
    for (idx,num) in enumerate(data['monthly_fee'].split(',')):
        data[age_list[idx]] = num

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

    for program in program_list.values():
        data[program] = 0
    
    program_by_age = []
    for program in data['special_activity']['info']:        
        data[program_list[program[1]]] = 1
        program_by_age.append(program[0]+'&'+program[1])
    data['program_by_age'] = ','.join(program_by_age)

    del_columns = ['operating_time','services','area','building','cctv','age_by_class','staff','continuous_years','fee','other_fee','special_activity','poisoning','air_quality','disinfection','water_quality','rating_certificate','rating_history','extension_class_status','extension_class_program']
    for column in del_columns:
        del data[column]

area_per_cctv_list.sort()
child_per_staff_list.sort()
total = len(datas)

for data in datas:
    cctv_rank = bisect_right(area_per_cctv_list, data['area_per_cctv']) / total
    staff_rank = bisect_right(child_per_staff_list, data['child_per_staff']) / total
    if cctv_rank <= 0.20:
        data['cctv_grade'] = 1
    elif cctv_rank <= 0.40:
        data['cctv_grade'] = 2
    elif cctv_rank <= 0.60:
        data['cctv_grade'] = 3
    elif cctv_rank <= 0.80:
        data['cctv_grade'] = 4
    else:
        data['cctv_grade'] = 5

    if staff_rank <= 0.20:
        data['staff_grade'] = 1
    elif staff_rank <= 0.40:
        data['staff_grade'] = 2
    elif staff_rank <= 0.60:
        data['staff_grade'] = 3
    elif staff_rank <= 0.80:
        data['staff_grade'] = 4
    else:
        data['staff_grade'] = 5

    
    
print(datas[3])
    
with open("./data2.json", "w") as outfile:
    json.dump(datas, outfile)