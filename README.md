## A prova de conceito

Na Sprint 1 a gente apresentou a ideia do ChargeGrid Intelligence e a proposta de transformar o carregador residencial da GoodWe em uma solução voltada para o comércio. Na Sprint 2 o objetivo era validar uma parte dessa proposta por meio de um protótipo funcional.

A gente escolheu trabalhar na precificação dinâmica porque ela está diretamente ligada ao modelo de negócio do projeto. Como o carregador HCA G2 ainda não possui um sistema próprio de cobrança, entendemos que era importante demonstrar como a plataforma poderia definir o valor da recarga de forma automática antes do início da sessão.

### O protótipo desenvolvido

O protótipo foi desenvolvido em Python e representa uma versão simplificada do módulo de precificação da plataforma.

Ele recebe informações relacionadas à situação da recarga e utiliza esses dados para calcular o valor da sessão. Entre os fatores considerados estão o horário do dia, a geração solar disponível, a quantidade de veículos carregando simultaneamente, a disponibilidade da bateria da loja e a energia necessária para carregar o veículo.

A proposta foi reproduzir, de forma simplificada, o comportamento que a plataforma teria em uma instalação real.

### Como funciona a precificação

O cálculo parte de uma tarifa-base e aplica ajustes de acordo com as condições de operação.

Quando existe maior disponibilidade de energia solar, o sistema reduz o preço da recarga através da tarifa Eco, incentivando o aproveitamento da energia gerada localmente. Em horários de maior demanda ou quando existem vários veículos utilizando os carregadores ao mesmo tempo, a tarifa aumenta para refletir o maior custo operacional da instalação.

A bateria da loja também faz parte da estratégia, ajudando a reduzir o consumo da rede elétrica em períodos mais críticos e contribuindo para evitar custos relacionados à demanda contratada.

### O que foi validado

Os testes realizados mostraram que o sistema consegue gerar preços diferentes para situações diferentes de operação.

Na prática, uma recarga realizada durante períodos de alta geração solar tende a apresentar um valor menor do que uma recarga realizada em horários de pico. Da mesma forma, a utilização da bateria da loja reduz o impacto dos momentos de maior consumo.

Esses resultados mostram que a proposta de tarifa dinâmica pode ser utilizada para incentivar o uso da energia solar disponível na instalação e, ao mesmo tempo, ajudar o lojista a controlar custos operacionais.

### Relação com a proposta principal

A Sprint 2 não teve como objetivo reproduzir toda a plataforma ChargeGrid Intelligence, mas sim validar uma das funcionalidades apresentadas na solução.

O módulo de precificação desenvolvido faz parte da camada de inteligência do sistema e trabalha em conjunto com os conceitos de recarga solar-aware, gerenciamento de potência e utilização da bateria apresentados no projeto.

### Sobre os dados utilizados

Os dados utilizados no protótipo são simulados e foram definidos apenas para validar a lógica de precificação proposta.

Apesar disso, os cenários utilizados procuram representar situações que poderiam ocorrer em uma operação real. A estrutura desenvolvida também permite a utilização de dados reais em futuras evoluções da solução.
