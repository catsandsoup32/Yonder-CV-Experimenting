# Yonder-CV-Experimenting

# 11-16-2024
Used Hugging Face's example script to fine-tune Stable Diffusion 1.5 with new \<wide-mouth-bottle\> and \<orange-mallet\> tokens.
- Initial training run on the wide-mouth bottle went really poorly because of large backgrounds, model doing bad with "nalgene" text, and the bottle having inconsistent shape/color
- Second run with orange mallet is not as bad, but still lots of room for improvement
- Stable Diffusion 3 and 3.5 use a transformer instead of a U-Net, requires some modification of the Hugging Face example script
- Stable Diffusion 2 uses a U-Net, but online consensus seems to be that 1.5 is actually mostly better and easier to prompt
- To-do: experiment with modifying the prompt templates and using example images with a smaller mallet 

# 11-15-2024
Trained YOLO on original Roboflow dataset to get a baseline.
- From confusion matrix, really bad at recognizing backgrounds w/o object 
- Very likely because only 60 / 2000 images are null class

# 11-14-2024
Started work on generating synthetic data with the following pipeline:
- Use Stable Diffusion to generate a larger dataset with images in wide variety of contexts
- And use Hugging Face's [textual inversion API](https://huggingface.co/docs/diffusers/main/en/training/text_inversion) to add the wide-mouth bottle and mallet as custom tokens
- Chose [textual inversion](https://arxiv.org/pdf/2208.01618) over LoRA and Dreambooth because small files, local training, and the fact that bottle and mallet are already common objects
- Use [Grounding Dino](https://github.com/IDEA-Research/GroundingDINO) to automatically annotate each image

