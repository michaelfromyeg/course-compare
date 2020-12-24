from reader import Reader

class User:
    '''
    A class representing a user of the application, including username, password, and a course list
    '''

    def __init__(self, email, password, courses):
        self.email = email
        self.password = password
        self.courses = courses
    
    def share_class(self, o_user: 'User') -> bool:
        '''
        Check if two users share a course
        '''
        for course in self.courses:
            if course in o_user.courses:
                return True
        return False

    def add_courses(self, filename: str) -> None:
        '''
        Add the courses at a given filename to this user
        '''
        ical_event = Reader("", filename)
        ical_event.init_calendar_file()
        ical_events = ical_event.get_calendar().events
        ical_courses = ical_event.events_to_course_list(ical_events)
        self.courses = ical_courses
    
    def print_courses(self):
        '''
        Print this users current courses
        '''
        for course in self.courses:
            print(course)

    def classmates(self, o_users):
        '''
        Return a list of names that represent all of the people this person shares a class with
        '''
        classmates = []
        for user in o_users:
            for course in self.courses:
                if course in user.courses:
                    classmates.append(user.email)
                    break
        return classmates

    def __str__(self):
        return f"USER: {self.email} with {self.password}"