import json
from rover_connect2.rover_connect import RoverConnect

if __name__ == "__main__":
#    pdb.set_trace()

    rover = RoverConnect('/dev/ttyS0', 'internet.mts.ru')
    
    gnss_data = rover.get_cgns_data()
    gnss_parsed_data = rover.parse_cgns_info(gnss_data)
    gnss_parsed_data = json.loads(gnss_parsed_data)
    
    print(json.dumps(gnss_parsed_data, indent=4))
 

