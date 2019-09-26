from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')

    def __str__(self):
        # Exemplo de return: 'Category1 - 10'
        return f'{self.name} - {self.products.count()}'


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    price = models.DecimalField(
        'Preço', 
        max_digits=8,  # Máximo de dígitos totais
        decimal_places=2  # Máximo de dígitos decimais, ou seja, 6 dígitos antes da virgula e 2 depois
        )

    # Dependencia do objeto Product com o Category
    category = models.ForeignKey(
        Category,
        on_delete = models.deletion.DO_NOTHING,
        related_name='products'
    )

    def __str__(self):
        return self.name


'''
====================================================

	INSTALANDO FERRAMENTA IPYTHON

$ pip install ipython

====================================================

	RODANDO FERRAMENTA IPYTHON

$ python manage.py shell


# Importa os objetos Product e Category
$$ from products.models import Product, Category

# Cria a categoria
$$ category = Category.objects.create(name='Category1', description='Desc1')

# Verificar se salvou no banco
# Se for um objeto que não ta salvo no banco ele retorna none
$$ category.pk
### retorna 1


# Criando vários produtos
$$ for i in range(10):
	product = Product()
	product.name = f'Product{i}'
	product.description = f'Prod Desc{i}'
	product.price = i * 0.5
	product.category = category
	product.save()


# Verificando os produtos no banco
$$ Product.objects.all()
### retorna algo assim: <QuerySet [<Product: Product0>, <Product: Product1>, <Product: Product2>, <Product: Product3>, <Product: Product4>, <Product: Product5>, <Product: Product6>, <Product: Product7>, <Product: Product8>, <Product: Product9>]>


# Verificando quantos produtos tem no banco
$$ Product.objects.count()
### retornou 10


# Verificando quantos produtos tem uma categoria especifica no banco
$$ str(category)
### retornou 'Category1 - 10'


# Saindo do shell
$$ exit
'''