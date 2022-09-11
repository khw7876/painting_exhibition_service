from user.models import User as UserModel
from art.serializers import ArtSerializer
from applicant.models import Artist as ArtistModel
def check_is_artist(user : UserModel):
    try:
        ArtistModel.objects.get(user=user.id)
        return True
    except ArtistModel.DoesNotExist:
        return False

def create_art(create_data, user):
    create_data["artist"] = ArtistModel.objects.get(user=user.id).id
    art_serializer = ArtSerializer(data=create_data)
    art_serializer.is_valid(raise_exception=True)
    art_serializer.save()

