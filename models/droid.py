from datetime import date

class Droid:

    def __init__(self, input_name, input_type, input_reg_date, input_repair_notes, input_owner, input_technician, generated_id = None):
        self.name = input_name
        self.type = input_type
        self.registration_date = input_reg_date
        self.repair_notes = input_repair_notes
        self.owner = input_owner
        self.technician = input_technician
        self.id = generated_id

    def convert_date(self, string):
        # Assume string is of the format "YYYY-MM-DD"
        date_list = string.split("-")  #['YYYY', 'MM', 'DD']
        converted_date = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return converted_date

    def calculate_age(self):
        actual_date = date.today()
        # year = current_date.year - 960
        droid_date = date(actual_date.year - 960, actual_date.month, actual_date.day)
        age = droid_date.year - self.registration_date.year
        return age
