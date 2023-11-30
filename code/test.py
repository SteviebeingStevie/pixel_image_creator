import imagineer as img

image = img.load("images/before/proxy-image.jpeg")

print(img.information(image))



img.show(img.resize_by_ratio(image, 4))
