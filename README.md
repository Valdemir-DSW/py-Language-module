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

```
Para iniciar, você importa a biblioteca como no arquivo de exemplo e define uma variável como ela. Você deve passar um diretório de um arquivo .vidm e se você quiser salvar as configurações do último idioma selecionado no APPDATA. Se você colocar o verdadeiro, toda vez que o código reiniciar ele vai definir o idioma como o último selecionado. Pode ser interessante, você não deixe como falso, isso não vai alterar em nada. Depois, você precisa passar um idioma que você quer utilizar, utilizando a função set_language. Esse idioma é o idioma que você definiu no gerenciador, aquele aplicativo que está disponível no arquivo zip. Se você não passar, ele vai selecionar qualquer um também, que ele achar aleatório na lista. E depois, para utilizar, você vai utilizar a função get_content, que você pode passar um id que você criou lá nos idiomas, que ele vai ver se existe aquele id no idioma selecionado e vai puxar o que tem dentro daquela célula. Simplesmente assim.
Pois é, eu falei que você poderia utilizar em qualquer linguagem de programação. Sim, qualquer linguagem que você pode importar um arquivo JSON, você pode utilizar. Dentro do aplicativo tem um compilador que consegue extrair ou melhor, exportar um arquivo .idmjson que é um arquivo de idioma JSON, que você pode utilizar.
```JSOM
{
    "ex1": {
        "msg": "bom dia  !"
    },
    "ex2": {
        "msg": "Dzień dobry  !"
    }
}

```
EX1 e EX2 são exemplos de idiomas que eu mesmo coloquei, mas, obviamente, você poderá colocar o nome que você quiser para o idioma. INSG é um ID que eu coloquei disponível lá nos dois idiomas. Claro que um idioma pode ter mais IDs que o outro, mas isso não importa. Mas, você pode colocar o que você quiser.

O aplicativo falado é esse que está disponível aqui > https://github.com/Valdemir-DSW/py-Language-module/raw/refs/heads/main/idm%20editor%20setup.zip que também tem um tradutor automático dele o que você pode usar mas confira a tradução se está correta sempre !

Também você poderá encontrar funções para puxar todos os idiomas(get_available_languages() e todos os ids de um idioma(get_ids_by_language() ! 
