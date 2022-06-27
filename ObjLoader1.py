import numpy as np
class Objfileexporter:
    buf = []

    @staticmethod
    def search_data(data_values, coordinates, skip, typ):
        for vertext in data_values:
            if vertext == skip:
                continue
            if typ == 'float':
                coordinates.append(float(vertext))
            elif typ == 'int' and vertext != '':
                coordinates.append(int(vertext) - 1)

    @staticmethod  
    def sorted_vertex(vrtx_data, vertices, textu, norm):
        for i, ind in enumerate(vrtx_data):
            if i % 3 == 0:  
                start = ind * 3
                end = start + 3
                Objfileexporter.buf.extend(vertices[start:end])
            elif i % 3 == 1:  
                start = ind * 2
                end = start + 2
                Objfileexporter.buf.extend(textu[start:end])
            elif i % 3 == 2:  
                start = ind * 3
                end = start + 3
                Objfileexporter.buf.extend(norm[start:end])

    @staticmethod  # TODO 
    def create_unsorted_vertex_buffer(indices_data, vertices, textures, normals):
        num_verts = len(vertices) // 3

        for i1 in range(num_verts):
            start = i1 * 3
            end = start + 3
            Objfileexporter.buf.extend(vertices[start:end])

            for i2, data in enumerate(indices_data):
                if i2 % 3 == 0 and data == i1:
                    start = indices_data[i2 + 1] * 2
                    end = start + 2
                    Objfileexporter.buf.extend(textures[start:end])

                    start = indices_data[i2 + 2] * 3
                    end = start + 3
                    Objfileexporter.buf.extend(normals[start:end])

                    break

    @staticmethod
    def show_data(buffer):
        for i in range(len(buffer) // 8):
            start = i * 8
            end = start + 8
            print(buffer[start:end])

    @staticmethod
    def model_load(file, sorted=True):
        vert_coords = []  
        tex_coords = []  
        norm_coords = [] 

        all_vrtxs = []  
        vrtxs = []  

        with open(file, 'r') as f:
            straight_line = f.readline()
            while straight_line:
                results = straight_line.split()
                if results[0] == 'v':
                    Objfileexporter.search_data(results, vert_coords, 'v', 'float')
                elif results[0] == 'vt':
                    Objfileexporter.search_data(results, tex_coords, 'vt', 'float')
                elif results[0] == 'vn':
                    Objfileexporter.search_data(results, norm_coords, 'vn', 'float')
                elif results[0] == 'f':
                    for result in results[1:]:
                        val = result.split('/')
                        Objfileexporter.search_data(val, all_vrtxs, 'f', 'int')
                        vrtxs.append(int(val[0]) - 1)

                straight_line = f.readline()

        if sorted:
           
            Objfileexporter.sorted_vertex(all_vrtxs, vert_coords, tex_coords, norm_coords)
        else:
            
            Objfileexporter.create_unsorted_vertex_buffer(all_vrtxs, vert_coords, tex_coords, norm_coords)

        buffer = Objfileexporter.buf.copy()
        Objfileexporter.buf = []  

        return np.array(vrtxs, dtype='uint32'), np.array(buffer, dtype='float32')
