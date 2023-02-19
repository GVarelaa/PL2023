class Data:
    def __init__(self, data, bounds):
        self.data = data
        self.bounds = bounds

    def __str__(self):
        return f"Persons : {self.data}\nBounds : {self.bounds}"

    def __repr__(self):
        return f"Persons : {self.data}\nBounds : {self.bounds}"


class Person:
    def __init__(self, age, gender, tension, cholesterol, pulse, disease):
        self.age = age
        self.gender = gender
        self.tension = tension
        self.cholesterol = cholesterol
        self.pulse = pulse
        self.disease = disease

    def __str__(self):
        return f"Age : {self.age}\nGender : {self.gender}\nTension : {self.tension}\nCholesterol : {self.cholesterol}\n"\
            f"Pulse : {self.pulse}\nDisease : {self.disease}\n"

    def __repr__(self):
        return f"Age : {self.age}\nGender : {self.gender}\nTension : {self.tension}\nCholesterol : {self.cholesterol}\n"\
            f"Pulse : {self.pulse}\nDisease : {self.disease}\n"
