from typing import TYPE_CHECKING, Any, Iterable, Optional, Set, Tuple, Union

from django.contrib import auth
from django.contrib.auth.models import AnonymousUser, GroupManager, Permission
from django.core.exceptions import PermissionDenied
from django.db import models

from patient_management.core.models import ModelsBase

if TYPE_CHECKING:
    from .user import User


class Function(models.Model):
    name = models.CharField("name", max_length=150, unique=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name="permissions",
        blank=True,
    )

    objects = GroupManager()

    class Meta:
        verbose_name = "function"
        verbose_name_plural = "functions"

    def __str__(self) -> str:
        return self.name

    def natural_key(self) -> Tuple[str]:
        return (self.name,)


def _user_get_permissions(
    user: Union["User", AnonymousUser], obj: Optional[Any], from_name: str
) -> Set[str]:
    permissions = set()
    name = "get_%s_permissions" % from_name
    for backend in auth.get_backends():
        if hasattr(backend, name):
            permissions.update(getattr(backend, name)(user, obj))
    return permissions


def _user_has_perm(
    user: Union["User", AnonymousUser], perm: str, obj: Optional[Any]
) -> bool:
    for backend in auth.get_backends():
        if not hasattr(backend, "has_perm"):
            continue
        try:
            if backend.has_perm(user, perm, obj):
                return True
        except PermissionDenied:
            return False
    return False


def _user_has_module_perms(user: Union["User", AnonymousUser], app_label: str) -> bool:
    for backend in auth.get_backends():
        if not hasattr(backend, "has_module_perms"):
            continue
        try:
            if backend.has_module_perms(user, app_label):
                return True
        except PermissionDenied:
            return False
    return False


class PermissionsMixin(models.Model):
    is_superuser = models.BooleanField(
        "superuser status",
        default=False,
        help_text="Designates that this user has all permissions without "
        "explicitly assigning them.",
    )
    functions = models.ManyToManyField(
        Function,
        verbose_name="functions",
        blank=True,
        help_text="The functions this user belongs to. A user will get all permissions "
        "granted to each of their functions.",
        related_name="users",
        related_query_name="profile",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="users",
        related_query_name="profile",
    )

    class Meta:
        abstract = True


class EmployeProfile(PermissionsMixin, ModelsBase):
    user = models.OneToOneField(
        "account.User",
        on_delete=models.CASCADE,
        related_name="profile",
    )
    first_name = models.CharField(  # noqa: DJ001
        verbose_name="first name",
        max_length=150,
        blank=True,
        null=True,
    )
    last_name = models.CharField(  # noqa: DJ001
        verbose_name="last name",
        max_length=150,
        blank=True,
        null=True,
    )
    crm = models.CharField(verbose_name="crm", max_length=150, blank=True, null=True)  # noqa: DJ001

    def __str__(self) -> str:
        return self.first_name or ""

    def get_user_permissions(self, obj: Optional[Any] = None) -> Set[str]:
        return _user_get_permissions(self.user, obj, "user")

    def get_group_permissions(self, obj: Optional[Any] = None) -> Set[str]:
        return _user_get_permissions(self.user, obj, "function")

    def get_all_permissions(self, obj: Optional[Any] = None) -> Set[str]:
        return _user_get_permissions(self.user, obj, "all")

    def has_perm(self, perm: str, obj: Optional[Any] = None) -> bool:
        # Active superusers have all permissions.
        if self.user.is_active and self.is_superuser:
            return True

        # Otherwise we need to check the backends.
        return _user_has_perm(self.user, perm, obj)

    def has_perms(
        self, perm_list: Union[Iterable[str], str], obj: Optional[Any] = None
    ) -> bool:
        if not isinstance(perm_list, Iterable) or isinstance(perm_list, str):
            raise ValueError("perm_list must be an iterable of permissions.")
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label: str) -> bool:
        if self.user.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self.user, app_label)
