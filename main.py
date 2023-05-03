from defisheye import Defisheye

dtype = 'linear'
format = 'fullframe'
fov = 220
pfov = 120

img = "fisheyeExampleImage.jpg"
img_out = f"resultFishEye.jpg"

obj = Defisheye(img, dtype=dtype, format=format, fov=fov, pfov=pfov)

# To save image locally
obj.convert(outfile=img_out)

# To use the converted image in memory
new_image = obj.convert()