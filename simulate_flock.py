###########################################################################
# March 2019, Christoph Uhl (christophuhl07@gmail.com), Dr. Orit Peleg (orit.peleg@colorado.edu)
# Code for HW3 CSCI 4314/5314 Dynamic Models in Biology
###########################################################################

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib

class flock():
    def handle_edges(self, r, L):
        if r[0] > L/2:
            r[0] = r[0]-L
        elif r[0] < -L/2:
            r[0] = r[0]+L

        if r[1] > L/2:
            r[1] = r[1]-L
        elif r[1] < -L/2:
            r[1] = r[1]+L    
        return r

    def flocking_python(self, c1=0.00001, c2=0.01, c3=1, c4=0.01, title="Default", num_repulse_agents = 0):
        # c1 = 0.00001 #Attraction Scaling factor
        # c2 = 0.01 #Repulsion scaling factor
        # c3 = 1 #Heading scaling factor
        # c4 = 0.01 #Randomness scaling factor

        N = 50 #No. of Bodies to simulate
        frames = 100 #No. of frames
        limit = 100 #Axis Limits
        L  = limit*2
        P = 10 #Spread of initial position (gaussian)
        V = 10 #Spread of initial velocity (gaussian)
        delta = 1 #Time Step
        vlimit = 1 #Maximum velocity

        #Initialize
        p = P*np.random.randn(2,N)
        v = V*np.random.randn(2,N)

        #place repulsive agents at cooradinates
        repulse_agents = np.zeros((num_repulse_agents, 2))
        for i in range(num_repulse_agents):
            repulse_agents[i,0] = -(num_repulse_agents/2)
            repulse_agents[i,1] = i-(num_repulse_agents/2)

        #Initializing plot
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)

        for i in range(0, frames):
            v1 = np.zeros((2,N))
            v2 = np.zeros((2,N))
            
            #Calculate Average Velocity v3 
            v3 = np.array([coordinate*c3 for coordinate in [sum(v[0,:]), sum(v[1,:])]]) #turn into numpy array to make them the same
            

            if (np.linalg.norm(v3) > vlimit): #limit maximum velocity
                v3 = v3*vlimit/np.linalg.norm(v3)

            for n in range(0, N):
                for m in range(0, N):
                    if m!=n:
                        total_attractive_forces = 0 #doing these to not have to reference memory so many times
                        total_repulsion_forces = 0
                        n_pos = p[:, n]

                        #Compute vector r from one agent to the next
                        r = p[:,m]-n_pos

                        #handling edge cases i think
                        r = self.handle_edges(r, L)

                        #Compute distance between agents rmag
                        rmag = np.sqrt((r[0]**2) + (r[1]**2))

                        #Compute attraction v1
                        total_attractive_forces += c1*r

                        #Compute Repulsion [non-linear scaling] v2
                        total_repulsion_forces -= ((c2*r)/(rmag**2))
                
                #Now calculate for repulse agents
                for m in range(num_repulse_agents):
                    r = repulse_agents[m] - n_pos #repulse_agents[m] give the x,y coordinates if repulse agent m
                    r = self.handle_edges(r, L)
                    rmag = np.sqrt((r[0]**2) + (r[1]**2))
                    #Calculate repulsion
                    total_repulsion_forces -= ((c2*r)/(rmag**2))

                v1[:,n] = total_attractive_forces
                v2[:,n] = total_repulsion_forces

                #Compute random velocity component v4
                v4 = c4 * np.random.randn(2, 1)

                #Update velocity
                v[:,n] = v1[:,n] + v2[:,n] + v3 + v4[:,0]

            #Update position
            for coord in [0,1]:
                for boid in range(len(v[coord, :])):
                    v[coord, boid] *= delta
            p = p+v

            #Periodic boundary
            tmp_p = p

            tmp_p[0, p[0,:] > L/2] = tmp_p[0,p[0,:] > (L/2)] - L
            tmp_p[1, p[1,:] > L/2] = tmp_p[1, p[1,:] > (L/2)] - L
            tmp_p[0, p[0,:] < -L/2]  = tmp_p[0, p[0,:] < (-L/2)] + L
            tmp_p[1, p[1,:] < -L/2]  = tmp_p[1, p[1,:] < (-L/2)] + L

            p = tmp_p
            # Can Also be written as:
            # p[p > limit] -= limit * 2
            # p[p < -limit] += limit * 2

            line1, = ax.plot(p[0, 0], p[1, 0])

            #update plot
            ax.clear()
            ax.scatter(repulse_agents[:,0], repulse_agents[:, 1], color = 'red')
            ax.quiver(p[0,:], p[1,:], v[0,:], v[1,:]) # For drawing velocity arrows
            plt.title(title)
            plt.xlim(-limit, limit)
            plt.ylim(-limit, limit)
            line1.set_data(p[0,:], p[1,:])

            fig.canvas.draw()

flock_py = flock()
flock_py.flocking_python()

#Try with repulse agents
# flock_py.flocking_python(c1 =  0.001, title = "Barrier with c1=0.001", num_repulse_agents = 100)