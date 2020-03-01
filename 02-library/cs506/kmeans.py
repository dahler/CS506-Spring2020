from collections import defaultdict
from math import inf
import random
import csv
from cs506 import  sim


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
<<<<<<< HEAD
    #raise NotImplementedError()

    res = []

    if len(points) == 0:
        raise ValueError("No point")

    if len(points) == 1:

        return points


    for point_i in range(len(points[0])):
        sum_i = 0;
        for i in points:
            sum_i = sum_i+i[point_i]
        res.append(sum_i/len(points))

    return res
=======
    n = len(points)
    x = sum([p[0] for p in points]) / n
    y = sum([p[1] for p in points]) / n
    return [x, y]
>>>>>>> upstream/master


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
<<<<<<< HEAD
    #raise NotImplementedError()

    centers = [];
    centerNum = unique(assignments)

    for c in centerNum:
        points = [];
        for index, ass in enumerate(assignments):
            if (ass == c):
                points.append(dataset[index])
        centers.append(point_avg(points))

    return centers


def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
            # print list
    return unique_list;
=======
    k = max(assignments) + 1
    clusters = [[] for i in range(k)]
    for pointIndex, pointAssignment in enumerate(assignments):
        clusters[pointAssignment].append(dataset[pointIndex])
>>>>>>> upstream/master

    new_centers = []
    for cluster in clusters:
        new_centers.append(point_avg(cluster))

    return new_centers

def assign_points(data_points, centers):
    """
    """
    print("data_points center is", centers)
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
<<<<<<< HEAD
    #raise NotImplementedError()

    return sim.euclidean_dist(a,b)

    #sumSQ = 0
    #for i in  range(len(a)):
    #   sumSQ = sumSQ + (a[i] - b[i])**2

    #return sumSQ**(1/2)


=======
    return sum([(a - b) ** 2 for a, b in zip(a, b)]) ** 0.5

def distance_squared(a, b):
    return distance(a, b) ** 2
>>>>>>> upstream/master


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
<<<<<<< HEAD


    sampling = random.choices(dataset, k=k)


    return sampling


def cost_function(clustering):


    res = 0
    for k, v in clustering.items():
        mu = point_avg(v)
        for i in v:
            res = res + distance(i, mu)**2

    return res



def generate_k_pp(dataset, k):

    #if k == None or k == 0:
    #    raise ValueError("k must not be zero")

    #if k == 1:
    #    return random.choice(dataset)

    #if k == len(dataset):
    #    return dataset

    centers = []
    centers.append(random.choice(dataset))

    while len(centers) < k :
        dis = []
        totalLen = 0
        for i in dataset:
            mindis = float('inf')
            for c in centers:
                if mindis > distance(c,i):
                    mindis = distance(c,i)
            totalLen = totalLen+ mindis **2;
            dis.append(mindis**2)
        #ran = random.uniform(0, totalLen)

        dis = [p / totalLen for p in dis]
        ran = random.choices(dataset, dis)[0]
        centers.append(ran)



    return centers

=======
    return random.sample(dataset, k)


def cost_function(clustering):
    cost = 0
    for idx in clustering:
        center = point_avg(clustering[idx])
        cost += sum([distance_squared(center, p) for p in clustering[idx]])

    return cost


def generate_k_pp(dataset, k):
    center = random.choice(dataset)
    k_points = [center]

    while len(k_points) < k:
        prob = []
        for point in dataset:
            prob.append(distance_squared(center, point))
        
        prob = [p/sum(prob) for p in prob]
        center = random.choices(dataset, prob)[0]

        k_points.append(center)

    return k_points
>>>>>>> upstream/master


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
