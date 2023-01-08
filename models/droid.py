from datetime import date

class Droid:

    def __init__(self, input_name, input_type, input_activation_date, input_owner, input_technician = None, generated_id = None):
        self.name = input_name
        self.type = input_type
        self.activation_date = input_activation_date
        self.owner = input_owner
        self.technician = input_technician
        self.id = generated_id 

    def calculate_years_active(self):
        actual_date = date.today()
        current_date = date(actual_date.year - 960, actual_date.month, actual_date.day)
        age = current_date.year - self.activation_date.year
        return age


    # Pseudocode for method to change the format of a date for display in app:

    # Define a function called change_date_format that takes one parameter, self:
    #   Create a variable called display_date which is equal to the self.activation_date variable converted to a dd-mm-yyyy format
    #   Return the display_date variable


    def change_date_format(self):
        display_date = self.activation_date.strftime("%d-%m-%Y")
        return display_date

