from blog.models import image


def image():
    image = list(image)
    return image
    # return [
    #     {
    #         'id': 1,
    #         'photo': 'https://portal-amb-imgs.clubedaana.com.br/2019/01/pizza-de-frango-com-catupiry-18845.jpg',
    #         'name': 'Pizza de Frango com Catupiry',
    #         'description': 'Frango e Catupiry',
    #         'price': 20.50
    #     },
    #     {
    #         'id': 2,
    #         'photo': 'https://img.itdg.com.br/tdg/images/recipes/000/002/807/96170/96170_original.jpg?mode=crop&width=710&height=400',
    #         'name': 'Pizza Portuguesa',
    #         'description': 'Presunto, ovo, ervilha, queijo e cebola.',
    #         'price': 30.20
    #     },
    # ]
