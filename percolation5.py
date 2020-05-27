'''Author - MD. ELIOUS ALI MONDAL
   Created - 30/7/2017'''

import random
import turtle
from math import *
#random.seed(12)
turtle.title('percolation lattice')
turtle.setworldcoordinates(0,0,21,21)
turtle.hideturtle()
turtle.speed(0)
# p = threshold frequency of percolation

'''
generating the lattice sites
'''
x = []
for i in range(1,21):
    for j in range(1,21):
        x.append(i)
y = []
for i in range(1,21):
    for j in range(1,21):
        y.append(j)
ai = []
for i in range(len(x)):
    ai.append(random.random())
##for i in range(len(x)):
##        turtle.up()
##        turtle.goto(x[i],y[i])
##        turtle.down()
##        turtle.dot(5)
'''
generating points which are to be plotted in graph and storing the points in
list m
'''
touches_all_sides = False
p = 0
while (p < 1) and (touches_all_sides == False ):
    print(p)
    #print(touches_all_sides)
    xi = []
    yi = []
    m = []
    for i in range(len(x)):
        #print(i)
        if p >= ai[i]:
            xi.append(x[i])
            yi.append(y[i])
            m.append((x[i],y[i]))

    '''
    finding the points which are not alone(i.e. within some cluster) and storing
    them in list n
    '''
    n = []
    for i in range(len(m)):
        for j in range(len(m)):
            if sqrt((xi[i]-xi[j])**2 + (yi[i]-yi[j])**2) == 1:
                if (xi[i],yi[i]) not in n:
                    n.append((xi[i],yi[i]))
                if (xi[j],yi[j]) not in n:    
                    n.append((xi[j],yi[j]))
            else:
                continue        

    def dist(i,j):
        '''
        takes two pairs of coordinates
        returns the distance between them
        '''
        return sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2)

    '''
    finding the clusters generated and storing the points of a cluster in a list z
    we will obtain many such clusters
    storing the clusters in list a
    '''
    a = []
    for i in n:
        z = []
        def cluster(i,l):
            '''
            takes a coordinate pair and a list of coordinates
            returns a list of pairs consisting of cluster formed by neighbours of i
            and by their negbours and so on
            '''
            
           
            for j in l:
                    
                if dist(i,j) == 1:
                        if j in z:
                             continue
                        else:    
                            z.append(j)
                            cluster(j,l)
            return z
        if len(a)==0:
            cluster(i,n)
            a.append(z)
        else:
            for j in a:
                if i in j:
                    value = False
                    break
                else:
                    value = True
                    
            if value == True:        
                cluster(i,n)
                a.append(z)

    '''
    finding the largest cluster
    '''
    largest_cluster = []
    for i in range(len(a)):
        if i == 0:
            largest_cluster = a[i]
        elif len(a[i]) >= len(largest_cluster):
            largest_cluster = a[i]
    '''
    clouring the clusters and plotting th sites dynamically using turtle
    if point belongs to the largest cluster then it is painted red
    if it belongs to any other cluster then green
    and if it doesn't belong to any cluster(i.i. alone point) the blue
    '''
    for i in m:
        if i not in n:
            turtle.up()
            turtle.goto(i)
            turtle.down()
            turtle.dot(32,'blue')
        
    for i in a:
        if i == largest_cluster:
            for j in largest_cluster:
                turtle.up()
                turtle.goto(j)
                turtle.down()
                turtle.dot(32,'red')
        else:
            b = random.choice(['green','yellow','brown','purple','orange','indigo','pink','violet'])
            for j in i:
                turtle.up()
                turtle.goto(j)
                turtle.down()
                turtle.dot(32,b)

    

    a10 = False
    a11 = False
    b10 = False
    b11 = False
    for i in range(len(largest_cluster)):
        if largest_cluster[i][0] == 1:
            a10 = True
            break
    for i in range(len(largest_cluster)):        
        if largest_cluster[i][0] == 20:        
            b10 = True
            break
    for i in range(len(largest_cluster)):
        if largest_cluster[i][1] == 1:
            a11 = True
            break
    for i in range(len(largest_cluster)):
        if largest_cluster[i][1] == 20:
            b11 = True
    if  (a10 == True) and  (b10 == True) and  (a11 == True) and  (b11 == True):
        touches_all_sides = True

    p = p + 0.1
if touches_all_sides == True:
    print('Threshold frequency = ',p-0.1)    
        
    
    
            
        
            

    

            
            
    
       
       
                        
           
