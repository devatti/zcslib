# zcslib
ZCS Azzurro API client  
A simple python implementation of rest api client to query ZCS Azzurro inverters

#### You need
DEVICE SERIAL: take from the label of your inverter  
CLIENT CODE and AUTH_KEY: ask opening a ticket to https://www.zcsazzurro.com/ portal

### Usage example
```
from datetime import datetime
from zcslib import ZCSClient

zcs_client = ZCSClient('https://third.zcsazzurroportal.com:19003/',
                       thingkey='<DEVICE SERIAL>',
                       client_code='<CLIENT CODE>',
                       auth_code='<AUTH_KEY>')
data = zcs_client.get_historic_data(start_dt=datetime(year=2022, month=9, day=1),
                                    end_dt=datetime(year=2022, month=9, day=2))
print(data)

data = zcs_client.get_realtime_data()
print(data)
```