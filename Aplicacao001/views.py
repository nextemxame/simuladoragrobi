from django.shortcuts import render
from django.views import View

import pickle


class Inicial(View):

    # Pegando Informação
    def get(self, request):
        return render ( request, 'Pagina_Inicial.html' )

    # Enviando informação
    def post(self, request):

        # Selecionado a informação da Pesquisa
        Pesquisar_Idade = request.POST.get('Idade', None)
        Pesquisar_Renda = request.POST.get('Renda', None)
        Pesquisar_TipoRenda = request.POST.get('TipoRenda', None)
        Pesquisar_Score = request.POST.get('Score', None)
        Pesquisar_Restricao = request.POST.get('Restricao', None)

        # Modelo Treinado
        with open('Estaticos/Modelo_Treinado/Regressao_Linear.pkl', 'rb') as f:
            Funcao_Regressao = pickle.load(f)

        # Previsao
        Limite = Funcao_Regressao.predict( [[
            Pesquisar_Idade,
            Pesquisar_Renda,
            Pesquisar_TipoRenda,
            Pesquisar_Score,
            Pesquisar_Restricao
        ]] )

        # Retonando
        return render(request, 'Pagina_Inicial.html', {
            'Limite' : round ( Limite[0][0], 2 ) }
        )
