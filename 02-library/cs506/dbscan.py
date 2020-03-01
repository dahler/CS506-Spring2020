from .sim import euclidean_dist

class DBC():
    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon

    def _get_neighborhood(self, P):
        Neighborhood = []
        for Pn in range(len(self.dataset)):
            if euclidean_dist(self.dataset[P], self.dataset[Pn]) <= self.epsilon:
                Neighborhood.append(Pn)
        return Neighborhood

    def _assign_cluster(self, P, PNeighborhood, assignment, assignments):
        assignments[P] = assignment
        while PNeighborhood:
            Pn = PNeighborhood.pop()
            if assignments[Pn] == -1:
                # border point
                assignments[Pn] = assignment
            if assignments[Pn] == 0:
                # could be a core point
                assignments[Pn] = assignment
                new_neighborhood = self._get_neighborhood(Pn)

                if len(new_neighborhood) >= self.min_pts:
                    PNeighborhood += new_neighborhood



        return assignments

    def dbscan(self):
        assignments = [0 for i in range(len(self.dataset))]
        assignment = 0
        for P in range(len(self.dataset)):
            if assignments[P] != 0:
                continue

            PNeighborhood = self._get_neighborhood(P)

            if len(PNeighborhood) >= self.min_pts:
                # core point
                assignment += 1
                assignments = self._assign_cluster(P, PNeighborhood, assignment, assignments)
            else:
                # either border or noise
                assignment = -1

        return assignments