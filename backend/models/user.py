class User:
    id = 0
    name = ''
    points = 0
    access_token = ''

    def __init__(self, id, name, points, access_token):
        self.id = id
        self.name = name
        self.points = points
        self.access_token = access_token