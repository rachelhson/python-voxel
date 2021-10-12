import open3d as o3d
import numpy as np



# max limit
x = np.vstack(np.linspace(-2,2,4))
print (x[:])
y = np.vstack(np.linspace(-3,3,4))
print(y) 
z = np.vstack(np.linspace(-1,1,4))
print(z)
pcd = o3d.geometry.PointCloud()
points = np.hstack((x,y,z))
pcd.points = o3d.utility.Vector3dVector(points)
pcd.estimate_normals()
o3d.visualization.draw_geometries([pcd])

print(np.asarray(pcd.points))

voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,voxel_size=0.40)
o3d.visualization.draw_geometries([voxel_grid])

## voxel grid distance to points < 800 remove voxel