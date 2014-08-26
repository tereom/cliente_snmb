# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de Conglomerado, es decir: Conglomerate_sample, Site_sample y Reference_image_site:
## El campo de ID es automático en Web2py, por lo que no se incluye:

db.define_table('Conglomerate_sample',
                Field('name','integer', required='TRUE'),
                Field('visit_date', 'date', required='TRUE'),
                Field('municipio', 'integer', required='TRUE'),
                Field('predio', 'text', required='TRUE'),
                Field('property_', 'text', required='TRUE'),
                Field('soil_use_type', 'text', required='TRUE'),
                Field('vegetation_type', 'text', required='TRUE'),
                Field('is_perturbed', 'boolean'),
                Field('comment_', 'text'))

                #Field('type_', 'reference Conglomerate_type_option', required='TRUE'),\
                #Field('state', 'reference State', required='TRUE'),\
                #Field('soil_use_type', 'reference Soil_use_type_option', required='TRUE'),\
                #Field('vegetation_type', 'reference Vegetation_type_option'),\        


db.Conglomerate_sample.name.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.visit_date.requires=IS_NOT_EMPTY()
#db.Conglomerate_sample.type_.requires=IS_NOT_EMPTY()
#db.Conglomerate_sample.state.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.municipio.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.predio.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.property_.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.soil_use_type.requires=IS_NOT_EMPTY()

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
