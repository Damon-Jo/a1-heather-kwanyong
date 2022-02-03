
from user import User


class Angel(User):

    WARNING_PERCENT = 0.9
    LOCK_LIMIT = None
    REMINDER = "\nYou exceeded 90% of your budget"
    EXCEEDED_MSG = "\nexceeded your budget"
