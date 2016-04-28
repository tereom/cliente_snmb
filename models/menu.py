# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

#########################################################################
#########################################################################
# <Editado para el cliente>
#########################################################################
#########################################################################

# response.logo = A(B('web', SPAN(2), 'py'), XML('&trade;&nbsp;'),
#                   _class="navbar-brand", _href="http://www.web2py.com/",
#                   _id="web2py-logo")

#########################################################################
#########################################################################
# </Editado para el cliente>
#########################################################################
#########################################################################

response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

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

    # (T('Conteo de aves'), False, URL('06_conteo_aves', 'index1'), [
    #   (T('Punto de conteo'), False, URL('06_conteo_aves', 'index1')),
    #   (T('Avistamientos'), False, URL('06_conteo_aves', 'index2'))]),

    ###########################################
    # Especies invasoras y huellas/excretas
    ###########################################

    (T('Especies invasoras y huellas/excretas'), False, URL('04_invasoras_huellas_excretas', 'index1'), [
      (T('Transectos'), False, URL('04_invasoras_huellas_excretas', 'index1')),
      (T('Registros especies invasoras'), False, URL('04_invasoras_huellas_excretas', 'index2')),
      (T('Registros huellas y excretas'), False, URL('04_invasoras_huellas_excretas', 'index3'))
    ]),

    ###########################################
    # Carbono
    ###########################################

    # (T('Vegetación y suelo'), False, URL('11_carbono', 'index1'), [
    #   (T('Material leñoso caído'), False, URL('11_carbono', 'index1')),
    #   (T('Material 1000h'), False, URL('11_carbono', 'index2')),
    #   (T('Carbono en el mantillo'), False, URL('11_carbono', 'index3')),
    #   (T('Árboles pequeños y arbustos'), False, URL('11_carbono', 'index4')),
    #   (T('Árboles grandes'), False, URL('11_carbono', 'index5'))]),

    # ### Epífitas
    # (T('Epífitas'), False, URL('12_epifitas', 'index'),[]),

    # ### Impactos ambientales
    # (T('Impactos ambientales'),False,URL('13_impactos_ambientales','index3'), [
    #   (T('Incendios'),False,URL('13_impactos_ambientales','index3')),
    #   (T('Plagas'),False,URL('13_impactos_ambientales','index2')),
    #   (T('Impactos actuales'),False,URL('13_impactos_ambientales','index1'))
    #   ]),

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
      #(T('Conteo de aves'), False, URL('09_revisar_registros', 'editarConteoAves')),
      (T('Especies invasoras y huellas/excretas'), False, URL('09_revisar_registros', 'invasoras_huellas_excretas')),
      #(T('Material leñoso'), False, URL('09_revisar_registros', 'editarCarbonoRamas')),
      #(T('Carbono mantillo'), False, URL('09_revisar_registros', 'editarCarbono')),
      #(T('Árboles pequeños'), False, URL('09_revisar_registros', 'editarArbolTransecto')),
      #(T('Árboles grandes'), False, URL('09_revisar_registros', 'editarArbolCuadrante')),
      #(T('Epífitas'), False, URL('09_revisar_registros', 'editarEpifitas')),
      #(T('Incendios'), False, URL('09_revisar_registros', 'editarIncendio')),
      #(T('Plagas'), False, URL('09_revisar_registros', 'editarPlaga')),
      #(T('Impactos ambientales'), False, URL('09_revisar_registros', 'editarImpacto')),
      (T('Cámara'), False, URL('09_revisar_registros', 'camara')),
      (T('Grabadora'), False, URL('09_revisar_registros', 'grabadora')),
      (T('Registros extra'), False, URL('09_revisar_registros', 'registros_extra'))
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

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('This App'), False, '#', [
            (T('Design'), False, URL('admin', 'default', 'design/%s' % app)),
            LI(_class="divider"),
            (T('Controller'), False,
             URL(
                 'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
            (T('View'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
            (T('DB Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/db.py' % app)),
            (T('Menu Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/menu.py' % app)),
            (T('Config.ini'), False,
             URL(
                 'admin', 'default', 'edit/%s/private/appconfig.ini' % app)),
            (T('Layout'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/layout.html' % app)),
            (T('Stylesheet'), False,
             URL(
                 'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % app)),
            (T('Database'), False, URL(app, 'appadmin', 'index')),
            (T('Errors'), False, URL(
                'admin', 'default', 'errors/' + app)),
            (T('About'), False, URL(
                'admin', 'default', 'about/' + app)),
        ]),
        ('web2py.com', False, '#', [
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
            (T('Recipes'), False, 'http://web2pyslices.com/'),
        ]),
        (T('Documentation'), False, '#', [
            (T('Online book'), False, 'http://www.web2py.com/book'),
            LI(_class="divider"),
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
            (T('Helping web2py'), False,
             'http://www.web2py.com/book/default/chapter/15'),
            (T("Buy web2py's book"), False,
             'http://stores.lulu.com/web2py'),
        ]),
        (T('Community'), False, None, [
            (T('Groups'), False,
             'http://www.web2py.com/examples/default/usergroups'),
            (T('Twitter'), False, 'http://twitter.com/web2py'),
            (T('Live Chat'), False,
             'http://webchat.freenode.net/?channels=web2py'),
        ]),
    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()