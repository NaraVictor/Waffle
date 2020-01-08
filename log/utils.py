from .models import *


def log_error(error_type, error_msg, app_name, **kwargs):
    """function used to log server errors into database. 
       additional **kwargs expected: url & user_id (both optional)
    """
    url = kwargs.get('url', '')
    user_id = kwargs.get('user_id', '')

    ErrorLogger.objects.create(
        error_type=error_type,
        error_msg=error_msg,
        app=app_name,
        url=url,
        user_id=user_id
    )
