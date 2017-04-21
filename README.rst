Drift API
=========

This package wraps the Drift API. It only wraps the 'track' and 
'identify' endpoints offered by the HTTP API.

https://www.drift.com/

Installation
------------

Install with pip::

$ pip install drift-api

Usage
-----

    from drift_api import Drift

    company_data = {
        'companyId': company_id,
        'attributes': {'revenue': 'bajillions'},
    }

    user_data = {
        'userId': user_id,
        'attributes': {'hair_color': 'red'},
    }

    drift = Drift(DRIFT_ORG_ID)
    drift.identify(company_data)
    drift.identify(user_data)


The package also exposes a `drift.track` method and `multi` methods for both
`track` and `identify`.


PyPI
----

https://pypi.python.org/pypi/drift-api

Source
------

https://github.com/15five/drift-api


License
-------

This library is released under the terms of the **MIT license**.
Full details in ``LICENSE.txt`` file.

