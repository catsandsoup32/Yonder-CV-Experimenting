# Yonder-CV-Experimenting

# 11-14-2024
Started work on generating synthetic data with the following pipeline:
- Use Stable Diffusion to generate a larger dataset with images in wide variety of contexts
- And use Hugging Face's [textual inversion API](https://huggingface.co/docs/diffusers/main/en/training/text_inversion) to add the wide-mouth bottle and mallet as custom tokens
- Chose [textual inversion](https://arxiv.org/pdf/2208.01618) over LoRA and Dreambooth because small files, local training, and the fact that bottle and mallet are already common objects
- Use [Grounding Dino](https://github.com/IDEA-Research/GroundingDINO) to automatically annotate each image

