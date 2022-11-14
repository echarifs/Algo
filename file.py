#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 00:26:25 2021

@author: mac
"""




class Cellule:
    def __init__(self, item = None):
        self.item = item
        self.next = None
        self.previous = None


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, value):
        newCellule = Cellule(value)
        if self.head is None:
            self.head = self.tail = newCellule
        else:
            self.tail.next = newCellule
            newCellule.previous = self.tail
            self.tail = newCellule
        self.length += 1

    def dequeue(self):
        item = self.head.item
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return item
    
    def isEmpty(self):
        return self.length == 0

def Quadrant_coordinates(pnt, distance):
    quad = pnt.bounding_quadrant()
    quad_1 = quad.inflate(distance)
    return quad_1.get_arrays()

def Points_within_quadrant(points, pnt_0, distance):
     array = Quadrant_coordinates(pnt_0, distance)
     min_coordinates = array[0]
     max_coordinates = array[1]
     new_points = []
     points_out_quadrant = []
     for pnt in points: 
        if pnt.coordinates[0] >= min_coordinates[0] and pnt.coordinates[1] >= min_coordinates[1] and pnt.coordinates[0] <= max_coordinates[0]and  pnt.coordinates[1] <= max_coordinates[1]:
            new_points.append(pnt)    
        else :
            points_out_quadrant.append(pnt)
     return (new_points, points_out_quadrant)
    
def Points_within_radius(pnt_0, points, distance):
     a = Points_within_quadrant(points, pnt_0, distance)
     new_points = a[0]
     points_out_quadrant = a[1]
     liste = []
     for pnt in new_points:
         if pnt_0.distance_to(pnt) <= distance:
             liste.append(pnt)
         else:
             points_out_quadrant.append(pnt)
     return (liste, points_out_quadrant)




    
