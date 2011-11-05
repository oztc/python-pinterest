import urllib, urllib2

def ensure_access_token(f):
    def g(self, *args, **kwargs):
        if not self.access_token:
            raise PinterestException("You need an access token to make that call")
        f(self, *args, **kwargs)
    return g

class PinterestAPI(object):
    prefix_path = "https://api.pinterest.com/v2/"
    authorize_url = "https://api.pinterest.com/oauth/authorize"
    access_token_url = "https://api.pinterest.com/oauth/access_token"

    def __init__(self, access_token=None):
        self.access_token = access_token

    @ensure_access_token
    def _get_request(self, path, params={}):
        params["access_token"] = self.access_token
        url = "%s%s?%s" %(self.prefix_path, path, urllib.urlencode(params))
        try:
            return urllib2.urlopen(url).read()
        except urllib2.HTTPError, err:
            raise PinterestException(err.read())

    def get_homefeed(self, page=1, limit=20):
        return self._get_request("home", {"page": page, "limit": limit})

    def get_pin(self, pin_id):
        return self._get_request("pin/%d" %(pin_id))


class PinterestException(Exception):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

