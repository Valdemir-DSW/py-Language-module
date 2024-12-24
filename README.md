# py-Language-module
Special language mode for Python but can be used in other languages
![image](https://github.com/user-attachments/assets/2fe48a0b-ee78-443a-b87f-a5c9a2c15316)

```python
from idmlib import idmManager  # Importa a classe idmManager

# Caminho para o seu arquivo de idiomas existente
file_path = 'test.vidm'
idm = idmManager(file_path, save_in_appdata=False)
print(idm.get_content('msg'))


idm.set_language('ex2')
print(idm.get_content('msg'))  


Para iniciar, você importa a biblioteca como no arquivo de exemplo e define uma variável como ela. Você deve passar um diretório de um arquivo .vidm e se você quiser salvar as configurações do último idioma selecionado no ATPDATO. Se você colocar o verdadeiro, toda vez que o código reiniciar ele vai definir o idioma como o último selecionado. Pode ser interessante, você não deixe como falso, isso não vai alterar em nada. Depois, você precisa passar um idioma que você quer utilizar, utilizando a função setLanguage. Esse idioma é o idioma que você definiu no gerenciador, aquele aplicativo que está disponível no arquivo zip. Se você não passar, ele vai selecionar qualquer um também, que ele achar aleatório na lista. E depois, para utilizar, você vai utilizar a função getContent, que você pode passar um id que você criou lá nos idiomas, que ele vai ver se existe aquele id no idioma selecionado e vai puxar o que tem dentro daquela célula. Simplesmente assim.
