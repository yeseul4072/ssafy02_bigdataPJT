from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model


def custom_user_field(user, field, *args):
    """
    Sets (optional) user model fields. No-op if fields do not exist.
    """
    if not field:
        return
    User = get_user_model()
    try:
        field_meta = User._meta.get_field(field)
        max_length = field_meta.max_length
    except FieldDoesNotExist:
        if not hasattr(user, field):
            return
        max_length = None
    if args:
        # Setter
        v = args[0]
        if hasattr(v, "__getitem__"):
            v = v[0:max_length]
        setattr(user, field, v)
    else:
        # Getter
        return getattr(user, field)


class CustomUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        
        user = super().save_user(request, user, form, False)
        custom_user_field(user, 'latitude', request.data.get('latitude', None))
        custom_user_field(user, 'longitude', request.data.get('longitude', None))
        custom_user_field(user, 'address', request.data.get('address', None))
        custom_user_field(user, 'nickname', request.data.get('nickname', ''))
        custom_user_field(user, 'is_director', request.data.get('is_director', False))
        custom_user_field(user, 'kindergarten_id', request.data.get('kindergarten_id', 1))
        custom_user_field(user, 'profile_image', request.data.get('profile_image', None))
        user.save()
        return user