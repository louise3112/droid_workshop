class Droid:

    def __init__(self, input_name, input_type, input_reg_date, input_repair_notes, input_owner, input_technician, generated_id = None):
        self.name = input_name
        self.type = input_type
        self.registration_date = input_reg_date
        self.repair_notes = input_repair_notes
        self.owner = input_owner
        self.technician = input_technician
        self.id = generated_id