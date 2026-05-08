Proyecto PreEntrega:  Automation QA - Bernardo Borges


Descripcion

Este proyecto consiste en una suite de pruebas automatizadas desarrollada con Python, Pytest y Selenium WebDriver para el sitio Sauce Demo.
Se enfoca en la modularidad, el uso de fixtures y la generación de reportes detallados.


Tecnologías 
```bash
Python 3.xFramework
Pytest 
Selenium WebDriver
Pytest HTLM
Google Chrome 
```
Instalacion

Clonar el repositorio

git clone: https://github.com/bernardoborges787-sketch/pre-entrega-automation-testing-Bernardo-Borges.git


Instalacion dependencias
```bash
pip install -r requirements.txt
```

Estructura
```bash
Proyecto_PreEntrega/
├── test/
│   ├── test_login.py      # Validación de acceso exitoso
│   ├── test_inventory.py  # Verificación de productos y UI
│   └── test_cart.py       # Flujo de carrito de compras
├── utils/
│   └── LoginPage.py       # Funciones auxiliares de autenticación
├── conftest.py            # Fixtures (Driver y Login automático)
├── pytest.ini             # Configuración y reportes HTML
└── requirements.txt       # Dependencias del proyecto
```

Ejecución

```bash
py -m pytest -v
pytest --html=report.html --self-contained-html
```

Resultados

Al finalizar la ejecución, se generará un archivo llamado report.html en la raíz del proyecto. 
Ábrelo en cualquier navegador para ver el resumen detallado de los casos de prueba (Pass/Fail).



