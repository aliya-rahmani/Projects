def debt_calc(emprestimo, taxa_juros_mensal, pagamento_mensal):
    #Calculate how much time it would take to pay a debt
    #Returns time in months
    divida = emprestimo
    t=0
    while(divida > 0):
        t+=1
        divida -= pagamento_mensal - divida*taxa_juros_mensal
    return t