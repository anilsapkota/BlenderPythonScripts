import bpy


def clean_scene():
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj)
        
def create_cube():
    bpy.ops.mesh.primitive_cube_add(size=1)
    return bpy.context.object 

def subdivide(obj,name,levels=5,apply=True):
    subdiv_modifier = obj.modifiers.new(type='SUBSURF',name=name)
    subdiv_modifier.levels = levels
    if apply:
        bpy.ops.object.modifier_apply(modifier=subdiv_modifier.name)
    
        

def spherify(obj,name,apply=True):
    cast_modifier = obj.modifiers.new(type='CAST',name=name)
    if apply:
         bpy.ops.object.modifier_apply(modifier=cast_modifier.name)
    
        

def decimate(obj,name,degrees = 20,apply=True):
    decimate_modifier = obj.modifiers.new(type='DECIMATE',name=name)
    decimate_modifier.decimate_type = 'DISSOLVE'
    decimate_modifier.angle_limit = 0.349066
    decimate_modifier.use_dissolve_boundaries = True
    if apply:
        bpy.ops.object.modifier_apply(modifier=decimate_modifier.name)
    
        
        

def create_unique_sphere():
    #create a cube
    cube = create_cube()
    
    #subdivide it
    subdivide(cube,'subdiv_cube',5,True)



    #spherify it (apply cast)
    spherify(cube,'cast_cube',True)
    
    
    #Decimate it(planar surface)
    decimate(cube,'decimate_cube',20,True)





clean_scene()
create_unique_sphere()
