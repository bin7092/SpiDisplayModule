import numpy as np
from PIL import Image


def scale_and_crop_image(image, target_width, target_height):
    """Scale and crop the image to fit the target dimensions."""
    try:
        # Calculate the scaling ratio
        ratio_width = target_width / image.width
        ratio_height = target_height / image.height
        scale_ratio = min(ratio_width, ratio_height)

        # Calculate the new size after scaling
        new_size = (int(image.width * scale_ratio), int(image.height * scale_ratio))

        # Resize the image using LANCZOS resampling
        # image = image.resize(new_size, Image.Resampling.LANCZOS)
        image = image.resize(new_size, Image.ANTIALIAS)

        # Calculate the position for cropping
        crop_box = (
            (new_size[0] - target_width) // 2,
            (new_size[1] - target_height) // 2,
            (new_size[0] + target_width) // 2,
            (new_size[1] + target_height) // 2
        )

        # Crop the image
        image = image.crop(crop_box)
        return image

    except Exception as e:
        print(f"An error occurred while scaling and cropping the image: {e}")
        return None


def convert_image_to_pix(image):
    """Convert PIL Image to pixel list with exception handling."""
    try:
        # Ensure the image is in RGB format
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Get image dimensions
        imwidth, imheight = image.size

        # Convert image to numpy array
        img = np.asarray(image)

        # Create a pixel array with RGB565 format
        pix = np.zeros((imheight, imwidth, 2), dtype=np.uint8)
        pix[..., [0]] = np.add(np.bitwise_and(img[..., [0]], 0xF8), np.right_shift(img[..., [1]], 5))
        pix[..., [1]] = np.add(np.bitwise_and(np.left_shift(img[..., [1]], 3), 0xE0), np.right_shift(img[..., [2]], 3))

        # Flatten the pixel array to a list
        return pix.flatten().tolist()

    except Exception as e:
        print(f"An error occurred while converting the image to pixel list: {e}")
        return None


def rotate_image(image, rotation_angle):
    """Rotate the given image by the specified rotation angle."""
    try:
        rotated_image = image.rotate(rotation_angle, expand=True)
        return rotated_image
    except Exception as e:
        print(f"An error occurred while rotating the image: {e}")
        return None
