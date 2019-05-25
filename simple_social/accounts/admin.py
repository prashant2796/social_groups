from django.contrib import admin
from . import models
from groups.models import Group,GroupMember

# Register your models here.

class GroupMemberInLine(admin.TabularInline):
	model = GroupMember
	
admin.site.register(Group)
