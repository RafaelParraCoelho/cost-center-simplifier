import pandas as pd

xls = pd.ExcelFile("Ultimo custo.xlsx")

for sheet_name in xls.sheet_names:
    print(f"\nProcessando aba: {sheet_name}")
    
    # Usa a segunda linha (índice 1) como cabeçalho
    df = pd.read_excel(xls, sheet_name=sheet_name, header=1)
    print("Colunas detectadas:", list(df.columns))

    col_cod = "Cod. Volpe"
    col_custo = "Custo unit."

    if col_cod not in df.columns or col_custo not in df.columns:
        print("⚠️ Não achei as colunas esperadas.")
        continue

    # Converte para número (substitui vírgula por ponto antes)
    df[col_custo] = (
        df[col_custo]
        .astype(str)
        .str.replace(",", ".")
        .astype(float)
    )

    # Arredonda e garante que vai sair com ponto decimal
    df["VALOR_ARRED"] = df[col_custo].round(2).astype(str)

    updates = []
    for _, row in df.iterrows():
        if pd.notna(row[col_cod]) and pd.notna(row[col_custo]):
            sql = f"UPDATE TB_PRODUTOS SET VL_CUSTOULTLIQ = {row['VALOR_ARRED']} WHERE PK_ID = '{row[col_cod]}';"
            updates.append(sql)

    print(f"👉 Linhas processadas: {len(updates)}")

    # Mostra os 5 primeiros para conferência
    print("\nExemplo de updates:")
    for u in updates[:5]:
        print(u)

    if updates:
        output_file = f"updates_{sheet_name}.sql"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(updates))
        print(f"✅ Arquivo {output_file} gerado.")
