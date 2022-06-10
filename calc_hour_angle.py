'''
This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
'''

def calcAngle(h,m):     
    if (h < 0 or m < 0 or h > 12 or m > 60):
        print('Wrong input')
        
    if (h == 12):
        h = 0
    if (m == 60):
        m = 0
        h += 1;
        if(h>12):
            h = h-12;
        
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m

    angle = abs(hour_angle - minute_angle)

    angle = min(360 - angle, angle)
        
    return angle
 
h = 9
m = 60
print('Angle ', calcAngle(h,m))