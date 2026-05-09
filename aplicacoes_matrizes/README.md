# Como os filtros detectam bordas?

As imagens podem ser vistas como matrizes, onde cada número representa a intensidade de um pixel. Os kernels são pequenas matrizes que percorrem a imagem realizando multiplicações e somas entre os valores dos pixels vizinhos.

Os filtros detectam bordas procurando mudanças bruscas nesses valores (diferença nos pixels). Quando os pixels possuem intensidades parecidas, o resultado da operação tende a ser baixo. Por outro lado, quando há uma grande diferença entre regiões claras e escuras, o resultado aumenta, indicando uma possível borda.

## Filtros utilizados

### Laplacian-Gaussian
Primeiro suaviza a imagem para reduzir ruídos e depois destaca regiões onde a intensidade muda rapidamente.

### Sobel
Detecta bordas horizontais e verticais separadamente utilizando os eixos `x` e `y`. Ao combinar os dois resultados, é possível destacar os contornos da imagem.

### Gaussian Gradient
Calcula a intensidade das mudanças entre pixels vizinhos. Quanto maior a variação, mais forte aparece a borda.

### Fourier + Prewitt
Realiza suavização e destaca linhas e contornos da imagem, permitindo visualizar bordas mais finas.

## Conclusão

A detecção de bordas funciona através de operações matemáticas entre matrizes. Os filtros analisam a diferença de intensidade entre pixels vizinhos e destacam regiões onde essas diferenças são maiores.