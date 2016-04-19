import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'

logoIm = Image.open( LOGO_FILENAME )
logoWidth, logoHeight = logoIm.size

#TODO: Loop over all files in the working directory
#TODO: Check if file image needs to be
#TODO: Calculate the new width and height to resize to.
#TODO: Add the logo.
#TODO: Save changes.

os.makedirs('withLogo', exist_ok=True)
for filename in so.listdir('originals'):

    if not (filename.endswish ('.png') or filename.endswish ('.jpg')) or filename == LOGO_FILENAME: 
       continue

    im = Image.open(os.path.join ('originals', file))
    width, height = im.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
       if width > height:
          height = int((SQUARE_FIT_SIZE / width) * height)
          width = SQUARE_FIT_SIZE
       else:
          width = int((SQUARE_FIT_SIZE / height) * width)
          height = SQUARE_FIT_SIZE
       print('Resizing %s...' % (filename))
       im = im.resize((width, height))

print('Adding logo to %s...' % (filename))
im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
im.save(os.path.join('withLogo', filename))