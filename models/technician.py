class Technician:

    def __init__(self, input_name, input_picture, input_bio, input_type, generated_id = None):
        self.name = input_name
        self.picture = input_picture
        self.bio = input_bio
        self.type = input_type
        self.id = generated_id