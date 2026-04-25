programa {
  funcao inicio() {
    cadeia nome
     real peso , altura , imc
     escreva("Digite o primeiro peso: ")
     leia(peso)
     escreva("Digite o primeiro altura: ")
     leia(altura)
     imc = peso / (altura * altura)
     escreva("o resultado do imc é: ",imc)

     escreva("digite seu nome: ")
     leia(nome)
     escreva ("digite seu peso: ")
    leia(peso)
    escreva("Digite sua altura: ")
    leia(altura)

    // nao esquecer de colocar a multplicacao
    // emtre parenteses (altura * altura)
    imc = peso / (altura * altura)
    escreva("---bem vindo---", nome)
    escreva("seu imc é: ", imc )
}
}
