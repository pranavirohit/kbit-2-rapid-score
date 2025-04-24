class Categories:
    def __init__(self):
        self.data = {
            'verbal': {
                'all': False,
                'rawScore': False,
                'standScore': False,
                'confInt': False,
                'percentile': False,
                'descriptive': False,
                'ageEq': False

            },
            'nonverbal': {
                'all': False,
                'rawScore': False,
                'standScore': False,
                'confInt': False,
                'percentile': False,
                'descriptive': False,
                'ageEq': False
            },
            'composite': {
                'all': False,
                'standScore': False,
                'confInt': False,
                'percentile': False,
                'descriptive': False,
                'ageEq': False
            }
        }

    def select(self, testType, category):
        if testType in self.data and category in self.data[testType]:
            self.data[testType][category] = True
    