#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""


import file
from sys import argv
from geo.quadrant import Quadrant
from geo.point import Point
from geo.segment import Segment


def load_instance(filename):
    """
    loads .pts file.
    returns distance limit and points.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in l.split(",")]) for l in lines]

    return distance, points

   
    
def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    Liste = []
    out_points = points
    while out_points != []:
        pnt = out_points[0]
        queue = file.Queue()
        queue.enqueue(pnt)
        taille = 0
        while  queue.isEmpty() == False :
               w = queue.dequeue()
               a = file.Points_within_radius(w, out_points, distance)
               list_points =a[0]
               out_points = a[1]
               for pt in list_points :
                        queue.enqueue(pt)
                        taille += 1
        Liste += [taille]
    Liste.sort(reverse = True)
    print(Liste)

def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)
          
main()
