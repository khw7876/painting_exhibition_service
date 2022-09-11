from applicant.models import Applicant as ApplicantModel, Gender, Status
from applicant.serializers import ApplicantSerializer, ArtistSerializer

from user.models import User as UserModel

def read_apply():
    all_applicant = ApplicantModel.objects.all()
    applicant_serializer = ApplicantSerializer(all_applicant, many = True).data
    return applicant_serializer


def create_apply(create_data: dict[str, str], user: UserModel) -> None:
    """
    Args:
        create_data (dict[str, str]): {
            "title" (str) : 20자 이하의 제목,
            "content" (str) : 200자 이하의 내용,
            "password" (str) : 숫자를 포함한 6글자 이상의 비밀번호
        }
    """
    create_data["user"] = user.id
    gender_str = create_data.pop("gender")
    gender_obj = Gender.objects.get(gender = gender_str)
    status_obj = Status.objects.get(status="waiting")
    applicant_serializer = ApplicantSerializer(data = create_data)
    applicant_serializer.is_valid(raise_exception=True)
    applicant_serializer.save(gender = gender_obj, status=status_obj)

def check_admin(user: UserModel):
    if user.is_admin == True:
        return True
    return False

def check_is_applied(user: UserModel):
    try:
        ApplicantModel.objects.get(user = user)
        return False
    except ApplicantModel.DoesNotExist:
        return True

def accept_applicant(applicant_id_list):
    for applicant_id in applicant_id_list:
        accept_applicant_obj = ApplicantModel.objects.get(id=applicant_id)
        applicant_serializer = ApplicantSerializer(accept_applicant_obj).data
        artist_serializer = ArtistSerializer(data=applicant_serializer)
        artist_serializer.is_valid(raise_exception=True)
        accept_status = Status.objects.get(status = "accept")
        accept_applicant_obj.status = accept_status
        artist_serializer.save()
