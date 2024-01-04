from . import __version__ as app_version

app_name = "mehta"
app_title = "Mehta Group"
app_publisher = "Prashant Kamble"
app_description = "Mehta Group Customisation(EXPAI & CADCAM)"
app_email = "kambleprashant@outlook.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mehta/css/mehta.css"
# app_include_js = "/assets/mehta/js/mehta.js"

# include js, css files in header of web template
# web_include_css = "/assets/mehta/css/mehta.css"
# web_include_js = "/assets/mehta/js/mehta.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mehta/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}
fixtures = [
	 {"doctype": "Custom Field",
	  "filters": [
		[
            "name", "in", [
                "BOM-name_of_bom",
                "BOM Item-reference",
                "BOM Explosion Item-reference",
                "Material Request-requester",
                "Material Request-your_purpose",
                "Purchase Receipt-supplier_invoice_date",
                
            ]
        ]
    ]},
]
# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views

doctype_js = {
    "Journal Entry" : "public/js/journal_entry.js",
}


# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "mehta.utils.jinja_methods",
#	"filters": "mehta.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mehta.install.before_install"
# after_install = "mehta.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mehta.uninstall.before_uninstall"
# after_uninstall = "mehta.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mehta.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"mehta.tasks.all"
#	],
#	"daily": [
#		"mehta.tasks.daily"
#	],
#	"hourly": [
#		"mehta.tasks.hourly"
#	],
#	"weekly": [
#		"mehta.tasks.weekly"
#	],
#	"monthly": [
#		"mehta.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "mehta.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "mehta.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "mehta.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mehta.utils.before_request"]
# after_request = ["mehta.utils.after_request"]

# Job Events
# ----------
# before_job = ["mehta.utils.before_job"]
# after_job = ["mehta.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"mehta.auth.validate"
# ]
