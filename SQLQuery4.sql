select * from users;

select * from beneficios;

select * from usuario_beneficio;




select concat(u.first_name,' ', u.last_name)Cliente , des_beneficio Beneficio  from users u, beneficios b , usuario_beneficio ub
where u.id_user=ub.id_usuario and ub.id_beneficio=b.id_beneficio;


select concat(u.first_name,' ', u.last_name)Cliente,
(select des_beneficio from
from users u






insert into usuario_beneficio (id_usuario,id_beneficio)
values ('4','2')



insert into users (id_user,first_name,last_name,birthday,gender,email,cellphone)
values ('2','Diego','Sanchez','12-23-1970','M','diego@hotmail.com','784749171');



insert into users (id_user,first_name,last_name,birthday,gender,email,cellphone) values ('3','María','Lopez','08-12-1999','F','maria@hotmail.com','969475394');





insert into users (id_user,first_name,last_name,birthday,gender,email,cellphone) values ('4','Carolina','Guzmán','12-25-2002','F','carolina@gmail.com','974639394');
insert into users (id_user,first_name,last_name,birthday,gender,email,cellphone) values ('5','Roberto','Villalobos','11-09-1989','F','roberto@hotmail.com','969471296');