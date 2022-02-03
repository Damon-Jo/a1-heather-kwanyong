
from user import User

class Rebel(User):

    WARNING_LIMIT = 0.5
    LOCK_LIMIT = 1
    LOCKED_ACCOUNTS_ALLOWED = 2
    REMINDER = "\nYou exceeded 50% of your budget"
    EXCEEDED_MSG = "\nexceeded your budget"
    LOCK_MSG = "\nBudget is locked"
