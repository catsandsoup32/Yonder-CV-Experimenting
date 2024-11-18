from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt

pipeline = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")
pipeline.load_textual_inversion(r"C:\Users\edmun\Desktop\VSCode Projects\Yonder\Yonder-CV-Experimenting\synthetic_pipeline\textual_inversion_weights\bottle1_step3000_not_good.safetensors")
image = pipeline("a photo of a <wide-mouth-bottle>", num_inference_steps=50).images[0]
plt.imshow(image)
plt.show()