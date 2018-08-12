from django.contrib import admin

# Register your models here.
from organizations.base_admin import BaseOwnerInline, BaseOrganizationAdmin, BaseOrganizationUserAdmin, \
    BaseOrganizationOwnerAdmin
from organizations.models import Organization, OrganizationUser, OrganizationOwner

from users.models import Organization as Organizacion
from users.models import OrganizationOwner as OrganizacionOwner
from users.models import OrganizationUser as OrganizacionUsuario



class OwnerInline(BaseOwnerInline):
    model = OrganizacionOwner


class OrganizationAdmin(BaseOrganizationAdmin):
    inlines = [OwnerInline]


class OrganizationUserAdmin(BaseOrganizationUserAdmin):
    pass


class OrganizationOwnerAdmin(BaseOrganizationOwnerAdmin):
    pass



admin.site.unregister(Organization)
admin.site.unregister(OrganizationUser)
admin.site.unregister(OrganizationOwner)
admin.site.register(Organizacion, OrganizationAdmin)
admin.site.register(OrganizacionOwner, OrganizationOwnerAdmin)
admin.site.register(OrganizacionUsuario, OrganizationUserAdmin)