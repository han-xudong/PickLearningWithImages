import os
import sys
import tensorflow.compat.v1 as tf
import PIL
import os
import wget


def download(m):
  if m not in os.listdir():
    # !wget https://storage.googleapis.com/cloud-tpu-checkpoints/efficientdet/coco/{m}.tar.gz
    dl_url = 'https://storage.googleapis.com/cloud-tpu-checkpoints/efficientdet/coco/'+m+'.tar.gz'
    wget.download(dl_url)
    !tar zxf {m}.tar.gz
  ckpt_path = os.path.join(os.getcwd(), m)
  return ckpt_path



if __name__ == '__main__':
    MODEL = 'efficientdet-d0'  #@param

    # Download checkpoint.
    ckpt_path = download(MODEL)
    print('Use model in {}'.format(ckpt_path))

    # Prepare image and visualization settings.
    image_url =  'https://user-images.githubusercontent.com/11736571/77320690-099af300-6d37-11ea-9d86-24f14dc2d540.png'#@param
    image_name = 'test0.png' #@param
    # wget.download(image_url, 'img.png')

    img_path = os.path.join(os.getcwd(), 'test0.png')

    min_score_thresh = 0.35  #@param
    max_boxes_to_draw = 200  #@param
    line_thickness =   2#@param


    # Get the largest of height/width and round to 128.
    image_size = max(PIL.Image.open(img_path).size)

    # In case you need to specify different image size or batch size or #boxes, then
    # you need to export a new saved model and run the inferernce.

    serve_image_out = 'serve_image_out'
    # !mkdir {serve_image_out}
    saved_model_dir = 'savedmodel'
    # !rm -rf {saved_model_dir}

    # # Step 1: export model
    # !python model_inspect.py --runmode=saved_model \
    #   --model_name=efficientdet-d0 --ckpt_path=efficientdet-d0 \
    #   --hparams="image_size=1920x1280" --saved_model_dir={saved_model_dir}

    # Step 2: do inference with saved model.
    !python model_inspect.py --runmode=saved_model_infer \
    --model_name=efficientdet-d0 --saved_model_dir={saved_model_dir} \
    --input_image=test0.png --output_image_dir={serve_image_out} \
    --min_score_thresh={min_score_thresh}  --max_boxes_to_draw={max_boxes_to_draw} \

    from IPython import display
    display.display(display.Image(os.path.join(serve_image_out, '0.jpg')))