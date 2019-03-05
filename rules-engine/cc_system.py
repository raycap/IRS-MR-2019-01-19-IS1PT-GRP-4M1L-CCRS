#!/usr/bin/env python
# coding: utf-8

# In[1]:


from durable.lang import *
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import json
import csv
import math
import requests
import copy


# In[2]:


queries_database = []


# In[3]:


with ruleset('recommendation'):
    @when_all((m.income >= 30000) & (m.isCitizen == 'Y'))
    def is_eligible(c):   
        global queries_database
        dict_recommend = calculate_cashback(c)
        queries_database.append(dict_recommend)
        print (queries_database)
        c.s.result = dict_recommend 
        return c.s.result
        
    def calculate_cashback(c):
        
        list_cc = []
        dict_cashback = {}
        dict_max_cashback = {}
        exp = c.m.spending 
        
        with open ("./cc_data.csv") as file:
            reader = csv.DictReader(file)
    
            for row in reader:
                list_cc.append(dict(row))
        
        for cc in list_cc:  
            

            if ((cc.get('credit_card') != 'UOB One Card') & (exp < float(cc.get('min_spend')))):  

                total_cash_back = exp * float(cc.get('cbr_min'))

                if(cc.get('cbc_total') != 'inf'):
                    eligible_cash_back = min(total_cash_back, float(cc.get('cbc_total')))
                    dict_cashback[cc.get('credit_card')] = eligible_cash_back
                else:
                    dict_cashback[cc.get('credit_card')] = total_cash_back

            elif ((cc.get('credit_card') == 'Standard Chartered Unlimited Cash Back') & (exp >= float(cc.get('min_spend')))):

                eligible_cash_back = exp * float(cc.get('cbr_min'))

                dict_cashback[cc.get('credit_card')] = eligible_cash_back

            elif (((cc.get('credit_card') != 'Standard Chartered Unlimited Cash Back') & (cc.get('credit_card') != 'UOB One Card')) 
                  & (exp >= float(cc.get('min_spend')))):        

                cb_dining = min(exp * c.m.expense_dining / 100.0 * float(cc.get('cbr_dining')), float(cc.get('cbc_dining')))     

                cb_bills = min(exp * c.m.expense_bill / 100.0 * float(cc.get('cbr_bills')), float(cc.get('cbc_bills')))

                cb_phv = min(exp * c.m.expense_phv / 100.0 * float(cc.get('cbr_phv')), float(cc.get('cbc_phv')))

                cb_petrol = min(exp * c.m.expense_petrol / 100.0 * float(cc.get('cbr_petrol')), float(cc.get('cbc_petrol')))

                cb_pubtrpt = min(exp * c.m.expense_pubtrpt / 100.0 * float(cc.get('cbr_pubtprt')), float(cc.get('cbc_pubtprt')))

                exp_others = exp - ((c.m.expense_dining + c.m.expense_bill + c.m.expense_phv + c.m.expense_petrol + c.m.expense_pubtrpt)/100.0 * exp) 

                cb_others = min(exp_others * float(cc.get('cbr_general')), float(cc.get('cbc_general')))

                total_cash_back = cb_dining + cb_bills + cb_phv + cb_petrol + cb_pubtrpt + cb_others

                dict_cashback[cc.get('credit_card')] = min(total_cash_back, float(cc.get('cbc_total')))   

            elif (cc.get('credit_card') == 'UOB One Card'):

                if (exp < 500):

                    dict_cashback[cc.get('credit_card')] = 0

                elif (500 <= exp < 1000) :

                    dict_cashback[cc.get('credit_card')] = 16.67

                elif (1000 <= exp < 2000) :

                    dict_cashback[cc.get('credit_card')] = 33.33

                elif (exp >= 2000) :

                    dict_cashback[cc.get('credit_card')] = 1000
        
        max_cashback_cc = max(dict_cashback, key=dict_cashback.get)
        print (max_cashback_cc)
        dict_max_cashback['Eligible'] = 'Y'
        dict_max_cashback['Cardname'] = max_cashback_cc
        dict_max_cashback['CashbackAmount'] = dict_cashback.get(max_cashback_cc)
        dict_max_cashback['QueryId'] = c.m.queryid

        return (dict_max_cashback)
        
    
    @when_all((m.income < 30000))
    def not_eligible(c):
        resp = {}
        resp['Eligible'] = 'N'
        print (resp)
        
#     @when_start
#     def start(host):
#         host.post('test', {})


# In[4]:


host = create_host()


# In[ ]:


flaskApp = Flask('CreditCardRecommendationSystem')
CORS(flaskApp)


# In[ ]:


@flaskApp.route('/search/<myId>')
def search(myId):
    
    outcome = find_id(myId)
    
    return jsonify(outcome)

@flaskApp.route('/recommendation', methods=['POST']) 
def post_event():
    message = json.loads(request.stream.read())
    print(message)
    result = host.post('recommendation', message)
    return make_response(json.dumps({'outcome': result}))    


# In[ ]:


def find_id(myId):
    
    query = {}
    database = copy.copy(get_database())
    print(type(database))
    
    for d in database:
         if d.get('QueryId') == int(myId): 
                query = d
        
    print (type(query))
    
    return (query)

def get_database():
    global queries_database
    return queries_database
    
    


# In[ ]:


flaskApp.run()


# In[ ]:




