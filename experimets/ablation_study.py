from subprocess import run
import mlflow


models_set = [
    # {'model': 'vgg16', 'bs': 128, 'dev': [5]},
    # {'model': 'vgg16_bn', 'bs': 128, 'dev': [5]},
    # {'model': 'inception_v3', 'bs': 256, 'dev': [5]},
    # {'model': 'alexnet', 'bs': 512, 'dev': [5]},
    {'model': 'resnet18', 'bs': 512, 'dev': [5]},
    # {'model': 'resnet50', 'bs': 512, 'dev': [5]},
    # {'model': 'resnet101', 'bs': 512, 'dev': [5]}
]

mset = models_set[0]
exp_name = 'res18_u_eval_8bit'
bits_act = 8

qtypes = ['aciq_laplace', 'aciq_gaus', 'mse_direct', 'mse_decomp', 'mse_quant_est', 'max_static']

for qt in qtypes:
    run(["python", "quantization/posttrainng/cnn_classifier_inference.py"] + ['-a', mset['model']] + ['-b', str(mset['bs'])]
        + ['--dataset', 'imagenet'] + ['--gpu_ids'] + " ".join(map(str, mset['dev'])).split(" ")
        + "--pretrained --custom_resnet -sh -q".split(" ") + ['-exp', exp_name]
        + ['--qtype', qt] + ['-ba', str(bits_act)]
        )