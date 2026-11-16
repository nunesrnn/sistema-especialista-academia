# Dicionario de Fatos e Regras - Sistema Especialista de Academia

Este documento descreve a base de conhecimento estruturada para o protótipo de recomendação de planos de academia, detalhando o identificador, a categoria e a lógica de cada regra de produção implementada no sistema.

## Tabela de Regras

| ID | Categoria | Descrição / Significado |
|---|---|---|
| **R01** | objetivo | Quem busca hipertrofia ou emagrecimento avancado precisa de suporte completo de estrutura. |
| **R02** | frequencia | Alunos que pretendem frequentar 4 ou mais vezes na semana precisam de acesso total em qualquer horario. |
| **R03** | frequencia | Alunos com frequencia de ate 3 vezes na semana podem se adaptar bem ao plano essencial. |
| **R04** | servicos | Quem faz questao de participar de aulas coletivas (spinning, danca, yoga) precisa do plano Plus ou Black. |
| **R05** | servicos | Quem deseja levar amigos ou convidados para treinar precisa obrigatoriamente do plano Black. |
| **R06** | horario | Se o aluno so pode treinar em horarios de pico e quer flexibilidade, descartar planos restritos. |
| **R07** | orcamento | Se o orcamento maximo do cliente for inferior a 90 reais, nenhum plano padrao cobre. |
| **R08** | orcamento | Se o orcamento esta entre 90 e 128 reais, o plano aplicavel e o Essencial. |
| **R09** | orcamento | Se o orcamento esta entre 129 e 178 reais, o teto passa a ser o plano Plus. |
| **R10** | orcamento | Se o orcamento e igual ou superior a 179 reais, o cliente tem elegibilidade financeira para o plano Black. |
| **R11** | descarte | Descartar plano Essencial se o cliente exige aulas coletivas. |
| **R12** | descarte | Descartar plano Essencial se o cliente quer levar convidados. |
| **R13** | descarte | Descartar plano Plus se o cliente quer levar convidados. |
| **R14** | descarte | Descartar qualquer plano cujo preco mensal ultrapasse o orcamento informado pelo cliente. |
| **R15** | recomendacao | Se nenhum restritivo extra foi acionado e a frequencia e baixa, sugerir o plano Essencial como melhor custo-beneficio. |
| **R16** | recomendacao | Se o cliente quer aulas coletivas e tem orcamento compativel, recomendar o plano Plus. |
| **R17** | recomendacao | Se o cliente busca hipertrofia intensa, frequenta 5x na semana e quer diferenciais, recomendar o plano Black. |
| **R18** | ajuste_certeza | Reduzir levemente a certeza da recomendacao se o usuario informar dados genericos na faixa de horario. |
| **R19** | excecao | Se o orcamento for menor que o plano mais barato e o cliente recusar financiamento de taxa, encerrar com inconclusao orientada. |
| **R20** | validacao | Garantir que a frequencia semanal informada esteja entre 1 e 7 dias. |
| **R21** | validacao | Identificar ausencia de dados essenciais caso o objetivo nao seja preenchido. |