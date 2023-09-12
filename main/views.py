from django.shortcuts import render

# Create your views here.
def show_main(request):
    products = [
        {
            'image_url': 'https://pictures.abebooks.com/isbn/9780132306331-us.jpg',
            'name': 'Calculus 9th Edition',
            'author': 'Edwin J. Purcell',
            'year': 2008,
            'publisher': 'Pearson',
            'genre': 'Non Fiction',
            'description': 'Kalkulus Purcell adalah buku teks kalkulus klasik yang membahas semua topik kalkulus dasar, termasuk limit, turunan, integral, deret, dan transformasi Laplace. Buku ini terkenal dengan penjelasannya yang jelas dan ringkas, serta contoh dan latihannya yang variatif.',
            'rating': 4.5,
            'amount': 7,
        }
    ]

    context = {
        'products': products
    }
    return render(request, 'main.html', context)
