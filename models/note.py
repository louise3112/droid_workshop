class Note:

    def __init__(self, input_date, input_note, input_droid, input_service, generated_id = None):
        self.date = input_date
        self.note = input_note
        self.droid = input_droid
        self.service = input_service
        self.id = generated_id