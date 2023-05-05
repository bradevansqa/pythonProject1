
import requests
import json
ENDPOINT = "https://census-toy.nceng.net/prod/toy-census"

file = open("post_api.json", "r")
json_input = file.read()
request_json = json.loads(json_input)


def test_endpoints():
    response = requests.post(ENDPOINT, json=request_json)
    assert response.status_code == 200
    response1 = requests.get(ENDPOINT)
    assert response1.status_code == 403


def test_count_gender(users):

    female_count = 0
    male_count = 0

    for user in users:
        if user['gender'] == 'female':
            female_count += 1
        elif user['gender'] == 'male':
            male_count += 1
    count = female_count + male_count
    assert count >= 1




def test_count_by_country(users):
    country_counts = {}
    for user in users:
        country = user['nat']
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1
    assert len(country_counts) > 0

def Tspasswords_sorted_by_complexity(users):
    passwords = {}
    for user in users:
        password = user['login']['password']
        complexity = sum(not x.isalnum() for x in password)
        passwords[password] = complexity
    sorted(passwords.items(), key=lambda x: x[1])

    assert len(passwords) > 0


