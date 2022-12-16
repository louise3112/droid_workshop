class Droid:

    def __init__(self, input_name, input_type, input_date_of_reg, input_repair_notes, input_owner, input_technician, generated_id = None):
        self.name = input_name
        self.type = input_type
        self.date_of_registration = input_date_of_reg
        self.repair_notes = input_repair_notes
        self.owner = input_owner
        self.technician = input_technician
        self.id = generated_id