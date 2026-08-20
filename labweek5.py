{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOjZl9QIahxMy0C3U1fdDoU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ming-Silpakorn030/lab-ai-69/blob/main/labweek5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UpJNRJskOxlG",
        "outputId": "fa7b3ee9-b6f4-4044-9ee7-2b93c2afab1a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ก้าว  0  x =  8.0000  ความสูง =  64.0000\n",
            "ก้าว  1  x =  6.4000  ความสูง =  40.9600\n",
            "ก้าว  2  x =  5.1200  ความสูง =  26.2144\n",
            "ก้าว  3  x =  4.0960  ความสูง =  16.7772\n",
            "ก้าว  5  x =  2.6214  ความสูง =   6.8719\n",
            "ก้าว 10  x =  0.8590  ความสูง =   0.7379\n",
            "ก้าว 20  x =  0.0922  ความสูง =   0.0085\n"
          ]
        }
      ],
      "source": [
        "x = 8.0\n",
        "lr = 0.1                      # ขนาดก้าว\n",
        "\n",
        "for i in range(21):\n",
        "    if i in (0, 1, 2, 3, 5, 10, 20):\n",
        "        print(f\"ก้าว {i:2d}  x = {x:7.4f}  ความสูง = {x*x:8.4f}\")\n",
        "    gradient = 2*x            # ความชันใต้ฝ่าเท้า\n",
        "    x = x - lr*gradient       # ก้าวสวนทางความชัน"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for lr in [0.01, 0.1, 0.45, 0.55, 1.05]:\n",
        "    x = 8.0\n",
        "    for _ in range(20):\n",
        "        x = x - lr*2*x\n",
        "    print(f\"lr {lr:5.2f}  หลัง 20 ก้าว x = {x:.4f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z88bDhR3O8Sh",
        "outputId": "5cb53741-6c8c-4cf0-d84a-1e3f249a08d7"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "lr  0.01  หลัง 20 ก้าว x = 5.3409\n",
            "lr  0.10  หลัง 20 ก้าว x = 0.0922\n",
            "lr  0.45  หลัง 20 ก้าว x = 0.0000\n",
            "lr  0.55  หลัง 20 ก้าว x = 0.0000\n",
            "lr  1.05  หลัง 20 ก้าว x = 53.8200\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "rng = np.random.default_rng(1)\n",
        "X = np.array([[0,0],[0,1],[1,0],[1,1]], float)\n",
        "y = np.array([[0],[1],[1],[0]], float)\n"
      ],
      "metadata": {
        "id": "WWQhZlkaSTpl"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "W1 = rng.normal(0, 1, (2,2)); b1 = np.zeros((1,2))\n",
        "W2 = rng.normal(0, 1, (2,1)); b2 = np.zeros((1,1))\n",
        "sig = lambda z: 1/(1+np.exp(-z))"
      ],
      "metadata": {
        "id": "oKoaghsfSWAO"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "h = sig(X@W1 + b1)            # ชั้นซ่อนคิด\n",
        "out = sig(h@W2 + b2)          # ชั้นตอบคิด"
      ],
      "metadata": {
        "id": "nI_02N0_Sgmd"
      },
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"คำตอบก่อนฝึก\", np.round(out.ravel(), 3))\n",
        "print(\"loss ก่อนฝึก\", round(float(np.mean((out-y)**2)), 4))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-kWYUeltSjLK",
        "outputId": "57f8f2ac-36d2-40c7-fc74-d70dba7e6ee3"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "คำตอบก่อนฝึก [0.663 0.651 0.699 0.684]\n",
            "loss ก่อนฝึก 0.2799\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lr = 0.5\n",
        "for epoch in range(20001):\n",
        "    h = sig(X@W1 + b1)                  # จังหวะ 1 คิดไปข้างหน้า\n",
        "    out = sig(h@W2 + b2)\n",
        "    loss = np.mean((out-y)**2)          # จังหวะ 2 วัดความผิด\n",
        "    if epoch in (0, 100, 1000, 5000, 20000):\n",
        "        print(f\"รอบ {epoch:5d}  loss = {loss:.4f}\")\n",
        "\n",
        "    d_out = (out-y)*out*(1-out)         # จังหวะ 3 ใบตำหนิชั้นตอบ\n",
        "    d_h = d_out@W2.T * h*(1-h)          # ส่งย้อนไปชั้นซ่อน\n",
        "    W2 -= lr*h.T@d_out; b2 -= lr*d_out.sum(0)\n",
        "    W1 -= lr*X.T@d_h;  b1 -= lr*d_h.sum(0)\n",
        "\n",
        "print(\"คำตอบหลังฝึก\", np.round(out.ravel(), 3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VnvG5ahBUUcN",
        "outputId": "e9b622f6-0285-45c9-9255-625673a63016"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "รอบ     0  loss = 0.2799\n",
            "รอบ   100  loss = 0.2486\n",
            "รอบ  1000  loss = 0.0155\n",
            "รอบ  5000  loss = 0.0007\n",
            "รอบ 20000  loss = 0.0001\n",
            "คำตอบหลังฝึก [0.013 0.989 0.989 0.011]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(np.round(sig(X@W1 + b1), 2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YQduXTs6UXn0",
        "outputId": "da3f240f-1085-4f2c-e33b-1da350f23370"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[0.04 0.03]\n",
            " [0.93 0.  ]\n",
            " [0.   0.95]\n",
            " [0.03 0.02]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import torch\n",
        "import torch.nn as nn\n",
        "\n",
        "torch.manual_seed(1)\n",
        "X = torch.tensor([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])\n",
        "y = torch.tensor([[0.],[1.],[1.],[0.]])\n",
        "\n",
        "model = nn.Sequential(nn.Linear(2,2), nn.Sigmoid(),\n",
        "                      nn.Linear(2,1), nn.Sigmoid())\n",
        "opt = torch.optim.SGD(model.parameters(), lr=0.5)\n",
        "loss_fn = nn.MSELoss()\n",
        "\n",
        "for epoch in range(20001):\n",
        "    out = model(X)                      # คิดไปข้างหน้า\n",
        "    loss = loss_fn(out, y)              # วัดความผิด\n",
        "    if epoch in (0, 100, 1000, 5000, 20000):\n",
        "        print(f\"รอบ {epoch:5d}  loss = {loss.item():.4f}\")\n",
        "    opt.zero_grad()\n",
        "    loss.backward()                     # ใบตำหนิย้อนกลับ ในบรรทัดเดียว\n",
        "    opt.step()                          # ขยับทุกน้ำหนักหนึ่งก้าว\n",
        "\n",
        "print(\"คำตอบหลังฝึก\", model(X).detach().numpy().round(3).ravel())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Wuw7DHQ6UmH0",
        "outputId": "c075605c-da63-43af-b50b-734dfe16435b"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "รอบ     0  loss = 0.2548\n",
            "รอบ   100  loss = 0.2501\n",
            "รอบ  1000  loss = 0.2500\n",
            "รอบ  5000  loss = 0.0355\n",
            "รอบ 20000  loss = 0.0004\n",
            "คำตอบหลังฝึก [0.021 0.982 0.982 0.019]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def train_xor(lr, epochs=20000, seed=1):\n",
        "    rng = np.random.default_rng(seed)\n",
        "    X = np.array([[0,0],[0,1],[1,0],[1,1]], float)\n",
        "    y = np.array([[0],[1],[1],[0]], float)\n",
        "    W1 = rng.normal(0,1,(2,2)); b1 = np.zeros((1,2))\n",
        "    W2 = rng.normal(0,1,(2,1)); b2 = np.zeros((1,1))\n",
        "    sig = lambda z: 1/(1+np.exp(-z))\n",
        "    for _ in range(epochs):\n",
        "        h = sig(X@W1+b1); out = sig(h@W2+b2)\n",
        "        d_out = (out-y)*out*(1-out)\n",
        "        d_h = d_out@W2.T * h*(1-h)\n",
        "        W2 -= lr*h.T@d_out; b2 -= lr*d_out.sum(0)\n",
        "        W1 -= lr*X.T@d_h;  b1 -= lr*d_h.sum(0)\n",
        "    h = sig(X@W1+b1); out = sig(h@W2+b2)\n",
        "    return float(np.mean((out-y)**2)), np.round(out.ravel(), 3)\n",
        "\n",
        "for lr in [0.01, 0.5, 5.0, 20.0]:\n",
        "    L, preds = train_xor(lr)\n",
        "    print(f\"lr {lr:5.2f}  loss = {L:.4f}  คำตอบ = {preds}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tJ02T-i5ahTL",
        "outputId": "47da2426-727a-47b9-a6c7-e0296936e16a"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "lr  0.01  loss = 0.2157  คำตอบ = [0.441 0.404 0.673 0.454]\n",
            "lr  0.50  loss = 0.0001  คำตอบ = [0.013 0.989 0.989 0.011]\n",
            "lr  5.00  loss = 0.0000  คำตอบ = [0.004 0.997 0.997 0.003]\n",
            "lr 20.00  loss = 0.1443  คำตอบ = [0.    0.303 0.998 0.303]\n"
          ]
        }
      ]
    }
  ]
}