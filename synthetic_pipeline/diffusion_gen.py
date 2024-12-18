from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt

pipeline = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")
pipeline.load_textual_inversion(
    r"C:\Users\edmun\Desktop\VSCode Projects\Yonder\Yonder-CV-Experimenting\synthetic_pipeline\textual_inversion_weights\learned_embeds-steps-3000.safetensors",
    mean_resizing = True
)

image = pipeline(
    "a photo of a <orange-mallet>", 
    negative_prompt="stick, gun, close-up, green", 
    num_inference_steps=50,
    #generator=torch.Generator("cuda").manual_seed(80)
    ).images[0]
plt.imshow(image)
plt.show()