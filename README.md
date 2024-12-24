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
Pois é, eu falei que você poderia utilizar em qualquer linguagem de programação. Sim, qualquer linguagem que você pode importar um arquivo JSON, você pode utilizar. Dentro do aplicativo tem um compilador que consegue extrair ou melhor, exportar um arquivo .idmjson que é um arquivo de idioma JSON, que você pode utilizar. Observe este exemplo em c#.
```C#
using System;
using System.Text.Json;

public class Program
{
    // IDMJSON
    public class Example
    {
        public Message ex1 { get; set; }
        public Message ex2 { get; set; }
    }

    public class Message
    {
        public string msg { get; set; }
    }

    // Função para selecionar o idioma e retornar o texto correspondente
    public static string SelecionarIdioma(Example example, string idioma)
    {
        switch (idioma.ToLower())
        {
            case "ex1":
                return example.ex1?.msg ?? "Idioma não encontrado";
            case "ex2":
                return example.ex2?.msg ?? "Idioma não encontrado";
            default:
                return "Idioma inválido";
        }
    }

    // Função para buscar o texto a partir de um ID (exemplo: "ex1" ou "ex2")
    public static string BuscarTextoPorId(Example example, string id)
    {
        switch (id.ToLower())
        {
            case "ex1":
                return example.ex1?.msg ?? "Texto não encontrado para o ID";
            case "ex2":
                return example.ex2?.msg ?? "Texto não encontrado para o ID";
            default:
                return "ID inválido";
        }
    }

    public static void Main()
    {
        // Definindo o JSON de exemplo
        string jsonString = @"
        {
            ""ex1"": {
                ""msg"": ""bom dia  !""
            },
            ""ex2"": {
                ""msg"": ""Dzień dobry  !""
            }
        }";

        // Deserializando o JSON
        var example = JsonSerializer.Deserialize<Example>(jsonString);

        // Selecionando o idioma "ex1" e exibindo a mensagem
        Console.WriteLine("Selecionando idioma 'ex1': " + SelecionarIdioma(example, "ex1"));
        
        // Selecionando o idioma "ex2" e exibindo a mensagem
        Console.WriteLine("Selecionando idioma 'ex2': " + SelecionarIdioma(example, "ex2"));
        
        // Buscando o texto usando o ID "ex1"
        Console.WriteLine("Texto do ID 'ex1': " + BuscarTextoPorId(example, "ex1"));

        // Buscando o texto usando o ID "ex2"
        Console.WriteLine("Texto do ID 'ex2': " + BuscarTextoPorId(example, "ex2"));
    }
}


```
