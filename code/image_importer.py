from PIL import Image
from matplotlib import pyplot as plt

def load_image(image_path):
    """
    Lädt ein Bild von einem Pfad und gibt das Bildobjekt zurück.
    
    Arguments:
    image_path -- Pfad des Bildes
    """
    try:
        # Bild einlesen
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        print("Datei nicht gefunden.")
        return None
    except Exception as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        return None

def information_image(image_object):
    """
    Takes an image as input and returns the Format, Color-Code and the size as a dictionary.
    
    Keyword arguments:
    image_object -- loaded image object
    """

    # Dateiformat abrufen
    image_format = image_object.format
    # Farbkodierung abrufen
    image_color_code = image_object.mode
    # Bildmasse erhalten
    width, height = image_object.size
    return {
        "format" : image_format,
        "color_code" : image_color_code,
        "size [x, y]" : (width, height)
        }

def show_image(image_object):
    """
    Displays an image.

    Keyword arguments:
    image_object -- loaded image object
    """
    plt.imshow(image_object)
    plt.axis('off')
    plt.show()

def resize_image(image_object, width, height):
    """
    Resize an input image to a certain size.

    Keyword arguments:
    image_object -- loaded image object
    width -- new width in pixels
    height -- new height in pixels
    """
    return image_object.resize((width, height))

def resize_by_ratio(image_object, percentage):
    """
    Resize an input image by percentage.
    Examples: 
        150 % = Upscale by 50 %
        100 % = same size
        50 % = Downscale by 50 %

    Keyword arguments:
    image_object -- loaded image object
    percentage -- [%] percentage number for scaling image 
    """
    
    width, height = image_object.size
    ratio = width / height

    new_width = round(percentage / 100 * width)
    new_height = round(new_width / ratio)
    
    return resize_image(loaded_image, new_width, new_height)

   




if __name__ == '__main__':
    pass

