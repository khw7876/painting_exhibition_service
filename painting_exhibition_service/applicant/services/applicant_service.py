from applicant.models import Applicant as ApplicantModel, Gender
from applicant.serializers import ApplicantSerializer

from user.models import User as UserModel

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
    applicant_serializer = ApplicantSerializer(data = create_data)
    applicant_serializer.is_valid(raise_exception=True)
    applicant_serializer.save(gender = gender_obj)