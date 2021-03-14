import requests
from ics import Calendar
from controllers.course import Course

class Reader:
    '''
    Course reader to build a course object (friendly for this module) from a .ics file
    '''

    def __init__(self, url: str, filename: str):
        self.cal = None
        self.reader_courses = []
        self.url = url
        self.filename = filename
    
    def init_calendar_file(self) -> None:
        '''
        Initialize calendar object through an iCal file
        '''
        with open(self.filename, 'r') as f:
            calendar_content = f.read()
            self.cal = Calendar(calendar_content)
    
    def init_calendar_url(self) -> None:
        '''
        Initialize calendar object through a URL
        '''
        self.cal = Calendar(requests.get(self.url).text)
    
    def events_to_course_list(self, ical_events):
        '''
        Convert event list to a list of courses
        '''

        # Build course list
        for ical_course in ical_events:
            course_name, course_number, course_section = ical_course.name.split(" ")
            new_course = Course(course_name, course_number, course_section, ical_course.location, ical_course.description, str(ical_course.begin).split("T")[0])
            self.course_list_merge(new_course)
        
        return self.reader_courses

    def course_list_merge(self, course_to_add) -> None:
        '''
        Merge two courses in a students calendar
        
        ASSUME: If a lab section appears the course's lecture section, assume the lecture will appear again, and then the lab again after that;
                this will ensure the lab is properly added
        '''
        # No courses to add
        if not course_to_add:
            return None
        
        # No existing courses, add it and return
        if len(self.reader_courses) == 0:
            self.reader_courses.append(course_to_add)
            return None
        
        # Check all old courses, and do the comparison
        for old_course in self.reader_courses:
            # Check for lab
            if ('L' in course_to_add.section and old_course.short_name == course_to_add.short_name):
                old_course.set_lab(course_to_add)
                return None
            # Check for tutorial
            if ('T' in course_to_add.section and old_course.short_name == course_to_add.short_name):
                old_course.set_tutorial(course_to_add)
                return None        
            # Check for discussion
            if ('D' in course_to_add.section and old_course.short_name == course_to_add.short_name):
                old_course.set_discussion(course_to_add)
                return None
            # Check for merge (add the time)
            if old_course.long_name == course_to_add.long_name:
                old_course.add_time(course_to_add)
                return None
        
        # Simply add the course, as long as its not a lab, tutorial, or discussion
        if not course_to_add.is_extra():
            self.reader_courses.append(course_to_add)
        return None

    def get_calendar(self) -> 'Calendar':
        return self.cal

    @staticmethod
    def is_course(event) -> bool:
        '''
        Checks if a given event is actually a course
        TODO: Update this to comapre against UBC Academic Calendar, or something similar
        '''
        return ('STAT 200 101' == event.name or 
                'LING 200 001' == event.name or
                'MATH 200 105' == event.name or
                'CPSC 221 101' == event.name or
                'CPSC 221 L1N' == event.name or
                'CPSC 213 101' == event.name or
                'CPSC 213 L1N' == event.name)
    
    def __self__(self):
        return f"Source: {self.filename}"
