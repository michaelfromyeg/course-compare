import datetime

class Course:
    '''
    An object representing a course on the UBC Academic Calendar
    '''
    
    # TODO: add way of capturing length of class on different days (to visualize)

    def __init__(self, name, number, section, location, description, time, lab: 'Course'=None, tutorial: 'Course'=None, discussion: 'Course'=None):
        self.name = name
        self.number = number
        self.section = section
        self.short_name = f"{self.name} {self.number}"
        self.long_name = f"{self.name} {self.number} {self.section}"
        self.location = self.location_helper(location)
        self.description = self.description_helper(description)
        self.time = [datetime.datetime.strptime(time, '%Y-%m-%d').weekday()]
        # Recursive definition of lab, tutorial, discussion
        # TODO: make lab, tutorial, discussion subclasses of course
        self.lab = lab
        self.tutorial = tutorial
        self.discussion = discussion
    
    def add_time(self, o_course: 'Course') -> None:
        '''
        Append a course's timeslot onto this course
        '''
        if (o_course.time[0] in self.time):
            return
        self.time.append(o_course.time[0])
        self.time = sorted(self.time)
    
    # Setters for lab, tutorial, discussion
    def set_lab(self, o_course: 'Course') -> None:
        self.lab = o_course
    def set_tutorial(self, o_course: 'Course') -> None:
        self.tutorial = o_course
    def add_discussion(self, o_course: 'Course') -> None:
        self.discussion = o_course
    
    def is_extra(self) -> bool:
        '''
        Return whether or not this course has an additional lab, tutorial, or discussion
        '''
        return 'L' in self.section or 'T' in self.section or 'D' in self.section

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
        return f"{self.name} {self.number} {self.section} in {self.location} at {self.time} with lab: {self.lab} | tut: {self.tutorial} | disc: {self.discussion}"