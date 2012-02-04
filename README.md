# djamboloader

**djamboloader** (for django combo loader) is a django application used to load
and combine a list of javascript or css files from the filesystem for a
specific library. 

It is very useful for projects containing a lot of javascript
or css files where making one single HTTP request that combines all required 
files at once can improve performance of a web application significantly. 

**djamboloader** is inspired by the combo handler provided by Yahoo! for YUI3 
(http://yui.yahooapis.com/combo) and is intended for developers willing to run
their own combo handler. It makes it easy to integrate the handler in your 
existing django web application but can also be run as a standalone handler.

## Installation

To add **djamboloader** to your django webapp you have to make sure the path 
to **djamboloader** is in your PYTHONPATH, add `'djamboloader'` to your django
`INSTALLED\_APPS` and add the following to your django url patterns:

    url(r'^djamboloader/', include('djamboloader.urls'))

Feel free to also add a new handler in your django logging configuration
for `'djamboloader'`.

For more information on how to setup django, refer to
http://www.djangoproject.com

## Configuration

To configure **djamboloader**, open djamboloader/settings.py and edit the LIBRARIES 
definition, for example:

    LIBRARIES = {
      "yui3": {
        "path": "/home/libs/yui3/build/",
      }.
      "yui2in3": {
        "path": "/home/libs/yui2in3/dist/2.8.0/build/",
      },
      "mylib": {
        "path": "/home/libs/mylib/build/",
      },
    }

## Examples

http://yourserver.com/djamboloader/yui3/combo?base/base.js&dom/dom.js&node/node.js...
http://yourserver.com/djamboloader/yourlib/combo?pathto/libfile1.js&pathto/libfile2.js...
will return a single response with all requested javascript files combined

