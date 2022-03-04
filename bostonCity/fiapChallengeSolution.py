# Qual o total de voos internacionais que partiram do aeroporto no ano de 2014?
with open("economic-indicators.csv", "r") as boston:
    total = 0
    for linha in boston.readlines()[1:-1]:
        total = total+float(linha.split(",")[3])
    print("Total de voos computados: ", total)

# Quando (mês/ano) ocorreu o maior trânsito de passageiros no aeroporto de Logan?
with open("economic-indicators.csv", "r") as boston:
    janeiro2013 = 0; janeiro2014 = 0; janeiro2015 = 0; fevereiro2013 = 0; fevereiro2014 = 0; marco2013 = 0; marco2014 = 0;
    abril2013 = 0; abril2014 = 0; maio2013 = 0; maio2014 = 0; junho2013 = 0; junho2014 = 0; julho2013 = 0; julho2014 = 0;
    agosto2013 = 0; agosto2014 = 0; setembro2013 = 0; setembro2014 =  outubro2013 = 0; outubro2014 = 0; novembro2013 = 0;
    novembro2014 = 0; dezembro2013 = 0; dezembro2014 = 0;

    for linha in boston.readlines()[1:-1]:
        if linha.split(",")[1] == "1" and linha.split(",")[0] == "2013":
            janeiro2013 = janeiro2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "1" and linha.split(",")[0] == "2014":
            janeiro2014 = janeiro2014 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "1" and linha.split(",")[0] == "2015":
            janeiro2015 = janeiro2015 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "2" and linha.split(",")[0] == "2013":
            fevereiro2013 = fevereiro2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "2" and linha.split(",")[0] == "2014":
            fevereiro2014 = fevereiro2014 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "3" and linha.split(",")[0] == "2013":
            marco2013 = marco2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "3" and linha.split(",")[0] == "2014":
            marco2014 = marco2014 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "4" and linha.split(",")[0] == "2013":
            abril2013 = abril2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "4" and linha.split(",")[0] == "2014":
            abril2014 = abril2014 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "5" and linha.split(",")[0] == "2013":
            maio2013 = maio2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "5" and linha.split(",")[0] == "2014":
            maio2014 = maio2014 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "6" and linha.split(",")[0] == "2013":
            junho2013 = junho2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "6" and linha.split(",")[0] == "2014":
            junho2014 = junho2014 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "7" and linha.split(",")[0] == "2013":
            julho2013 = julho2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "7" and linha.split(",")[0] == "2014":
            julho2014 = julho2014 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "8" and linha.split(",")[0] == "2013":
            agosto2013 = agosto2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "8" and linha.split(",")[0] == "2014":
            agosto2014 = agosto2014 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "9" and linha.split(",")[0] == "2013":
            setembro2013 = setembro2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "9" and linha.split(",")[0] == "2014":
            setembro2014 = setembro2014 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "10" and linha.split(",")[0] == "2013":
            outubro2013 = outubro2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "10" and linha.split(",")[0] == "2014":
            outubro2014 = outubro2014 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "11" and linha.split(",")[0] == "2013":
            novembro2013 = novembro2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "11" and linha.split(",")[0] == "2014":
            novembro2014 = novembro2014 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "12" and linha.split(",")[0] == "2013":
            dezembro2013 = dezembro2013 + float(linha.split(",")[2])
        elif linha.split(",")[1] == "12" and linha.split(",")[0] == "2014":
            dezembro2014 = dezembro2014 + float(linha.split(",")[2])

    meses = {}
    meses["Janeiro de 2013"] = [janeiro2013]; meses["Fevereiro de 2013"] = [fevereiro2013]; meses["Março de 2013"] = [marco2013];
    meses["Abril"] = [abril2013]; meses["Maio de 2013"] = [maio2013]; meses["Junho de 2013"] = [junho2013];
    meses["Julho de 2013"] = [julho2013]; meses["Agosto de 2013"] = [agosto2013]; meses["Setembro"] = [setembro2013];
    meses["Outubro de 2013"] = [outubro2013]; meses["Novembro de 2013"] = [novembro2013];
    meses["Dezembro de 2013"] = [dezembro2013]

    meses["Janeiro de 2014"] = [janeiro2014]; meses["Fevereiro de 2014"] = [fevereiro2014]; meses["Março de 2014"] = [marco2014];
    meses["Abril"] = [abril2014]; meses["Maio de 2014"] = [maio2014]; meses["Junho de 2014"] = [junho2014];
    meses["Julho de 2014"] = [julho2014]; meses["Agosto de 2014"] = [agosto2014]; meses["Setembro"] = [setembro2014];
    meses["Outubro de 2014"] = [outubro2014]; meses["Novembro de 2014"] = [novembro2014];
    meses["Dezembro de 2014"] = [dezembro2014]

    lista = []

    for mes in meses:
        #print(str(mes) + ": " + str(meses.get(mes)))
        lista.append(meses.get(mes))

    maior = max(lista)
    maior = maior[0]
    #print(maior)

    for mes in meses:
        if meses.get(mes)[0] == maior:
            mesMaisMovimentado = mes
    print("Em " + str(mesMaisMovimentado.lower()) + " foi quando ocorreu o maior trânsito de passageiros no aeroporto de Logan.")

#  Qual o total de passageiros que passaram pelo aeroporto de Logan, no ano que for especificado pelo usuário?
anoEscolhido = input("Usuário, insira um ano para ser filtrado: ")
with open("economic-indicators.csv", "r") as boston:
    passageiros = []
    for linha in boston.readlines()[1:-1]:
        if linha.split(",")[0] == anoEscolhido:
            #print(linha.split(",")[2])
            passageiros.append(float(linha.split(",")[2]))

somaPassageiros = sum(passageiros)

print(str(somaPassageiros) + " é o total de passageiros que passaram pelo aeroporto de Logan em " + str(anoEscolhido) + ".")

# Qual o mês que possui a maior média da diária de um hotel com base no ano especificado pelo usuário?
anoEscolhido = input("Usuário, insira um ano para ser filtrado: ")
listaMeses = {}
with open("economic-indicators.csv", "r") as boston:
    for linha in boston.readlines()[1:-1]:
        if linha.split(",")[0] == anoEscolhido:
            listaMeses[linha.split(",")[1]] = [linha.split(",")[5]]

listaValores = []
for mes in listaMeses:
    listaValores.append(listaMeses.get(mes))

i = 0
for item in listaValores:
    listaValores[i] = str(listaValores[i])
    listaValores[i] = str(listaValores[i].replace('[', ""))
    listaValores[i] = str(listaValores[i].replace(']', ""))
    listaValores[i] = str(listaValores[i].replace("'", ""))
    i = i + 1

maiorMedia = max(listaValores)

i = 0
for mes in listaMeses:
    if listaValores[i] == maiorMedia:
        chaveNecessaria = i + 1
    i = i + 1

mesDaMaiorMedia = "TBA"
if chaveNecessaria == 1:
    mesDaMaiorMedia = "janeiro"
elif chaveNecessaria == 2:
    mesDaMaiorMedia = "fevereiro"
elif chaveNecessaria == 3:
    mesDaMaiorMedia = "março"
elif chaveNecessaria == 4:
    mesDaMaiorMedia = "abril"
elif chaveNecessaria == 5:
    mesDaMaiorMedia = "maio"
elif chaveNecessaria == 6:
    mesDaMaiorMedia = "junho"
elif chaveNecessaria == 7:
    mesDaMaiorMedia = "julho"
elif chaveNecessaria == 8:
    mesDaMaiorMedia = "agosto"
elif chaveNecessaria == 9:
    mesDaMaiorMedia = "setembro"
elif chaveNecessaria == 10:
    mesDaMaiorMedia = "outubro"
elif chaveNecessaria == 11:
    mesDaMaiorMedia = "novembro"
elif chaveNecessaria == 12:
    mesDaMaiorMedia = "dezembro"

print("O mês que possui a maior média de um hotel no ano de " + str(anoEscolhido) + " é " + str(mesDaMaiorMedia) + ".")