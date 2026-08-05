"""Machine Learning Domain Content Provider - 365 Days Curriculum."""

from typing import List, Tuple
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import TopicContent


class MLTopicProvider(BaseTopicProvider):
    """Generates rich Machine Learning educational content for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="Machine Learning")
        self._curriculum: List[Tuple[str, str, str, str, List[str]]] = [
            # Day 1
            (
                "Scaled Dot-Product Attention & Multi-Head Attention in Transformers",
                "Advanced",
                "Self-attention allows sequences to dynamically compute token dependency weights based on Query (Q), Key (K), and Value (V) projections: $Attention(Q,K,V) = softmax(\\frac{QK^T}{\\sqrt{d_k}})V$.",
                """import torch
import torch.nn as nn
import torch.nn.functional as F

class ScaledDotProductAttention(nn.Module):
    def __init__(self, d_k: int):
        super().__init__()
        self.d_k = d_k

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, mask: torch.Tensor = None) -> torch.Tensor:
        # q, k, v shape: (batch_size, num_heads, seq_len, d_k)
        scores = torch.matmul(q, k.transpose(-2, -1)) / (self.d_k ** 0.5)
        
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
            
        attn_weights = F.softmax(scores, dim=-1)
        output = torch.matmul(attn_weights, v)
        return output, attn_weights

# Instantiate for key dimension = 64
attn_layer = ScaledDotProductAttention(d_k=64)
q = k = v = torch.randn(2, 4, 10, 64)  # Batch 2, 4 Heads, Seq Len 10, Dim 64
out, weights = attn_layer(q, k, v)
print(f"Output Tensor Shape: {out.shape}")""",
                [
                    "Scaling factor $\\sqrt{d_k}$ prevents dot products from pushing softmax into regions with vanishing gradients.",
                    "Multi-Head Attention enables joint processing of information from distinct representation subspaces.",
                    "Causal masking prevents tokens from attending to future positions during autoregressive decoding."
                ]
            )
        ]

    def get_topic(self, day_num: int) -> TopicContent:
        day_idx = self.normalize_day(day_num)
        if day_idx <= len(self._curriculum):
            title, diff, concept, code, takeaways = self._curriculum[day_idx - 1]
        else:
            topics = [
                "AdamW Optimizer with Decoupled Weight Decay Mechanics",
                "Low-Rank Adaptation (LoRA) for Fine-Tuning LLMs",
                "Quantization Aware Training (QAT) vs Post-Training Quantization (PTQ)",
                "Gradient Boosting Decision Trees (LightGBM vs XGBoost vs CatBoost)",
                "Kernel Methods & Support Vector Machines (SVM) Dual Formulation",
                "Convolutional Neural Network Architectures (ResNet Residual Connections)",
                "Autoencoders & Variational Latent Space Regularization",
                "Evaluating Classification Models: ROC-AUC, PR-AUC, and F1-Score",
                "Reinforcement Learning with Proximal Policy Optimization (PPO)",
                "MLOps Model Lineage Tracking & Registry with MLflow"
            ]
            selected = topics[(day_idx - 1) % len(topics)]
            title = f"{selected} (Day {day_idx})"
            diff = "Advanced" if day_idx % 2 == 0 else "Intermediate"
            concept = f"Mathematical and architectural deep dive into {selected} for production ML engineering."
            code = f"""# ML Pipeline Day {day_idx}: {selected}
import numpy as np

def compute_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    eps = 1e-15
    y_pred = np.clip(y_pred, eps, 1 - eps)
    # Binary cross entropy
    return -float(np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)))

y_t = np.array([1, 0, 1, 1])
y_p = np.array([0.9, 0.1, 0.8, 0.95])
print(f"Loss for {selected}: {{compute_loss(y_t, y_p):.4f}}")"""
            takeaways = [
                f"Master key principles of {selected}.",
                "Prevent overfitting using dropout, weight decay, and cross-validation.",
                "Track model metrics and feature drift in production environments."
            ]

        return TopicContent(
            domain=self.domain_name,
            topic_name=title,
            difficulty=diff,
            concept_summary=concept,
            code_example=code,
            key_takeaways=takeaways
        )
