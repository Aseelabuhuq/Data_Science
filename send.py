import requests
import datetime

x1= 'طول عمر التلفزيون العربي الاسرائيلي يبث  حوالي عام والجميع  يشاهده بكل شوق  السابعه'
x2 = 'امبارح تسحرت لبنة  شاي  صحيت اليوم الصبح ميت  العطش'
x3= 'الفرق  الغربه والاردن مو دايما سيء بالعكس الواحد ممكن يخسر لمه العيله  بنفس الوقت بصلي التراويح  مبسوط وبيختم القران  الامام وبحضر دعاء ختم'
x4 = 'الزعران وين   والتشحيط وين   والامن موجود   غرامه بتحل الموضوع'
x = ' زمان  اللي بيعمل حرام بيتخبا وبرمضان بيستحي شوي اما هالايام فصار الموضوع سهل جدا حياءاحترام شهر'
print(type(x))
pred = requests.post('http://127.0.0.1:5000/predict',params={'dial':x})
print(pred.text)
print(pred.status_code)

conpr = pred.text
pr= conpr.replace('[','')
pr = conpr.replace(']','')
currentDateTime = datetime.datetime.now()
print("current:", currentDateTime)

year = currentDateTime.strftime("%Y")
print("year:", year)

month = currentDateTime.strftime("%m")
print("month:", month)

day = currentDateTime.strftime("%d")
print("day:", day)

time = currentDateTime.strftime("%H:%M:%S")
print("time:", time)

date_time = currentDateTime.strftime("%Y/%m/%d, %H:%M:%S")
print("date and time:",date_time)

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# # logging in using private key
# cred = credentials.Certificate('C:\\Users\\Dell\\Desktop\\Data_Scince\\Python\\dialectsds-firebase-adminsdk-6v59e-0c24d97f9e.json')
# firebase_admin.initialize_app(cred, {'databaseURL' : 'https://dialectsds-default-rtdb.firebaseio.com/' , 'httpTimeout' : 30})
# print('logged in to firebase')
# # setting the loction where we want to write
        
# ref = "newref/"
# root = db.reference(ref)
# slang = {"dialects":pr}
# root.child(x).child(year).child(month).child(day).child(time).update(slang)
res=requests.post('http://127.0.0.1:5000/insert',params={'txto':x,'predict': pr, 'date':date_time,'year': year,'month':month,'day':day,'timess':time})