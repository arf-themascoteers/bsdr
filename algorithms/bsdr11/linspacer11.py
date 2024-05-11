import torch


def get_points(low, up, target_size, group_size):
    t = torch.linspace(low, up, 1000)
    anchors = torch.linspace(torch.min(t), torch.max(t), target_size+1)
    all_points = []
    for i in range(target_size):
        points = torch.linspace(anchors[i], anchors[i+1], group_size)
        for p in points:
            all_points.append(p)
    all_points = torch.tensor([all_points[i::target_size] for i in range(target_size)])
    all_points = all_points.view(-1)
    return all_points


if __name__ == "__main__":
    print(get_points(0.001, 0.99, 5, 10))