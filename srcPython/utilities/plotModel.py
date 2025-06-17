
import numpy as np
import math
from  matplotlib import pyplot as plt

def plotModel2d(nodes, members, nameModelProject=''):
    nodes = np.array(nodes)  # Convert to numpy array if not already
    members = np.array(members)  # Convert to numpy array if not already
    
    pendiente = np.zeros([members.shape[0], 1])
    L = np.zeros([members.shape[0], 1])

    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 2, 2])
    fig.gca().set_aspect('equal', adjustable='box')

    # Plot members
    for idx, mbr in enumerate(members):
        node_i = int(mbr[0])  # Node number for node i of this member
        node_j = int(mbr[1])  # Node number for node j of this member

        ix = nodes[node_i, 0]  # x-coord of node i of this member
        iy = nodes[node_i, 2]  # y-coord of node i of this member
        jx = nodes[node_j, 0]  # x-coord of node j of this member
        jy = nodes[node_j, 2]  # y-coord of node j of this member

        xm, ym = (ix + jx)/2, (iy + jy)/2
        L[idx] = ((jx - ix)**2 + (jy + iy)**2)**0.5
        pendiente[idx] = np.degrees(np.arctan2(jy-iy, jx-ix))

        axes.plot([ix, jx], [iy, jy], 'k')  # Member
        axes.text(xm, ym, f'{idx+1}', ha='center', va='bottom', color='red',
                fontsize=12, fontweight='bold', rotation=pendiente[idx].item())

    long_min_member = min(L)
    # Plot nodes
    # fuerzas = np.reshape(forceVector, (2*nodes.shape[0], 1))
    for idx, nudo in enumerate(nodes):
        axes.plot([nudo[0]], [nudo[2]], 'ko')
        axes.text(nudo[0], nudo[2], f'{idx+1}', ha='left', va='bottom',
                color='black', fontsize=12)  # , fontweight='bold' )

        x_fuerza = nodes[math.trunc(idx/2), 0]  # cambia de direccion en x o y
        y_fuerza = nodes[math.trunc(idx/2), 1]
        # if fuerza[idx, 0] != 0:  # pares - eje Y
        #     ax_fuerza = fuerza[idx, 0]
        #     ay_fuerza = 0
        #     plt.arrow(nudo[0]-0.15*(long_min_member.item()), nudo[1], 0.10*long_min_member.item(), 0,
        #             color='r',
        #             width=0.008*long_min_member.item(),
        #             head_width=0.030*long_min_member.item(),  # flecha en X
        #             head_length=0.025*long_min_member.item(),  # flecha en Y
        #             zorder=2)
        # if fuerza[idx, 1] != 0:  # impares - eje X
        #     ax_fuerza = 0
        #     ay_fuerza = fuerza[idx, 1]
        #     plt.arrow(nudo[0], nudo[1]+0.18*(long_min_member.item()), 0, -0.12*long_min_member.item(),
        #             color='r',
        #             width=0.008*long_min_member.item(),  # ancho de la barra en X
        #             head_width=0.03*long_min_member.item(),  # ancho de la flecha en X
        #             head_length=0.025*long_min_member.item(),  # altura de la flecha en Y
        #             zorder=1.5)

    axes.set_xlabel('Distance (m)')
    axes.set_ylabel('Distance (m)')
    axes.set_title('Structure to analyse')
    axes.grid()
    plt.show()

def plotModel3d(coords, elems, nameModelProject=''):
    coords = np.array(coords)
    elems = np.array(elems)

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

