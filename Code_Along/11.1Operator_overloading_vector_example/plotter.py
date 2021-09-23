class Plotvectors:
"""Plotting several vectors in cartesian coordinate system"""
    def __init__ (self, *vectors) -> None:
        X, Y = [], []
        for vector in vectors:
            X.append(vector[0])
            Y.append(vector[0])
        self.X, self.Y = X, Y
        self