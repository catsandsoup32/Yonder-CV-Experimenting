from diffusers import StableDiffusionPipeline
import torch

pipeline = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")
pipeline.load_textual_inversion(r"C:\Users\edmun\VSC_DIRS\Yonder-CV-Experimenting\synthetic_pipeline\textual_inversion_weights\bottle1_step3000_not_good.safetensors")
image = pipeline("a <wide-mouth-bottle> in a desert", num_inference_steps=50).images[0]
image.save("bottle-train.png")