# <h1 align=center> **PROYECTO INDIVIDUAL** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

<p align="center">
<img src=".\_src\etl.gif"  height=350>
</p>
  

<hr>  

## **Descripción del problema**

El proyecto consiste en procesar varios datasets de las plataformas **Amazon, Diney, hulu y Netflix**  y unificar los datasets para  elaborar unas <a href="https://github.com/aylinv94/Data_Engineer/blob/master/Consignas.md">consignas</a> </strong> mediante una serie de transformaciones especificas,  en la cual se disponibilizara los datos a traves de la plataforma **FastAPI**, un web framework moderno y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = 'https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png' height=250><p> 

<FONT SIZE=5>Las consultas a realizar son:</font>

+ Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

+ La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

+ Película que más duró según año, plataforma y tipo de duración

+ Cantidad de series y películas por rating
<br/>

**Es necesario destacar que en este proyeto se tomaron dos vertientes, la primera es la `creacion de la API en un entorno Docker` a traves de Docker-compuse y la segunda realizar un `deployment de la API sin docker`**

# ¿Cómo correr la FastApi utilizando el docker compuse?
1. Tenemos que clonar el repositorio: Encima de la lista de archivos, haga clic en <img src=".\_src\Flecha_descarga.png" height="15"> Código
<br>


<img src=".\_src\git_clone.png" height="400">
<br>

<br>

2. Abra la Terminal, cambia el directorio de trabajo actual a la ubicación en donde quieres clonar el directorio y Escriba git clone y pegue la dirección URL que ha copiado antes.

    ```shell
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    > Cloning into `Data_Engineer`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
    ```
<br>

3. Posicionar en el directorio de acabamos de crear
    ```shell
    $ cd Data_Engineer  
    ```
<br>

4. Ahora si podemos correr nuestro `Docker-compuse`, recuerda que para ello debes tener 'Docker previamente instalando y activo' 

   ```shell
    $ docker-compose up --build
    ```
 <br>

5. Cuando termine de correr las 6 info el programa esta lista para usarse

<img src=".\_src\terminal.png" height="400">

<br>
* <strong>Nota: Recuerda redirigirte al siguiente host <a href="http://0.0.0.0:8000/docs">http://0.0.0.0:8000/docs</a> </strong>

<img src=".\_src\Docker-compuse.png" height="400">

<br>
* No olvides salir del programa cuando termines, dentro de la terminal presiona `Ctrl + c `, te saldra el sieguiente mensaje.
    ```shell
    Stopping proyecto_etl_fast_api3_1   ... done

<br/>



# **Deployment (sin docker)**

Para disponibilizar los datos dentro framework ***FastAPI*** se realizo el **`Deployment`** con la empresa [Deta](https://www.deta.sh/?ref=fastapi) (no necesita dockerizacion) en lo cual una vez creado un entorno virtual de python se siguieron las siguientes pasos en la terminal:
    
1. Instalar Deta CLI
    ```shell
    curl -fsSL https://get.deta.dev/cli.sh | sh
    ```

2. Salir de la terminal y volver a entrar
    
3. Logearse en deta desde un navegador chrome o firefox
    ```shell
    deta login
    ```
4. Crear  un directorio llamado FirstMicro, y alli mismo se genera el endpoint junto con el archivo main.py

    ```shell
    deta new --python FirstMicro
    ```

5. Intalar las dependicias FastApi y pandas
    ```shell
    pip install fastapi
    pip install pandas
    ```

6. Ingresar al directorio FirstMicro
    ```shell
    cd FirstMicro
    ```
7. Crear el archivo requirements.txt
    ```shell
    pip freeze > requirements.txt
    ```
8. Modificar el archivo main.py para verificar si funciona
    ```shell
    from fastapi import FastAPI
    import pandas as pd

    app = FastAPI(title= 'ETL con docker y FastApi',
            description= 'Extract, Transform, Load of the platforms Amazon, Disney, Hulu y Netflix', 
            version= '1.0.1')

    @app.get('/')
    async def init():
    return {'Hello:World'}
    ```
9. Hacer el deploy
    ```shell
    deta deploy
    ```

Despues de hacer todas las modificaciones al archivo main.py este es el <a href="https://6w2dj8.deta.dev/docs">Deployment</a> de la Api 
<br/>

<br/>

### Por ultimo, se realizo un **`Video Demostrativo`** de ***5 minutos*** explicando el trabajo realizado durante este proyecto.




