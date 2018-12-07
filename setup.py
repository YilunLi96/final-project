requirements = ['math', 'theory', 'technical', 'breadth']

class cs182:
	name = ['cs182']
	# concurrent?
	pre_req = ['cs51', 'stat110']
	satisfying_req = ['breadth', 'elective']
	semester = ['fall']

class cs181:
	name = ['cs181']
	pre_req = ['cs51', 'stat110', '']
	satisfying_req = ['breadth', 'elective']
	semester = ['fall']


class Course:
    def __init__(self, name, prereqs, satisfies, sem):
        self.name = name
        self.semester = sem
        self.prereqs = prereqs
        self.satisfies = satisfies



        # The values still remaining for a factor.
        self.factorRemaining = {}

        # The number of conflicts at a factor.
        self.factorNumConflicts = {}

        # For local search. Keep track of the factor state.
        if isFirstLocal:
            self._initLocalSearch()


cs182 = Course(nam,pre,sat,sem)

