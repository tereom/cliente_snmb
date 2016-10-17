# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

#########################################################################
#########################################################################
# <Editado para el cliente>
#########################################################################
#########################################################################

# response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
#                  _class="brand",_href="http://www.web2py.com/")

#########################################################################
#########################################################################
# </Editado para el cliente>
#########################################################################
#########################################################################

response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

#########################################################################
#########################################################################
# <Editado para el cliente>
#########################################################################
#########################################################################

response.menu = [

    # describe el menú de la parte superior del cliente

    (T('Home'), False, URL('default', 'index'), []),

    ###########################################
    # Conglomerado
    ###########################################

    (T('Conglomerado'), False, URL('01_conglomerado', 'index'), []),

    ###########################################
    # Conteo de aves
    ###########################################

     (T('Conteo de aves'), False, URL('06_conteo_aves', 'index1'), [
       (T('Punto de conteo'), False, URL('06_conteo_aves', 'index1')),
       (T('Avistamientos'), False, URL('06_conteo_aves', 'index2'))]),

    ###########################################
    # Especies invasoras y huellas/excretas
    ###########################################

    (T('Especies invasoras y huellas/excretas'), False, URL('04_invasoras_huellas_excretas', 'index1'), [
      (T('Transectos'), False, URL('04_invasoras_huellas_excretas', 'index1')),
      (T('Registros especies invasoras'), False, URL('04_invasoras_huellas_excretas', 'index2')),
      (T('Registros huellas y excretas'), False, URL('04_invasoras_huellas_excretas', 'index3'))
    ]),

    ###########################################
    # Vegetación y suelo
    ###########################################

    (T('Vegetación y suelo'), False, URL('07_vegetacion_suelo', 'index1'), [
      (T('Material leñoso caído'), False, URL('07_vegetacion_suelo', 'index1')),
      (T('Material 1000h'), False, URL('07_vegetacion_suelo', 'index2')),
      (T('Carbono en el mantillo'), False, URL('07_vegetacion_suelo', 'index3')),
      (T('Árboles pequeños y arbustos'), False, URL('07_vegetacion_suelo', 'index4')),
      (T('Árboles grandes'), False, URL('07_vegetacion_suelo', 'index5')),
      (T('Epífitas'), False, URL('07_vegetacion_suelo', 'index6'))]),

    ###########################################
    # Impactos ambientales
    ###########################################
    
    (T('Impactos ambientales'),False,URL('08_impactos_ambientales','index3'), [
      (T('Incendios'),False,URL('08_impactos_ambientales','index3')),
      (T('Plagas'),False,URL('08_impactos_ambientales','index2')),
      (T('Impactos actuales'),False,URL('08_impactos_ambientales','index1'))
      ]),

    ###########################################
    # Cámara
    ###########################################

    (T('Trampa cámara'), False, URL('02_camara', 'index1'), [
      (T('Información de trampa cámara'), False, URL('02_camara', 'index1')),
      (T('Archivos trampa cámara'), False, URL('02_camara', 'index2')),
      # Revisión de imágenes
      (T('Selección de fauna'), False, URL('02_camara', 'index3'))]),
    
    ###########################################
    # Grabadora
    ###########################################

    (T('Grabadora'), False, URL('03_grabadora', 'index1'), [
      (T('Información de grabadora'), False, URL('03_grabadora', 'index1')),
      (T('Archivos de audio'), False, URL('03_grabadora', 'index2'))]),

    ###########################################
    # Registros extra
    ###########################################

    (T('Registros extra'), False, URL('05_registros_extra', 'index1'), [
      (T('Especies invasoras'), False, URL('05_registros_extra', 'index1')),
      (T('Huellas y excretas'), False, URL('05_registros_extra', 'index2')),
      (T('Especímenes y restos'), False, URL('05_registros_extra', 'index3'))]),

    ###########################################
    # Revisar registros
    ###########################################
    
    (T('Revisar registros'), False, URL('09_revisar_registros', 'conglomerado'), [
      (T('Conglomerado'), False, URL('09_revisar_registros', 'conglomerado')),
      (T('Conteo de aves'), False, URL('09_revisar_registros', 'punto_conteo_aves')),
      (T('Especies invasoras y huellas/excretas'), False, URL('09_revisar_registros', 'transecto_muestra')),
      (T('Material leñoso caído'), False, URL('09_revisar_registros', 'transecto_ramas')),
      (T('Carbono en el mantillo'), False, URL('09_revisar_registros', 'punto_carbono')),
      (T('Árboles pequeños'), False, URL('09_revisar_registros', 'arbol_transecto')),
      (T('Árboles grandes'), False, URL('09_revisar_registros', 'arbol_cuadrante')),
      (T('Epífitas'), False, URL('09_revisar_registros', 'informacion_epifitas')),
      (T('Incendios'), False, URL('09_revisar_registros', 'incendio')),
      (T('Plagas'), False, URL('09_revisar_registros', 'plaga')),
      (T('Impactos ambientales'), False, URL('09_revisar_registros', 'impacto_actual')),
      (T('Trampa cámara'), False, URL('09_revisar_registros', 'camara')),
      (T('Grabadora'), False, URL('09_revisar_registros', 'grabadora')),
      (T('Especies invasoras extra'), False, URL('09_revisar_registros', 'especie_invasora_extra')),
      (T('Huellas/excretas extra'), False, URL('09_revisar_registros', 'huella_excreta_extra')),
      (T('Especímenes/restos extra'), False, URL('09_revisar_registros', 'especimen_restos_extra'))

      ]),
    
    ###########################################
    # Exportar datos
    ###########################################

    (T('Exportar datos'), False, URL('10_exportar_datos', 'index'), [])
    ]

#########################################################################
#########################################################################
# </Editado para el cliente>
#########################################################################
#########################################################################

#########################################################################
#########################################################################
# <Editado para el cliente>
#########################################################################
#########################################################################

DEVELOPMENT_MENU = False

#########################################################################
#########################################################################
# </Editado para el cliente>
#########################################################################
#########################################################################

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
        (SPAN('web2py', _class='highlighted'), False, 'http://web2py.com', [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('This App'), False, URL('admin', 'default', 'design/%s' % app), [
        (T('Controller'), False,
         URL(
         'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
        (T('View'), False,
         URL(
         'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
        (T('Layout'), False,
         URL(
         'admin', 'default', 'edit/%s/views/layout.html' % app)),
        (T('Stylesheet'), False,
         URL(
         'admin', 'default', 'edit/%s/static/css/web2py.css' % app)),
        (T('DB Model'), False,
         URL(
         'admin', 'default', 'edit/%s/models/db.py' % app)),
        (T('Menu Model'), False,
         URL(
         'admin', 'default', 'edit/%s/models/menu.py' % app)),
        (T('Database'), False, URL(app, 'appadmin', 'index')),
        (T('Errors'), False, URL(
         'admin', 'default', 'errors/' + app)),
        (T('About'), False, URL(
         'admin', 'default', 'about/' + app)),
        ]),
            ('web2py.com', False, 'http://www.web2py.com', [
             (T('Download'), False,
              'http://www.web2py.com/examples/default/download'),
             (T('Support'), False,
              'http://www.web2py.com/examples/default/support'),
             (T('Demo'), False, 'http://web2py.com/demo_admin'),
             (T('Quick Examples'), False,
              'http://web2py.com/examples/default/examples'),
             (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
             (T('Videos'), False,
              'http://www.web2py.com/examples/default/videos/'),
             (T('Free Applications'),
              False, 'http://web2py.com/appliances'),
             (T('Plugins'), False, 'http://web2py.com/plugins'),
             (T('Layouts'), False, 'http://web2py.com/layouts'),
             (T('Recipes'), False, 'http://web2pyslices.com/'),
             (T('Semantic'), False, 'http://web2py.com/semantic'),
             ]),
            (T('Documentation'), False, 'http://www.web2py.com/book', [
             (T('Preface'), False,
              'http://www.web2py.com/book/default/chapter/00'),
             (T('Introduction'), False,
              'http://www.web2py.com/book/default/chapter/01'),
             (T('Python'), False,
              'http://www.web2py.com/book/default/chapter/02'),
             (T('Overview'), False,
              'http://www.web2py.com/book/default/chapter/03'),
             (T('The Core'), False,
              'http://www.web2py.com/book/default/chapter/04'),
             (T('The Views'), False,
              'http://www.web2py.com/book/default/chapter/05'),
             (T('Database'), False,
              'http://www.web2py.com/book/default/chapter/06'),
             (T('Forms and Validators'), False,
              'http://www.web2py.com/book/default/chapter/07'),
             (T('Email and SMS'), False,
              'http://www.web2py.com/book/default/chapter/08'),
             (T('Access Control'), False,
              'http://www.web2py.com/book/default/chapter/09'),
             (T('Services'), False,
              'http://www.web2py.com/book/default/chapter/10'),
             (T('Ajax Recipes'), False,
              'http://www.web2py.com/book/default/chapter/11'),
             (T('Components and Plugins'), False,
              'http://www.web2py.com/book/default/chapter/12'),
             (T('Deployment Recipes'), False,
              'http://www.web2py.com/book/default/chapter/13'),
             (T('Other Recipes'), False,
              'http://www.web2py.com/book/default/chapter/14'),
             (T('Buy this book'), False,
              'http://stores.lulu.com/web2py'),
             ]),
            (T('Community'), False, None, [
             (T('Groups'), False,
              'http://www.web2py.com/examples/default/usergroups'),
                        (T('Twitter'), False, 'http://twitter.com/web2py'),
                        (T('Live Chat'), False,
                         'http://webchat.freenode.net/?channels=web2py'),
                        ]),
                (T('Plugins'), False, None, [
                        ('plugin_wiki', False,
                         'http://web2py.com/examples/default/download'),
                        (T('Other Plugins'), False,
                         'http://web2py.com/plugins'),
                        (T('Layout Plugins'),
                         False, 'http://web2py.com/layouts'),
                        ])
                ]
         )]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu() 
