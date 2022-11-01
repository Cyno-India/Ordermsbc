import schedule
import time
import requests
import json

import datetime

def last_day_of_month(any_day):
    # The day 28 exists in every month. 4 days later, it's always next month
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    # subtracting the number of the current day brings us back one month
    return next_month - datetime.timedelta(days=next_month.day)



from datetime import date, datetime
import calendar as cal



def lastsat():
    today = date.today()
    month = today.month
    year = today.year
    length_month = cal.monthrange(year, month)[1]
    for day in range(length_month,length_month-7,-1):
        if datetime(year, month, day).weekday()==5:
            last_saturday = datetime(year, month, day).strftime("%d/%m/%Y")
    return last_saturday


    # return last_saturday

def currentDate():
    po= datetime.today().date().strftime("%d/%m/%Y")
    return po

def gettoken():
    purl = "https://api.insightsc3m.com/altria/oauth2/v2.0/token"
    headers = {'Content-Type' : 'application/x-www-form-urlencoded',
               'Ocp-Apim-Subscription-Key':'468d1441beeb487a838b7cefcc24009c'
    }    
    body = {'client_id' : 'c7a9289f-ca37-46d1-bc14-a73dea132b8b',
                'grant_type' : 'client_credentials',
                'client_secret' : 'MjZlB5ISWnxU1vJNEUVPF+bL0Ik2cAIvH/hXai+jmlQ=',
                'scope' : 'https://api.insightsc3m.com/.default',
                'Ocp-Apim-Subscription-Key':'468d1441beeb487a838b7cefcc24009c'
                }  

   
    r = requests.post(purl, headers=headers, data=body)
 
    res = r.json()
    token = res['access_token']
    # print(token,'token')
    return token  

def ppapi():
    Bearer_token_value = gettoken()
    oc1 = ["1070","1077","2000"]
    sat = lastsat()
    print(sat,'saturday')
    cd = currentDate()
    print(cd, 'currentdate')
    main_cycle = ['202210']
    new_cycle = 202210 + 1 
    new_data = "" 

    # for i in oc1:
    #     print(i)
    # for month in range(1, 13):
        # print(last_day_of_month(datetime.date(2022, month, 1)))

    # print(d,'token')
    params = {'operatingCompany' : '1070',
               'cycleCode':'202210'
    }
    try:
        for i in oc1:
            print(i)
            if cd > sat:
                purl = f"https://api.insightsc3m.com/PricePromotions/v3/ProductPriceAndAllowances?operatingCompany={i}&cycleCode={new_cycle}"
                headers = {
                            'Ocp-Apim-Subscription-Key':'3d3d34a1e3884ff286312f71a445b41e',
                            'Authorization' : "Bearer %s" %Bearer_token_value}
                            


                r = requests.get(purl, headers=headers)
                # p = r['PerUnitAllowances']
                res = r.json()
                # for k in res:
                #     l = k['OtherAllowances'][0]['Allowances']
                #     for j in l:
                #         print(j['EndDate'])
                print("hello")
            else:
                purl = f"https://api.insightsc3m.com/PricePromotions/v3/ProductPriceAndAllowances?operatingCompany={i}&cycleCode=202210"
                headers = {
                            'Ocp-Apim-Subscription-Key':'3d3d34a1e3884ff286312f71a445b41e',
                            'Authorization' : "Bearer %s" %Bearer_token_value}
                            


                r = requests.get(purl, headers=headers)
                # p = r['PerUnitAllowances']
                res = json.dumps(r.json(), indent=4, sort_keys=True)
                print(res)
                # print(res)
                # for k in res:
                #     l = k['OtherAllowances'][0]['Allowances']
                #     for j in l:
                #         print(j['EndDate'])
                print("bye")
                if res.status_code == 200:
                    print ('OK!')
                else:
                    print ('Boo!')

            # print(p)    
            # print(res)
    except :
        pass
    # token = res['access_token']
    # return token  

# ppapi()

# s =schedule.every(1).minutes.do(ppapi)
# print('helllloo')
# s =schedule.every(5).minutes.do(ppapi)

# while True:
#     schedule.run_pending()
#     time.sleep(1)





import datetime
import smtplib

def mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('immanishar1999@gmail.com','')