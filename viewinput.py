from PIL import Image as PILImage
from io import BytesIO
from IPython import display

#load the image
im = PILImage.open("input.ppm")
#display (assuming x server is configured and session has X forwarding)
im.show()
