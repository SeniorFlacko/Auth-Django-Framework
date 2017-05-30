from django.contrib.auth.models import User

class EmailAuthBackend(object):
    '''
    Authenticate using e-mail account.
    authenticate() : Takes user credentials as parameters. Has to return
    True if the user has been successfully authenticated, or False otherwise.
    '''

    def authenticate(self,username=None,password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
