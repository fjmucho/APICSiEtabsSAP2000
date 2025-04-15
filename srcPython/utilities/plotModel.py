
import numpy as np
from  matplotlib import pyplot as plt

def plotModel2d():
    pass

def plotModel3d(coords, elems, nameModelProject=''):
    fig = plt.figure()
    axes = fig.add_axes([0.1,0.1, 3,3], projection='3d') # Indicate a 3D plot
    axes.view_init(20, 60) # Set the viewing angle of the 3D plot

    # Plot members
    for mbr in elems:
        node_i = int(mbr[0]) #Node number for node i of this member
        node_j = int(mbr[1]) #Node number for node j of this member

        ix = coords[node_i,0] #x-coord of node i of this member
        iy = coords[node_i,1] #y-coord of node i of this member
        iz = coords[node_i,2] #z-coord of node i of this member
        jx = coords[node_j,0] #x-coord of node j of this member
        jy = coords[node_j,1] #y-coord of node j of this member
        jz = coords[node_j,2] #z-coord of node j of this member

        # Calculate direction cosines
        dx = jx-ix #x-component of vector along member
        dy = jy-iy #y-component of vector along member
        dz = jz-iz #z-component of vector along member
        mag = np.sqrt(dx**2 + dy**2 + dz**2) # Magnitude of vector (length of member)

        axes.plot3D([ix,jx],[iy,jy],[iz,jz],'k') # Plot 3D node

    #Plot coords
    for n, node in enumerate(coords):
        axes.plot3D([node[0]],[node[1]], [node[2]],'ok', ms=6, alpha=0.7) # Plot 3D node
        label = str(n+1) # Node number label
        axes.text(node[0], node[1], node[2], label, fontsize=16) # Add node label
    
    # Make the aspect ratio equal
    fig.gca().set_aspect('equal', adjustable='box') # comentar en caso de usar margenes ajustados

    axes.set_xlabel('X_Distance (m)')
    axes.set_ylabel('Y-Distance (m)')
    axes.set_zlabel('Z-Distance (m)')
    axes.set_title(f'{nameModelProject}')
    axes.grid()
    return

