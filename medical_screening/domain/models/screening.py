from django.db import models

from account.domain.models import EmployeProfile
from patient_management.core.models import ModelsBase


class MedicalChart(models.Model):  # noqa: DJ008
    complaints = models.TextField("patient complaints")
    prescription = models.TextField("doctor prescription")
    report = models.TextField("doctor report")


class PatientProfile(ModelsBase):
    first_name = models.CharField("patient first name", max_length=150, null=False)
    last_name = models.CharField("patient last name", max_length=150, null=False)


class Patient(models.Model):
    status = models.CharField("patient status", max_length=150)
    profile = models.OneToOneField(
        PatientProfile,
        verbose_name="patient profile",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.profile.first_name} {self.profile.last_name}"  # type: ignore


class SickNotes(ModelsBase):
    description = models.TextField("description of sick notes")
    created_by = models.ForeignKey(
        EmployeProfile,
        verbose_name="doctor who prescribe that sick note",
        on_delete=models.DO_NOTHING,
    )
    patient = models.ForeignKey(
        Patient,
        verbose_name="patient of sicknote",
        on_delete=models.DO_NOTHING,
    )
    print_count = models.IntegerField("quantity of print", default=0)
    medical_chart = models.ForeignKey(
        MedicalChart, verbose_name="medical chart", on_delete=models.DO_NOTHING
    )


class Department(ModelsBase):
    name = models.CharField("department name", max_length=150)
    workers = models.ManyToManyField(
        EmployeProfile,
        verbose_name="workers of department",
        blank=True,
        related_name="department",
    )


class Screening(models.Model):
    patient = models.ForeignKey(
        Patient,
        verbose_name="patient of screening",
        on_delete=models.DO_NOTHING,
        related_name="screenings",
        null=False,
    )
    is_closed = models.BooleanField("is screening closed", default=False)
    opening_date = models.DateTimeField("screning opening date", auto_now_add=True)
    closed_date = models.DateTimeField("screening closed date", null=True)

    def __str__(self) -> str:
        return f"Screening of {self.opening_date} of {self.patient}"


class ScreeningSteps(models.Model):
    last_step = models.ForeignKey(
        "self",
        verbose_name="last step",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    description = models.TextField("description")
    forwarded_from = models.ForeignKey(
        Department,
        verbose_name="patient forwarded from",
        on_delete=models.DO_NOTHING,
        related_name="comes_from",
    )
    forwarded_by = models.ForeignKey(
        EmployeProfile,
        verbose_name="forwarded by",
        on_delete=models.DO_NOTHING,
    )
    forwarded_to = models.ForeignKey(
        Department,
        verbose_name="patitent forwaeded to",
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="fowarded_to",
    )
    action_date = models.DateTimeField("date of action", auto_now=True)
    status = models.CharField("screening step status", max_length=50)
    screening = models.ForeignKey(
        Screening,
        verbose_name="step of screnning",
        on_delete=models.DO_NOTHING,
        related_name="steps",
    )
    medical_chart = models.OneToOneField(
        MedicalChart,
        verbose_name="medical chart",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self) -> str:
        return f"Patient forwarded from {self.forwarded_from} to {self.forwarded_to}"
