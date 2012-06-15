# djamboloader

**djamboloader** (for django combo loader) is a simple django application used
to load and combine a list of javascript or css files from the filesystem for 
a specific library. 

It is very useful for projects containing a lot of javascript
or css files where making one single HTTP request that combines all required 
files at once can improve performance of a web application significantly. 

**djamboloader** is inspired by the combo handler provided by Yahoo! for YUI3 
(http://yui.yahooapis.com/combo) and is intended for developers willing to run
their own combo handler. It makes it easy to integrate the handler in your 
existing django web application but can also be run as a standalone handler.

**djamboloader** is available for use under the MIT software license. See LICENSE file for more details.

## Installation

To add **djamboloader** to your django webapp you have to make sure the path 
to **djamboloader** is in your PYTHONPATH, add `'djamboloader'` to your django
`INSTALLED_APPS` and add the following to your django url patterns:

    url(r'^djamboloader/', include('djamboloader.urls'))

Feel free to also add a new handler in your django logging configuration
for `'djamboloader'`.

For more information on how to setup django, refer to
http://www.djangoproject.com

## Configuration

To configure **djamboloader**, open djamboloader/settings.py and edit the 
`LIBRARIES` definition, for example:

    LIBRARIES = {
      "yui3": {
        "path": "/home/libs/yui3/build/",
      },
      "yui2in3": {
        "path": "/home/libs/yui2in3/dist/2.8.0/build/",
      },
      "mylib": {
        "path": "/home/libs/mylib/build/",
      },
    }

## Configuration through Django's settings.py file

Alternatively, you could configure djamboloader in Django's settings.py file by 
using the JAVASCRIPT_LIBRARIES setting. 
The syntax is the same as for LIBRARIES above.

Djamboloader will try to import from Django's settings.py file first, then it falls
back on djamboloader/settings.py.

This option will make it easier to install djamboloader as a package in virtual environment 
and to easily upgrade to later versions, without having to change anything inside the
djamboloader package itself.

## Caching

Djamboloader supports caching of the JavaScript libraries by using Django's cache framework.

The first step is to make sure you have set up the Django cache as described in the Django documentation.

After that, you can use the *cache_for* setting to specify how many seconds would you like to cache each library.

Example for a Django settings.py file:

    TEN_DAYS = 10 * 24 * 60 * 60
    THIRTY_DAYS = 30 * 24 * 60 * 60
    JAVASCRIPT_LIBRARIES = {
        "yui_3_5_1": {
            "path": os.path.join(PROJECT_DIRECTORY, "static/javascript/lib/yui-3.5.1/build/"),
            "cache_for": TEN_DAYS, 
        },
        "yui2in3_2_9_0": {
            "path": os.path.join(PROJECT_DIRECTORY, "static/javascript/lib/yui-2in3/dist/2.9.0/build/"),
            "cache_for": THIRTY_DAYS,
        },
    }

In the example above YUI 3 will be cached for 10 days, yui2in3 will be cached for 30 days.
The *cache_for* setting is optional, in case you don't use it the libraries won't be cached at all. 

_Note_ In case you do cache for a long period, it is probably a good idea to include the version number
of the JS library in the URL (as you see above) to make upgrading of libraries easier.

## Examples

http://yourserver.com/djamboloader/yui3/combo?base/base.js&dom/dom.js&node/node.js...
http://yourserver.com/djamboloader/yourlib/combo?pathto/libfile1.js&pathto/libfile2.js...

will return a single response with all requested javascript files combined
