import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from ObjLoader1 import Objfileexporter
import pickle
from texture_loader import texture_loader




def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)


if not glfw.init():
    raise Exception("glfw can not be initialized!")

window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

glfw.set_window_pos(window, 400, 200)

glfw.set_window_size_callback(window, window_resize)

glfw.make_context_current(window)


road_verts, road_buff = Objfileexporter.model_load("road.obj")
floor_verts, floor_buff = Objfileexporter.model_load("floor.obj")
solarpanel_verts, solarpanel_buffer = Objfileexporter.model_load("solarpanelobj.obj")
tree_verts, tree_verts = Objfileexporter.model_load("tree.obj")
home_indices, home_buffer = Objfileexporter.model_load("home.obj")
door_indices, door_buffer = Objfileexporter.model_load("door.obj")
window_indices, window_buffer = Objfileexporter.model_load("window.obj")
hotel_indices, hotel_buffer = Objfileexporter.model_load("hotel.obj")
window2_indices, window2_buffer = Objfileexporter.model_load("window2.obj")
hotel2_indices, hotel2_buffer = Objfileexporter.model_load("hotel2.obj")
hotel3_indices, hotel3_buffer = Objfileexporter.model_load("hotel3.obj")
leg_indices, leg_buffer = Objfileexporter.model_load("leg.obj")
sun_indices, sun_buffer = Objfileexporter.model_load("sun.obj")
srcfor_vrtx = """
# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_normal;
uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;
out vec2 v_texture;
void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

srcfor_frag = """
# version 330
in vec2 v_texture;
out vec4 out_color;
uniform sampler2D s_texture;
void main()
{
    out_color = texture(s_texture, v_texture);
}
"""

shader_forcompile = compileProgram(compileShader(srcfor_vrtx, GL_VERTEX_SHADER), compileShader(srcfor_frag, GL_FRAGMENT_SHADER))


vertexArrayObject = glGenVertexArrays(13)
vertexBufferObject = glGenBuffers(13)


# road
glBindVertexArray(vertexArrayObject[0])
glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[0])
glBufferData(GL_ARRAY_BUFFER, road_buff.nbytes, road_buff, GL_STATIC_DRAW)



glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, road_buff.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, road_buff.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, road_buff.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# floor 
glBindVertexArray(vertexArrayObject[1])

glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[1])
glBufferData(GL_ARRAY_BUFFER, floor_buff.nbytes, floor_buff, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, floor_buff.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, floor_buff.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, floor_buff.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# solar_panel 
glBindVertexArray(vertexArrayObject[2])
glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[2])
glBufferData(GL_ARRAY_BUFFER, solarpanel_buffer.nbytes, solarpanel_buffer, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, solarpanel_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, solarpanel_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, solarpanel_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# tree
glBindVertexArray(vertexArrayObject[3])

glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[3])
glBufferData(GL_ARRAY_BUFFER, tree_verts.nbytes, tree_verts, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, tree_verts.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, tree_verts.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, tree_verts.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# home
glBindVertexArray(vertexArrayObject[4])

glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[4])
glBufferData(GL_ARRAY_BUFFER, home_buffer.nbytes, home_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, home_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, home_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, home_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(5)

# door
glBindVertexArray(vertexArrayObject[5])

glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[5])
glBufferData(GL_ARRAY_BUFFER, door_buffer.nbytes, door_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, door_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, door_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, door_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(6)

# window
glBindVertexArray(vertexArrayObject[6])

glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[6])
glBufferData(GL_ARRAY_BUFFER, window_buffer.nbytes, window_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, window_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, window_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, window_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(7)

# hotel
glBindVertexArray(vertexArrayObject[7])

glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[7])
glBufferData(GL_ARRAY_BUFFER, hotel_buffer.nbytes, hotel_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, hotel_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, hotel_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, hotel_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(8)

# window2
glBindVertexArray(vertexArrayObject[8])

glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[8])
glBufferData(GL_ARRAY_BUFFER, window2_buffer.nbytes, window2_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, window2_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, window2_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, window2_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(9)

# hotel2
glBindVertexArray(vertexArrayObject[9])

glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[9])
glBufferData(GL_ARRAY_BUFFER, hotel2_buffer.nbytes, hotel2_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, hotel2_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, hotel2_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, hotel2_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(10)

# hotel3
glBindVertexArray(vertexArrayObject[10])

glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[10])
glBufferData(GL_ARRAY_BUFFER, hotel3_buffer.nbytes, hotel3_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, hotel3_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, hotel3_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, hotel3_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(11)

# solarpanel leg
glBindVertexArray(vertexArrayObject[11])

glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[11])
glBufferData(GL_ARRAY_BUFFER, leg_buffer.nbytes, leg_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, leg_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, leg_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, leg_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(12)



# sun
glBindVertexArray(vertexArrayObject[12])

glBindBuffer(GL_ARRAY_BUFFER, vertexBufferObject[12])
glBufferData(GL_ARRAY_BUFFER, sun_buffer.nbytes, sun_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, sun_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, sun_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, sun_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(13)






texturesList = glGenTextures(12)
texture_loader("road.png", texturesList[0])
texture_loader("floor.jpeg", texturesList[1])
texture_loader("solarpanel.jpg", texturesList[2])
texture_loader("tree.jpeg", texturesList[3])
texture_loader("home.jpeg", texturesList[4])
texture_loader("door.jpeg", texturesList[5])
texture_loader("window.jpeg", texturesList[6])
texture_loader("black.png", texturesList[7])
texture_loader("wall4.jpeg", texturesList[8])
texture_loader("wall5.jpeg", texturesList[9])
texture_loader("sun.jpeg", texturesList[10])
texture_loader("yellow.jpeg", texturesList[11])

glUseProgram(shader_forcompile)
glClearColor(0, 0.1, 0.1, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)
road_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
floor_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
solarpanel_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
tree_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
home_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
door_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
window_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
hotel_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
window2_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
hotel2_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
hotel3_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
leg_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
sun_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))

view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 8]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))

model_loc = glGetUniformLocation(shader_forcompile, "model")
proj_loc = glGetUniformLocation(shader_forcompile, "projection")
view_loc = glGetUniformLocation(shader_forcompile, "view")

glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    rot_y = pyrr.Matrix44.from_y_rotation(0.1 * glfw.get_time())
    model = pyrr.matrix44.multiply(rot_y, road_pos)

    glBindVertexArray(vertexArrayObject[0])
    glBindTexture(GL_TEXTURE_2D, texturesList[0])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(road_verts))

    model = pyrr.matrix44.multiply(rot_y, floor_pos)
    glBindVertexArray(vertexArrayObject[1])
    glBindTexture(GL_TEXTURE_2D, texturesList[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(floor_verts))

    model = pyrr.matrix44.multiply(rot_y, solarpanel_pos)
    glBindVertexArray(vertexArrayObject[2])
    glBindTexture(GL_TEXTURE_2D, texturesList[2])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(solarpanel_verts))

    model = pyrr.matrix44.multiply(rot_y, tree_pos)
    glBindVertexArray(vertexArrayObject[3])
    glBindTexture(GL_TEXTURE_2D, texturesList[3])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(tree_verts))

    model = pyrr.matrix44.multiply(rot_y, home_pos)
    glBindVertexArray(vertexArrayObject[4])
    glBindTexture(GL_TEXTURE_2D, texturesList[4])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(home_indices))

    model = pyrr.matrix44.multiply(rot_y, window_pos)
    glBindVertexArray(vertexArrayObject[5])
    glBindTexture(GL_TEXTURE_2D, texturesList[5])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(window_indices))

    model = pyrr.matrix44.multiply(rot_y, window_pos)
    glBindVertexArray(vertexArrayObject[6])
    glBindTexture(GL_TEXTURE_2D, texturesList[11])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(window_indices))

    model = pyrr.matrix44.multiply(rot_y, hotel_pos)
    glBindVertexArray(vertexArrayObject[7])
    glBindTexture(GL_TEXTURE_2D, texturesList[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(hotel_indices))

    model = pyrr.matrix44.multiply(rot_y, window2_pos)
    glBindVertexArray(vertexArrayObject[8])
    glBindTexture(GL_TEXTURE_2D, texturesList[7])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(window2_indices))

    model = pyrr.matrix44.multiply(rot_y, hotel2_pos)
    glBindVertexArray(vertexArrayObject[9])
    glBindTexture(GL_TEXTURE_2D, texturesList[9])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(hotel2_indices))

    glBindVertexArray(vertexArrayObject[10])
    glBindTexture(GL_TEXTURE_2D, texturesList[8])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(hotel3_indices))

    glBindVertexArray(vertexArrayObject[11])
    glBindTexture(GL_TEXTURE_2D, texturesList[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(leg_indices))

    glBindVertexArray(vertexArrayObject[12])
    glBindTexture(GL_TEXTURE_2D, texturesList[10])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(sun_indices))

    glfw.swap_buffers(window)

glfw.terminate()
