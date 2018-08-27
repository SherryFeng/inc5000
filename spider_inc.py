#!/usr/bin/env python
from __future__ import unicode_literals
import requests
import json
import sys

result = open("test.txt", 'w')
sys.stdout = result

r = requests.get('https://www.inc.com/inc5000list/json/inc5000_2018.json')

company_list = json.loads(r.text)
company_id_list = []
company_base_url = 'https://www.inc.com/rest/inc5000company/inc5000-usa-2018/'


for company in company_list:
    company_id_list.append(company['id'])

for id in company_id_list:
    url = unicode(company_base_url) + unicode(id)
    r = requests.get(url)
    company_dict = json.loads(r.text)
    industry_list = company_dict['inc5000industryObj']
    print industry_list['ifi_industry']
    print company_dict['ifc_company'],
    print company_dict['ifc_ceo_name'],
    print company_dict['ifc_ceo_email'],
    print company_dict['ifc_ceo_phone']


