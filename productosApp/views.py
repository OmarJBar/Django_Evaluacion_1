from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static

# Create your views here.

def index(request):
    return render(request, 'views/index.html')

def vista_form_productos(request):
    if request.method == 'POST':
        userName = request.POST.get('userName', '')
        return render(request, 'views/products.html', {'userName': userName})
    else:
        return form_case_error(request)

def form_case_error(request):
    
    docHtml = """
        <html>
        <head>
            <meta charset='utf-8'>
            <meta http-equiv='X-UA-Compatible' content='IE=edge'>
            <title>index</title>
            <meta name='viewport' content='width=device-width, initial-scale=1'>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">    <script src='main.js'></script>
            <link href="signin.css" rel="stylesheet">
        </head>
        <body class="text-center">
            <div class="container mt-5">
                <div class="row">
                    <div class="col-md-6 offset-md-3">
                        <div class="alert alert-danger" role="alert">
                            <h4 class="alert-heading">Inicio de Sesión Fallido</h4>
                            <p>Las credenciales ingresadas son incorrectas. Por favor, intenta nuevamente.</p>
                        </div>
                        <a href="/" class="btn btn-primary">Volver al Inicio de Sesión</a>
                    </div>
                </div>
            </div>

            <!-- Agrega enlaces a los archivos JavaScript de Bootstrap (jQuery y Popper.js) -->
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        </body>
        </html>
                """

    return HttpResponse(docHtml)

def viewPoleras(request):
    data ={"producto1": productTemplate("Poleras.png", "polera1"),
           "producto2": productTemplate("Poleras.png", "polera2"),
           "producto3": productTemplate("Poleras.png", "polera3")}
    
    return render(request, 'views/productTemplate.html', data)

def viewJuguetes(request):
    data ={"producto1": productTemplate("Juguetes.png", "juguete1"),
           "producto2": productTemplate("Juguetes.png", "juguete2"),
           "producto3": productTemplate("Juguetes.png", "juguete3")}
    
    return render(request, 'views/productTemplate.html', data)

def viewElectronica(request):
    data ={"producto1": productTemplate("Electronica1.png", "electronica1"),
           "producto2": productTemplate("Electronica2.png", "electronica2"),
           "producto3": productTemplate("Electronica3.png", "electronica3")}
    
    return render(request, 'views/productTemplate.html', data)

def productTemplate(imagen, nombre):
    imgUrl = static(f'img/{imagen}')
    return f"""
                    <div class="col-md-4 mb-4">
                        <div class="card">
                            <img src="{ imgUrl}" class="card-img-top" alt="Producto 1">
                            <div class="card-body">
                                <h5 class="card-title">{nombre}</h5>
                                <a href="#" class="btn btn-primary">Ver mas</a>
                            </div>
                        </div>
                    </div>
         """
    