import route_data
from schedule_obj import Schedule

def write_arrival_times():

  for dir in route_data.directions:
     for route in route_data.routes:
        schedule_obj = Schedule(route, dir)
        schedule_obj.write_schedule()

  

if __name__ == "__main__":
    write_arrival_times()
