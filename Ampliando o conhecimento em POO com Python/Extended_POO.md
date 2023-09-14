#  Ampliando o conhecimento em POO com Python
## Variáveis de classe e Variáveis de instância
- Todos os objetos nascem com o mesmo número de atributos classe e de instância. Atributos de instância são diferentes para cada objeto( cada objeto tem uma cópia), já os atributos dde classe são compartilhados entre os objetos

## Métodos de classe e métodos estáticos
- Métodos de classe sestão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto

- Métodos estáticos não recebem um primeiro argumento ecplícito. Ele tembém é um método vinculado à classe e não ao objeto da classe. Este método não pode acessar ou modificar estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja presenta na classe

## Interfaces
- Definem o que uma classe deve fazer
- O conceito de intrface é definir um contrato onde são declarados os métodos(o que deve ser feito) e suas respectivas assinaturas. em Python utilizamos classes abstratas para criar contratos. Classes abstratas não podem ser instanciadas

## Classes absratas
- Por padrão, o python mão fornece classes abstratas. O python vem com um módulo que fornece a base para definir as classes abstratas, e o nome do módulo é ABC. o ABC funciona decorando métodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações de base abstrata.  Um método se torna abstrato quando decorado com @abstratcmethod

