# Patterns of Enterprise Application Architecture (Padrões de Arquitetura de Aplicativo Corporativo)

## Layering

O padrão de projeto Layering, também conhecido como padrão de camadas, é um padrão arquitetural comum usado para estruturar e organizar sistemas de software em camadas distintas e independentes. Cada camada é responsável por um conjunto específico de funcionalidades e possui uma responsabilidade clara no sistema.

O padrão Layering segue uma abordagem hierárquica, em que as camadas são empilhadas uma sobre a outra, com cada camada fornecendo serviços para a camada acima dela. Geralmente, as camadas são organizadas de forma que a camada superior dependa apenas das camadas inferiores, enquanto as camadas inferiores são independentes das camadas superiores.

Cada camada no padrão de camadas possui um propósito e responsabilidade distintos. As camadas típicas encontradas nesse padrão incluem:

- Camada de Apresentação: É a camada mais alta, responsável pela interface com o usuário e pela apresentação dos dados. Pode incluir componentes de interface do usuário, como telas, formulários ou páginas da web.

- Camada de Aplicação: É responsável pela lógica de negócio e processamento da aplicação. Ela coordena as interações entre a camada de apresentação e a camada de dados, realizando validações, regras de negócio e tomadas de decisão.

- Camada de Domínio: Contém a lógica de domínio e os objetos de negócio do sistema. Essa camada encapsula as regras de negócio e os conceitos essenciais do domínio do problema sendo resolvido.

- Camada de Infraestrutura: Fornece recursos de baixo nível, como acesso a bancos de dados, serviços externos, comunicação em rede e persistência de dados. Ela abstrai os detalhes da infraestrutura subjacente e oferece serviços para as camadas superiores.

O padrão Layering promove a separação de preocupações e a modularidade, permitindo que cada camada seja desenvolvida e testada independentemente. Isso facilita a manutenção, a escalabilidade e a evolução do sistema, além de permitir a substituição ou atualização de componentes em camadas específicas sem afetar as demais.

No entanto, é importante equilibrar a separação de camadas com a necessidade de comunicação e interação eficiente entre elas. Uma camada não deve depender diretamente de outra camada abaixo dela, pois isso violaria os princípios de encapsulamento e independência. O uso de interfaces claras e contratos bem definidos entre as camadas é fundamental para garantir a modularidade e a flexibilidade do sistema.

## Layer vs Tier

Layer e Tier são dois termos frequentemente usados no contexto de arquitetura de software, mas eles têm significados diferentes.

**Layer (Camada):**

Refere-se à organização lógica de um sistema em componentes ou módulos que têm responsabilidades específicas e interagem entre si. Cada camada representa um conjunto de funcionalidades relacionadas que são agrupadas juntas. O padrão de projeto Layering (ou padrão de camadas) é um exemplo de como as camadas podem ser estruturadas em um sistema, seguindo uma abordagem hierárquica.

**Tier (Nível):**

Refere-se à organização física ou de implantação de um sistema em diferentes camadas ou níveis de hardware ou infraestrutura. Cada nível é responsável por executar um conjunto específico de tarefas ou serviços. Um sistema de várias camadas pode ser implantado em um ambiente com vários níveis (tiers) físicos ou de infraestrutura, como front-end, back-end e camada de banco de dados, em servidores diferentes ou em diferentes instâncias de nuvem.

Em resumo, "layer" (camada) refere-se à organização lógica dos componentes e funcionalidades de um sistema, enquanto "tier" (nível) refere-se à organização física ou de implantação do sistema em diferentes níveis ou camadas de infraestrutura. Embora esses termos sejam usados frequentemente em conjunto, eles têm abordagens e significados distintos na arquitetura de software.

## 3 Layers Architecture/ Arquitetura de 3 camadas

A arquitetura de 3 camadas (3 Layers Architecture) é um padrão de arquitetura de software amplamente utilizado na construção de aplicativos. Ele divide a aplicação em três camadas distintas, cada uma com uma responsabilidade específica. As três camadas são:

**Camada de Apresentação (Presentation Layer):**
- Também conhecida como camada de interface do usuário ou camada de apresentação.
- Responsável pela interação direta com o usuário.
- Lida com a apresentação de informações e a coleta de entrada do usuário.
- Pode incluir interfaces gráficas, páginas da web, APIs, aplicativos móveis, etc.
- Foca-se na experiência do usuário e na apresentação dos dados de forma compreensível.

**Camada de Lógica de Negócios (Business Logic Layer):**
- Também conhecida como camada de processamento ou camada de regras de negócios.
- Responsável pela implementação das regras de negócios e lógica de processamento.
- Processa e manipula os dados recebidos da camada de apresentação.
- Executa operações como validação, cálculos, lógica de fluxo, etc.
- Geralmente independente de tecnologia e pode ser reutilizável.

**Camada de Acesso a Dados (Data Access Layer):**
- Também conhecida como camada de persistência ou camada de armazenamento.
- Responsável pelo acesso e gerenciamento dos dados armazenados.
- Fornece métodos para recuperar, inserir, atualizar e excluir dados no armazenamento.
- Interage com bancos de dados, sistemas de arquivos, serviços web, entre outros.
- Isola a lógica de acesso aos dados das outras camadas.

Essa arquitetura promove a separação de preocupações e a modularização do sistema, facilitando a manutenção, a escalabilidade e a evolução do aplicativo. Cada camada possui uma responsabilidade clara e pode ser desenvolvida, testada e atualizada independentemente das outras camadas. Além disso, permite a reutilização de componentes e facilita a adoção de melhores práticas de programação e design.

É importante mencionar que a arquitetura de 3 camadas é um modelo genérico e pode ser adaptado e expandido para atender às necessidades específicas de cada aplicativo.

A regra de ouro é manter a separação clara e a responsabilidade bem definida entre essas três camadas. Cada camada deve ser independente das outras e se comunicar apenas através de interfaces bem definidas. Isso permite uma maior modularidade, reutilização de código, testabilidade e facilita a manutenção do sistema. Além disso, essa separação permite que as mudanças em uma camada tenham um impacto mínimo nas outras camadas, promovendo a escalabilidade e flexibilidade do sistema como um todo.

## Domain Logic
### Transaction Script

O padrão Transaction Script é um padrão de projeto que organiza a lógica de negócios em torno das transações do sistema. Ele é frequentemente utilizado em sistemas simples ou com requisitos de negócios menos complexos.

Nesse padrão, a lógica de negócios é organizada em torno de scripts, que são unidades de execução que lidam com uma transação específica. Cada script é responsável por realizar todas as operações necessárias para concluir a transação, como validações, cálculos, atualizações de banco de dados, envio de notificações, entre outros.

Algumas características do padrão Transaction Script incluem:

- Procedural: O padrão Transaction Script segue uma abordagem procedural, em que a lógica de negócios é implementada como um conjunto de instruções sequenciais. Isso facilita a compreensão e manutenção do código, especialmente em sistemas menos complexos.

- **Foco na transação**: O padrão Transaction Script concentra-se na execução de transações individuais, em vez de em um conjunto complexo de regras de negócios. Cada script é responsável por uma única transação e contém todas as etapas necessárias para concluí-la.

- **Baixa abstração**: Em comparação com outros padrões arquiteturais, o padrão Transaction Script tem uma abstração relativamente baixa. A lógica de negócios é implementada diretamente nos scripts, sem a necessidade de camadas adicionais de abstração.

- **Adequado para sistemas simples**: O padrão Transaction Script é mais adequado para sistemas menos complexos, com requisitos de negócios mais simples e transações individuais diretas. Para sistemas mais complexos, com lógica de negócios complexa e múltiplas interações entre entidades, outros padrões arquiteturais, como o padrão Domain Model, podem ser mais apropriados.

É importante considerar que o padrão Transaction Script pode levar a código duplicado e dificuldades de manutenção em sistemas com muitas transações ou lógica de negócios complexa. Em tais casos, outros padrões que promovam a separação de responsabilidades, como o padrão Domain Model ou o padrão Service Layer, podem ser mais benéficos.

Cada padrão arquitetural tem suas vantagens e desvantagens, e a escolha do padrão mais adequado depende das características do sistema, dos requisitos de negócios e das necessidades de manutenção e escalabilidade.


### Domain Model
O padrão Domain Model é um padrão de projeto que organiza a lógica de negócios em torno do domínio do problema. Ele enfatiza a modelagem do domínio, representando conceitos do mundo real e as relações entre eles de forma estruturada e orientada a objetos.

Nesse padrão, o domínio do problema é mapeado em classes de domínio, que encapsulam o comportamento e o estado relacionados a esses conceitos. As classes de domínio representam entidades, valor de objetos, serviços e agregados que são relevantes para o problema em questão.

Algumas características do padrão Domain Model incluem:

- **Modelagem do domínio**: O padrão Domain Model coloca a modelagem do domínio no centro do projeto de software. Ele busca compreender e representar fielmente os conceitos, as regras e o comportamento do domínio em classes e relacionamentos.

- **Orientação a objetos**: O padrão Domain Model utiliza os princípios da orientação a objetos para representar o domínio. As classes de domínio encapsulam dados e comportamentos relacionados, permitindo a modelagem de relações, validações e operações específicas do domínio.

- **Separação de responsabilidades**: O padrão Domain Model promove a separação clara de responsabilidades, onde as classes de domínio são responsáveis por lidar com a lógica de negócios específica do domínio. Isso ajuda a manter o código mais coeso, facilita a compreensão e manutenção do sistema.

- **Foco na semântica do domínio**: O padrão Domain Model busca utilizar uma linguagem ubíqua, que seja compreensível tanto para os especialistas do domínio quanto para os desenvolvedores. Isso promove uma comunicação mais efetiva e ajuda a alinhar o software com as necessidades do negócio.

Ao adotar o padrão Domain Model, é possível obter uma representação mais fiel e compreensível do domínio do problema, facilitando o desenvolvimento, a manutenção e a evolução do sistema. Além disso, a separação de responsabilidades e a modelagem orientada a objetos tornam o código mais modular, flexível e reutilizável.

No entanto, é importante considerar que a aplicação do padrão Domain Model pode introduzir uma camada adicional de complexidade e exigir um maior esforço de modelagem e design. Em sistemas com domínios muito simples ou com regras de negócios pouco complexas, outros padrões mais simples, como o Transaction Script, podem ser mais adequados.

Cada padrão arquitetural tem suas vantagens e desvantagens, e a escolha do padrão mais apropriado depende das características do sistema, dos requisitos de negócios e das necessidades de manutenção e escalabilidade.


### Table Module
O padrão Table Module é um padrão de projeto que organiza a lógica de negócios em torno de tabelas de banco de dados individuais. Ele é especialmente útil em sistemas onde a lógica de negócios está diretamente relacionada às operações e manipulações de dados em tabelas específicas.

Nesse padrão, cada tabela do banco de dados é representada por um módulo (ou classe) específico, conhecido como Table Module. O Table Module encapsula todas as operações e regras de negócios relacionadas àquela tabela em particular. Isso inclui a leitura, escrita, validação e manipulação dos dados da tabela.

Algumas características do padrão Table Module incluem:

- **Coesão com tabelas**: O Table Module é altamente coeso com a estrutura das tabelas do banco de dados. Cada módulo é responsável por lidar com as operações e regras de negócios relacionadas a uma tabela específica, o que facilita o entendimento e a manutenção do código.

- **Acoplamento com banco de dados**: O Table Module possui um acoplamento mais forte com o banco de dados, pois está intimamente relacionado às tabelas e aos esquemas de dados. Ele lida diretamente com as operações de persistência e manipulação de dados, sem uma separação clara entre a camada de domínio e a camada de acesso a dados.

- **Lógica de negócios centralizada**: O Table Module concentra toda a lógica de negócios relacionada a uma tabela específica em um único local. Isso facilita a localização e o gerenciamento das regras de negócios, especialmente em sistemas com muitas operações e manipulações de dados.

- **Possibilidade de encapsulamento adicional**: Em alguns casos, o Table Module pode encapsular não apenas as operações de banco de dados, mas também a lógica de negócios mais complexa relacionada a uma tabela específica. Isso permite que a tabela tenha seu próprio conjunto de regras de negócios e comportamentos específicos.

No entanto, é importante observar que o padrão Table Module pode levar a uma proliferação de classes e módulos, especialmente em sistemas com muitas tabelas e operações. Isso pode aumentar a complexidade e a sobrecarga de gerenciamento do código. Além disso, o forte acoplamento com o banco de dados pode dificultar a testabilidade e a manutenção do código.

O padrão Table Module pode ser uma opção viável em sistemas com estruturas de dados simples e regras de negócios diretas e específicas de tabelas individuais. No entanto, em sistemas mais complexos, outros padrões como o Domain Model ou o Transaction Script podem oferecer uma maior flexibilidade e organização da lógica de negócios. A escolha do padrão mais adequado dependerá das necessidades e características específicas do sistema em questão.


## Service Layer / (Camada de Serviço)
O padrão de projeto Service Layer (Camada de Serviço) é um padrão arquitetural utilizado no desenvolvimento de software para separar a lógica de negócio da lógica de apresentação e acesso aos dados. Ele define uma camada intermediária entre a camada de apresentação (como a interface do usuário) e a camada de persistência (como o banco de dados).

A principal responsabilidade da camada de serviço é encapsular as regras de negócio e fornecer serviços ou operações específicas para serem utilizadas pela camada de apresentação. Essa camada atua como uma fachada para os componentes externos, fornecendo uma interface coesa e simplificada para as operações de negócio.

Alguns benefícios do uso do Service Layer são:

- Separação de preocupações: O padrão ajuda a manter a separação entre a lógica de negócio e as responsabilidades da camada de apresentação e da camada de persistência, tornando o código mais organizado e de fácil manutenção.

- Reutilização de código: A camada de serviço pode ser compartilhada por diferentes interfaces de usuário, permitindo a reutilização de lógica de negócio em vários contextos.

- Flexibilidade e adaptabilidade: A camada de serviço atua como um ponto centralizado para a implementação de regras de negócio complexas, facilitando a evolução e adaptação do sistema a novos requisitos sem afetar a camada de apresentação.

- Testabilidade: Ao isolar a lógica de negócio em uma camada separada, é mais fácil escrever testes unitários para validar as regras de negócio sem a necessidade de simular a interação com a camada de apresentação ou a camada de persistência.

É importante notar que o Service Layer não é um padrão exclusivo, mas sim uma prática comum no desenvolvimento de software. Sua implementação pode variar de acordo com a arquitetura do sistema e as necessidades específicas do projeto.

Ao utilizar o padrão Service Layer, é possível obter um código mais modular, reutilizável e testável, além de facilitar a evolução e manutenção do sistema. No entanto, é importante avaliar as necessidades e características do sistema para determinar se esse padrão é adequado para o contexto específico.

### Camada de serviço (Service Layer) vs padrão Transaction Script

A camada de serviço (Service Layer) e o padrão Transaction Script são dois padrões arquiteturais diferentes usados no desenvolvimento de software.

**Camada de serviço (Service Layer):**

A camada de serviço é uma abordagem arquitetural que separa a lógica de negócio do acesso aos dados. Nessa abordagem, as operações de negócio são encapsuladas em serviços independentes, que fornecem uma interface para interagir com a aplicação. A camada de serviço orquestra as chamadas a diferentes componentes do sistema para realizar uma operação de negócio completa. Essa camada é responsável por validar dados, coordenar transações e aplicar regras de negócio.

**Vantagens da camada de serviço:**

- Separação clara entre a lógica de negócio e o acesso aos dados.
- Maior modularidade e reutilização de código.
- Facilita a manutenção e testabilidade da aplicação.

**Desvantagens da camada de serviço:**

- Introdução de complexidade adicional: A introdução de uma camada de serviço pode adicionar uma camada extra de complexidade ao sistema, tornando-o mais difícil de entender e manter, especialmente para sistemas menores ou menos complexos.
- Overhead de desenvolvimento: A implementação da camada de serviço requer tempo e esforço adicionais, pois envolve a definição de interfaces, a criação de serviços e a coordenação entre eles.
- Possível sobrecarga de comunicação: Em sistemas distribuídos, a camada de serviço pode introduzir uma sobrecarga de comunicação devido à necessidade de troca de mensagens entre os diferentes serviços.
- Em sistemas maiores gerará complexidade ao longo do tempo, com maior acoplamento e complexidade em equipes

**Transaction Script:**

O Transaction Script é um padrão arquitetural mais simples, onde a lógica de negócio é organizada em scripts individuais, que são acionados por transações. Cada script é responsável por executar todas as etapas necessárias para completar uma transação específica. Geralmente, cada script está associado a uma única tela ou ação do usuário.

**Vantagens do Transaction Script:**

- Simplicidade e facilidade de implementação.
- Apropriado para sistemas menores e menos complexos.
- Fácil entendimento e manutenção para casos de uso simples.

**Desvantagens do Transaction Script:**

- Falta de modularidade e reutilização de código: O padrão Transaction Script geralmente resulta em código menos modular, onde a lógica de negócio está diretamente incorporada nos scripts, dificultando a reutilização em outros contextos.
- Dificuldade em lidar com complexidade crescente: À medida que a complexidade do sistema aumenta, o Transaction Script pode se tornar difícil de manter e evoluir, pois a lógica de negócio está espalhada em vários scripts, dificultando a compreensão do fluxo geral.
- Dificuldade em separar preocupações: O Transaction Script não oferece uma separação clara entre a lógica de negócio e o acesso aos dados, o que pode resultar em uma mistura de responsabilidades e dificuldade em implementar mudanças em uma parte específica do sistema.

A escolha entre a camada de serviço e o Transaction Script depende do tamanho, complexidade e necessidades específicas do sistema. A camada de serviço é mais adequada para sistemas maiores e complexos, onde é necessário separar as preocupações e manter a escalabilidade e a modularidade. O Transaction Script é mais adequado para sistemas menores e casos de uso simples, onde a simplicidade e a facilidade de implementação são mais importantes do que a separação completa das preocupações.

## Padrões de dados

### Gateway

O padrão de projeto Gateway é um padrão arquitetural que tem como objetivo fornecer uma interface unificada e simplificada para acesso a sistemas externos, como bancos de dados, serviços web ou sistemas legados. O padrão Gateway atua como uma abstração entre a aplicação e os sistemas externos, encapsulando a complexidade do acesso e fornecendo uma interface consistente para a comunicação.

O padrão Gateway é útil em cenários em que a aplicação precisa interagir com sistemas externos de diferentes tipos e protocolos, mas deseja manter a lógica de negócio isolada e independente desses detalhes de implementação. Além disso, o padrão Gateway também oferece benefícios como reuso de código, testabilidade e flexibilidade na substituição ou adição de novos sistemas externos.

Existem dois tipos principais de Gateway:

**Data Gateway (Gateway de Dados):** Este tipo de Gateway é usado para acessar e manipular dados em sistemas externos, como bancos de dados ou serviços de armazenamento. Ele fornece métodos e operações abstratas para executar consultas, atualizações, inserções e exclusões nos dados, ocultando a complexidade do acesso ao sistema externo.

**Integration Gateway (Gateway de Integração):** Este tipo de Gateway é usado para integrar a aplicação com serviços web, APIs ou sistemas legados. Ele fornece uma camada de abstração que encapsula as chamadas e respostas do serviço externo, convertendo e mapeando os dados de acordo com o formato esperado pela aplicação.

Os Gateways são projetados para serem genéricos e reutilizáveis, permitindo que a aplicação se comunique com diferentes sistemas externos usando a mesma interface simplificada. Eles podem ser implementados como classes ou componentes separados que são responsáveis pelo acesso e comunicação com os sistemas externos, enquanto a aplicação utiliza esses Gateways para realizar suas operações sem precisar conhecer os detalhes internos da implementação dos sistemas externos.

Em resumo, o padrão de projeto Gateway oferece uma abstração entre a aplicação e os sistemas externos, simplificando o acesso e fornecendo uma interface consistente. Ele ajuda a separar a lógica de negócio da complexidade do acesso aos sistemas externos, permitindo maior flexibilidade, reuso de código e testabilidade.

### Row Data Gateway vs Table Data Gateway
Row Data Gateway e Table Data Gateway são dois padrões de projeto relacionados ao acesso a dados em um sistema.

**Row Data Gateway:**
O padrão Row Data Gateway (ou Gateway de Dados por Linha) é usado para encapsular o acesso a dados de uma única linha em uma tabela de banco de dados. Cada instância do Row Data Gateway representa uma única linha da tabela e é responsável por fornecer métodos para recuperar, atualizar e excluir os dados dessa linha específica. O Row Data Gateway é uma abstração que encapsula as operações de banco de dados e fornece uma interface orientada a objetos para interagir com os dados em nível de linha.

**Table Data Gateway:**
O padrão Table Data Gateway (ou Gateway de Dados por Tabela) é usado para encapsular o acesso a uma tabela inteira de um banco de dados. O Table Data Gateway é responsável por fornecer métodos para executar operações de leitura e gravação na tabela, como recuperar registros, inserir novos registros, atualizar registros existentes e excluir registros. O Table Data Gateway oferece uma interface de alto nível para interagir com os dados da tabela, abstraindo os detalhes do banco de dados subjacente.

A diferença principal entre esses dois padrões está no nível de granularidade dos objetos de acesso a dados. Enquanto o Row Data Gateway lida com operações em nível de linha, o Table Data Gateway opera em nível de tabela. Isso significa que, com o Row Data Gateway, cada linha da tabela é representada por um objeto separado, enquanto o Table Data Gateway lida com a tabela como um todo.

Ambos os padrões podem ser implementados de forma simples ou mais complexa, dependendo dos requisitos do sistema e do contexto em que são aplicados. Eles ajudam a encapsular a lógica de acesso a dados, proporcionando uma interface clara e coesa para interagir com as tabelas do banco de dados.

**Obs importante: É importante mencionar que esses padrões são considerados mais tradicionais e têm sido substituídos por abordagens mais modernas, como o padrão Active Record ou o uso de ORMs (Object-Relational Mapping), que fornecem mapeamento automático entre objetos e tabelas do banco de dados, simplificando ainda mais o acesso e manipulação de dados.**


## Active Record

O padrão Active Record é um padrão de projeto de software que combina a lógica de negócios (modelos) com a persistência de dados em um único objeto chamado de "registro ativo" (active record). Esse padrão é comumente utilizado em frameworks e bibliotecas de mapeamento objeto-relacional (ORM), como o Ruby on Rails.

No padrão Active Record, cada objeto representa uma única linha em uma tabela do banco de dados e possui métodos para acessar e manipular os dados dessa linha. O objeto active record encapsula a lógica de persistência, permitindo que você crie, leia, atualize e exclua registros no banco de dados de forma simples e direta.

### Principais características do padrão Active Record:

- **Mapeamento de objetos-relacionais**: O padrão Active Record fornece um mapeamento direto entre os objetos da aplicação e as tabelas do banco de dados. Cada atributo do objeto corresponde a uma coluna na tabela, e as operações de leitura/gravação são mapeadas para operações de consulta/atualização no banco de dados.

- **Abstração do acesso aos dados**: O objeto active record abstrai os detalhes de acesso ao banco de dados, como a criação de consultas SQL, permitindo que você interaja com os dados usando métodos de alto nível. Isso simplifica o desenvolvimento, reduzindo a quantidade de código necessário para manipular os dados.

- **Comportamento de negócio incorporado**: Além das operações básicas de CRUD (Create, Read, Update, Delete), o objeto active record também pode incorporar comportamentos de negócio específicos. Você pode adicionar métodos personalizados para executar validações, cálculos, relacionamentos entre objetos e outras regras de negócio.

- **Relacionamentos entre objetos**: O padrão Active Record também suporta a definição de relacionamentos entre objetos, como associações um-para-um, um-para-muitos e muitos-para-muitos. Isso facilita a navegação e manipulação de objetos relacionados, simplificando a lógica de busca e manipulação dos dados relacionados.

Embora o padrão Active Record simplifique o desenvolvimento de aplicações CRUD, ele pode apresentar algumas limitações quando se trata de separar completamente as responsabilidades de persistência de dados das entidades de negócio. Em casos mais complexos, onde a persistência de dados e a lógica de negócios são mais distintas, pode ser preferível adotar outros padrões, como o padrão Repository ou o padrão Data Mapper, para garantir uma maior separação de preocupações.

