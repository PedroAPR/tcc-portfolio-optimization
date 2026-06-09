# Relatório de Revisão Onda 4 - Coerência Lógica e Alinhamento

### [PROBLEMA LOGICO/ESTRUTURAL] - Cap. 1 / Introdução
**Descricao:** Há um descompasso de escopo entre as estratégias prometidas na introdução e o que foi de fato executado. A introdução lista nominalmente apenas uma fração dos modelos avaliados, omitindo estratégias importantes que são extensamente analisadas na Metodologia e Resultados (16 estratégias no total), como Ômega, Kappa-3, CDaR, as carteiras EqualWeight e InvVol, além das variantes com teto de 10% (c10).
**Trecho relevante (original):** "Serão testados otimizadores distintos: Média-Variância, Mínima Variância Global, Máximo Índice de Sortino, Mínimo-CVaR e a abordagem mista de Black-Litterman."
**Impacto na avaliacao da banca:** GERA_QUESTIONAMENTO
**Sugestao de acao:** Expandir ou generalizar o trecho na introdução para abranger todas as 16 estratégias testadas, citando explicitamente as demais métricas de risco de cauda (Ômega, Kappa-3, CDaR), as abordagens ingênuas (1/N, InvVol) e a aplicação do teto de concentração.

### [PROBLEMA LOGICO/ESTRUTURAL] - Cap. 3 / Metodologia (Síntese e Limitações)
**Descricao:** A quantificação do custo transacional está faltando no texto da metodologia (provavelmente por erro de compilação/digitação de uma variável matemática), aparecendo apenas um espaço em branco. Contudo, o valor de "50 basis points" surge diretamente nos Capítulos 4 e 5 sem ter sido formalmente introduzido no Cap 3.
**Trecho relevante (original):** "Terceiro, o custo transacional é modelado como uma taxa proporcional fixa de sobre o giro, não capturando spreads..."
**Impacto na avaliacao da banca:** COMPROMETE_NOTA
**Sugestao de acao:** Preencher a lacuna com o valor utilizado no backtest. Reformular para: "Terceiro, o custo transacional é modelado como uma taxa proporcional fixa de 50 basis points (0,5%) sobre o giro..."

### [PROBLEMA LOGICO/ESTRUTURAL] - Cap. 5 / Sugestões para Pesquisas Futuras
**Descricao:** A forma como a sugestão de redes neurais é redigida expõe uma mudança de planejamento, sugerindo à banca que o trabalho entregue falhou em atingir a proposta original. Isso desvaloriza os excelentes resultados obtidos com o Momentum 12-1 e pode gerar perguntas indesejadas sobre por que os modelos LSTM "não foram implementados".
**Trecho relevante (original):** "A proposta original deste trabalho contemplava a geração de visões por redes neurais recorrentes (LSTM) e modelos ARIMA, não implementada na versão final em favor do fator de momentum."
**Impacto na avaliacao da banca:** GERA_QUESTIONAMENTO
**Sugestao de acao:** Reformular a frase para soar como um próximo passo evolutivo, e não como uma falha do presente projeto. Excluir a confissão de abandono da proposta. Sugestão: "Como extensão natural, sugere-se a geração de visões por modelos preditivos de aprendizado de máquina, como redes neurais recorrentes (LSTM) e ARIMA, comparando-os diretamente contra o fator de momentum..."

---

### NOTAS DE AUDITORIA (Pontos de Atenção Verificados)
- **O problema de pesquisa está definido na Intro?** Sim, está claro e alinhado com a conclusão.
- **As limitações do Cap 3 aparecem no Cap 4?** Sim. O parâmetro $\lambda = 2,5$ e as deficiências em capturar os custos de transação na totalidade para carteiras de alto giro são retomados e discutidos no Capítulo 4.
- **Metodologia x Resultados:** A correlação de métodos é sólida. Os 16 modelos detalhados no Capítulo 3 batem 100% com os tabelados no Capítulo 4.
- **Discussão dos Resultados:** Muito bem executada. Os resultados não são apenas descritos, mas interpretados à luz das teorias (ex: confirmação do Paradoxo do 1/N, robustez da Mínima Variância). 
- **O MaxDD de -81,81% do MinCDaR é discutido?** Sim, foi dedicada uma seção inteira (4.4 - "O Caso de Degeneração do Mínimo CDaR") explicando a falha da métrica dependente da trajetória em subperíodos de múltiplos choques, demonstrando alta profundidade analítica.
