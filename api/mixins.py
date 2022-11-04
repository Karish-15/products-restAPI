from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffEditorMixin():
    permission_classes = [
        IsStaffEditorPermission,
        permissions.IsAdminUser,
    ]