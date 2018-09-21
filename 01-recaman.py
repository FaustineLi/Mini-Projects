import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

'''
A visualization of  Recamán's sequence: a(0) = 0; for n > 0, 
a(n) = a(n-1) - n if positive and not already in the sequence, 
otherwise a(n) = a(n-1) + n. http://oeis.org/A005132
'''

def semicircle(start, end):
    '''Returns a tuple with x, y coordinates to draw a semicircle on the 
    number line given a start and end point.'''
    r = abs(end - start) / 2
    x0 = (start + end) / 2
    x = np.linspace(start, end, 100 * r)
    y = np.sqrt(np.square(r) - np.square(x - x0))
    return x, y

    
def recaman_seq(n):
    '''Returns a list of the first n terms of the Recamán sequence.'''
    N = [0]
    for i in range(1, n):
        if N[i - 1] - i in N or N[i - 1] - i < 0:
            N.append(N[i - 1] + i)
        else:
            N.append(N[i - 1] - i)
    return N


def plot_recaman(n):
    '''Visualizes the first n terms of the Recamán sequence with semicircles.'''
    N = recaman_seq(n)
    r = []
    for i in range(1, len(N)):
        r.append(abs(N[i - 1] - N[i]))
        
    for i in range(1, len(N)):
        x, y = semicircle(N[i - 1], N[i])
        if i % 2 == 1:
            y *= -1
        plt.plot(x, y, c=cm.viridis(r[i - 1] / (np.max(r) - np.min(r))))

    plt.axes().set_aspect('equal')
    plt.show()
    

if __name__ == '__main__':
    plot_recaman(100)
