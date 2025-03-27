# crawler-images

Crowler para baixar imagens de um site específico.

O script está configurado para percorrer todas as tags de links de uma página, checar o apontamento do link e caso o link aponte para uma imagem é feito o download da mesma.

Para utilizar basta clonar o projeto e instalar as depedência do python com o seguinte comando:
`pip install -r requirements.txt`

Após isso é só executá-lo utilizando a linha de comando abaixo, onde **{sua_url}** deve ser trocada pelo link da página que você deseja utilizar:
`python main.py {sua_url}`
