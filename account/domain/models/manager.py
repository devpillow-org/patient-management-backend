from typing import TYPE_CHECKING, Any, Optional

from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as DefaultManager
from django.db import IntegrityError, transaction

from account.domain.models.profile import EmployeProfile

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class UserManager(DefaultManager["User"]):
    def _create_user(  # type: ignore
        self,
        username: str,
        password: Optional[str],
        **extra_fields: Any,
    ):
        if not username:
            raise ValueError("The given username must be set")

        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        try:
            with transaction.atomic():
                user = self.model(username=username)
                user.password = make_password(password)
                user.save(using=self._db)

                profile = EmployeProfile(**extra_fields, user=user)
                profile.save(using=self._db)

        except IntegrityError as e:
            raise e
        return user

    def create_user(  # type: ignore
        self,
        username: str,
        password: Optional[str] = None,
        **extra_fields: Any,
    ):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(  # type: ignore
        self,
        username: str,
        password: Optional[str] = None,
        **extra_fields: Any,
    ):
        extra_fields.setdefault("is_superuser", True)

        is_superuser = extra_fields.get("is_superuser")
        if not is_superuser or is_superuser is None:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)
