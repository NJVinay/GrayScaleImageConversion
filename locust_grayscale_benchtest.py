from locust import HttpUser, task, between

class ImageProcessingUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_grayscale_conversion(self):
        with open("test_image.png", "rb") as f:
            img_data = f.read()

        self.client.post("/convert-to-grayscale", files={"file": ("test_image.png", img_data, "image/png")})
