from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.cache import cache_page
from functools import wraps

import logging

from djamboloader       import settings
from djamboloader.util  import LibraryLoader

logger = logging.getLogger("djamboloader")

SUPPORTED_FILE_TYPES = {
  ".css": "text/css",
  ".js":  "application/javascript",
}


def cache_library(load_view):
  '''Caches the page if 'cache_for' is set in settings'''

  def get_cache_ttl(library=None):
    cache_ttl = None
    libconfig = settings.LIBRARIES.get(library)
    if libconfig is not None:
      cache_ttl = libconfig.get('cache_for')
    return cache_ttl

  @wraps(load_view)
  def wrapper(request, library=None):
    cache_ttl = get_cache_ttl(library)
    if cache_ttl is not None:
      cached_load_view = cache_page(load_view, cache_ttl)
      return cached_load_view(request, library)
    else:
      return load_view(request, library)
  return wrapper
 
   
@cache_library
def load(request, library=None):
  """
  Django view to load and combine a list of javascript/css files passed
  as GET query parameters for the given library.
  """
  libs = None
  mimetype = None

  if request.GET:
    libs = request.GET.keys()

  # Process and validate query parameters
  if not libs:
    logger.error("Missing parameters")
    return HttpResponseBadRequest()

  for ext, mimetype in SUPPORTED_FILE_TYPES.iteritems():
    if libs[0].endswith(ext):
      break

  if mimetype is None:
    logger.error("Unsupported file format")
    return HttpResponseBadRequest()

  for lib in libs:
    if not lib.endswith(ext):
      logger.error("All parameters must be of the same type")
      return HttpResponseBadRequest()

  if not settings.LIBRARIES.has_key(library):
    logger.error("Unsupported library")
    return HttpResponseBadRequest()

  # Get library configuration and run the loader to combine files

  libconfig = settings.LIBRARIES[library]

  loader = LibraryLoader(libconfig["path"])
  response = loader.combine(libs)

  return HttpResponse(response, mimetype=mimetype)
