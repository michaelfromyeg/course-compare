import datetime

class Course:
    '''
    An object representing a course on the UBC Academic Calendar
    '''
    
    # TODO: add way of capturing length of class on different days (to visualize)
    # TODO: add lab, tutorial, discussion support
    
    def __init__(self, name, number, section, location, description, time):
        self.name = name
        self.number = number
        self.section = section
        self.long_name = f"{self.name} {self.number} {self.section}"
        self.location = self.location_helper(location)
        self.description = self.description_helper(description)
        self.time = [datetime.datetime.strptime(time, '%Y-%m-%d').weekday()]
    
    def add_time(self, o_course: 'Course') -> None:
        '''
        Append a course's timeslot onto this course
        '''
        if (o_course.time[0] in self.time):
            return
        self.time.append(o_course.time[0])
        self.time = sorted(self.time)
    
    def __eq__(self, o_course: 'Course') -> bool:
        '''
        Compare two classes
        '''
        return self.long_name == o_course.long_name

    @staticmethod
    def location_helper(loc: str) -> str:
        '''
        Clean incoming location data
        '''
        if not loc or loc == ", Room ":
            return "NA"
        return loc

    @staticmethod
    def description_helper(desc: str) -> str:
        '''
        Clean incoming description data
        '''
        return desc.replace('\n', " ").replace("  ", " ") + "\n"

    def __str__(self):
        return f"{self.name} {self.number} {self.section} in {self.location} at {self.time}"