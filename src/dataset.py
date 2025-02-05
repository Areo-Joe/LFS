import torch
from torch.utils.data import Dataset
from torch import tensor


# 对于一段文本，构造用来训练的 DataSet，问题 => 答案
# 滑动窗口
class GPTDataSet(Dataset):
    def __init__(self, txt, tokenizer, window_size, step):
        self.input_ids = []
        self.target_ids = []

        token_ids = tokenizer.encode(txt)
        for i in range(
            0, len(token_ids) - window_size + 1 - 1, step
        ):  # 正常滑动窗口的下标最大为 len(token_ids) - window_size + 1，但是对于每个 input 的滑动窗口，都要整体向后滑动 1 格来取到 target 的滑动窗口，所以要减去 1 格留 buffer
            input_chunk = token_ids[i : i + window_size]
            target_chunk = token_ids[i + 1 : i + window_size + 1]
            self.input_ids.append(input_chunk)
            self.target_ids.append(target_chunk)

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.target_ids[idx]
