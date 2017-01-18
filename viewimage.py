from PIL import Image as PILImage
from io import BytesIO
from IPython import display

#load the image from local system
im = PILImage.open("input.ppm")
im.show()

#load convert and display
#b = BytesIO()
#im.save(b, format='png')
#im_data = b.getvalue()
#display.Image(data=im_data, format='png', embed=True)