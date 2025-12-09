CREATE database AMPRIC;
use AMPRIC;
CREATE TABLE utilisateurs (
    id INTEGER AUTO_INCREMENT KEY  ,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    telephone VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    comment TEXT
);

insert INTO utilisateurs(nom,prenom,telephone,email) VALUES ("sory","keita","78666666","sooo@jj,ca") ;
select * from utilisateurs ;
DELETE FROM utilisateurs ;
 