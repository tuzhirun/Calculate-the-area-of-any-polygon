# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:29:27 2019

@author: Tuzhirun
"""

import math
import re


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def calculate_distance(self, other_point):
        """计算两点间距离"""
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

    def __str__(self):
        return "({},{})".format(self.x, self.y)


class Polygon:
    def __init__(self):
        self.vertices = []
        self.points2vertices()

    def points2vertices(self):
        """读取坐标文件，并转换为顶点对象"""
        with open(VERTICES_FILE, "r", encoding="utf-8") as fr:
            # 定义一个用于切割字符串的正则
            seq = re.compile(",")
            for d in fr.readlines():
                # 读取出来的数据d为字符串，需切割后拼接为列表
                point = seq.split(d.strip())
#                print(point)
                # 将列表转为坐标元组,测绘坐标与绘图坐标x,y互换
                point = (float(point[1]), float(point[0]))
#                print("-------------------")
                print(point)
                if isinstance(point, tuple):
                    point = Point(*point)
                    self.vertices.append(point)
#                print(self.vertices)
    
    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].calculate_distance(points[i + 1])
        return perimeter

    def area(self):
        """给出任意一个多边形，其顶点坐标依次为（x0，y0），（x1，y1），（x2，y2），...，（xn，yn）（其中n=2，3，4，…），
        则其面积可表示为：

                     |Xi      Yi     |
        AREA = sigma |               | /2
        (i= 0,...n)  |X(i+1)  Y(i+1) |

        """
        n = len(self.vertices)
        if n < 3:
            return 0
        area = 0
        for i in range(n-2):
            # 以第一个坐标点为原点，将多边形分割为n-2个三角形，分别计算每个三角形面积后累加得多边形面积
            area += self.calculate_triangle_area(self.vertices[0], self.vertices[i+1], self.vertices[i+2])
        return abs(area)

    @staticmethod
    def calculate_triangle_area(point_a, point_b, point_c):
        """向量叉乘法计算三角形面积"""
        triangle_area = 0.5*((point_b.x - point_a.x)*(point_c.y - point_a.y) -
                             (point_b.y - point_a.y)*(point_c.x - point_a.x))
        return triangle_area


if __name__ == "__main__":
    
    VERTICES_FILE = "F:\\TianchiMatch\\DataSet\\面料2坐标数据\\"+"polygon_"+str(313)+".txt"
    polygon1 = Polygon()
    print("面积：{:.3f},周长：{:.3f}".format(polygon1.area(), polygon1.perimeter()))
