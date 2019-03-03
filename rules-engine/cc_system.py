#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from durable.lang import *
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import json
import csv
import math


# In[ ]:


with ruleset('recommendation'):
    @when_all((m.income >= 30000) & (m.age >= 21))
    def is_eligible(c):
        c.s.result = calculate_cashback(c)
        print (c.s.result)

        
    def calculate_cashback(c):
        
        list_cc = []
        dict_cashback = {}
        dict_max_cashback = {}
        exp = c.m.spending 
        print("here")
        with open ("D:/Intellij/Project/machine-reasoning/machine-reasoning/rules-engine/cc_data.csv") as file:
            reader = csv.DictReader(file)
            print("here")
            for row in reader:
                list_cc.append(dict(row))
            print (list_cc)
        
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
                
                eligible_cash_back = cb_dining + cb_bills + cb_phv + cb_petrol + cb_pubtrpt + cb_others
                
                dict_cashback[cc.get('credit_card')] = eligible_cash_back   

            
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
        
        dict_max_cashback['Eligible'] = 'Y'
        dict_max_cashback['Cardname'] = max_cashback_cc
        dict_max_cashback['CashbackAmount'] = dict_cashback.get(max_cashback_cc)
        
        return (dict_max_cashback)
        
    
    @when_all((m.income < 30000) | (m.age < 21))
    def not_eligible(c):
        resp = {}
        resp['Eligible'] = 'N'
        print (resp)
        
#     @when_start
#     def start(host):
#         host.post('test', {})


# In[ ]:


host = create_host()


# In[ ]:


flaskApp = Flask('CreditCardRecommendationSystem')
CORS(flaskApp)

# In[ ]:


@flaskApp.route('/recommendation', methods=['POST']) 
def post_event():
    message = json.loads(request.stream.read())
    result = host.post('recommendation', message)
    print(result)
    return make_response(json.dumps({'outcome': result}))    


# In[ ]:


flaskApp.run()


# In[ ]:




