from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt

pipeline = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")
pipeline.load_textual_inversion(r"C:\Users\edmun\Desktop\VSCode Projects\Yonder\Yonder-CV-Experimenting\synthetic_pipeline\textual_inversion_weights\mallet1_step500.safetensors")
image = pipeline("a <orange-mallet> in a desert", num_inference_steps=50).images[0]
plt.imshow(image)
plt.show()