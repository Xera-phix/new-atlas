from geoclip import GeoCLIP
from PIL import Image
from io import BytesIO

model = GeoCLIP().to("cuda")

def get_coordinates_from_image(image_bytes: bytes):
    """
    Takes image bytes and returns predicted coordinates.
    """
    try:
        image = Image.open(BytesIO(image_bytes))
        # The model expects a list of images
        predictions = model.predict([image])
        if predictions and len(predictions) > 0:
            prediction = predictions[0]
            return {"latitude": prediction['lat'], "longitude": prediction['lon']}
        return None
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

