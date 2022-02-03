
from user import User


class Troublemaker(User):

    WARNING_PERCENT = 0.75
    LOCK_LIMIT = 1.2
    REMINDER = "\nYou exceeded 75% of your budget"
    EXCEEDED_MSG = "\nexceeded your budget"
    LOCK_MSG = "\nBudget is locked"
