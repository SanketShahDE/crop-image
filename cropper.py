from PIL import Image

def crop_image(input_path, output_path, x, y, w, h):
    """
    Crop an image at specific pixel coordinates.

    Parameters:
        input_path (str): Path to the input image.
        output_path (str): Path to save the cropped image.
        x (int): Top-left x coordinate.
        y (int): Top-left y coordinate.
        w (int): Width of the crop.
        h (int): Height of the crop.
    """
    img = Image.open(input_path)
    crop_box = (x, y, x + w, y + h)
    cropped_img = img.crop(crop_box)
    cropped_img.save(output_path)
    print(f"Cropped image saved to {output_path}")


if __name__ == "__main__":
    #change coordinated here determined from pixspy.com
    MOUTH_X = 485
    MOUTH_Y = 100
    MOUTH_WIDTH = 390
    MOUTH_HEIGHT = 550

    crop_image("7_mouth_closed.png", "mouth_closed.png", MOUTH_X, MOUTH_Y, MOUTH_WIDTH, MOUTH_HEIGHT)
    crop_image("7_mouth_open.png", "mouth_open.png", MOUTH_X, MOUTH_Y, MOUTH_WIDTH, MOUTH_HEIGHT)
    crop_image("7_mouth_half.png", "mouth_half.png", MOUTH_X, MOUTH_Y, MOUTH_WIDTH, MOUTH_HEIGHT)
