import requests
import route_data
import os

base_URL = "https://external.transitapp.com/v3/public/stop_departures"

class RealTime:
  def __init__(self, route: str, dir: str):
    self._route = route
    self._direction = dir
    self._stop = route_data.stop_ids[(self._route, self._direction)]