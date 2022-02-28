# Pizza

Antes de iniciar se debe instalar [python](https://www.python.org/downloads/).

## Configuración

#### 1 ) Preparar maquina

Instalar Django
```bash
python -m pip install django
```
Instalar entorno virtual
```bash
python -m pip install virtualenv
```
Crear entorno virtual
```bash
python -m venv pizza
```
Activar entorno virtual
```bash
cd pizza/Scritps
```
```bash
activate
```

#### 2 ) Clonar repositorio

```bash
git clone https://github.com/dtorres3095007/pizza-back.git
```

#### 3 ) Instalar dependencias

Entrar a la carpeta del proyecto

```bash
cd pizza-back
```
entonces

```bash
pip3 install -r requirements.txt
```

#### 4 ) Ejecutar Migraciones

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
#### 5 ) Ejecutar aplicación

```bash
python manage.py runserver
```

#### 6 ) Revisar aplicación

ir a http://127.0.0.1:8000//


