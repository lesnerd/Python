def ConnectCities(numberOfConnectedCities, connectedCities, numberOfCities, costConncetingCities):
    return -1


def main():
    connectedCities = [[1, 4], [4, 5], [2, 3], [2, 4], [3, 4]]
    costConnecToCity = [[1, 6, 10], [4, 3, 12], [5, 6, 2]]
    ConnectCities(len(connectedCities), connectedCities, 6, costConnecToCity)


if __name__ == "__main__":   # ifdef
    main()
