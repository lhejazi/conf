from PIL import Image
from math import ceil

# resize new image to provided new_width using aspect ratio
def size_image(image, new_width=500):
    original_width, original_height = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio*new_width)
    return image.resize((new_width, new_height))

# assigns a shade on the gray scale to an ascii value, determined by 
# provided character set
def shade_to_ascii(chars):
    d = {}
    for x in xrange(0,256):
        char_buckets = int((ceil(256.0/len(chars))))
        d[x] = chars[x/char_buckets]
    return d

# The bellow set of chars gives you a really sharp ascii photo
chars = ['#','@','%','0','M','8','B','&','$','o','r','=','*','+','x','|',':','\"',',','.']
# All of the chars in "The Americans, I'll be yours"
chars1 = list("#MNHAERSCTI!lbhmaeosucntri*+:\',.")

asciis = shade_to_ascii(chars1)

# Assign chars to different colored pixels
def pixels_to_ascii(image_data, width):
    new_image = []
    for x in xrange(0, len(image_data), width):
        tmp = []
        for y in xrange(x, width+x):
            tmp.append(asciis[image_data[y]])
        new_image.append("".join(tmp))
    return "\n".join(new_image)

# Save image by writing data to file
def write_to_file(new_image, filename):
    with open(filename, 'wb') as fp:
        fp.write(new_image)

if __name__ == '__main__':
    # To generate ascii art from a photo, run the following:
    # $ python ascii.py <input-image> [output-filename] [width]
    #
    #   ARGUMENTS:
    #       input-image(required):      the image file you use to make ascii art
    #
    #       output-filename(optional):  the filename you'll give your new ascii art. By 
    #                                   default 'out.txt' is used
    #
    #       width(optional):            an adjusted width of your image. The height will be adjusted
    #                                   to specified width using the aspect ratio. Original image
    #                                   height is used by default

    import sys
    
    filename = sys.argv[1]
    outfile = sys.argv[2] if len(sys.argv) > 2 else 'out.txt'

    # Convert to grayscale
    image = Image.open(filename).convert('L')

    # resize if necessary
    new_width = int(sys.argv[3]) if len(sys.argv) > 3 else image.size[0]
    i = size_image(image, new_width)
    width, height = i.size

    # get raw grayscale value of data of data
    image_data = list(i.getdata())

    # turn pixels into ascii
    new_image = pixels_to_ascii(image_data, width)

    # write out to file
    write_to_file(new_image, outfile)

    print "Ascii photo successfully printed to", outfile



