from django.shortcuts import render

from products.models import Product

# Create your views here.

# View para listas os produtos
# Toda view recebe um request como argumento e precisa retornar uma resposta
def list_products(request):
    # Lendo todos os produtos
    products = Product.objects.all()

    # O contexto é sempre um dicionario
    context = {
        'products': products,
        'products_empty': []
    }

    # Retorna um render(request, nomeDoTemplate, contexto)
    # Criar a pasta do template na mão, na pasta products: uma pasta templates -> products -> list.html
    return render(request, 'products/list.html', context=context)