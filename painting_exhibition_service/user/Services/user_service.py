from django.contrib.auth.hashers import check_password
from user.serializers import UserSignupSerializer, UserUpdateSerializer
from user.models import User as UserModel

def create_user(create_data : dict[str,str]) -> None:
    """
    Args:
        create_data (dict[str,str]): views.py에서 넘겨준 request.data{
            "username" (str): user의 username,
            "password: (str): user의 password
        }
    """
    user_data_serializer = UserSignupSerializer(data=create_data)
    user_data_serializer.is_valid(raise_exception=True)
    user_data_serializer.save()
    
def update_user(update_data : dict[str, str], user_id : int) -> None:
    user_for_update = UserModel.objects.get(id=user_id)
    update_data["cur_password"] = user_for_update.password
    user_data_serializer = UserUpdateSerializer(user_for_update, data=update_data, partial=True)
    user_data_serializer.is_valid(raise_exception=True)
    user_data_serializer.save()

def check_password_is_possible(password, user_id):
    user_for_check = UserModel.objects.get(id=user_id)
    if (check_password(password, user_for_check.password)):
        return True
    return False

def delete_user(user_id):
    user_for_delete = UserModel.objects.get(id=user_id)
    user_for_delete.is_active = False