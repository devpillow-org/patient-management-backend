from django.db import models


class ModelsBase(models.Model):
    created_at = models.DateTimeField(
        "created at",
        help_text="Date which that instance has been created",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        "updated at",
        auto_now=True,
        help_text="Last time which that instance has been modified",
    )

    class Meta:
        abstract = True
