"""
Copyright (C) 2024, Amazon.com. All Rights Reserved

Stable Diffusion Attention NKI kernel implementation.

"""

# NKI_EXAMPLE_32_BEGIN
import torch
from torch_xla.core import xla_model as xm

from sd_attention_nki_kernels import fused_self_attn_for_SD_small_head_size_decode, fused_att_interface_decode


if __name__ == "__main__":

  device = xm.xla_device()

  def cpu_golden_attn(q, k, v, mask=None):
      softmax_scale = 1 / (q.size(-1) ** 0.5)
      q_scaled = q * softmax_scale
      raw_score = torch.matmul(q_scaled, k.transpose(-1, -2))

      if mask is not None:
        raw_score = raw_score.masked_fill(~mask, -9984.0)

      norm_score = torch.nn.functional.softmax(raw_score, dim=-1)

      return torch.matmul(norm_score, v)

  q_tensor = torch.rand((2, 4, 1, 128), dtype=torch.float32).to(device=device)
  k_tensor = torch.rand((2, 4, 4000, 128), dtype=torch.float32).to(device=device)
  v_tensor = torch.rand((2, 4, 4000, 128), dtype=torch.float32).to(device=device)
  mask = torch.rand(1, 4000) < 0.5
  mask = mask.to(device=device) 

  output_nki = fused_att_interface_decode(q_tensor, k_tensor, v_tensor, att_mask=mask.view(1, 1, 1, 4000))

  output_torch = cpu_golden_attn(q_tensor, k_tensor, v_tensor, mask)

  allclose = torch.allclose(output_torch, output_nki, atol=0.03, rtol=0.01)

  if allclose:
    print("NKI and Torch match")
  else:
    print("NKI and Torch differ")

  assert allclose
  # NKI_EXAMPLE_32_END
