# 📊 Simplificação de Central de Custo  

Este script em **Python** automatiza a extração e transformação de dados de planilhas de custo em **queries SQL de atualização**, eliminando a necessidade de ajustes manuais e tornando o processo mais rápido, confiável e padronizado.  

## 🚀 Funcionalidade  

- Lê todas as abas de um arquivo Excel (`Ultimo custo.xlsx`).  
- Define a segunda linha como cabeçalho (caso o Excel contenha títulos acima da tabela).  
- Identifica as colunas **`Cod. Volpe`** (chave de produto) e **`Custo unit.`** (valor do custo).  
- Converte valores de custo para **float** (aceitando vírgulas como separador decimal).  
- Arredonda os valores para **2 casas decimais**.  
- Gera instruções SQL no formato:  

