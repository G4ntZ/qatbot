CREATE ROLE botuser WITH
	NOLOGIN
	SUPERUSER
	CREATEDB
	CREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD 'k4k4roto';

CREATE DATABASE bot
    WITH
    OWNER = botuser
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

CREATE TABLE public.tb_bot
(
    id integer NOT NULL,
    "Jira" character varying NOT NULL,
    name character varying NOT NULL,
    coverage character varying,
    technical_debt character varying,
    version character varying,
    PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE IF EXISTS public.tb_bot
    OWNER to botuser;