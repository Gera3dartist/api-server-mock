from api_server_mock.models.domain.row_model import RowModel
from api_server_mock.models.domain.common import DateTimeModelMixin, IDModelMixin, PublicIDModelMixin


class User(RowModel):
    email: str
    name: str


class UserInDB(DateTimeModelMixin, PublicIDModelMixin, IDModelMixin, User):
    pass
