import requests
import route_data
import os

base_URL = "http://www3.septa.org/sms/"

class Schedule:
  def __init__(self, route: str, dir: str):
    self._route = route
    self._direction = dir
    self._stop = route_data.stop_ids[(self._route, self._direction)]

    self.data = requests.get(base_URL + self._stop)

  def get_route(self):
    return self._route
  
  def get_direction(self):
    return self._direction
  
  def write_schedule(self):
    if self.data.status_code == 200:
      data_directory = '../../data/schedule_data'
      output = os.path.join(data_directory, f"schedule_{self._route}_{self._direction}.txt")
      
      with open(output, 'w', encoding='utf-8') as file:
        file.write(self.data.text)

    else:
      print("Invalid status code")
      print(self.data.status_code)