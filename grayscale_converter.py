from PIL import Image
import io

def convert_to_grayscale(image_bytes):
    # Load image from bytes
    image = Image.open(io.BytesIO(image_bytes))
    # Convert to grayscale
    grayscale_image = image.convert("L")
    # Save back to bytes
    output = io.BytesIO()
    grayscale_image.save(output, format="PNG")
    return output.getvalue()

# Example usage:
# with open('input.png', 'rb') as f:
#     img_bytes = f.read()
# gray_bytes = convert_to_grayscale(img_bytes)
# with open('output.png', 'wb') as f:
#     f.write(gray_bytes)
