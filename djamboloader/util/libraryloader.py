import os
import logging

logger = logging.getLogger("djamboloader")

class LibraryLoader:
  """
  LibraryLoader is used to load and combine a list of libraries from the
  filesystem for a given path
  """
  def __init__(self, path, logger=None):
    self.path = path

  def combine(self, libs):
    """
    Loads files from filesystem and combines them into one string
    input: list of files within given path (see constructor)
    output: combined result of all files
    """
    if not libs:
      return

    content = ""

    for lib in libs:
      path = os.path.join(self.path, lib)
      path = os.path.abspath(path)

      try:
        f = open(path, "r")
        content += f.read()
        f.close()
      except IOError, e:
        logger.error(e)

    return content
