# import gradio as gr

# https://gradio.app/quickstart/
# http://localhost:7860 
# def sketch_recognition(img):
#     pass# Implement your sketch recognition model here...

# gr.Interface(fn=sketch_recognition, inputs="sketchpad", outputs="label").launch()

# def greet(name):
#     return "Hello " + name + "!"

# demo = gr.Interface(fn=greet, inputs="text", outputs="text")
# demo.launch()

# def greet(name):
#     return "Hello " + name + "!"

# demo = gr.Interface(
#     fn=greet,
#     inputs=gr.Textbox(lines=2, placeholder="Name Here..."),
#     outputs="text",
# )
# demo.launch()


# import numpy as np
# import gradio as gr

# def sepia(input_img):
#     sepia_filter = np.array([
#         [0.393, 0.769, 0.189], 
#         [0.349, 0.686, 0.168], 
#         [0.272, 0.534, 0.131]
#     ])
#     sepia_img = input_img.dot(sepia_filter.T)
#     sepia_img /= sepia_img.max()
#     return sepia_img

# demo = gr.Interface(sepia, gr.Image(shape=(200, 200)), "image")
# demo.launch()


import gradio as gr
import requests
from PIL import Image
from torchvision import transforms

# Download human-readable labels for ImageNet.
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def predict(inp):
  inp = transforms.ToTensor()(inp).unsqueeze(0)
  with torch.no_grad():
    prediction = torch.nn.functional.softmax(model(inp)[0], dim=0)
    confidences = {labels[i]: float(prediction[i]) for i in range(1000)}    
  return confidences
  
gr.Interface(fn=predict, 
             inputs=gr.Image(type="pil"),
             outputs=gr.Label(num_top_classes=3)).launch()
             # examples=["lion.jpg", "cheetah.jpg"]