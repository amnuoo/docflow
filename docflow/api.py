import frappe

@frappe.whitelist()
def get_archived_versions(parent):
    return frappe.get_all(
        "Document Version",
        filters={"parent": parent, "archived": 1},
        fields=["name", "version_no", "uploaded_on", "file"]
    )

@frappe.whitelist()
def unarchive_version(name):
    dv = frappe.get_doc("Document Version", name)
    dv.archived = 0
    dv.is_latest = 0
    dv.save(ignore_permissions=True)
    return "Unarchived"
