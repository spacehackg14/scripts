select * from users;


select * from tipo_doc_identidad;

select * from usuario_documento_identidad;

insert into usuario_documento_identidad (id_user,cod_tipo_doc_identidad,num_documento)
values ('5', '3','00235474758')


select * from pagina_facebook;

insert  into pagina_facebook (nombre_pagina,info_pagina,categoria_pagina,url_pagina)
values ('BBVA',
'Página del  banco BBVA..',
'Producto/servicio','https://www.facebook.com/bbvaenperu')

select * from language;

insert into language (id_language,description)
values('IT','Italiano')


select * from user_languages;

insert into user_languages(id_user,id_language)
values ('4','EN');


select concat(u.first_name,' ', u.last_name)Cliente , des_beneficio Beneficio  from users u, beneficios b , usuario_beneficio ub
where u.id_user=ub.id_usuario and ub.id_beneficio=b.id_beneficio;