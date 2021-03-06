import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms


def load_mnist(bsize):
    
    # data_loader
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
        ])
    
    dataset = datasets.MNIST(root = '../data/',
                         transform=transform,
                          download = True)


    loader = torch.utils.data.DataLoader(dataset = dataset,
                                     batch_size = bsize,
                                     shuffle = True)

    return loader