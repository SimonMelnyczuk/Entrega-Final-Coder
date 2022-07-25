from django.shortcuts import render, redirect
from CoderApp.models import Planta
from CoderApp.models import Arbol
from CoderApp.models import Cactus
from CoderApp.forms import PlantaFormulario, ArbolFormulario, CactusFormulario , UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def inicio(request):
     return render(request,"inicio.html")

def planta(request):
     planta = Planta.objects.all()
     print(planta)
     return render(request,"planta.html",{'planta':planta})

def arbol(request):
     arbol = Arbol.objects.all()
     print(arbol)
     return render(request,"arbol.html",{'arboles':arbol})

def cactus(request):
     cactus = Cactus.objects.all()
     print(cactus)
     return render(request,"cactus.html",{'cactus':cactus})

def registrarArbol(request):
     print(request.POST)
     nombre = request.POST['txtnombre']
     nombreCientifico = request.POST['txtnombreCientifico']
     alturaMax = request.POST['txtalturaMax']

     arbol = Arbol.objects.create(nombre=nombre, nombreCientifico=nombreCientifico, alturaMax=alturaMax)

     return redirect('arbol')

def registrarPlanta(request):
     print(request.POST)
     nombre = request.POST['txtnombre']
     nombreCientifico = request.POST['txtnombreCientifico']
     deInterior = request.POST['txtdeInterior']

     planta = Planta.objects.create(nombre=nombre, nombreCientifico=nombreCientifico, deInterior=deInterior)

     return redirect('planta')

def registrarCactus(request):
     print(request.POST)
     nombre = request.POST['txtnombre']
     nombreCientifico = request.POST['txtnombreCientifico']
     diasSinAgua = request.POST['txtdiasSinAgua']

     cactus = Cactus.objects.create(nombre=nombre, nombreCientifico=nombreCientifico, diasSinAgua=diasSinAgua)

     return redirect('cactus')

def buscarCactus(request):

     if  request.POST["nombre"]:
 
          nombre = request.POST['nombre'] 
          cactus = Cactus.objects.filter(nombre__icontains=nombre)
          return render(request, "cactus.html", {"cactus":cactus})
            
     else: 
	     respuesta = "No enviaste datos"
     return render(request,"resultadoBusqueda.html")



def buscarPlanta(request):

     if  request.POST["nombre"]:
 
          nombre = request.POST['nombre'] 
          planta = Planta.objects.filter(nombre__icontains=nombre)
          return render(request, "planta.html", {"planta":planta})
            
     else: 
	     respuesta = "No enviaste datos"
     return render(request,"resultadoBusqueda.html")

def buscarArbol(request):

     if  request.POST["nombre"]:
 
          nombre = request.POST['nombre'] 
          arbol = Arbol.objects.filter(nombre__icontains=nombre)
          return render(request, "arbol.html", {"arbol":arbol})
            
     else: 
	     respuesta = "No enviaste datos"
     return render(request,"resultadoBusqueda.html")

@login_required
def leerPlantas(request):
     if request.user.is_staff:
      plantas = Planta.objects.all()
      contexto= {'plantas':plantas}
      return render(request,'leerPlantas.html',contexto)
     else:
          return render(request,'needAdmin.html')

@login_required
def leerArboles(request):
     if request.user.is_staff:
      arboles = Arbol.objects.all()
      contexto= {'arboles':arboles}
      return render(request,'leerArboles.html',contexto)
     else:
          return render(request,'needAdmin.html')

@login_required
def leerCactus(request):
     if request.user.is_staff:
      cactus = Cactus.objects.all()
      contexto= {'cactus':cactus}
      return render(request,'leerCactus.html',contexto)
     else:
          return render(request,'needAdmin.html')

def eliminarPlanta(request,planta_nombre):
     planta = Planta.objects.get(nombre=planta_nombre)
     planta.delete()
     plantas= Planta.objects.all()
     contexto={'plantas':plantas}
     return render(request,'leerPlantas.html',contexto) 

def eliminarArbol(request,arbol_nombre):
     arbol = Arbol.objects.get(nombre=arbol_nombre)
     arbol.delete()
     arboles= Arbol.objects.all()
     contexto={'arboles':arboles}
     return render(request,'leerArboles.html',contexto) 

def eliminarCactus(request,cactus_nombre):
     cactus = Cactus.objects.get(nombre=cactus_nombre)
     cactus.delete()
     cactus= Cactus.objects.all()
     contexto={'cactus':cactus}
     return render(request,'leerCactus.html',contexto)      

def editarPlanta(request, planta_nombre):

      planta = Planta.objects.get(nombre=planta_nombre)

      if request.method == 'POST':

            miFormulario = PlantaFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  planta.nombre = informacion['nombre']
                  planta.nombreCientifico = informacion['nombreCientifico']
                  planta.deInterior= informacion['deInterior']                
                  planta.save()

                  return render(request, "inicio.html")  
      else: 
            miFormulario= PlantaFormulario(initial={'nombre': planta.nombre, 'nombreCientifico':planta.nombreCientifico , 
            'deInterior':planta.deInterior}) 
      return render(request, "editarPlanta.html", {"miFormulario":miFormulario, "planta_nombre":planta_nombre})

def editarArbol(request, arbol_nombre):

      arbol = Arbol.objects.get(nombre=arbol_nombre)

      if request.method == 'POST':

            miFormulario = ArbolFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  arbol.nombre = informacion['nombre']
                  arbol.nombreCientifico = informacion['nombreCientifico']
                  arbol.alturaMax= informacion['alturaMax']                
                  arbol.save()

                  return render(request, "inicio.html")  
      else: 
            miFormulario= ArbolFormulario(initial={'nombre': arbol.nombre, 'nombreCientifico':arbol.nombreCientifico , 
            'alturaMax':arbol.alturaMax})
      return render(request, "editarArbol.html", {"miFormulario":miFormulario, "arbol_nombre":arbol_nombre})

def editarCactus(request, cactus_nombre):

      cactus = Cactus.objects.get(nombre=cactus_nombre)

      if request.method == 'POST':

            miFormulario = CactusFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  cactus.nombre = informacion['nombre']
                  cactus.nombreCientifico = informacion['nombreCientifico']
                  cactus.diasSinAgua= informacion['diasSinAgua']                
                  cactus.save()

                  return render(request, "inicio.html")  
      else: 
            miFormulario= CactusFormulario(initial={'nombre': cactus.nombre, 'nombreCientifico':cactus.nombreCientifico , 
            'diasSinAgua':cactus.diasSinAgua})
      return render(request, "editarCactus.html", {"miFormulario":miFormulario, "cactus_nombre":cactus_nombre})

def login_request(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
               
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "inicio.html", {"mensaje": f"Bienvenido/a {usuario}"})
                  else:
                       
                        return render (request, "inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "inicio.html", {"mensaje":"Formulario erroneo"})
      
      form = AuthenticationForm()
    
      return render(request, "login.html", {'form': form})

def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, "inicio.html", {"mensaje": f"usuario creado, bienvenido {username}"})

      else: 
            form = UserRegisterForm()

      return render(request, "register.html", {"form": form})

@login_required
def formularios(request):
     return render(request,"formularios.html")

def needAdmin(request):
     return render(request,"needAdmin.html")

def sobreMi(request):
     return render(request,"sobreMi.html")







