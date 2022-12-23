import bpy


def clean_scene():
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj)
        
def create_cube():
    bpy.ops.mesh.primitive_cube_add(size=1)
    return bpy.context.object 



def create_unique_sphere():
    #create a cube
    cube = create_cube()
    
    #subdivide it
    
    subdiv_modifier = cube.modifiers.new(type='SUBSURF',name='subdiv_cube')
    
    #increase resolution
    subdiv_modifier.levels = 5
    bpy.ops.object.modifier_apply(modifier="subdiv_cube")



    #spherify it (apply cast)
    cast_modifier = cube.modifiers.new(type='CAST',name='cast_cube')
    bpy.ops.object.modifier_apply(modifier="cast_cube")
    
    #Decimate it(planar surface)
    decimate_modifier = cube.modifiers.new(type='DECIMATE',name='decimate_cube')
    decimate_modifier.decimate_type = 'DISSOLVE'
    decimate_modifier.angle_limit = 0.349066

    decimate_modifier.use_dissolve_boundaries = True
    
    bpy.ops.object.modifier_apply(modifier="decimate_cube")





clean_scene()
create_unique_sphere()
