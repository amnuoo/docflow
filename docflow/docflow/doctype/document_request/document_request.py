from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class DocumentRequest(Document):

    def before_insert(self):
        """Automatically store the user who created the request."""
        if not self.requested_by:
            self.requested_by = frappe.session.user