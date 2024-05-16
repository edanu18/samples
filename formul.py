import math

# Noktaları temsil eden liste
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Tüm nokta çiftleri arasındaki mesafeleri hesaplayan fonksiyon
def calculateDistances(points):
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distances.append(euclideanDistance(points[i], points[j]))
    return distances

# Minimum mesafeyi bulma
def findMinimumDistance(distances):
    return min(distances)

# Nokta çiftleri arasındaki mesafeleri hesaplayıp yazdırma
distances = calculateDistances(points)
print("Tüm nokta çiftleri arasındaki mesafeler:", distances)

# Minimum mesafeyi bulup yazdırma
min_distance = findMinimumDistance(distances)
print("Minimum mesafe:", min_distance)
