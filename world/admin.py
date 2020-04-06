from django.contrib import admin

from .models import (Contact, ConstructionUnit, DesignInstitute, Address,
                     Department, Staff, Expert, ExpertReview, ReviewCom,
                     Commission, Project)

# Register your models here.

admin.site.register(Contact)
admin.site.register(ConstructionUnit)
admin.site.register(DesignInstitute)
admin.site.register(Address)
admin.site.register(Department)
admin.site.register(Staff)
admin.site.register(Expert)
admin.site.register(ExpertReview)
admin.site.register(ReviewCom)
admin.site.register(Commission)
admin.site.register(Project)

