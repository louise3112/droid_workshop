class Service:

    def __init__(self, input_name, input_cost, generated_id = None):
        self.name = input_name
        self.cost = input_cost
        self.id = generated_id
        self.valid_types = []