# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de Conglomerado, es decir: Conglomerate_sample, Site_sample y Reference_image_site:
## El campo de ID es automático en Web2py, por lo que no se incluye:

db.define_table('Conglomerate_sample',
                Field('name','integer', required='TRUE'),
                Field('visit_date', 'date', required='TRUE'),
                Field('type_', 'reference Conglomerate_type_option', required='TRUE'),
                Field('state_', 'reference Conglomerate_state_option', required='TRUE'),
                Field('municipio', 'integer', required='TRUE'),
                Field('predio', 'text', required='TRUE'),
                Field('property_', 'reference Conglomerate_property_option', required='TRUE'),
                Field('soil_use_type', 'reference Conglomerate_soil_option', required='TRUE'),
                Field('vegetation_type', 'reference Conglomerate_vegetation_option'),
                Field('is_perturbed', 'boolean'),
                Field('comment_', 'text'))

db.Conglomerate_sample.name.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.visit_date.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.type_.requires=IS_IN_DB(db,db.Conglomerate_type_option.num_type,'%(name_type)s')
db.Conglomerate_sample.state_.requires=IS_IN_DB(db,db.Conglomerate_state_option.num_state,'%(name_state)s')
db.Conglomerate_sample.municipio.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.predio.requires=IS_NOT_EMPTY()
db.Conglomerate_sample.property_.requires==IS_IN_DB(db,db.Conglomerate_property_option.num_property,'%(name_property)s')
db.Conglomerate_sample.soil_use_type.requires=IS_IN_DB(db,db.Conglomerate_soil_option.num_soil,'%(name_soil)s')
db.Conglomerate_sample.vegetation_type.requires=IS_IN_DB(db,db.Conglomerate_vegetation_option.num_vegetation,'%(name_vegetation)s')



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
