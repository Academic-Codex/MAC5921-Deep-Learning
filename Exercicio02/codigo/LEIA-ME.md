
# Tarefa 2 — MNIST (NN × CNN) com PyTorch

## Como rodar
1. Abra `mnist_nn_cnn_tarefa2.ipynb` no seu Jupyter local, no Colab ou no Kaggle (GPU recomendado).
2. Execute as células em ordem. Elas baixam o MNIST, treinam MLP e CNN, salvam figuras e `resultados.csv`.
3. Compile `relatorio_tarefa2.tex` (XeLaTeX/LuaLaTeX/PDFLaTeX). Ele referencia as figuras geradas.

## Saídas importantes
- `figures/mlp_curves_loss.png`, `figures/mlp_curves_acc.png`
- `figures/cnn_curves_loss.png`, `figures/cnn_curves_acc.png`
- `figures/cm_mlp.png`, `figures/cm_cnn.png`
- `resultados.csv`

## Explorações
- Ajuste `samples_per_class` (e.g., 50/100/300/1000).
- Ative t-SNE e Grad-CAM nas células extras (podem ser mais lentas).
- Para ruído/desbalanceamento, siga as células indicadas e refaça os *loaders*.
