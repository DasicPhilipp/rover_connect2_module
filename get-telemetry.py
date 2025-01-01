from rover_connect2.rover_connect import RoverConnect
from rover_connect2.rover_connect import Telemetry

if __name__ == "__main__":
#    pdb.set_trace()
    api_url = "http://my-json-server.ru:9000/api/data"
    rover = RoverConnect('/dev/ttyS0', 'internet.mts.ru')
    telemetry_data = Telemetry(rover)
    td = telemetry_data.get_telemetry_data()
    print(td)
    
    rover.post_get(td, api_url)

    


