#   This library is free software; you can redistribute it and/or
#   modify it under the terms of the GNU Lesser General Public
#   License as published by the Free Software Foundation; either
#   version 2.1 of the License, or (at your option) any later version.
#
#   This library is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with this library; if not, write to the 
#      Free Software Foundation, Inc., 
#      59 Temple Place, Suite 330, 
#      Boston, MA  02111-1307  USA

# This file is part of urlgrabber, a high-level cross-protocol url-grabber
# Copyright 2002-2004 Michael D. Stenner, Ryan Tomayko
# Copyright 2009 Red Hat inc, pycurl code written by Seth Vidal

"""A high-level cross-protocol url-grabber.

GENERAL ARGUMENTS (kwargs)

  Where possible, the module-level default is indicated, and legal
  values are provided.

  copy_local = 0   [0|1]

    ignored except for file:// urls, in which case it specifies
    whether urlgrab should still make a copy of the file, or simply
    point to the existing copy. The module level default for this
    option is 0.

  close_connection = 0   [0|1]

    tells URLGrabber to close the connection after a file has been
    transfered. This is ignored unless the download happens with the
    http keepalive handler (keepalive=1).  Otherwise, the connection
    is left open for further use. The module level default for this
    option is 0 (keepalive connections will not be closed).

  keepalive = 1   [0|1]

    specifies whether keepalive should be used for HTTP/1.1 servers
    that support it. The module level default for this option is 1
    (keepalive is enabled).

  progress_obj = None

    a class instance that supports the following methods:
      po.start(filename, url, basename, length, text)
      # length will be None if unknown
      po.update(read) # read == bytes read so far
      po.end()

  text = None
  
    specifies alternative text to be passed to the progress meter
    object.  If not given, the default progress meter will use the
    basename of the file.

  throttle = 1.0

    a number - if it's an int, it's the bytes/second throttle limit.
    If it's a float, it is first multiplied by bandwidth.  If throttle
    == 0, throttling is disabled.  If None, the module-level default
    (which can be set on default_grabber.throttle) is used. See
    BANDWIDTH THROTTLING for more information.

  timeout = None

    a positive float expressing the number of seconds to wait for socket
    operations. If the value is None or 0.0, socket operations will block
    forever. Setting this option causes urlgrabber to call the settimeout
    method on the Socket object used for the request. See the Python
    documentation on settimeout for more information.
    http://www.python.org/doc/current/lib/socket-objects.html

  bandwidth = 0

    the nominal max bandwidth in bytes/second.  If throttle is a float
    and bandwidth == 0, throttling is disabled.  If None, the
    module-level default (which can be set on
    default_grabber.bandwidth) is used. See BANDWIDTH THROTTLING for
    more information.

  range = None

    a tuple of the form (first_byte, last_byte) describing a byte
    range to retrieve. Either or both of the values may set to
    None. If first_byte is None, byte offset 0 is assumed. If
    last_byte is None, the last byte available is assumed. Note that
    the range specification is python-like in that (0,10) will yeild
    the first 10 bytes of the file.

    If set to None, no range will be used.
    
  reget = None   [None|'simple'|'check_timestamp']

    whether to attempt to reget a partially-downloaded file.  Reget
    only applies to .urlgrab and (obviously) only if there is a
    partially downloaded file.  Reget has two modes:

      'simple' -- the local file will always be trusted.  If there
        are 100 bytes in the local file, then the download will always
        begin 100 bytes into the requested file.

      'check_timestamp' -- the timestamp of the server file will be
        compared to the timestamp of the local file.  ONLY if the
        local file is newer than or the same age as the server file
        will reget be used.  If the server file is newer, or the
        timestamp is not returned, the entire file will be fetched.

    NOTE: urlgrabber can do very little to verify that the partial
    file on disk is identical to the beginning of the remote file.
    You may want to either employ a custom "checkfunc" or simply avoid
    using reget in situations where corruption is a concern.

  user_agent = 'urlgrabber/VERSION'

    a string, usually of the form 'AGENT/VERSION' that is provided to
    HTTP servers in the User-agent header. The module level default
    for this option is "urlgrabber/VERSION".

  http_headers = None

    a tuple of 2-tuples, each containing a header and value.  These
    will be used for http and https requests only.  For example, you
    can do
      http_headers = (('Pragma', 'no-cache'),)

  ftp_headers = None

    this is just like http_headers, but will be used for ftp requests.

  proxies = None

    a dictionary that maps protocol schemes to proxy hosts. For
    example, to use a proxy server on host "foo" port 3128 for http
    and https URLs:
      proxies={ 'http' : 'http://foo:3128', 'https' : 'http://foo:3128' }
    note that proxy authentication information may be provided using
    normal URL constructs:
      proxies={ 'http' : 'http://user:host@foo:3128' }
    Lastly, if proxies is None, the default environment settings will
    be used.

  prefix = None

    a url prefix that will be prepended to all requested urls.  For
    example:
      g = URLGrabber(prefix='http://foo.com/mirror/')
      g.urlgrab('some/file.txt')
      ## this will fetch 'http://foo.com/mirror/some/file.txt'
    This option exists primarily to allow identical behavior to
    MirrorGroup (and derived) instances.  Note: a '/' will be inserted
    if necessary, so you cannot specify a prefix that ends with a
    partial file or directory name.

  opener = None
    No-op when using the curl backend (default)

  cache_openers = True
    No-op when using the curl backend (default)

  data = None

    Only relevant for the HTTP family (and ignored for other
    protocols), this allows HTTP POSTs.  When the data kwarg is
    present (and not None), an HTTP request will automatically become
    a POST rather than GET.  This is done by direct passthrough to
    urllib2.  If you use this, you may also want to set the
    'Content-length' and 'Content-type' headers with the http_headers
    option.  Note that python 2.2 handles the case of these
    badly and if you do not use the proper case (shown here), your
    values will be overridden with the defaults.
    
  urlparser = URLParser()

    The URLParser class handles pre-processing of URLs, including
    auth-handling for user/pass encoded in http urls, file handing
    (that is, filenames not sent as a URL), and URL quoting.  If you
    want to override any of this behavior, you can pass in a
    replacement instance.  See also the 'quote' option.

  quote = None

    Whether or not to quote the path portion of a url.
      quote = 1    ->  quote the URLs (they're not quoted yet)
      quote = 0    ->  do not quote them (they're already quoted)
      quote = None ->  guess what to do

    This option only affects proper urls like 'file:///etc/passwd'; it
    does not affect 'raw' filenames like '/etc/passwd'.  The latter
    will always be quoted as they are converted to URLs.  Also, only
    the path part of a url is quoted.  If you need more fine-grained
    control, you should probably subclass URLParser and pass it in via
    the 'urlparser' option.

  ssl_ca_cert = None

    this option can be used if M2Crypto is available and will be
    ignored otherwise.  If provided, it will be used to create an SSL
    context.  If both ssl_ca_cert and ssl_context are provided, then
    ssl_context will be ignored and a new context will be created from
    ssl_ca_cert.

  ssl_context = None

    No-op when using the curl backend (default)
   

  self.ssl_verify_peer = True 

    Check the server's certificate to make sure it is valid with what our CA validates
  
  self.ssl_verify_host = True

    Check the server's hostname to make sure it matches the certificate DN

  self.ssl_key = None

    Path to the key the client should use to connect/authenticate with

  self.ssl_key_type = 'PEM' 

    PEM or DER - format of key
     
  self.ssl_cert = None

    Path to the ssl certificate the client should use to to authenticate with

  self.ssl_cert_type = 'PEM' 

    PEM or DER - format of certificate
    
  self.ssl_key_pass = None 

    password to access the ssl_key
    
  self.size = None

    size (in bytes) or Maximum size of the thing being downloaded. 
    This is mostly to keep us from exploding with an endless datastream
  
  self.max_header_size = 2097152 

    Maximum size (in bytes) of the headers.
    

RETRY RELATED ARGUMENTS

  retry = None

    the number of times to retry the grab before bailing.  If this is
    zero, it will retry forever. This was intentional... really, it
    was :). If this value is not supplied or is supplied but is None
    retrying does not occur.

  retrycodes = [-1,2,4,5,6,7]

    a sequence of errorcodes (values of e.errno) for which it should
    retry. See the doc on URLGrabError for more details on this.  You
    might consider modifying a copy of the default codes rather than
    building yours from scratch so that if the list is extended in the
    future (or one code is split into two) you can still enjoy the
    benefits of the default list.  You can do that with something like
    this:

      retrycodes = urlgrabber.grabber.URLGrabberOptions().retrycodes
      if 12 not in retrycodes:
          retrycodes.append(12)
      
  checkfunc = None

    a function to do additional checks. This defaults to None, which
    means no additional checking.  The function should simply return
    on a successful check.  It should raise URLGrabError on an
    unsuccessful check.  Raising of any other exception will be
    considered immediate failure and no retries will occur.

    If it raises URLGrabError, the error code will determine the retry
    behavior.  Negative error numbers are reserved for use by these
    passed in functions, so you can use many negative numbers for
    different types of failure.  By default, -1 results in a retry,
    but this can be customized with retrycodes.

    If you simply pass in a function, it will be given exactly one
    argument: a CallbackObject instance with the .url attribute
    defined and either .filename (for urlgrab) or .data (for urlread).
    For urlgrab, .filename is the name of the local file.  For
    urlread, .data is the actual string data.  If you need other
    arguments passed to the callback (program state of some sort), you
    can do so like this:

      checkfunc=(function, ('arg1', 2), {'kwarg': 3})

    if the downloaded file has filename /tmp/stuff, then this will
    result in this call (for urlgrab):

      function(obj, 'arg1', 2, kwarg=3)
      # obj.filename = '/tmp/stuff'
      # obj.url = 'http://foo.com/stuff'
      
    NOTE: both the "args" tuple and "kwargs" dict must be present if
    you use this syntax, but either (or both) can be empty.

  failure_callback = None

    The callback that gets called during retries when an attempt to
    fetch a file fails.  The syntax for specifying the callback is
    identical to checkfunc, except for the attributes defined in the
    CallbackObject instance.  The attributes for failure_callback are:

      exception = the raised exception
      url       = the url we're trying to fetch
      tries     = the number of tries so far (including this one)
      retry     = the value of the retry option

    The callback is present primarily to inform the calling program of
    the failure, but if it raises an exception (including the one it's
    passed) that exception will NOT be caught and will therefore cause
    future retries to be aborted.

    The callback is called for EVERY failure, including the last one.
    On the last try, the callback can raise an alternate exception,
    but it cannot (without severe trickiness) prevent the exception
    from being raised.

  interrupt_callback = None

    This callback is called if KeyboardInterrupt is received at any
    point in the transfer.  Basically, this callback can have three
    impacts on the fetch process based on the way it exits:

      1) raise no exception: the current fetch will be aborted, but
         any further retries will still take place

      2) raise a URLGrabError: if you're using a MirrorGroup, then
         this will prompt a failover to the next mirror according to
         the behavior of the MirrorGroup subclass.  It is recommended
         that you raise URLGrabError with code 15, 'user abort'.  If
         you are NOT using a MirrorGroup subclass, then this is the
         same as (3).

      3) raise some other exception (such as KeyboardInterrupt), which
         will not be caught at either the grabber or mirror levels.
         That is, it will be raised up all the way to the caller.

    This callback is very similar to failure_callback.  They are
    passed the same arguments, so you could use the same function for
    both.
      
BANDWIDTH THROTTLING

  urlgrabber supports throttling via two values: throttle and
  bandwidth Between the two, you can either specify and absolute
  throttle threshold or specify a theshold as a fraction of maximum
  available bandwidth.

  throttle is a number - if it's an int, it's the bytes/second
  throttle limit.  If it's a float, it is first multiplied by
  bandwidth.  If throttle == 0, throttling is disabled.  If None, the
  module-level default (which can be set with set_throttle) is used.

  bandwidth is the nominal max bandwidth in bytes/second.  If throttle
  is a float and bandwidth == 0, throttling is disabled.  If None, the
  module-level default (which can be set with set_bandwidth) is used.

  THROTTLING EXAMPLES:

  Lets say you have a 100 Mbps connection.  This is (about) 10^8 bits
  per second, or 12,500,000 Bytes per second.  You have a number of
  throttling options:

  *) set_bandwidth(12500000); set_throttle(0.5) # throttle is a float

     This will limit urlgrab to use half of your available bandwidth.

  *) set_throttle(6250000) # throttle is an int

     This will also limit urlgrab to use half of your available
     bandwidth, regardless of what bandwidth is set to.

  *) set_throttle(6250000); set_throttle(1.0) # float

     Use half your bandwidth

  *) set_throttle(6250000); set_throttle(2.0) # float

    Use up to 12,500,000 Bytes per second (your nominal max bandwidth)

  *) set_throttle(6250000); set_throttle(0) # throttle = 0

     Disable throttling - this is more efficient than a very large
     throttle setting.

  *) set_throttle(0); set_throttle(1.0) # throttle is float, bandwidth = 0

     Disable throttling - this is the default when the module is loaded.

  SUGGESTED AUTHOR IMPLEMENTATION (THROTTLING)

  While this is flexible, it's not extremely obvious to the user.  I
  suggest you implement a float throttle as a percent to make the
  distinction between absolute and relative throttling very explicit.

  Also, you may want to convert the units to something more convenient
  than bytes/second, such as kbps or kB/s, etc.

"""



import os
import sys
import urlparse
import time
import string
import urllib
import urllib2
import mimetools
import thread
import types
import stat
import pycurl
from ftplib import parse150
from StringIO import StringIO
from httplib import HTTPException
import socket
from byterange import range_tuple_normalize, range_tuple_to_header, RangeError

########################################################################
#                     MODULE INITIALIZATION
########################################################################
try:
    exec('from ' + (__name__.split('.'))[0] + ' import __version__')
except:
    __version__ = '???'

########################################################################
# functions for debugging output.  These functions are here because they
# are also part of the module initialization.
DEBUG = None
def set_logger(DBOBJ):
    """Set the DEBUG object.  This is called by _init_default_logger when
    the environment variable URLGRABBER_DEBUG is set, but can also be
    called by a calling program.  Basically, if the calling program uses
    the logging module and would like to incorporate urlgrabber logging,
    then it can do so this way.  It's probably not necessary as most
    internal logging is only for debugging purposes.

    The passed-in object should be a logging.Logger instance.  It will
    be pushed into the keepalive and byterange modules if they're
    being used.  The mirror module pulls this object in on import, so
    you will need to manually push into it.  In fact, you may find it
    tidier to simply push your logging object (or objects) into each
    of these modules independently.
    """

    global DEBUG
    DEBUG = DBOBJ

def _init_default_logger(logspec=None):
    '''Examines the environment variable URLGRABBER_DEBUG and creates
    a logging object (logging.logger) based on the contents.  It takes
    the form

      URLGRABBER_DEBUG=level,filename
      
    where "level" can be either an integer or a log level from the
    logging module (DEBUG, INFO, etc).  If the integer is zero or
    less, logging will be disabled.  Filename is the filename where
    logs will be sent.  If it is "-", then stdout will be used.  If
    the filename is empty or missing, stderr will be used.  If the
    variable cannot be processed or the logging module cannot be
    imported (python < 2.3) then logging will be disabled.  Here are
    some examples:

      URLGRABBER_DEBUG=1,debug.txt   # log everything to debug.txt
      URLGRABBER_DEBUG=WARNING,-     # log warning and higher to stdout
      URLGRABBER_DEBUG=INFO          # log info and higher to stderr
      
    This funtion is called during module initialization.  It is not
    intended to be called from outside.  The only reason it is a
    function at all is to keep the module-level namespace tidy and to
    collect the code into a nice block.'''

    try:
        if logspec is None:
            logspec = os.environ['URLGRABBER_DEBUG']
        dbinfo = logspec.split(',')
        import logging
        level = logging._levelNames.get(dbinfo[0], None)
        if level is None: level = int(dbinfo[0])
        if level < 1: raise ValueError()

        formatter = logging.Formatter('%(asctime)s %(message)s')
        if len(dbinfo) > 1: filename = dbinfo[1]
        else: filename = ''
        if filename == '': handler = logging.StreamHandler(sys.stderr)
        elif filename == '-': handler = logging.StreamHandler(sys.stdout)
        else:  handler = logging.FileHandler(filename)
        handler.setFormatter(formatter)
        DBOBJ = logging.getLogger('urlgrabber')
        DBOBJ.addHandler(handler)
        DBOBJ.setLevel(level)
    except (KeyError, ImportError, ValueError):
        DBOBJ = None
    set_logger(DBOBJ)

def _log_package_state():
    if not DEBUG: return
    DEBUG.info('urlgrabber version  = %s' % __version__)
    DEBUG.info('trans function "_"  = %s' % _)
        
_init_default_logger()
_log_package_state()


# normally this would be from i18n or something like it ...
def _(st):
    return st

########################################################################
#                 END MODULE INITIALIZATION
########################################################################



class URLGrabError(IOError):
    """
    URLGrabError error codes:

      URLGrabber error codes (0 -- 255)
        0    - everything looks good (you should never see this)
        1    - malformed url
        2    - local file doesn't exist
        3    - request for non-file local file (dir, etc)
        4    - IOError on fetch
        5    - OSError on fetch
        6    - no content length header when we expected one
        7    - HTTPException
        8    - Exceeded read limit (for urlread)
        9    - Requested byte range not satisfiable.
        10   - Byte range requested, but range support unavailable
        11   - Illegal reget mode
        12   - Socket timeout
        13   - malformed proxy url
        14   - HTTPError (includes .code and .exception attributes)
        15   - user abort
        16   - error writing to local file
        
      MirrorGroup error codes (256 -- 511)
        256  - No more mirrors left to try

      Custom (non-builtin) classes derived from MirrorGroup (512 -- 767)
        [ this range reserved for application-specific error codes ]

      Retry codes (< 0)
        -1   - retry the download, unknown reason

    Note: to test which group a code is in, you can simply do integer
    division by 256: e.errno / 256

    Negative codes are reserved for use by functions passed in to
    retrygrab with checkfunc.  The value -1 is built in as a generic
    retry code and is already included in the retrycodes list.
    Therefore, you can create a custom check function that simply
    returns -1 and the fetch will be re-tried.  For more customized
    retries, you can use other negative number and include them in
    retry-codes.  This is nice for outputting useful messages about
    what failed.

    You can use these error codes like so:
      try: urlgrab(url)
      except URLGrabError, e:
         if e.errno == 3: ...
           # or
         print e.strerror
           # or simply
         print e  #### print '[Errno %i] %s' % (e.errno, e.strerror)
    """
    def __init__(self, *args):
        IOError.__init__(self, *args)
        self.url = "No url specified"

class CallbackObject:
    """Container for returned callback data.

    This is currently a dummy class into which urlgrabber can stuff
    information for passing to callbacks.  This way, the prototype for
    all callbacks is the same, regardless of the data that will be
    passed back.  Any function that accepts a callback function as an
    argument SHOULD document what it will define in this object.

    It is possible that this class will have some greater
    functionality in the future.
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def urlgrab(url, filename=None, **kwargs):
    """grab the file at <url> and make a local copy at <filename>
    If filename is none, the basename of the url is used.
    urlgrab returns the filename of the local file, which may be different
    from the passed-in filename if the copy_local kwarg == 0.
    
    See module documentation for a description of possible kwargs.
    """
    return default_grabber.urlgrab(url, filename, **kwargs)

def urlopen(url, **kwargs):
    """open the url and return a file object
    If a progress object or throttle specifications exist, then
    a special file object will be returned that supports them.
    The file object can be treated like any other file object.
    
    See module documentation for a description of possible kwargs.
    """
    return default_grabber.urlopen(url, **kwargs)

def urlread(url, limit=None, **kwargs):
    """read the url into a string, up to 'limit' bytes
    If the limit is exceeded, an exception will be thrown.  Note that urlread
    is NOT intended to be used as a way of saying "I want the first N bytes"
    but rather 'read the whole file into memory, but don't use too much'
    
    See module documentation for a description of possible kwargs.
    """
    return default_grabber.urlread(url, limit, **kwargs)


class URLParser:
    """Process the URLs before passing them to urllib2.

    This class does several things:

      * add any prefix
      * translate a "raw" file to a proper file: url
      * handle any http or https auth that's encoded within the url
      * quote the url

    Only the "parse" method is called directly, and it calls sub-methods.

    An instance of this class is held in the options object, which
    means that it's easy to change the behavior by sub-classing and
    passing the replacement in.  It need only have a method like:

        url, parts = urlparser.parse(url, opts)
    """

    def parse(self, url, opts):
        """parse the url and return the (modified) url and its parts

        Note: a raw file WILL be quoted when it's converted to a URL.
        However, other urls (ones which come with a proper scheme) may
        or may not be quoted according to opts.quote

          opts.quote = 1     --> quote it
          opts.quote = 0     --> do not quote it
          opts.quote = None  --> guess
        """
        quote = opts.quote
        
        if opts.prefix:
            url = self.add_prefix(url, opts.prefix)
            
        parts = urlparse.urlparse(url)
        (scheme, host, path, parm, query, frag) = parts

        if not scheme or (len(scheme) == 1 and scheme in string.letters):
            # if a scheme isn't specified, we guess that it's "file:"
            if url[0] not in '/\\': url = os.path.abspath(url)
            url = 'file:' + urllib.pathname2url(url)
            parts = urlparse.urlparse(url)
            quote = 0 # pathname2url quotes, so we won't do it again
            
        if scheme in ['http', 'https']:
            parts = self.process_http(parts, url)
            
        if quote is None:
            quote = self.guess_should_quote(parts)
        if quote:
            parts = self.quote(parts)
        
        url = urlparse.urlunparse(parts)
        return url, parts

    def add_prefix(self, url, prefix):
        if prefix[-1] == '/' or url[0] == '/':
            url = prefix + url
        else:
            url = prefix + '/' + url
        return url

    def process_http(self, parts, url):
        (scheme, host, path, parm, query, frag) = parts
        # TODO: auth-parsing here, maybe? pycurl doesn't really need it
        return (scheme, host, path, parm, query, frag)

    def quote(self, parts):
        """quote the URL

        This method quotes ONLY the path part.  If you need to quote
        other parts, you should override this and pass in your derived
        class.  The other alternative is to quote other parts before
        passing into urlgrabber.
        """
        (scheme, host, path, parm, query, frag) = parts
        path = urllib.quote(path)
        return (scheme, host, path, parm, query, frag)

    hexvals = '0123456789ABCDEF'
    def guess_should_quote(self, parts):
        """
        Guess whether we should quote a path.  This amounts to
        guessing whether it's already quoted.

        find ' '   ->  1
        find '%'   ->  1
        find '%XX' ->  0
        else       ->  1
        """
        (scheme, host, path, parm, query, frag) = parts
        if ' ' in path:
            return 1
        ind = string.find(path, '%')
        if ind > -1:
            while ind > -1:
                if len(path) < ind+3:
                    return 1
                code = path[ind+1:ind+3].upper()
                if     code[0] not in self.hexvals or \
                       code[1] not in self.hexvals:
                    return 1
                ind = string.find(path, '%', ind+1)
            return 0
        return 1
    
class URLGrabberOptions:
    """Class to ease kwargs handling."""

    def __init__(self, delegate=None, **kwargs):
        """Initialize URLGrabberOptions object.
        Set default values for all options and then update options specified
        in kwargs.
        """
        self.delegate = delegate
        if delegate is None:
            self._set_defaults()
        self._set_attributes(**kwargs)
    
    def __getattr__(self, name):
        if self.delegate and hasattr(self.delegate, name):
            return getattr(self.delegate, name)
        raise AttributeError, name
    
    def raw_throttle(self):
        """Calculate raw throttle value from throttle and bandwidth 
        values.
        """
        if self.throttle <= 0:  
            return 0
        elif type(self.throttle) == type(0): 
            return float(self.throttle)
        else: # throttle is a float
            return self.bandwidth * self.throttle
        
    def derive(self, **kwargs):
        """Create a derived URLGrabberOptions instance.
        This method creates a new instance and overrides the
        options specified in kwargs.
        """
        return URLGrabberOptions(delegate=self, **kwargs)
        
    def _set_attributes(self, **kwargs):
        """Update object attributes with those provided in kwargs."""
        self.__dict__.update(kwargs)
        if kwargs.has_key('range'):
            # normalize the supplied range value
            self.range = range_tuple_normalize(self.range)
        if not self.reget in [None, 'simple', 'check_timestamp']:
            raise URLGrabError(11, _('Illegal reget mode: %s') \
                               % (self.reget, ))

    def _set_defaults(self):
        """Set all options to their default values. 
        When adding new options, make sure a default is
        provided here.
        """
        self.progress_obj = None
        self.throttle = 1.0
        self.bandwidth = 0
        self.retry = None
        self.retrycodes = [-1,2,4,5,6,7]
        self.checkfunc = None
        self.copy_local = 0
        self.close_connection = 0
        self.range = None
        self.user_agent = 'urlgrabber/%s' % __version__
        self.keepalive = 1
        self.proxies = None
        self.reget = None
        self.failure_callback = None
        self.interrupt_callback = None
        self.prefix = None
        self.opener = None
        self.cache_openers = True
        self.timeout = None
        self.text = None
        self.http_headers = None
        self.ftp_headers = None
        self.data = None
        self.urlparser = URLParser()
        self.quote = None
        self.ssl_ca_cert = None # sets SSL_CAINFO - path to certdb
        self.ssl_context = None # no-op in pycurl
        self.ssl_verify_peer = True # check peer's cert for authenticityb
        self.ssl_verify_host = True # make sure who they are and who the cert is for matches
        self.ssl_key = None # client key
        self.ssl_key_type = 'PEM' #(or DER)
        self.ssl_cert = None # client cert
        self.ssl_cert_type = 'PEM' # (or DER)
        self.ssl_key_pass = None # password to access the key
        self.size = None # if we know how big the thing we're getting is going
                         # to be. this is ultimately a MAXIMUM size for the file
        self.max_header_size = 2097152 #2mb seems reasonable for maximum header size
        
    def __repr__(self):
        return self.format()
        
    def format(self, indent='  '):
        keys = self.__dict__.keys()
        if self.delegate is not None:
            keys.remove('delegate')
        keys.sort()
        s = '{\n'
        for k in keys:
            s = s + indent + '%-15s: %s,\n' % \
                (repr(k), repr(self.__dict__[k]))
        if self.delegate:
            df = self.delegate.format(indent + '  ')
            s = s + indent + '%-15s: %s\n' % ("'delegate'", df)
        s = s + indent + '}'
        return s

class URLGrabber:
    """Provides easy opening of URLs with a variety of options.
    
    All options are specified as kwargs. Options may be specified when
    the class is created and may be overridden on a per request basis.
    
    New objects inherit default values from default_grabber.
    """
    
    def __init__(self, **kwargs):
        self.opts = URLGrabberOptions(**kwargs)
    
    def _retry(self, opts, func, *args):
        tries = 0
        while 1:
            # there are only two ways out of this loop.  The second has
            # several "sub-ways"
            #   1) via the return in the "try" block
            #   2) by some exception being raised
            #      a) an excepton is raised that we don't "except"
            #      b) a callback raises ANY exception
            #      c) we're not retry-ing or have run out of retries
            #      d) the URLGrabError code is not in retrycodes
            # beware of infinite loops :)
            tries = tries + 1
            exception = None
            retrycode = None
            callback  = None
            if DEBUG: DEBUG.info('attempt %i/%s: %s',
                                 tries, opts.retry, args[0])
            try:
                r = apply(func, (opts,) + args, {})
                if DEBUG: DEBUG.info('success')
                return r
            except URLGrabError, e:
                exception = e
                callback = opts.failure_callback
                retrycode = e.errno
            except KeyboardInterrupt, e:
                exception = e
                callback = opts.interrupt_callback

            if DEBUG: DEBUG.info('exception: %s', exception)
            if callback:
                if DEBUG: DEBUG.info('calling callback: %s', callback)
                cb_func, cb_args, cb_kwargs = self._make_callback(callback)
                obj = CallbackObject(exception=exception, url=args[0],
                                     tries=tries, retry=opts.retry)
                cb_func(obj, *cb_args, **cb_kwargs)

            if (opts.retry is None) or (tries == opts.retry):
                if DEBUG: DEBUG.info('retries exceeded, re-raising')
                raise

            if (retrycode is not None) and (retrycode not in opts.retrycodes):
                if DEBUG: DEBUG.info('retrycode (%i) not in list %s, re-raising',
                                     retrycode, opts.retrycodes)
                raise
    
    def urlopen(self, url, **kwargs):
        """open the url and return a file object
        If a progress object or throttle value specified when this 
        object was created, then  a special file object will be 
        returned that supports them. The file object can be treated 
        like any other file object.
        """
        opts = self.opts.derive(**kwargs)
        if DEBUG: DEBUG.debug('combined options: %s' % repr(opts))
        (url,parts) = opts.urlparser.parse(url, opts) 
        def retryfunc(opts, url):
            return PyCurlFileObject(url, filename=None, opts=opts)
        return self._retry(opts, retryfunc, url)
    
    def urlgrab(self, url, filename=None, **kwargs):
        """grab the file at <url> and make a local copy at <filename>
        If filename is none, the basename of the url is used.
        urlgrab returns the filename of the local file, which may be 
        different from the passed-in filename if copy_local == 0.
        """
        opts = self.opts.derive(**kwargs)
        if DEBUG: DEBUG.debug('combined options: %s' % repr(opts))
        (url,parts) = opts.urlparser.parse(url, opts) 
        (scheme, host, path, parm, query, frag) = parts
        if filename is None:
            filename = os.path.basename( urllib.unquote(path) )
        if scheme == 'file' and not opts.copy_local:
            # just return the name of the local file - don't make a 
            # copy currently
            path = urllib.url2pathname(path)
            if host:
                path = os.path.normpath('//' + host + path)
            if not os.path.exists(path):
                err = URLGrabError(2, 
                      _('Local file does not exist: %s') % (path, ))
                err.url = url
                raise err
            elif not os.path.isfile(path):
                err = URLGrabError(3, 
                                 _('Not a normal file: %s') % (path, ))
                err.url = url
                raise err

            elif not opts.range:
                if not opts.checkfunc is None:
                    cb_func, cb_args, cb_kwargs = \
                       self._make_callback(opts.checkfunc)
                    obj = CallbackObject()
                    obj.filename = path
                    obj.url = url
                    apply(cb_func, (obj, )+cb_args, cb_kwargs)        
                return path
        
        def retryfunc(opts, url, filename):
            fo = PyCurlFileObject(url, filename, opts)
            try:
                fo._do_grab()
                if not opts.checkfunc is None:
                    cb_func, cb_args, cb_kwargs = \
                             self._make_callback(opts.checkfunc)
                    obj = CallbackObject()
                    obj.filename = filename
                    obj.url = url
                    apply(cb_func, (obj, )+cb_args, cb_kwargs)
            finally:
                fo.close()
            return filename
        
        return self._retry(opts, retryfunc, url, filename)
    
    def urlread(self, url, limit=None, **kwargs):
        """read the url into a string, up to 'limit' bytes
        If the limit is exceeded, an exception will be thrown.  Note
        that urlread is NOT intended to be used as a way of saying 
        "I want the first N bytes" but rather 'read the whole file 
        into memory, but don't use too much'
        """
        opts = self.opts.derive(**kwargs)
        if DEBUG: DEBUG.debug('combined options: %s' % repr(opts))
        (url,parts) = opts.urlparser.parse(url, opts) 
        if limit is not None:
            limit = limit + 1
            
        def retryfunc(opts, url, limit):
            fo = PyCurlFileObject(url, filename=None, opts=opts)
            s = ''
            try:
                # this is an unfortunate thing.  Some file-like objects
                # have a default "limit" of None, while the built-in (real)
                # file objects have -1.  They each break the other, so for
                # now, we just force the default if necessary.
                if limit is None: s = fo.read()
                else: s = fo.read(limit)

                if not opts.checkfunc is None:
                    cb_func, cb_args, cb_kwargs = \
                             self._make_callback(opts.checkfunc)
                    obj = CallbackObject()
                    obj.data = s
                    obj.url = url
                    apply(cb_func, (obj, )+cb_args, cb_kwargs)
            finally:
                fo.close()
            return s
            
        s = self._retry(opts, retryfunc, url, limit)
        if limit and len(s) > limit:
            err = URLGrabError(8, 
                               _('Exceeded limit (%i): %s') % (limit, url))
            err.url = url
            raise err

        return s
        
    def _make_callback(self, callback_obj):
        if callable(callback_obj):
            return callback_obj, (), {}
        else:
            return callback_obj

# create the default URLGrabber used by urlXXX functions.
# NOTE: actual defaults are set in URLGrabberOptions
default_grabber = URLGrabber()


class PyCurlFileObject():
    def __init__(self, url, filename, opts):
        self.fo = None
        self._hdr_dump = ''
        self._parsed_hdr = None
        self.url = url
        self.scheme = urlparse.urlsplit(self.url)[0]
        self.filename = filename
        self.append = False
        self.reget_time = None
        self.opts = opts
        if self.opts.reget == 'check_timestamp':
            raise NotImplementedError, "check_timestamp regets are not implemented in this ver of urlgrabber. Please report this."
        self._complete = False
        self._rbuf = ''
        self._rbufsize = 1024*8
        self._ttime = time.time()
        self._tsize = 0
        self._amount_read = 0
        self._reget_length = 0
        self._prog_running = False
        self._error = (None, None)
        self.size = None
        self._do_open()
        
        
    def __getattr__(self, name):
        """This effectively allows us to wrap at the instance level.
        Any attribute not found in _this_ object will be searched for
        in self.fo.  This includes methods."""

        if hasattr(self.fo, name):
            return getattr(self.fo, name)
        raise AttributeError, name

    def _retrieve(self, buf):
        try:
            if not self._prog_running:
                if self.opts.progress_obj:
                    size  = self.size + self._reget_length
                    self.opts.progress_obj.start(self._prog_reportname, 
                                                 urllib.unquote(self.url), 
                                                 self._prog_basename, 
                                                 size=size,
                                                 text=self.opts.text)
                    self._prog_running = True
                    self.opts.progress_obj.update(self._amount_read)

            self._amount_read += len(buf)
            self.fo.write(buf)
            return len(buf)
        except KeyboardInterrupt:
            return -1
            
    def _hdr_retrieve(self, buf):
        if self._over_max_size(cur=len(self._hdr_dump), 
                               max_size=self.opts.max_header_size):
            return -1            
        try:
            self._hdr_dump += buf
            # we have to get the size before we do the progress obj start
            # but we can't do that w/o making it do 2 connects, which sucks
            # so we cheat and stuff it in here in the hdr_retrieve
            if self.scheme in ['http','https'] and buf.lower().find('content-length') != -1:
                length = buf.split(':')[1]
                self.size = int(length)
            elif self.scheme in ['ftp']:
                s = None
                if buf.startswith('213 '):
                    s = buf[3:].strip()
                elif buf.startswith('150 '):
                    s = parse150(buf)
                if s:
                    self.size = int(s)
            
            return len(buf)
        except KeyboardInterrupt:
            return pycurl.READFUNC_ABORT

    def _return_hdr_obj(self):
        if self._parsed_hdr:
            return self._parsed_hdr
        statusend = self._hdr_dump.find('\n')
        hdrfp = StringIO()
        hdrfp.write(self._hdr_dump[statusend:])
        self._parsed_hdr =  mimetools.Message(hdrfp)
        return self._parsed_hdr
    
    hdr = property(_return_hdr_obj)
    http_code = property(fget=
                 lambda self: self.curl_obj.getinfo(pycurl.RESPONSE_CODE))

    def _set_opts(self, opts={}):
        # XXX
        if not opts:
            opts = self.opts


        # defaults we're always going to set
        self.curl_obj.setopt(pycurl.NOPROGRESS, False)
        self.curl_obj.setopt(pycurl.NOSIGNAL, True)
        self.curl_obj.setopt(pycurl.WRITEFUNCTION, self._retrieve)
        self.curl_obj.setopt(pycurl.HEADERFUNCTION, self._hdr_retrieve)
        self.curl_obj.setopt(pycurl.PROGRESSFUNCTION, self._progress_update)
        self.curl_obj.setopt(pycurl.FAILONERROR, True)
        self.curl_obj.setopt(pycurl.OPT_FILETIME, True)
        
        if DEBUG:
            self.curl_obj.setopt(pycurl.VERBOSE, True)
        if opts.user_agent:
            self.curl_obj.setopt(pycurl.USERAGENT, opts.user_agent)
        
        # maybe to be options later
        self.curl_obj.setopt(pycurl.FOLLOWLOCATION, True)
        self.curl_obj.setopt(pycurl.MAXREDIRS, 5)
        
        # timeouts
        timeout = 300
        if opts.timeout:
            timeout = int(opts.timeout)
            self.curl_obj.setopt(pycurl.CONNECTTIMEOUT, timeout)

        # ssl options
        if self.scheme == 'https':
            if opts.ssl_ca_cert: # this may do ZERO with nss  according to curl docs
                self.curl_obj.setopt(pycurl.CAPATH, opts.ssl_ca_cert)
                self.curl_obj.setopt(pycurl.CAINFO, opts.ssl_ca_cert)
            self.curl_obj.setopt(pycurl.SSL_VERIFYPEER, opts.ssl_verify_peer)
            self.curl_obj.setopt(pycurl.SSL_VERIFYHOST, opts.ssl_verify_host)
            if opts.ssl_key:
                self.curl_obj.setopt(pycurl.SSLKEY, opts.ssl_key)
            if opts.ssl_key_type:
                self.curl_obj.setopt(pycurl.SSLKEYTYPE, opts.ssl_key_type)
            if opts.ssl_cert:
                self.curl_obj.setopt(pycurl.SSLCERT, opts.ssl_cert)
            if opts.ssl_cert_type:                
                self.curl_obj.setopt(pycurl.SSLCERTTYPE, opts.ssl_cert_type)
            if opts.ssl_key_pass:
                self.curl_obj.setopt(pycurl.SSLKEYPASSWD, opts.ssl_key_pass)

        #headers:
        if opts.http_headers and self.scheme in ('http', 'https'):
            headers = []
            for (tag, content) in opts.http_headers:
                headers.append('%s:%s' % (tag, content))
            self.curl_obj.setopt(pycurl.HTTPHEADER, headers)

        # ranges:
        if opts.range or opts.reget:
            range_str = self._build_range()
            if range_str:
                self.curl_obj.setopt(pycurl.RANGE, range_str)
            
        # throttle/bandwidth
        if hasattr(opts, 'raw_throttle') and opts.raw_throttle():
            self.curl_obj.setopt(pycurl.MAX_RECV_SPEED_LARGE, int(opts.raw_throttle()))
            
        # proxy settings
        if opts.proxies:
            for (scheme, proxy) in opts.proxies.items():
                if self.scheme in ('ftp'): # only set the ftp proxy for ftp items
                    if scheme not in ('ftp'):
                        continue
                    else:
                        if proxy == '_none_': proxy = ""
                        self.curl_obj.setopt(pycurl.PROXY, proxy)
                elif self.scheme in ('http', 'https'):
                    if scheme not in ('http', 'https'):
                        continue
                    else:
                        if proxy == '_none_': proxy = ""
                        self.curl_obj.setopt(pycurl.PROXY, proxy)
            
        # FIXME username/password/auth settings

        #posts - simple - expects the fields as they are
        if opts.data:
            self.curl_obj.setopt(pycurl.POST, True)
            self.curl_obj.setopt(pycurl.POSTFIELDS, self._to_utf8(opts.data))
            
        # our url
        self.curl_obj.setopt(pycurl.URL, self.url)
        
    
    def _do_perform(self):
        if self._complete:
            return
        
        try:
            self.curl_obj.perform()
        except pycurl.error, e:
            # XXX - break some of these out a bit more clearly
            # to other URLGrabErrors from 
            # http://curl.haxx.se/libcurl/c/libcurl-errors.html
            # this covers e.args[0] == 22 pretty well - which will be common
            
            code = self.http_code
            errcode = e.args[0]
            if self._error[0]:
                errcode = self._error[0]
                
            if errcode == 23 and code >= 200 and code < 299:
                err = URLGrabError(15, _('User (or something) called abort %s: %s') % (self.url, e))
                err.url = self.url
                
                # this is probably wrong but ultimately this is what happens
                # we have a legit http code and a pycurl 'writer failed' code
                # which almost always means something aborted it from outside
                # since we cannot know what it is -I'm banking on it being
                # a ctrl-c. XXXX - if there's a way of going back two raises to 
                # figure out what aborted the pycurl process FIXME
                raise KeyboardInterrupt
            
            elif errcode == 28:
                err = URLGrabError(12, _('Timeout on %s: %s') % (self.url, e))
                err.url = self.url
                raise err
            elif errcode == 35:
                msg = _("problem making ssl connection")
                err = URLGrabError(14, msg)
                err.url = self.url
                raise err
            elif errcode == 37:
                msg = _("Could not open/read %s") % (self.url)
                err = URLGrabError(14, msg)
                err.url = self.url
                raise err
                
            elif errcode == 42:
                err = URLGrabError(15, _('User (or something) called abort %s: %s') % (self.url, e))
                err.url = self.url
                # this is probably wrong but ultimately this is what happens
                # we have a legit http code and a pycurl 'writer failed' code
                # which almost always means something aborted it from outside
                # since we cannot know what it is -I'm banking on it being
                # a ctrl-c. XXXX - if there's a way of going back two raises to 
                # figure out what aborted the pycurl process FIXME
                raise KeyboardInterrupt
                
            elif errcode == 58:
                msg = _("problem with the local client certificate")
                err = URLGrabError(14, msg)
                err.url = self.url
                raise err

            elif errcode == 60:
                msg = _("client cert cannot be verified or client cert incorrect")
                err = URLGrabError(14, msg)
                err.url = self.url
                raise err
            
            elif errcode == 63:
                if self._error[1]:
                    msg = self._error[1]
                else:
                    msg = _("Max download size exceeded on %s") % (self.url)
                err = URLGrabError(14, msg)
                err.url = self.url
                raise err
                    
            elif str(e.args[1]) == '' and self.http_code != 0: # fake it until you make it
                msg = 'HTTP Error %s : %s ' % (self.http_code, self.url)
            else:
                msg = 'PYCURL ERROR %s - "%s"' % (errcode, str(e.args[1]))
                code = errcode
            err = URLGrabError(14, msg)
            err.code = code
            err.exception = e
            raise err

    def _do_open(self):
        self.curl_obj = _curl_cache
        self.curl_obj.reset() # reset all old settings away, just in case
        # setup any ranges
        self._set_opts()
        self._do_grab()
        return self.fo

    def _add_headers(self):
        pass
        
    def _build_range(self):
        reget_length = 0
        rt = None
        if self.opts.reget and type(self.filename) in types.StringTypes:
            # we have reget turned on and we're dumping to a file
            try:
                s = os.stat(self.filename)
            except OSError:
                pass
            else:
                self.reget_time = s[stat.ST_MTIME]
                reget_length = s[stat.ST_SIZE]

                # Set initial length when regetting
                self._amount_read = reget_length    
                self._reget_length = reget_length # set where we started from, too

                rt = reget_length, ''
                self.append = 1
                
        if self.opts.range:
            rt = self.opts.range
            if rt[0]: rt = (rt[0] + reget_length, rt[1])

        if rt:
            header = range_tuple_to_header(rt)
            if header:
                return header.split('=')[1]



    def _make_request(self, req, opener):
        #XXXX
        # This doesn't do anything really, but we could use this
        # instead of do_open() to catch a lot of crap errors as 
        # mstenner did before here
        return (self.fo, self.hdr)
        
        try:
            if self.opts.timeout:
                old_to = socket.getdefaulttimeout()
                socket.setdefaulttimeout(self.opts.timeout)
                try:
                    fo = opener.open(req)
                finally:
                    socket.setdefaulttimeout(old_to)
            else:
                fo = opener.open(req)
            hdr = fo.info()
        except ValueError, e:
            err = URLGrabError(1, _('Bad URL: %s : %s') % (self.url, e, ))
            err.url = self.url
            raise err

        except RangeError, e:
            err = URLGrabError(9, _('%s on %s') % (e, self.url))
            err.url = self.url
            raise err
        except urllib2.HTTPError, e:
            new_e = URLGrabError(14, _('%s on %s') % (e, self.url))
            new_e.code = e.code
            new_e.exception = e
            new_e.url = self.url
            raise new_e
        except IOError, e:
            if hasattr(e, 'reason') and isinstance(e.reason, socket.timeout):
                err = URLGrabError(12, _('Timeout on %s: %s') % (self.url, e))
                err.url = self.url
                raise err
            else:
                err = URLGrabError(4, _('IOError on %s: %s') % (self.url, e))
                err.url = self.url
                raise err

        except OSError, e:
            err = URLGrabError(5, _('%s on %s') % (e, self.url))
            err.url = self.url
            raise err

        except HTTPException, e:
            err = URLGrabError(7, _('HTTP Exception (%s) on %s: %s') % \
                            (e.__class__.__name__, self.url, e))
            err.url = self.url
            raise err

        else:
            return (fo, hdr)
        
    def _do_grab(self):
        """dump the file to a filename or StringIO buffer"""

        if self._complete:
            return
        _was_filename = False
        if type(self.filename) in types.StringTypes and self.filename:
            _was_filename = True
            self._prog_reportname = str(self.filename)
            self._prog_basename = os.path.basename(self.filename)
            
            if self.append: mode = 'ab'
            else: mode = 'wb'

            if DEBUG: DEBUG.info('opening local file "%s" with mode %s' % \
                                 (self.filename, mode))
            try:
                self.fo = open(self.filename, mode)
            except IOError, e:
                err = URLGrabError(16, _(\
                  'error opening local file from %s, IOError: %s') % (self.url, e))
                err.url = self.url
                raise err

        else:
            self._prog_reportname = 'MEMORY'
            self._prog_basename = 'MEMORY'

            
            self.fo = StringIO()
            # if this is to be a tempfile instead....
            # it just makes crap in the tempdir
            #fh, self._temp_name = mkstemp()
            #self.fo = open(self._temp_name, 'wb')

            
        self._do_perform()
        


        if _was_filename:
            # close it up
            self.fo.flush()
            self.fo.close()
            # set the time
            mod_time = self.curl_obj.getinfo(pycurl.INFO_FILETIME)
            if mod_time != -1:
                os.utime(self.filename, (mod_time, mod_time))
            # re open it
            self.fo = open(self.filename, 'r')
        else:
            #self.fo = open(self._temp_name, 'r')
            self.fo.seek(0)

        self._complete = True
    
    def _fill_buffer(self, amt=None):
        """fill the buffer to contain at least 'amt' bytes by reading
        from the underlying file object.  If amt is None, then it will
        read until it gets nothing more.  It updates the progress meter
        and throttles after every self._rbufsize bytes."""
        # the _rbuf test is only in this first 'if' for speed.  It's not
        # logically necessary
        if self._rbuf and not amt is None:
            L = len(self._rbuf)
            if amt > L:
                amt = amt - L
            else:
                return

        # if we've made it here, then we don't have enough in the buffer
        # and we need to read more.
        
        if not self._complete: self._do_grab() #XXX cheater - change on ranges
        
        buf = [self._rbuf]
        bufsize = len(self._rbuf)
        while amt is None or amt:
            # first, delay if necessary for throttling reasons
            if self.opts.raw_throttle():
                diff = self._tsize/self.opts.raw_throttle() - \
                       (time.time() - self._ttime)
                if diff > 0: time.sleep(diff)
                self._ttime = time.time()
                
            # now read some data, up to self._rbufsize
            if amt is None: readamount = self._rbufsize
            else:           readamount = min(amt, self._rbufsize)
            try:
                new = self.fo.read(readamount)
            except socket.error, e:
                err = URLGrabError(4, _('Socket Error on %s: %s') % (self.url, e))
                err.url = self.url
                raise err

            except socket.timeout, e:
                raise URLGrabError(12, _('Timeout on %s: %s') % (self.url, e))
                err.url = self.url
                raise err

            except IOError, e:
                raise URLGrabError(4, _('IOError on %s: %s') %(self.url, e))
                err.url = self.url
                raise err

            newsize = len(new)
            if not newsize: break # no more to read

            if amt: amt = amt - newsize
            buf.append(new)
            bufsize = bufsize + newsize
            self._tsize = newsize
            self._amount_read = self._amount_read + newsize
            #if self.opts.progress_obj:
            #    self.opts.progress_obj.update(self._amount_read)

        self._rbuf = string.join(buf, '')
        return

    def _progress_update(self, download_total, downloaded, upload_total, uploaded):
        if self._over_max_size(cur=self._amount_read-self._reget_length):
            return -1

        try:
            if self._prog_running:
                downloaded += self._reget_length
                self.opts.progress_obj.update(downloaded)
        except KeyboardInterrupt:
            return -1
    
    def _over_max_size(self, cur, max_size=None):

        if not max_size:
            max_size = self.size
        if self.opts.size: # if we set an opts size use that, no matter what
            max_size = self.opts.size
        if not max_size: return False # if we have None for all of the Max then this is dumb
        if cur > max_size + max_size*.10:

            msg = _("Downloaded more than max size for %s: %s > %s") \
                        % (self.url, cur, max_size)
            self._error = (pycurl.E_FILESIZE_EXCEEDED, msg)
            return True
        return False
        
    def _to_utf8(self, obj, errors='replace'):
        '''convert 'unicode' to an encoded utf-8 byte string '''
        # stolen from yum.i18n
        if isinstance(obj, unicode):
            obj = obj.encode('utf-8', errors)
        return obj
        
    def read(self, amt=None):
        self._fill_buffer(amt)
        if amt is None:
            s, self._rbuf = self._rbuf, ''
        else:
            s, self._rbuf = self._rbuf[:amt], self._rbuf[amt:]
        return s

    def readline(self, limit=-1):
        if not self._complete: self._do_grab()
        return self.fo.readline()
        
        i = string.find(self._rbuf, '\n')
        while i < 0 and not (0 < limit <= len(self._rbuf)):
            L = len(self._rbuf)
            self._fill_buffer(L + self._rbufsize)
            if not len(self._rbuf) > L: break
            i = string.find(self._rbuf, '\n', L)

        if i < 0: i = len(self._rbuf)
        else: i = i+1
        if 0 <= limit < len(self._rbuf): i = limit

        s, self._rbuf = self._rbuf[:i], self._rbuf[i:]
        return s

    def close(self):
        if self._prog_running:
            self.opts.progress_obj.end(self._amount_read)
        self.fo.close()
        

_curl_cache = pycurl.Curl() # make one and reuse it over and over and over


#####################################################################
# DEPRECATED FUNCTIONS
def set_throttle(new_throttle):
    """Deprecated. Use: default_grabber.throttle = new_throttle"""
    default_grabber.throttle = new_throttle

def set_bandwidth(new_bandwidth):
    """Deprecated. Use: default_grabber.bandwidth = new_bandwidth"""
    default_grabber.bandwidth = new_bandwidth

def set_progress_obj(new_progress_obj):
    """Deprecated. Use: default_grabber.progress_obj = new_progress_obj"""
    default_grabber.progress_obj = new_progress_obj

def set_user_agent(new_user_agent):
    """Deprecated. Use: default_grabber.user_agent = new_user_agent"""
    default_grabber.user_agent = new_user_agent
    
def retrygrab(url, filename=None, copy_local=0, close_connection=0,
              progress_obj=None, throttle=None, bandwidth=None,
              numtries=3, retrycodes=[-1,2,4,5,6,7], checkfunc=None):
    """Deprecated. Use: urlgrab() with the retry arg instead"""
    kwargs = {'copy_local' :  copy_local, 
              'close_connection' : close_connection,
              'progress_obj' : progress_obj, 
              'throttle' : throttle, 
              'bandwidth' : bandwidth,
              'retry' : numtries,
              'retrycodes' : retrycodes,
              'checkfunc' : checkfunc 
              }
    return urlgrab(url, filename, **kwargs)

        
#####################################################################
#  TESTING
def _main_test():
    try: url, filename = sys.argv[1:3]
    except ValueError:
        print 'usage:', sys.argv[0], \
              '<url> <filename> [copy_local=0|1] [close_connection=0|1]'
        sys.exit()

    kwargs = {}
    for a in sys.argv[3:]:
        k, v = string.split(a, '=', 1)
        kwargs[k] = int(v)

    set_throttle(1.0)
    set_bandwidth(32 * 1024)
    print "throttle: %s,  throttle bandwidth: %s B/s" % (default_grabber.throttle, 
                                                        default_grabber.bandwidth)

    try: from progress import text_progress_meter
    except ImportError, e: pass
    else: kwargs['progress_obj'] = text_progress_meter()

    try: name = apply(urlgrab, (url, filename), kwargs)
    except URLGrabError, e: print e
    else: print 'LOCAL FILE:', name


def _retry_test():
    try: url, filename = sys.argv[1:3]
    except ValueError:
        print 'usage:', sys.argv[0], \
              '<url> <filename> [copy_local=0|1] [close_connection=0|1]'
        sys.exit()

    kwargs = {}
    for a in sys.argv[3:]:
        k, v = string.split(a, '=', 1)
        kwargs[k] = int(v)

    try: from progress import text_progress_meter
    except ImportError, e: pass
    else: kwargs['progress_obj'] = text_progress_meter()

    def cfunc(filename, hello, there='foo'):
        print hello, there
        import random
        rnum = random.random()
        if rnum < .5:
            print 'forcing retry'
            raise URLGrabError(-1, 'forcing retry')
        if rnum < .75:
            print 'forcing failure'
            raise URLGrabError(-2, 'forcing immediate failure')
        print 'success'
        return
        
    kwargs['checkfunc'] = (cfunc, ('hello',), {'there':'there'})
    try: name = apply(retrygrab, (url, filename), kwargs)
    except URLGrabError, e: print e
    else: print 'LOCAL FILE:', name

def _file_object_test(filename=None):
    import cStringIO
    if filename is None:
        filename = __file__
    print 'using file "%s" for comparisons' % filename
    fo = open(filename)
    s_input = fo.read()
    fo.close()

    for testfunc in [_test_file_object_smallread,
                     _test_file_object_readall,
                     _test_file_object_readline,
                     _test_file_object_readlines]:
        fo_input = cStringIO.StringIO(s_input)
        fo_output = cStringIO.StringIO()
        wrapper = PyCurlFileObject(fo_input, None, 0)
        print 'testing %-30s ' % testfunc.__name__,
        testfunc(wrapper, fo_output)
        s_output = fo_output.getvalue()
        if s_output == s_input: print 'passed'
        else: print 'FAILED'
            
def _test_file_object_smallread(wrapper, fo_output):
    while 1:
        s = wrapper.read(23)
        fo_output.write(s)
        if not s: return

def _test_file_object_readall(wrapper, fo_output):
    s = wrapper.read()
    fo_output.write(s)

def _test_file_object_readline(wrapper, fo_output):
    while 1:
        s = wrapper.readline()
        fo_output.write(s)
        if not s: return

def _test_file_object_readlines(wrapper, fo_output):
    li = wrapper.readlines()
    fo_output.write(string.join(li, ''))

if __name__ == '__main__':
    _main_test()
    _retry_test()
    _file_object_test('test')
