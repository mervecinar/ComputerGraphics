import re
import numpy
from PIL import Image
from matplotlib import pyplot as plt
def pbm2numpy(filename):

    fin = None
    debug = True

    try:
        fin = open(filename, 'r')

        while True:
            header = fin.readline().strip()
            if header.startswith('#'):
                continue
            elif header == 'P3':
                break
            elif header == 'P6':
                assert False, 'Raw PBM reading not implemented yet'
            else:

                if debug:
                    print ('Display:', header)
                return None

        rows, cols = 0, 0
        while True:
            header = fin.readline().strip()
            if header.startswith('#'):
                continue

            match = re.match('^(\d+) (\d+)$', header)
            if match == None:
                if debug:
                    print ('Bad size:', repr(header))
                return None

            cols, rows = match.groups()
            break

        rows = int(rows)
        cols = int(cols)

        assert (rows, cols) != (0, 0)

        if debug:
            print ('Rows: %d, cols: %d' % (rows, cols))

        #
        # Initialise a 2D numpy array
        #
        result = numpy.zeros((rows, cols), numpy.int8)

        pxs = []

        #
        # Read to EOF.
        #
        while True:
            line = fin.readline().strip()
            if line == '':
                break

            for c in line:
                if c == ' ':
                    continue

                pxs.append(int(c))

        if len(pxs) != rows*cols:
            if debug:
                print( 'Insufficient image data:', len(pxs))
            return None

        for r in range(rows):
            for c in range(cols):
                #
                # Index into the numpy array and set the pixel value.
                #
                result[r, c] = pxs[r*cols + c]

        return result
    finally:
        if fin != None:
            fin.close()
        fin = None
    return None
im = Image.open("ppmpicture.ppm")
im.save("newjpgFile.jpg")
imgplot = plt.imshow(im)
plt.show()
pbm2numpy('ppmpicture.ppm')