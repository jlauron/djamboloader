# Library configuration:
#
# LIBRARIES = {
#   "LIBRARY_NAME": {
#     "path": "LIBRARY_FILESYSTEM_PATH",
#   },
#   ...
# }
#

from django.conf import settings as django_settings

LIBRARIES = getattr(django_settings, 'JAVASCRIPT_LIBRARIES', '')

# Overwrite your settings.JAVASCRIPT_LIBRARIES here if required
#
# LIBRARIES = {
# }

