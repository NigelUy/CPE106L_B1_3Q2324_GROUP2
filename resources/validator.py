import re

class Validator():
    def __init__(self) -> None:
        pass

    def is_correct_user(self, user):
        if not isinstance(user, str):
            return None
        if len(user.strip(), ) < 2:
            return None
        if not all(c.isalpha() or c.isspace() or c in "-'." for c in user):
            return None
        
        return True
    
    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def is_valid_password(self, password):
        r_p = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
        if not r_p.match(password):
            return False
        
        return True
    