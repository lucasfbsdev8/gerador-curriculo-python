ARQ_PESSOAIS = "pessoais.txt"
ARQ_PROFISSIONAIS = "profissionais.txt"
ARQ_FORMACAO = "formacao.txt"
ARQ_QUALIDADES = "qualidades.txt"
ARQ_IDIOMAS = "idiomas.txt"
ARQ_SAIDA_HTML = "curriculo.html"


def ler_dados_pessoais():
    print("\n=== INFORMAÇÕES PESSOAIS ===")
    nome = input("Nome completo: ").strip()
    data_nasc = input("Data de nascimento: ").strip()
    endereco = input("Endereço (cidade/UF): ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    linkedin = input("Usuário LinkedIn: ").strip()
    foto = input("Nome do arquivo de foto (ex: foto.jpg, deve estar na mesma pasta): ").strip()

    with open(ARQ_PESSOAIS, "w", encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")
        arquivo.write(data_nasc + "\n")
        arquivo.write(endereco + "\n")
        arquivo.write(telefone + "\n")
        arquivo.write(email + "\n")
        arquivo.write(linkedin + "\n")
        arquivo.write(foto + "\n")


def ler_dados_profissionais():
    print("\n=== INFORMAÇÕES PROFISSIONAIS ===")
    cargo_pretendido = input("Cargo atual / pretendido: ").strip()
    objetivo = input("Objetivo profissional: ").strip()
    resumo = input("Resumo Profissional: ").strip()

    with open(ARQ_PROFISSIONAIS, "w", encoding="utf-8") as arquivo:
        arquivo.write(cargo_pretendido + "\n")
        arquivo.write(objetivo + "\n")
        arquivo.write(resumo + "\n")

        print("Cadastro de experiências profissionais.")
        print("Digite 'fim' no campo Empresa para encerrar a lista.")
        empresa = input("Empresa: ").strip()

        while empresa.lower() != "fim":
            cargo = input("Cargo ocupado: ").strip()
            tempo = input("Período (ex: 2020-2022): ").strip()
            arquivo.write("EXP|" + empresa + "|" + cargo + "|" + tempo + "\n")
            empresa = input("Empresa (ou 'fim' para encerrar): ").strip()

def ler_dados_academicos():
    print("\n=== FORMAÇÃO ACADÊMICA ===")
    print("Cadastro de formações acadêmicas. Informe pelo menos 1.")
 
    with open(ARQ_FORMACAO, "w", encoding="utf-8") as arquivo:
        continuar = "S"
        while continuar.upper() == "S":
            instituicao = input("Instituição: ").strip()
            graduacao = input("Curso: ").strip()
            conclusao = input("Situação (Concluído / Em Andamento): ").strip()
 
            if conclusao == "Concluído":
                ano = input("Ano de Conclusão: ").strip()
                arquivo.write(f"FORM|{instituicao}|{graduacao}|{conclusao}|{ano}|\n")
            else:
                periodo = input("Data de Início: ").strip()
                termino = input("Previsão de Término (ex: 2029): ").strip()
                arquivo.write(f"FORM|{instituicao}|{graduacao}|{conclusao}|{periodo}|{termino}\n")
 
            continuar = input("Adicionar outra formação acadêmica? [S/N]: ").strip()


def ler_qualidades():
    print("\n=== QUALIDADES ===")
    print("Cadastro de qualidades. Informe pelo menos 3.")
    print("Digite 'fim' para encerrar a lista.")
 
    with open(ARQ_QUALIDADES, "w", encoding="utf-8") as arquivo:
        qualidade = input("Qualidade: ").strip()
        while qualidade.lower() != "fim":
            arquivo.write(qualidade + "\n")
            qualidade = input("Qualidade (ou 'fim' para encerrar): ").strip()


def ler_idiomas():
    print("\n=== IDIOMAS ===")
    print("Cadastro de idiomas. Informe pelo menos 3.")
    print("Digite 'fim' no campo Idioma para encerrar a lista.")

    with open(ARQ_IDIOMAS, "w", encoding="utf-8") as arquivo:
        idioma = input("Idioma: ").strip()
        while idioma.lower() != "fim":
            nivel = input("Nível (Básico/Intermediário/Avançado/Fluente): ").strip()
            arquivo.write(idioma + "|" + nivel + "\n")
            idioma = input("Idioma (ou 'fim' para encerrar): ").strip()


def gerar_curriculo_html():
    with open(ARQ_PESSOAIS, encoding="utf-8") as arquivo:
        linhas = [linha.strip() for linha in arquivo.readlines()]
    nome, data_nasc, endereco, telefone, email, linkedin, foto = linhas[0:7]

    with open(ARQ_PROFISSIONAIS, encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    cargo_pretendido = linhas[0].strip()
    objetivo = linhas[1].strip()
    resumo = linhas[2].strip()

    experiencias = []
    for linha in linhas[2:]:
        partes = linha.strip().split("|")
        if partes[0] == "EXP":
            experiencias.append((partes[1], partes[2], partes[3]))

    formacoes = []
    with open(ARQ_FORMACAO, encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            partes = linha.strip().split("|")
            if partes[0] == "FORM":
                formacoes.append(partes[1:])

    qualidades = []
    with open(ARQ_QUALIDADES, encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            qualidades.append(linha.strip())

    idiomas = []
    with open(ARQ_IDIOMAS, encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            idioma, nivel = linha.strip().split("|")
            idiomas.append((idioma, nivel))

    linhas = []

    linhas.append("<!DOCTYPE html>\n")
    linhas.append('<html lang="pt-br">\n')
    linhas.append("<head>\n")
    linhas.append('<meta charset="UTF-8">\n')
    linhas.append(f"<title>Currículo - {nome}</title>\n")
    linhas.append("<style>\n")
    linhas.append("    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');\n")
    linhas.append("    body { font-family: 'Poppins', 'Segoe UI', sans-serif; background-color: #eef2f7; margin: 0; padding: 0; color: #2b2b2b; }\n")
    linhas.append("    .container { max-width: 800px; margin: 30px auto; background: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.15); }\n")
    linhas.append("    header { background: linear-gradient(135deg, #1f3c88, #274b9f); color: #ffffff; display: flex; align-items: center; padding: 25px; }\n")
    linhas.append("    header img { width: 130px; height: 130px; border-radius: 50%; object-fit: cover; border: 4px solid #ffffff; margin-right: 25px; }\n")
    linhas.append("    header h1 { margin: 0 0 5px 0; font-size: 28px; }\n")
    linhas.append("    a { color: #ffffff; text-decoration: none; \n}")
    linhas.append("    header p { margin: 2px 0; font-size: 14px; color: #dbe4ff; }\n")
    linhas.append("    section { padding: 20px 30px; border-bottom: 1px solid #e0e0e0; }\n")
    linhas.append("    section h2 { color: #1f3c88; border-left: 5px solid #f2a71b; padding-left: 10px; font-size: 19px; margin-bottom: 15px; }\n")
    linhas.append("    .item { margin-bottom: 10px; line-height: 1.4; }\n")
    linhas.append("    .periodo { color: #777; font-size: 13px; }\n")
    linhas.append("    ul { list-style: none; padding-left: 0; }\n")
    linhas.append("    ul li { background: #f2f6ff; margin-bottom: 6px; padding: 8px 12px; border-radius: 6px; }\n")
    linhas.append("    .qualidades ul { display: flex; flex-wrap: wrap; gap: 8px; }\n")
    linhas.append("    .qualidades ul li { background: #fff3da; color: #8a5600; margin-bottom: 0; }\n")
    linhas.append("</style>\n")
    linhas.append("</head>\n")
    linhas.append("<body>\n")
    linhas.append('    <div class="container">\n')
    linhas.append("        <header>\n")
    linhas.append(f'            <img src="{foto}" alt="Foto de {nome}">\n')
    linhas.append("            <div>\n")
    linhas.append(f"                <h1>{nome}</h1>\n")
    linhas.append(f"                <p>{cargo_pretendido}</p>\n")
    linhas.append(f"                <p>{telefone} | {email} | <a href='https://www.linkedin.com/in/{linkedin}/'>{linkedin}</a></p>\n")
    linhas.append(f"                <p>{endereco} — Nascimento: {data_nasc}</p>\n")
    linhas.append("            </div>\n")
    linhas.append("        </header>\n")
    linhas.append("        <section>\n")
    linhas.append("            <h2>Objetivo Profissional</h2>\n")
    linhas.append(f'            <div class="item">{objetivo}</div>\n')
    linhas.append("        </section>\n")
    linhas.append("        <section>\n")
    linhas.append("            <h2>Resumo Profissional</h2>\n")
    linhas.append(f'            <div class="item">{resumo}</div>\n')
    linhas.append("        </section>\n")
    linhas.append("        <section>\n")
    linhas.append("            <h2>Experiências Profissionais</h2>\n")
    if experiencias:
        for empresa, cargo, tempo in experiencias:
            linhas.append('            <div class="item">\n')
            linhas.append(f"                <strong>{cargo}</strong> — {empresa}\n")
            linhas.append(f'                <span class="periodo">({tempo})</span>\n')
            linhas.append("            </div>\n")
    else:
        linhas.append('            <div class="item">Nenhuma experiência cadastrada.</div>\n')
    linhas.append("        </section>\n")
    linhas.append("        <section>\n")
    linhas.append("            <h2>Formação Acadêmica</h2>\n")
    if formacoes:
        for instituicao, graduacao, conclusao, campo4, campo5 in formacoes:
            linhas.append('            <div class="item">\n')
            linhas.append(f"                <strong>{graduacao}</strong> — {instituicao}\n")
            if conclusao == "Concluído":
                linhas.append(f'                <span class="periodo">(Concluído em {campo4})</span>\n')
            else:
                linhas.append(f'                <span class="periodo">(Em andamento: {campo4} - {campo5})</span>\n')
            linhas.append("            </div>\n")
    else:
        linhas.append('            <div class="item">Nenhuma formação cadastrada.</div>\n')
    linhas.append("        </section>\n")
    linhas.append('        <section class="qualidades">\n')
    linhas.append("            <h2>Qualidades</h2>\n")
    linhas.append("            <ul>\n")
    if qualidades:
        for qualidade in qualidades:
            linhas.append(f"                <li>{qualidade}</li>\n")
    else:
        linhas.append("                <li>Nenhuma qualidade cadastrada.</li>\n")
    linhas.append("            </ul>\n")
    linhas.append("        </section>\n")
    linhas.append("        <section>\n")
    linhas.append("            <h2>Idiomas</h2>\n")
    linhas.append("            <ul>\n")
    if idiomas:
        for idioma, nivel in idiomas:
            linhas.append(f"                <li>{idioma} — <em>{nivel}</em></li>\n")
    else:
        linhas.append("                <li>Nenhum idioma cadastrado.</li>\n")
    linhas.append("            </ul>\n")
    linhas.append("        </section>\n")

    linhas.append("    </div>\n")
    linhas.append("</body>\n")
    linhas.append("</html>\n")

    with open(ARQ_SAIDA_HTML, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(linhas)

def main():
    print("=== GERADOR DE CURRÍCULO EM HTML ===")
    ler_dados_pessoais()
    ler_dados_profissionais()
    ler_dados_academicos()
    ler_qualidades()
    ler_idiomas()
    gerar_curriculo_html()
    print(f"\nCurrículo gerado com sucesso: {ARQ_SAIDA_HTML}")


if __name__ == "__main__":
    main()