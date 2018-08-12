
# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.db import models
from organizations.abstract import AbstractOrganization, AbstractOrganizationUser, AbstractOrganizationOwner


class Organization(AbstractOrganization):

    image=models.ImageField()

    class Meta:
        verbose_name = _("organizacion")
        verbose_name_plural = _("organizaciones")


class OrganizationUser(AbstractOrganizationUser):
    pass


class OrganizationOwner(AbstractOrganizationOwner):
    pass