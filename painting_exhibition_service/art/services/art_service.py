from user.models import User as UserModel

def check_is_artist(user : UserModel):
    if user.artist_set:
        return True
    return False
