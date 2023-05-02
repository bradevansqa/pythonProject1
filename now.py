import requests

def test_data():
    payload = {
        "actions": [
            {"actionType": "CountByCountry", "top": 0},
            {"actionType": "CountByGender", "top": 0},
            {"actionType": "CountPasswordComplexity", "top": 0}
            ],
        "users": [
            {
                "gender": "female",
                "name": {
                    "title": "miss",
                    "first": "lorraine",
                    "last": "bryant"
                },
                "location": {
                    "street": "4422 harrison ct",
                    "city": "gladstone",
                    "state": "tasmania",
                    "postcode": 3294
                },
                "email": "lorraine.bryant@example.com",
                "login": {
                    "username": "smallduck444",
                    "password": "aaron",
                    "salt": "fYBp4g4a",
                    "md5": "5d0785427febd6d262f00929c10247e7",
                    "sha1": "a12a6925740eefebebcbc79add949fa108a78bf0",
                    "sha256": "61a79aebd11cd5910dd9e77dd49b3dd11df2b4b397e328697f33b86e5b082b84"
                },
                "dob": "1956-09-17 02:13:36",
                "registered": "2009-05-03 14:40:51",
                "phone": "00-3540-6154",
                "cell": "0498-678-691",
                "id": {
                    "name": "TFN",
                    "value": "377488473"
                },
                "picture": {
                    "large": "https://randomuser.me/api/portraits/women/38.jpg",
                    "medium": "https://randomuser.me/api/portraits/med/women/38.jpg",
                    "thumbnail": "https://randomuser.me/api/portraits/thumb/women/38.jpg"
                },
                "nat": "AU"},

            {
                "gender": "female",
                "name": {
                    "title": "ms",
                    "first": "jessica",
                    "last": "harris"
                },
                "location": {
                    "street": "4382 james street",
                    "city": "sydney",
                    "state": "new south wales",
                    "postcode": 2000
                },
                "email": "jessica.harris@example.com",
                "login": {
                    "username": "bluecat666",
                    "password": "password123",
                    "salt": "D2Bh5r5F",
                    "md5": "3d276f449ea0dcd342ec7f1c9bb8d03c",
                    "sha1": "02c27b23b03e55e225fa8600c9ab06e2b200fa04",
                    "sha256": "b70efbf7ebd74e8340d7b15b6c0eb6f935e6c4416966e4c6f55d143b692968c4"
                },
                "dob": "1989-03-27 12:34:56",
                "registered": "2015-08-17 08:21:09",
                "phone": "(02) 1234 5678",
                "cell": "0412 345 678",
                "id": {
                    "name": "TFN",
                    "value": "678901234"
                },
                "picture": {
                    "large": "https://randomuser.me/api/portraits/women/24.jpg",
                    "medium": "https://randomuser.me/api/portraits/med/women/24.jpg",
                    "thumbnail": "https://randomuser.me/api/portraits/thumb/women/24.jpg"
                },
                "nat": "AU"
            },
            {
                "gender": "male",
                "name": {
                    "title": "mr",
                    "first": "luke",
                    "last": "nguyen"
                },
                "location": {
                    "street": "123 george street",
                    "city": "sydney",
                    "state": "new south wales",
                    "postcode": 2000
                },
                "email": "luke.nguyen@example.com",
                "login": {
                    "username": "luke.nguyen123",
                    "password": "myPassword123",
                    "salt": "qf1zCpMi",
                    "md5": "7985f5c5f5b5af2d34e9e3317e6c0a6f",
                    "sha1": "19bb59a92df85f5437b1d2679bb11e062ccbe935",
                    "sha256": "2d8a7b4a4f1e4d007bd7439f9e2f2e3700f7b74e3ed8f38e1fcd287244a7f449"
                },
                "dob": "1992-07-14 05:28:13",
                "registered": "2018-11-20 22:42:16",
                "phone": "0421 123 456",
                "cell": "0456 789 012",
                "id": {
                    "name": "TFN",
                    "value": "876543210"
                },
                "picture": {
                    "large": "https://randomuser.me/api/portraits/men/84.jpg",
                    "medium": "https://randomuser.me/api/portraits/med/men/84.jpg",
                    "thumbnail": "https://randomuser.me/api/portraits/thumb/men/84.jpg"
                },
                "nat": "AU"
            },
            {
                "gender": "female",
                "name": {
                    "title": "ms",
                    "first": "Emily",
                    "last": "Jones"
                },
                "location": {
                    "street": "123 Main St",
                    "city": "Los Angeles",
                    "state": "California",
                    "postcode": 90001
                },
                "email": "emily.jones@example.com",
                "login": {
                    "username": "emily.jones123",
                    "password": "password1234",
                    "salt": "xgjCpM1f",
                    "md5": "a2d2f2b86a0125af5b5c401d7bf1efc4",
                    "sha1": "c2d266f85fa2954c2114c4c7483c66669a011faa",
                    "sha256": "16c3b7c1c031e28dc7e60e2fb72b6d30d6da82d6f4928bcaed7667d85d6aa1b6"
                },
                "dob": "1990-12-06 07:11:22",
                "registered": "2016-05-10 16:35:28",
                "phone": "(323) 555-1212",
                "cell": "(323) 555-4321",
                "id": {
                    "name": "SSN",
                    "value": "123-45-6789"
                },
                "picture": {
                    "large": "https://randomuser.me/api/portraits/women/13.jpg",
                    "medium": "https://randomuser.me/api/portraits/med/women/13.jpg",
                    "thumbnail": "https://randomuser.me/api/portraits/thumb/women/13.jpg"
                },
                "nat": "US"
            },
            {
                "gender": "male",
                "name": {
                    "title": "mr",
                    "first": "Daniel",
                    "last": "Wong"
                },
                "location": {
                    "street": "456 Queen St",
                    "city": "Toronto",
                    "state": "Ontario",
                    "postcode": "M5V 2A2"
                },
                "email": "daniel.wong@example.com",
                "login": {
                    "username": "daniel.wong123",
                    "password": "password1234",
                    "salt": "c0pMjXg1",
                    "md5": "4813e3f71e67f5a5c9880a8b37c58f2d",
                    "sha1": "8fcb498f1a7f579ce3292c8557e0733f3bf9b9ef",
                    "sha256": "1b4c4d7ab59f121dcb6b19f6db153c9c832d6d84c4a4fa0f04e847f0df94a62d"
                },
                "dob": "1987-05-28 12:30:45",
                "registered": "2015-08-14 18:23:12",
                "phone": "(416) 555-1212",
                "cell": "(416) 555-4321",
                "id": {
                    "name": "SSN",
                    "value": "123-45-6789"
                },
                "picture": {
                    "large": "https://randomuser.me/api/portraits/men/51.jpg",
                    "medium": "https://randomuser.me/api/portraits/med/men/51.jpg",
                    "thumbnail": "https://randomuser.me/api/portraits/thumb/men/51.jpg"
                },
                "nat": "CA"
            }

        ]
            }

    def count_gender(users):
        female_count = 0
        male_count = 0

        for user in users:
            if user['gender'] == 'female':
                female_count += 1
            elif user['gender'] == 'male':
                male_count += 1

        return female_count, male_count

    def count_by_country(users):
        country_counts = {}
        for user in users:
            country = user['nat']
            if country in country_counts:
                country_counts[country] += 1
            else:
                country_counts[country] = 1
        return country_counts

    def get_passwords_sorted_by_complexity(users):
        passwords = {}
        for user in users:
            password = user['password']
            complexity = sum(not c.isalnum() for c in password)
            passwords[password] = complexity
        sorted_passwords = sorted(passwords.items(), key=lambda x: x[1])
        return [p[0] for p in sorted_passwords]

    url = "https://census-toy.nceng.net/prod/toy-census"
    response = requests.post(url)
    assert response.status_code == 200
    response1 = requests.get(url)
    assert response1.status_code == 403

    response2 = requests.post(url, json=payload)
    assert response2.status_code == 200






