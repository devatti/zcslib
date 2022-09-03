import requests
from datetime import datetime, timezone


class ZCSClient:
    def __init__(self, zcs_url, thingkey, client_code, auth_code):
        self.__zcs_url = zcs_url
        self.__thingkey = thingkey
        self.__client_code = client_code
        self.__auth_code = auth_code

    @property
    def zcs_url(self):
        return self.__zcs_url

    @property
    def thingkey(self):
        return self.__thingkey

    @property
    def client_code(self):
        return self.__client_code

    @staticmethod
    def __make_dt_aware_utc(dt):
        if not dt.tzinfo:
            local_timezone = datetime.now(timezone.utc).astimezone().tzinfo
            dt = dt.replace(tzinfo=local_timezone)

        return dt.astimezone(timezone.utc)

    def __post(self, json_data):
        headers = {
            "Client": self.__client_code,
            "Authorization": self.__auth_code
        }

        response = requests.post(self.__zcs_url, json=json_data, headers=headers)

        response.raise_for_status()

        return response.json()

    def get_historic_data(self, start_dt, end_dt):
        """Get historic data.
        :param start_dt: start date time
        :param end_dt: end date time, delta can be max 24 hours

        :return: a dictionary with historic data
        """

        json_data = {
            "historicData": {
                "command": "historicData",
                "params": {
                    "thingKey": f"{self.__thingkey}",
                    "requiredValues": "*",
                    "start": f"{self.__make_dt_aware_utc(start_dt).isoformat().replace('+00:00', 'Z')}",
                    "end": f"{self.__make_dt_aware_utc(end_dt).isoformat().replace('+00:00', 'Z')}",
                }
            }
        }

        return self.__post(json_data)

    def get_realtime_data(self):
        """Get realtime data.

        :return: a dictionary with realtime data
        """

        json_data = {
            "realtimeData": {
                "command": "realtimeData",
                "params": {
                    "thingKey": f"{self.__thingkey}",
                    "requiredValues": "*",

                }
            }
        }

        return self.__post(json_data)
