import frappe

@frappe.whitelist()
def get_archived_versions(parent):
    return frappe.get_all(
        "Document Version",
        filters={"parent": parent, "archived": 1},
        fields=["name", "version_no", "uploaded_on", "file"]
    )
