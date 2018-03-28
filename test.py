from pyroutelib3 import Router # Import the router
import csv
#router = Router("car") # Initialise it

#start = router.data.findNode(4.36122,18.55496) # Find start and end nodes
#end = router.data.findNode(4.1005,18.6584)

#status, route = router.doRoute(start, end) # Find the route - a list of OSM nodes

#if status == 'success':
#    routeLatLons = list(map(router.nodeLatLon, route)) # Get actual route coordinates

#print(routeLatLons)




def read_in_nodes(filename):
    cz_list = []
    camp_list = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            if row[5] == 'conflict_zone':
                cz_list.append(row[3:5])
            elif row[5] == 'camp':
                camp_list.append(row[3:5])
            else:
                assert False
    return cz_list, camp_list


def generate_all_cz_to_camp_routes(cz_list, camp_list):
    list_of_routes = []
    for cz in cz_list:
        for camp in camp_list:
            router = Router("car")  # Initialise it
            print(cz, camp)
            start = router.data.findNode(float(cz[0]), float(cz[1]))  # Find start and end nodes
            end = router.data.findNode(float(camp[0]), float(camp[1]))
            print('starting router')
            status, route = router.doRoute(start, end)  # Find the route - a list of OSM nodes
            print('finish router')
            if status == 'success':
                print('success')
                routeLatLons = list(map(router.nodeLatLon, route)) # Get actual route coordinates
                routeLatLons.insert(0, cz)
                routeLatLons.append(camp)
                list_of_routes.append(routeLatLons)
                print('here', len(routeLatLons))
            elif status == 'gave_up':
                print('skipping as too long')
            else:
                print(status)
                assert False

    return(list_of_routes)


def extract_nodes(list_of_routes):
    list_of_nodes = []
    for route in list_of_routes:
        list_of_nodes.append(route[0])
        list_of_nodes.append(route[-1])
    list_of_unique_nodes = []
    for node in list_of_nodes:
        if node not in list_of_unique_nodes:
            list_of_unique_nodes.append(node)
    return list_of_unique_nodes


def merge_routes(list_of_routes):
    route_a = list_of_routes[0]
    route_b = list_of_routes[1]
    this_shared_route = shared_route(route_a, route_b)
    list_of_merged_routes = []
    return list_of_merged_routes


def shared_route(route_a, route_b):
    this_shared_route = [element for element in route_a if element in route_b]
    print(this_shared_route)
    return this_shared_route


if __name__ == "__main__":
    cz_list, camp_list = read_in_nodes('/home/s/sc676/Desktop/locations_sharing.csv')
    print('CZs: ', cz_list)
    print('camps: ', camp_list)
    list_of_routes = generate_all_cz_to_camp_routes(cz_list, camp_list)
    print(list_of_routes[0])
    print(list_of_routes[1])
    print(len(list_of_routes))
    list_of_merged_routes = merge_routes(list_of_routes)
    list_of_nodes = extract_nodes(list_of_routes)
    print(list_of_nodes)
