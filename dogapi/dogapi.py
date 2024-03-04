import requests
"""from PIL import Image
from io import BytesIO"""


for _ in range(11):
    
    response=requests.get("https://dog.ceo/api/breeds/image/random")
    
    image_url=response.json()["message"]
    
    image_response=requests.get(image_url)
    
    file=open(f"dog{_}.jpg","wb")
    
    file.write(image_response.content)
    
    #Image.open(BytesIO(image_response.content))
    file.close()
print("===over====")