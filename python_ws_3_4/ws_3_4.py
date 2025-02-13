import requests
from pprint import pprint as print

number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people+=1
    return number_of_people


def create_user(name1, age1, address1):
    print(f'{name1}님 환영합니다!')

    data = {'name':name1, 'age' : age1, 'address' : address1 }

    return data


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user =  list(map(create_user,name,age,address))
print(user)


API_URL = []
# API_URL = 'https://jsonplaceholder.typicode.com/users/'
# # API 요청
# response = requests.get(API_URL)
response = []
dummy_data = []
rotal = {}
for i in range(1, 11) :
    API_URL = 'https://jsonplaceholder.typicode.com/users/'
    API_URL += str(i)
    print(API_URL)
    response = requests.get(API_URL)
    parsed_data = response.json()
    if float(parsed_data['address']['geo']['lat']) <80 :
        a = parsed_data['address']['geo']['lat']
    if float(parsed_data['address']['geo']['lng']) > -80 :
        b = parsed_data['address']['geo']['lng']

    rotal = {'name':parsed_data['name'],'lat' :parsed_data['address']['geo']['lat'], 'company name' : parsed_data['company']['name'],'lat' : a,'ing' :b}
    dummy_data.append(rotal)
    print(type(rotal))
    print(dummy_data)
