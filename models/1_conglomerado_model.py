# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de Conglomerado, es decir: Conglomerate_sample, Site_sample y Reference_image_site:
## El campo de ID es automático en Web2py, por lo que no se incluye:

db.define_table('Conglomerate_sample',
                Field('name','integer',label=T("Num. conglomerado"),\
                        required='TRUE'),
                Field('visit_date', 'date',label=T("Fecha de visita"),\
                        required='TRUE'),
                Field('type_', 'reference Conglomerate_type_option',\
                        label=T("Tipo de conglomerado"),required='TRUE'),
                Field('state_', 'reference Conglomerate_state_option',\
                        label=T("Estado"),required='TRUE'),
                Field('municipio', 'integer',label=T("Municipio"),required='TRUE'),
                Field('predio','string',label=T("Predio"),required='TRUE'),
                Field('property_', 'reference Conglomerate_property_option',\
                        label=T("Propiedad"), required='TRUE'),
                Field('soil_use_type', 'reference Conglomerate_soil_option',
                        label=T("Tipo de uso de suelo"),required='TRUE'),
                Field('vegetation_type',\
                        'reference Conglomerate_vegetation_option',\
                        label=T("Tipo de vegetación")),
                Field('is_perturbed', 'boolean',label=T("Perturbado")),
                Field('comment_', 'text',label=T("Observaciones")))

db.Conglomerate_sample.name.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.visit_date.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.type_.requires=IS_IN_DB(db,db.Conglomerate_type_option.num_type,'%(name_type)s')
db.Conglomerate_sample.state_.requires=IS_IN_DB(db,db.Conglomerate_state_option.num_state,'%(name_state)s')
db.Conglomerate_sample.municipio.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.predio.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.property_.requires=IS_IN_DB(db,db.Conglomerate_property_option.num_property,'%(name_property)s')
db.Conglomerate_sample.soil_use_type.requires=IS_IN_DB(db,db.Conglomerate_soil_option.num_soil,'%(name_soil)s')
db.Conglomerate_sample.vegetation_type.requires=(IS_IN_DB(db,db.Conglomerate_vegetation_option.num_vegetation,'%(name_vegetation)s') or None)


db.define_table('Site_sample',
                Field('conglomerate_sample_id','reference Conglomerate_sample'),
                Field('site_number', 'reference Site_number_option',\
                        label=T("Número de sitio")),
                Field('lat_deg','integer',label=T("grado"),required='TRUE'),
                Field('lat_min','integer',label=T("minuto"),required='TRUE'),
                Field('lat_sec','double',label=T("segundo"),required='TRUE'),
                Field('lon_deg','integer',label=T("grado"),required='TRUE'),
                Field('lon_min','integer',label=T("minuto"),required='TRUE'),
                Field('lon_sec','double',label=T("segundo"),required='TRUE'),
                Field('altitude','double',label=T("Altitud(m)"),required='TRUE'),
                Field('gps_error','double',label=T("Error(m)"),required='TRUE'),
                Field('ellipsoid', 'reference Site_ellipsoid_option',\
                        label=T("Datum"),required='TRUE'), 
                Field('is_evidence', 'boolean',label=T("Evidencias")), 
                Field('exists_', 'boolean',label=T("Existe")))


db.Site_sample.site_number.requires=IS_IN_DB(db,db.Site_number_option.num_number,'%(name_number)s')
db.Site_sample.lat_deg.requires=IS_NOT_EMPTY()
db.Site_sample.lat_min.requires=IS_NOT_EMPTY()
db.Site_sample.lat_sec.requires=IS_NOT_EMPTY()
db.Site_sample.lon_deg.requires=IS_NOT_EMPTY()
db.Site_sample.lon_min.requires=IS_NOT_EMPTY()
db.Site_sample.lon_sec.requires=IS_NOT_EMPTY()
db.Site_sample.altitude.requires=IS_NOT_EMPTY()
db.Site_sample.gps_error.requires=IS_NOT_EMPTY()
db.Site_sample.ellipsoid.requires=IS_IN_DB(db,db.Site_ellipsoid_option.num_ellipsoid,'%(name_ellipsoid)s')



# db.define_table('Reference_image_site',
#                 Field('site_sample_id','reference Site_sample'),
#                 Field('filename','text',label=T("Archivo")),
#                 Field('oldfilename','text',label=T("Archivo")),
#                 )



########################################################################
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################
