import time
from itertools import permutations
from haversine import haversine

# City Bank branch locations
locations = {
    1: {'latitude': 23.8728568, 'longitude': 90.3984184, 'address': 'Uttara Branch'},
    2: {'latitude': 23.8513998, 'longitude': 90.3944536, 'address': 'City Bank Airport'},
    3: {'latitude': 23.8330429, 'longitude': 90.4092871, 'address': 'City Bank Nikunja'},
    4: {'latitude': 23.8679743, 'longitude': 90.3840879, 'address': 'City Bank Beside Uttara Diagnostic'},
    5: {'latitude': 23.8248293, 'longitude': 90.3551134, 'address': 'City Bank Mirpur 12'},
    6: {'latitude': 23.827149, 'longitude': 90.4106238, 'address': 'City Bank Le Meridien'},
    7: {'latitude': 23.8629078, 'longitude': 90.3816318, 'address': 'City Bank Shaheed Sarani'},
    8: {'latitude': 23.8673789, 'longitude': 90.429412, 'address': 'City Bank Narayanganj'},
    9: {'latitude': 23.8248938, 'longitude': 90.3549467, 'address': 'City Bank Pallabi'},
    10: {'latitude': 23.813316, 'longitude': 90.4147498, 'address': 'City Bank JFP'},
}

# Function to calculate the total distance for a given route
def calc_distance(route, locations):
    """
    Calculate the total distance from given latitude & longitude point for the branch.
    -:param: route
    -:param: branch locations
    -:return: distance
    """
    total_distance = 0
    for i in range(len(route) - 1):
        location1 = locations[route[i]]
        location2 = locations[route[i + 1]]
        coord1 = (location1['latitude'], location1['longitude'])
        coord2 = (location2['latitude'], location2['longitude'])
        total_distance += haversine(coord1, coord2)
    return total_distance

def optimize_expo():
    """
    Find the optimized route from branch locations using the Permutations Method.
    And then export the optimized route and minimum distance.
    -:param: none
    -:return: none
    """
    # Generate all possible permutations of branch locations
    branch_permutations = permutations(locations.keys())

    # Initialize variables for the best route and minimum distance
    best_route = None
    min_distance = float('inf')
        
    # Iterate through all permutations and find the one with the minimum distance
    for route in branch_permutations:
        distance = calc_distance(route, locations)
        if distance < min_distance:
            min_distance = distance
            best_route = route

    # Export the optimized route and minimum distance
    filename = 'output.txt'
    with open(filename, 'w') as file:
        file.write("Optimized Route:\n")
        for branch in best_route:
            file.write(f"{locations[branch]['address']} ({branch})\n")
        file.write(f"\nMinimum Distance: {min_distance:.2f} kilometers\n")
    print(f"Results exported to {filename}")


if __name__ == '__main__':
    start = time.time()
    # Call the main function
    optimize_expo()
    print(f'This script took {round(time.time() - start, 2)} seconds to generate the results')
