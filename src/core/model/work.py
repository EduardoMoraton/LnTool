from profile import Profile
import re

class Work:
    def __init__(self, search_name, location, job_name, profile: Profile, apply_link, desc):
        self.search_name = search_name
        self.location = location
        self.job_name = job_name
        self.profile = profile
        self.apply_link = apply_link
        self.desc = desc
        pass
    
    def pass_filter(self, pattern):
        return re.match(pattern, self.desc)
        
    def __str__(self):
        return "name: " + self.job_name + " link: " + self.apply_link