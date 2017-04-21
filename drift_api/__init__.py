"""
This library abstracts communication with and provides a pythonic interface to the Drift API. 

http://help.drift.com/developer-docs/http-api
"""
import requests

__version__ = '0.1.0'

__all__ = ['Drift']


def chunks(l, n):
    """
    Yield successive n-sized chunks from l.

    Pulled from: http://stackoverflow.com/questions/312443
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]


class Identify(object):
    def __init__(self, drift_obj):
        self.drift_obj = drift_obj

    def __call__(self, obj):
        path = '/identify'
        self.validate_obj(obj)
        self.drift_obj.post(path, obj)

    def multi(self, objs):
        path = '/identify/multi'
        for obj in objs:
            self.validate_obj(obj)
        for objs_slice in chunks(objs, 600):
            self.drift_obj.post(path, objs_slice)

    @staticmethod
    def validate_obj(obj):
        if 'companyId' not in obj and 'userId' not in obj:
            raise ValueError('Unable to identify object with Drift API. '
                             'No company or user ID present.')


class Track(object):
    def __init__(self, drift_obj):
        self.drift_obj = drift_obj

    def __call__(self, event):
        path = '/track'
        self.validate_event(event)
        self.drift_obj.post(path, event)

    def multi(self, events):
        path = '/track/multi'
        for event in events:
            self.validate_event(event)
        for events_slice in chunks(events, 600):
            self.drift_obj.post(path, events_slice)

    @staticmethod
    def validate_event(event):
        if 'companyId' not in event and 'userId' not in event:
            raise ValueError('Unable to track event with Drift API. '
                             'No company or user ID present.')

        if 'event' not in event:
            raise ValueError('Unable to track event with Drift API. '
                             'No event name present.')


class Drift(object):
    API_BASE_URL = 'https://event.api.drift.com'

    def __init__(self, org_id):
        self.org_id = org_id

    @property
    def identify(self):
        return Identify(self)

    @property
    def track(self):
        return Track(self)

    def post(self, url, data):
        url = self.API_BASE_URL + url

        data['orgId'] = self.org_id

        resp = requests.post(url, json=data)

        if resp.status_code != 200:
            raise ValueError(
                'Unable to send data to Drift API. '
                'Received Status Code {}'.format(resp.status_code)
            )
