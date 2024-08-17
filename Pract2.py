class College:
    
    name = 'R.A.Podar College'

    def college_name(cls):
        print('College Name is :', cls.name)

College.college_name = classmethod(College.college_name)

College.college_name()
