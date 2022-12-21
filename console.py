# from models.droid import Droid
# from datetime import date

import repositories.service_repository as service_repo
import repositories.type_repository as type_repo

# reg_date = date(1051, 10, 10)
# droid_1 = Droid("R2D2", 2, reg_date, "None", 1, 2)
# current_date = date.today()
# year = current_date.year - 960
# current_sw_date = date(year, current_date.month, current_date.day)
# droid_1_age = current_sw_date.year - droid_1.registration_date.year

# print(current_date)
# print(current_sw_date)
# print(droid_1_age)

# def loop():
#     services = service_repo.select_all()
#     for service in services:
#         types = type_repo.select_types_by_service(service.id)
#         for type in types:
#             service.valid_types.append(type)
#     return services

# output = loop()
# service = output[0]
# for type in service.valid_types:
#         print(type.__dict__)

        # <h4>Droid Types:</h4> <br>
        # {% for type in all_types %}
        #     <label for="{{type.name}}"">{{type.name}}</label>
        #         <input type="checkbox" name="{{type.id}}" id="{{type.name}}"
        #             {% if type in relevant_types %} checked {% endif %}>
        # {% endfor %}

all_types = type_repo.select_all()
relevant_types = type_repo.select_types_by_service(19)

relevant_type_ids = []
for type in relevant_types:
    relevant_type_ids.append(type.id)

for id in relevant_type_ids:
    print(id)

# for type in relevant_types:
#     print(type.__dict__)

# print("line break")

# for type in all_types:
#     print(type.__dict__)

# for type in all_types:
#     if type in relevant_types:
#         print(type.__dict__)
#     else:
#         print("Not in list")


