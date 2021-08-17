--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Drop databases (except postgres and template1)
--

DROP DATABASE post;




--
-- Drop roles
--

DROP ROLE post;


--
-- Roles
--

CREATE ROLE post;
ALTER ROLE post WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'md57f3504a67662ee6f264bde4235063e08';






--
-- Databases
--

--
-- Database "template1" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

UPDATE pg_catalog.pg_database SET datistemplate = false WHERE datname = 'template1';
DROP DATABASE template1;
--
-- Name: template1; Type: DATABASE; Schema: -; Owner: post
--

CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE template1 OWNER TO post;

\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: post
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: template1; Type: DATABASE PROPERTIES; Schema: -; Owner: post
--

ALTER DATABASE template1 IS_TEMPLATE = true;


\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: ACL; Schema: -; Owner: post
--

REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- Database "post" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: post; Type: DATABASE; Schema: -; Owner: post
--

CREATE DATABASE post WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE post OWNER TO post;

\connect post

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO post;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO post;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO post;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO post;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO post;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO post;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: authnapp_user; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.authnapp_user (
    id integer NOT NULL,
    is_client boolean NOT NULL,
    is_staff boolean NOT NULL,
    personal_account character varying(128) NOT NULL,
    password character varying(128) NOT NULL,
    name character varying(128),
    email character varying(254),
    phone character varying(11),
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    last_login timestamp with time zone,
    activation_key character varying(128) NOT NULL,
    activation_key_expires timestamp with time zone NOT NULL
);


ALTER TABLE public.authnapp_user OWNER TO post;

--
-- Name: authnapp_user_groups; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.authnapp_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.authnapp_user_groups OWNER TO post;

--
-- Name: authnapp_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.authnapp_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authnapp_user_groups_id_seq OWNER TO post;

--
-- Name: authnapp_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.authnapp_user_groups_id_seq OWNED BY public.authnapp_user_groups.id;


--
-- Name: authnapp_user_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.authnapp_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authnapp_user_id_seq OWNER TO post;

--
-- Name: authnapp_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.authnapp_user_id_seq OWNED BY public.authnapp_user.id;


--
-- Name: authnapp_user_user_permissions; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.authnapp_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.authnapp_user_user_permissions OWNER TO post;

--
-- Name: authnapp_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.authnapp_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authnapp_user_user_permissions_id_seq OWNER TO post;

--
-- Name: authnapp_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.authnapp_user_user_permissions_id_seq OWNED BY public.authnapp_user_user_permissions.id;


--
-- Name: directory_appartament; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.directory_appartament (
    id integer NOT NULL,
    number character varying(3) NOT NULL,
    add_number integer NOT NULL,
    sq_appart numeric(5,2),
    num_owner integer,
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    house_id integer NOT NULL,
    user_id integer,
    CONSTRAINT directory_appartament_add_number_check CHECK ((add_number >= 0)),
    CONSTRAINT directory_appartament_num_owner_check CHECK ((num_owner >= 0))
);


ALTER TABLE public.directory_appartament OWNER TO post;

--
-- Name: directory_appartament_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.directory_appartament_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directory_appartament_id_seq OWNER TO post;

--
-- Name: directory_appartament_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.directory_appartament_id_seq OWNED BY public.directory_appartament.id;


--
-- Name: directory_city; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.directory_city (
    id integer NOT NULL,
    city character varying(128) NOT NULL,
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL
);


ALTER TABLE public.directory_city OWNER TO post;

--
-- Name: directory_city_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.directory_city_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directory_city_id_seq OWNER TO post;

--
-- Name: directory_city_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.directory_city_id_seq OWNED BY public.directory_city.id;


--
-- Name: directory_house; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.directory_house (
    id integer NOT NULL,
    number character varying(3) NOT NULL,
    add_number character varying(3) NOT NULL,
    sq_home numeric(7,2) NOT NULL,
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    category_rate_id integer,
    city_id integer,
    street_id integer
);


ALTER TABLE public.directory_house OWNER TO post;

--
-- Name: directory_house_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.directory_house_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directory_house_id_seq OWNER TO post;

--
-- Name: directory_house_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.directory_house_id_seq OWNED BY public.directory_house.id;


--
-- Name: directory_metrics; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.directory_metrics (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL
);


ALTER TABLE public.directory_metrics OWNER TO post;

--
-- Name: directory_metrics_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.directory_metrics_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directory_metrics_id_seq OWNER TO post;

--
-- Name: directory_metrics_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.directory_metrics_id_seq OWNED BY public.directory_metrics.id;


--
-- Name: directory_postnews; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.directory_postnews (
    id integer NOT NULL,
    title character varying(128) NOT NULL,
    content text NOT NULL,
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL
);


ALTER TABLE public.directory_postnews OWNER TO post;

--
-- Name: directory_postnews_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.directory_postnews_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directory_postnews_id_seq OWNER TO post;

--
-- Name: directory_postnews_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.directory_postnews_id_seq OWNED BY public.directory_postnews.id;


--
-- Name: directory_privileges; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.directory_privileges (
    id integer NOT NULL,
    sale integer NOT NULL,
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    "desc" text,
    service_id integer NOT NULL,
    user_id integer NOT NULL,
    CONSTRAINT directory_privileges_sale_check CHECK ((sale >= 0))
);


ALTER TABLE public.directory_privileges OWNER TO post;

--
-- Name: directory_privileges_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.directory_privileges_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directory_privileges_id_seq OWNER TO post;

--
-- Name: directory_privileges_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.directory_privileges_id_seq OWNED BY public.directory_privileges.id;


--
-- Name: directory_services; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.directory_services (
    id integer NOT NULL,
    name character varying(256) NOT NULL,
    rate numeric(7,3) NOT NULL,
    factor numeric(3,2) NOT NULL,
    const boolean NOT NULL,
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    category_id integer NOT NULL,
    unit_id integer NOT NULL
);


ALTER TABLE public.directory_services OWNER TO post;

--
-- Name: directory_services_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.directory_services_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directory_services_id_seq OWNER TO post;

--
-- Name: directory_services_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.directory_services_id_seq OWNED BY public.directory_services.id;


--
-- Name: directory_servicescategory; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.directory_servicescategory (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL
);


ALTER TABLE public.directory_servicescategory OWNER TO post;

--
-- Name: directory_servicescategory_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.directory_servicescategory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directory_servicescategory_id_seq OWNER TO post;

--
-- Name: directory_servicescategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.directory_servicescategory_id_seq OWNED BY public.directory_servicescategory.id;


--
-- Name: directory_street; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.directory_street (
    id integer NOT NULL,
    street character varying(128) NOT NULL,
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    city_id integer NOT NULL
);


ALTER TABLE public.directory_street OWNER TO post;

--
-- Name: directory_street_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.directory_street_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directory_street_id_seq OWNER TO post;

--
-- Name: directory_street_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.directory_street_id_seq OWNED BY public.directory_street.id;


--
-- Name: directory_subsidies; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.directory_subsidies (
    id integer NOT NULL,
    sale integer NOT NULL,
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    "desc" text,
    service_id integer NOT NULL,
    user_id integer NOT NULL,
    CONSTRAINT directory_subsidies_sale_check CHECK ((sale >= 0))
);


ALTER TABLE public.directory_subsidies OWNER TO post;

--
-- Name: directory_subsidies_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.directory_subsidies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directory_subsidies_id_seq OWNER TO post;

--
-- Name: directory_subsidies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.directory_subsidies_id_seq OWNED BY public.directory_subsidies.id;


--
-- Name: directory_userprofile; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.directory_userprofile (
    id integer NOT NULL,
    gender character varying(1),
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.directory_userprofile OWNER TO post;

--
-- Name: directory_userprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.directory_userprofile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directory_userprofile_id_seq OWNER TO post;

--
-- Name: directory_userprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.directory_userprofile_id_seq OWNED BY public.directory_userprofile.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO post;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO post;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO post;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO post;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO post;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO post;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO post;

--
-- Name: mainapp_averageсalculationbuffer; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public."mainapp_averageсalculationbuffer" (
    id integer NOT NULL,
    col_water numeric(10,2),
    hot_water numeric(10,2),
    sewage numeric(10,2),
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public."mainapp_averageсalculationbuffer" OWNER TO post;

--
-- Name: mainapp_averageсalculationbuffer_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public."mainapp_averageсalculationbuffer_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."mainapp_averageсalculationbuffer_id_seq" OWNER TO post;

--
-- Name: mainapp_averageсalculationbuffer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public."mainapp_averageсalculationbuffer_id_seq" OWNED BY public."mainapp_averageсalculationbuffer".id;


--
-- Name: mainapp_constantpayments; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_constantpayments (
    id integer NOT NULL,
    data jsonb NOT NULL,
    total numeric(8,3) NOT NULL,
    pre_total numeric(8,3) NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.mainapp_constantpayments OWNER TO post;

--
-- Name: mainapp_constantpayments_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_constantpayments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_constantpayments_id_seq OWNER TO post;

--
-- Name: mainapp_constantpayments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_constantpayments_id_seq OWNED BY public.mainapp_constantpayments.id;


--
-- Name: mainapp_currentcounter; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_currentcounter (
    id integer NOT NULL,
    period date NOT NULL,
    col_water numeric(8,3),
    hot_water numeric(8,3),
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.mainapp_currentcounter OWNER TO post;

--
-- Name: mainapp_currentcounter_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_currentcounter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_currentcounter_id_seq OWNER TO post;

--
-- Name: mainapp_currentcounter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_currentcounter_id_seq OWNED BY public.mainapp_currentcounter.id;


--
-- Name: mainapp_headerdata; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_headerdata (
    id integer NOT NULL,
    data jsonb NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    user_id integer
);


ALTER TABLE public.mainapp_headerdata OWNER TO post;

--
-- Name: mainapp_headerdata_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_headerdata_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_headerdata_id_seq OWNER TO post;

--
-- Name: mainapp_headerdata_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_headerdata_id_seq OWNED BY public.mainapp_headerdata.id;


--
-- Name: mainapp_historycounter; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_historycounter (
    id integer NOT NULL,
    period date NOT NULL,
    col_water numeric(8,3),
    hot_water numeric(8,3),
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    user_id integer
);


ALTER TABLE public.mainapp_historycounter OWNER TO post;

--
-- Name: mainapp_historycounter_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_historycounter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_historycounter_id_seq OWNER TO post;

--
-- Name: mainapp_historycounter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_historycounter_id_seq OWNED BY public.mainapp_historycounter.id;


--
-- Name: mainapp_housecurrent; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_housecurrent (
    id integer NOT NULL,
    period date NOT NULL,
    col_water numeric(8,3),
    hot_water numeric(8,3),
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    house_id integer
);


ALTER TABLE public.mainapp_housecurrent OWNER TO post;

--
-- Name: mainapp_housecurrent_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_housecurrent_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_housecurrent_id_seq OWNER TO post;

--
-- Name: mainapp_housecurrent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_housecurrent_id_seq OWNED BY public.mainapp_housecurrent.id;


--
-- Name: mainapp_househistory; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_househistory (
    id integer NOT NULL,
    period date NOT NULL,
    col_water numeric(8,3),
    hot_water numeric(8,3),
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    house_id integer
);


ALTER TABLE public.mainapp_househistory OWNER TO post;

--
-- Name: mainapp_househistory_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_househistory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_househistory_id_seq OWNER TO post;

--
-- Name: mainapp_househistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_househistory_id_seq OWNED BY public.mainapp_househistory.id;


--
-- Name: mainapp_mainbook; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_mainbook (
    id integer NOT NULL,
    period date NOT NULL,
    direction character varying(1) NOT NULL,
    amount numeric(12,2) NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    user_id integer
);


ALTER TABLE public.mainapp_mainbook OWNER TO post;

--
-- Name: mainapp_mainbook_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_mainbook_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_mainbook_id_seq OWNER TO post;

--
-- Name: mainapp_mainbook_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_mainbook_id_seq OWNED BY public.mainapp_mainbook.id;


--
-- Name: mainapp_paymentorder; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_paymentorder (
    id integer NOT NULL,
    period date NOT NULL,
    header_data jsonb,
    constant_data jsonb NOT NULL,
    variable_data jsonb NOT NULL,
    amount numeric(7,2) NOT NULL,
    pre_amount numeric(7,2) NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    user_id integer
);


ALTER TABLE public.mainapp_paymentorder OWNER TO post;

--
-- Name: mainapp_paymentorder_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_paymentorder_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_paymentorder_id_seq OWNER TO post;

--
-- Name: mainapp_paymentorder_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_paymentorder_id_seq OWNED BY public.mainapp_paymentorder.id;


--
-- Name: mainapp_personalaccountstatus; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_personalaccountstatus (
    id integer NOT NULL,
    amount numeric(8,2) NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.mainapp_personalaccountstatus OWNER TO post;

--
-- Name: mainapp_personalaccountstatus_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_personalaccountstatus_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_personalaccountstatus_id_seq OWNER TO post;

--
-- Name: mainapp_personalaccountstatus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_personalaccountstatus_id_seq OWNED BY public.mainapp_personalaccountstatus.id;


--
-- Name: mainapp_recalculations; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_recalculations (
    id integer NOT NULL,
    period date NOT NULL,
    recalc numeric(10,2) NOT NULL,
    "desc" text,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    service_id integer,
    user_id integer
);


ALTER TABLE public.mainapp_recalculations OWNER TO post;

--
-- Name: mainapp_recalculations_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_recalculations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_recalculations_id_seq OWNER TO post;

--
-- Name: mainapp_recalculations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_recalculations_id_seq OWNED BY public.mainapp_recalculations.id;


--
-- Name: mainapp_standart; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_standart (
    id integer NOT NULL,
    period date NOT NULL,
    col_water numeric(11,6) NOT NULL,
    hot_water numeric(11,6) NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    house_id integer
);


ALTER TABLE public.mainapp_standart OWNER TO post;

--
-- Name: mainapp_standart_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_standart_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_standart_id_seq OWNER TO post;

--
-- Name: mainapp_standart_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_standart_id_seq OWNED BY public.mainapp_standart.id;


--
-- Name: mainapp_variablepayments; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.mainapp_variablepayments (
    id integer NOT NULL,
    period date NOT NULL,
    data jsonb NOT NULL,
    total numeric(10,2) NOT NULL,
    pre_total numeric(10,2) NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.mainapp_variablepayments OWNER TO post;

--
-- Name: mainapp_variablepayments_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.mainapp_variablepayments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mainapp_variablepayments_id_seq OWNER TO post;

--
-- Name: mainapp_variablepayments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.mainapp_variablepayments_id_seq OWNED BY public.mainapp_variablepayments.id;


--
-- Name: personalacc_siteconfiguration; Type: TABLE; Schema: public; Owner: post
--

CREATE TABLE public.personalacc_siteconfiguration (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    city character varying(128) NOT NULL,
    street character varying(256) NOT NULL,
    num_building character varying(5) NOT NULL,
    phone character varying(11),
    email character varying(254) NOT NULL,
    inn character varying(10) NOT NULL,
    ps character varying(20) NOT NULL,
    bik character varying(10) NOT NULL,
    ks character varying(20) NOT NULL,
    bank character varying(128) NOT NULL,
    web_addr character varying(128) NOT NULL,
    key_ya character varying(128) NOT NULL,
    lat character varying(64) NOT NULL,
    lon character varying(64) NOT NULL,
    footer_copyright character varying(256) NOT NULL,
    is_active boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL
);


ALTER TABLE public.personalacc_siteconfiguration OWNER TO post;

--
-- Name: personalacc_siteconfiguration_id_seq; Type: SEQUENCE; Schema: public; Owner: post
--

CREATE SEQUENCE public.personalacc_siteconfiguration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.personalacc_siteconfiguration_id_seq OWNER TO post;

--
-- Name: personalacc_siteconfiguration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: post
--

ALTER SEQUENCE public.personalacc_siteconfiguration_id_seq OWNED BY public.personalacc_siteconfiguration.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: authnapp_user id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user ALTER COLUMN id SET DEFAULT nextval('public.authnapp_user_id_seq'::regclass);


--
-- Name: authnapp_user_groups id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user_groups ALTER COLUMN id SET DEFAULT nextval('public.authnapp_user_groups_id_seq'::regclass);


--
-- Name: authnapp_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.authnapp_user_user_permissions_id_seq'::regclass);


--
-- Name: directory_appartament id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_appartament ALTER COLUMN id SET DEFAULT nextval('public.directory_appartament_id_seq'::regclass);


--
-- Name: directory_city id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_city ALTER COLUMN id SET DEFAULT nextval('public.directory_city_id_seq'::regclass);


--
-- Name: directory_house id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_house ALTER COLUMN id SET DEFAULT nextval('public.directory_house_id_seq'::regclass);


--
-- Name: directory_metrics id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_metrics ALTER COLUMN id SET DEFAULT nextval('public.directory_metrics_id_seq'::regclass);


--
-- Name: directory_postnews id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_postnews ALTER COLUMN id SET DEFAULT nextval('public.directory_postnews_id_seq'::regclass);


--
-- Name: directory_privileges id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_privileges ALTER COLUMN id SET DEFAULT nextval('public.directory_privileges_id_seq'::regclass);


--
-- Name: directory_services id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_services ALTER COLUMN id SET DEFAULT nextval('public.directory_services_id_seq'::regclass);


--
-- Name: directory_servicescategory id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_servicescategory ALTER COLUMN id SET DEFAULT nextval('public.directory_servicescategory_id_seq'::regclass);


--
-- Name: directory_street id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_street ALTER COLUMN id SET DEFAULT nextval('public.directory_street_id_seq'::regclass);


--
-- Name: directory_subsidies id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_subsidies ALTER COLUMN id SET DEFAULT nextval('public.directory_subsidies_id_seq'::regclass);


--
-- Name: directory_userprofile id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_userprofile ALTER COLUMN id SET DEFAULT nextval('public.directory_userprofile_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: mainapp_averageсalculationbuffer id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public."mainapp_averageсalculationbuffer" ALTER COLUMN id SET DEFAULT nextval('public."mainapp_averageсalculationbuffer_id_seq"'::regclass);


--
-- Name: mainapp_constantpayments id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_constantpayments ALTER COLUMN id SET DEFAULT nextval('public.mainapp_constantpayments_id_seq'::regclass);


--
-- Name: mainapp_currentcounter id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_currentcounter ALTER COLUMN id SET DEFAULT nextval('public.mainapp_currentcounter_id_seq'::regclass);


--
-- Name: mainapp_headerdata id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_headerdata ALTER COLUMN id SET DEFAULT nextval('public.mainapp_headerdata_id_seq'::regclass);


--
-- Name: mainapp_historycounter id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_historycounter ALTER COLUMN id SET DEFAULT nextval('public.mainapp_historycounter_id_seq'::regclass);


--
-- Name: mainapp_housecurrent id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_housecurrent ALTER COLUMN id SET DEFAULT nextval('public.mainapp_housecurrent_id_seq'::regclass);


--
-- Name: mainapp_househistory id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_househistory ALTER COLUMN id SET DEFAULT nextval('public.mainapp_househistory_id_seq'::regclass);


--
-- Name: mainapp_mainbook id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_mainbook ALTER COLUMN id SET DEFAULT nextval('public.mainapp_mainbook_id_seq'::regclass);


--
-- Name: mainapp_paymentorder id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_paymentorder ALTER COLUMN id SET DEFAULT nextval('public.mainapp_paymentorder_id_seq'::regclass);


--
-- Name: mainapp_personalaccountstatus id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_personalaccountstatus ALTER COLUMN id SET DEFAULT nextval('public.mainapp_personalaccountstatus_id_seq'::regclass);


--
-- Name: mainapp_recalculations id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_recalculations ALTER COLUMN id SET DEFAULT nextval('public.mainapp_recalculations_id_seq'::regclass);


--
-- Name: mainapp_standart id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_standart ALTER COLUMN id SET DEFAULT nextval('public.mainapp_standart_id_seq'::regclass);


--
-- Name: mainapp_variablepayments id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_variablepayments ALTER COLUMN id SET DEFAULT nextval('public.mainapp_variablepayments_id_seq'::regclass);


--
-- Name: personalacc_siteconfiguration id; Type: DEFAULT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.personalacc_siteconfiguration ALTER COLUMN id SET DEFAULT nextval('public.personalacc_siteconfiguration_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.auth_group (id, name) FROM stdin;
1	Client
2	Manager
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	17
2	1	20
3	1	28
4	1	32
5	1	36
6	1	40
7	1	56
8	1	60
9	1	61
10	1	62
11	1	64
12	1	68
13	1	72
14	1	80
15	1	84
16	1	88
17	1	92
18	1	96
19	1	100
20	1	102
21	1	104
22	1	108
23	1	112
24	1	116
25	1	120
26	1	124
27	2	17
28	2	20
29	2	21
30	2	24
31	2	28
32	2	29
33	2	32
34	2	36
35	2	40
36	2	44
37	2	45
38	2	46
39	2	48
40	2	49
41	2	52
42	2	53
43	2	56
44	2	60
45	2	61
46	2	62
47	2	64
48	2	68
49	2	72
50	2	76
51	2	77
52	2	80
53	2	81
54	2	82
55	2	84
56	2	85
57	2	86
58	2	88
59	2	89
60	2	90
61	2	92
62	2	93
63	2	94
64	2	96
65	2	97
66	2	98
67	2	100
68	2	101
69	2	102
70	2	104
71	2	105
72	2	106
73	2	108
74	2	109
75	2	110
76	2	112
77	2	113
78	2	114
79	2	116
80	2	117
81	2	118
82	2	120
83	2	121
84	2	122
85	2	124
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add Платеж (перепенные)	6	add_variablepayments
22	Can change Платеж (перепенные)	6	change_variablepayments
23	Can delete Платеж (перепенные)	6	delete_variablepayments
24	Can view Платеж (перепенные)	6	view_variablepayments
25	Can add Норматив	7	add_standart
26	Can change Норматив	7	change_standart
27	Can delete Норматив	7	delete_standart
28	Can view Норматив	7	view_standart
29	Can add Перерасчет	8	add_recalculations
30	Can change Перерасчет	8	change_recalculations
31	Can delete Перерасчет	8	delete_recalculations
32	Can view Перерасчет	8	view_recalculations
33	Can add Состояние счета	9	add_personalaccountstatus
34	Can change Состояние счета	9	change_personalaccountstatus
35	Can delete Состояние счета	9	delete_personalaccountstatus
36	Can view Состояние счета	9	view_personalaccountstatus
37	Can add Начисление	10	add_paymentorder
38	Can change Начисление	10	change_paymentorder
39	Can delete Начисление	10	delete_paymentorder
40	Can view Начисление	10	view_paymentorder
41	Can add Главная книга	11	add_mainbook
42	Can change Главная книга	11	change_mainbook
43	Can delete Главная книга	11	delete_mainbook
44	Can view Главная книга	11	view_mainbook
45	Can add Домовой счетчик (история)	12	add_househistory
46	Can change Домовой счетчик (история)	12	change_househistory
47	Can delete Домовой счетчик (история)	12	delete_househistory
48	Can view Домовой счетчик (история)	12	view_househistory
49	Can add Домовой счетчик (текущий)	13	add_housecurrent
50	Can change Домовой счетчик (текущий)	13	change_housecurrent
51	Can delete Домовой счетчик (текущий)	13	delete_housecurrent
52	Can view Домовой счетчик (текущий)	13	view_housecurrent
53	Can add Индивид. счетчик (история)	14	add_historycounter
54	Can change Индивид. счетчик (история)	14	change_historycounter
55	Can delete Индивид. счетчик (история)	14	delete_historycounter
56	Can view Индивид. счетчик (история)	14	view_historycounter
57	Can add Начисление	15	add_headerdata
58	Can change Начисление	15	change_headerdata
59	Can delete Начисление	15	delete_headerdata
60	Can view Начисление	15	view_headerdata
61	Can add Индивид. счетчик (текущий)	16	add_currentcounter
62	Can change Индивид. счетчик (текущий)	16	change_currentcounter
63	Can delete Индивид. счетчик (текущий)	16	delete_currentcounter
64	Can view Индивид. счетчик (текущий)	16	view_currentcounter
65	Can add Платеж (постоянные)	17	add_constantpayments
66	Can change Платеж (постоянные)	17	change_constantpayments
67	Can delete Платеж (постоянные)	17	delete_constantpayments
68	Can view Платеж (постоянные)	17	view_constantpayments
69	Can add Буффер средних начислений	18	add_averageсalculationbuffer
70	Can change Буффер средних начислений	18	change_averageсalculationbuffer
71	Can delete Буффер средних начислений	18	delete_averageсalculationbuffer
72	Can view Буффер средних начислений	18	view_averageсalculationbuffer
73	Can add Пользователь	19	add_user
74	Can change Пользователь	19	change_user
75	Can delete Пользователь	19	delete_user
76	Can view Пользователь	19	view_user
77	Can add Настройки сайта	20	add_siteconfiguration
78	Can change Настройки сайта	20	change_siteconfiguration
79	Can delete Настройки сайта	20	delete_siteconfiguration
80	Can view Настройки сайта	20	view_siteconfiguration
81	Can add Город	21	add_city
82	Can change Город	21	change_city
83	Can delete Город	21	delete_city
84	Can view Город	21	view_city
85	Can add Единица измерения	22	add_metrics
86	Can change Единица измерения	22	change_metrics
87	Can delete Единица измерения	22	delete_metrics
88	Can view Единица измерения	22	view_metrics
89	Can add Новость	23	add_postnews
90	Can change Новость	23	change_postnews
91	Can delete Новость	23	delete_postnews
92	Can view Новость	23	view_postnews
93	Can add Услугу	24	add_services
94	Can change Услугу	24	change_services
95	Can delete Услугу	24	delete_services
96	Can view Услугу	24	view_services
97	Can add Категория услуг	25	add_servicescategory
98	Can change Категория услуг	25	change_servicescategory
99	Can delete Категория услуг	25	delete_servicescategory
100	Can view Категория услуг	25	view_servicescategory
101	Can add Профиль	26	add_userprofile
102	Can change Профиль	26	change_userprofile
103	Can delete Профиль	26	delete_userprofile
104	Can view Профиль	26	view_userprofile
105	Can add Субсидия	27	add_subsidies
106	Can change Субсидия	27	change_subsidies
107	Can delete Субсидия	27	delete_subsidies
108	Can view Субсидия	27	view_subsidies
109	Can add Улица	28	add_street
110	Can change Улица	28	change_street
111	Can delete Улица	28	delete_street
112	Can view Улица	28	view_street
113	Can add Льгота	29	add_privileges
114	Can change Льгота	29	change_privileges
115	Can delete Льгота	29	delete_privileges
116	Can view Льгота	29	view_privileges
117	Can add Дом	30	add_house
118	Can change Дом	30	change_house
119	Can delete Дом	30	delete_house
120	Can view Дом	30	view_house
121	Can add Квартира	31	add_appartament
122	Can change Квартира	31	change_appartament
123	Can delete Квартира	31	delete_appartament
124	Can view Квартира	31	view_appartament
\.


--
-- Data for Name: authnapp_user; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.authnapp_user (id, is_client, is_staff, personal_account, password, name, email, phone, is_active, is_superuser, last_login, activation_key, activation_key_expires) FROM stdin;
3	t	t	777002	pbkdf2_sha256$150000$ImxRxu7xyAuv$eoFAzX2aX12XKHfQjyrkJDcNvNPhFyXG0XVcEY/ZK8E=	Ибрагимова Инга Генадьевна	002@mail.com	79899099887	t	f	2021-08-17 22:18:20.89567+00		2021-08-19 22:09:31.591079+00
4	t	t	777003	pbkdf2_sha256$150000$R9afXPlmLO0o$8DGKNVejWm8ufv/okXcIdoPVBx/14Azowkpb9aUyOqE=	Деревянко Сергей Алексеевич	003@mail.com	78988787876	t	f	2021-08-17 22:19:13.090477+00		2021-08-19 22:09:31.591079+00
5	t	f	111001	pbkdf2_sha256$150000$RVUW1jc3YZi2$oUWSKMfeqiCdOU8uMumh+24cmQ3JSopgqapsBC7iapU=	Авакимян Татьяна Игнатьевна	avak@mail.com	78987776655	t	f	2021-08-17 22:29:15.464466+00		2021-08-19 22:09:31.591079+00
6	t	f	111002	pbkdf2_sha256$150000$g6zLJGsmTjon$4Sh11GG7OtbQ6zE7oDzYh8U5/JzB3v92lsAXsufrksw=	Светлая Ирина Ибрагимова	002@user.com	78998988765	t	f	2021-08-17 22:30:03.655444+00		2021-08-19 22:09:31.591079+00
7	t	f	111003	pbkdf2_sha256$150000$mRYKdui6e60h$chNsEMVT+2oyYau4YQGtysD7+pBmv7K/JnP6LqZRWNc=	Петров Геннадий Александрович	004@mail.com	78909988776	t	f	2021-08-17 22:30:55.925965+00		2021-08-19 22:09:31.591079+00
1	t	t	BigAdmin	pbkdf2_sha256$150000$EvRGtofVDXov$1zgAB1A4zxcrxSOY8Ph0ip2WZTq3e19nex65m6unTMI=	\N	admin@admin.com	\N	t	t	2021-08-17 22:44:01.831252+00		2021-08-19 21:29:23.47216+00
2	t	t	777001	pbkdf2_sha256$150000$IZRjyzo3IHu2$Aw9KaqubZfmAC1B9+3xtuWJao49tOtkaJC4GgWEtGvY=	Петров Иван Викторович	001@mail.ru	79873339876	t	f	2021-08-17 22:47:21.950955+00		2021-08-19 22:09:31.591079+00
\.


--
-- Data for Name: authnapp_user_groups; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.authnapp_user_groups (id, user_id, group_id) FROM stdin;
2	2	2
4	3	2
6	4	2
7	5	1
8	6	1
9	7	1
\.


--
-- Data for Name: authnapp_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.authnapp_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: directory_appartament; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.directory_appartament (id, number, add_number, sq_appart, num_owner, is_active, created, updated, house_id, user_id) FROM stdin;
1	1	0	76.00	3	t	2021-08-17 22:26:07.219308+00	2021-08-17 22:26:07.219325+00	2	5
2	2	0	54.00	2	t	2021-08-17 22:26:07.221253+00	2021-08-17 22:26:07.221269+00	2	6
3	3	0	65.00	2	t	2021-08-17 22:26:07.222098+00	2021-08-17 22:26:07.222111+00	2	7
\.


--
-- Data for Name: directory_city; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.directory_city (id, city, is_active, created, updated) FROM stdin;
1	Тюмень	t	2021-08-17 22:22:38.409684+00	2021-08-17 22:22:38.409708+00
\.


--
-- Data for Name: directory_house; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.directory_house (id, number, add_number, sq_home, is_active, created, updated, category_rate_id, city_id, street_id) FROM stdin;
1	1	-	4567.00	t	2021-08-17 22:23:42.31533+00	2021-08-17 22:23:42.315375+00	1	1	4
3	3	-	7654.00	t	2021-08-17 22:24:40.729912+00	2021-08-17 22:24:40.729927+00	1	1	3
4	4	-	6547.00	t	2021-08-17 22:24:40.731123+00	2021-08-17 22:24:40.731139+00	1	1	3
5	5	-	7654.00	t	2021-08-17 22:24:40.731909+00	2021-08-17 22:24:40.731923+00	1	1	3
2	2	-	6543.00	t	2021-08-17 22:24:03.669751+00	2021-08-17 22:26:07.217237+00	1	1	3
\.


--
-- Data for Name: directory_metrics; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.directory_metrics (id, name, is_active, created, updated) FROM stdin;
1	м2	t	2021-08-17 22:26:54.802558+00	2021-08-17 22:26:54.802675+00
2	м3	t	2021-08-17 22:26:59.779107+00	2021-08-17 22:26:59.779135+00
3	чел.	t	2021-08-17 22:27:55.136083+00	2021-08-17 22:27:55.136106+00
4	кв.	t	2021-08-17 22:27:59.671545+00	2021-08-17 22:27:59.671568+00
5	шт.	t	2021-08-17 22:28:05.156659+00	2021-08-17 22:28:05.156683+00
\.


--
-- Data for Name: directory_postnews; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.directory_postnews (id, title, content, is_active, created, updated) FROM stdin;
1	Мы запустились! УРА!	Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eum incidunt quibusdam necessitatibus consequatur numquam accusantium, voluptate vitae quae id cumque odit? Expedita qui doloribus vitae odio corrupti molestiae distinctio ipsum. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eum incidunt quibusdam necessitatibus consequatur numquam accusantium, voluptate vitae quae id cumque odit? Expedita qui doloribus vitae odio corrupti molestiae distinctio ipsum.	t	2021-08-17 21:42:52.404748+00	2021-08-17 21:42:52.404772+00
2	Поздравляем всех женщин с 8-м Марта!	Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eum incidunt quibusdam necessitatibus consequatur numquam accusantium, voluptate vitae quae id cumque odit? Expedita qui doloribus vitae odio corrupti molestiae distinctio ipsum. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eum incidunt quibusdam necessitatibus consequatur numquam accusantium, voluptate vitae quae id cumque odit? Expedita qui doloribus vitae odio corrupti molestiae distinctio ipsum. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eum incidunt quibusdam necessitatibus consequatur numquam accusantium, voluptate vitae quae id cumque odit? Expedita qui doloribus vitae odio corrupti molestiae distinctio ipsum.	t	2021-08-17 21:44:23.554541+00	2021-08-17 21:44:23.554562+00
3	Мир! Труд! Май!	Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eum incidunt quibusdam necessitatibus consequatur numquam accusantium, voluptate vitae quae id cumque odit? Expedita qui doloribus vitae odio corrupti molestiae distinctio ipsum.	t	2021-08-17 21:44:42.954401+00	2021-08-17 21:44:42.954424+00
4	Ура! Мы повышаем тарифы! ВСЕМ! ВСЕМ! ВСЕМ!	Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eum incidunt quibusdam necessitatibus consequatur numquam accusantium, voluptate vitae quae id cumque odit? Expedita qui doloribus vitae odio corrupti molestiae distinctio ipsum. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eum incidunt quibusdam necessitatibus consequatur numquam accusantium, voluptate vitae quae id cumque odit? Expedita qui doloribus vitae odio corrupti molestiae distinctio ipsum. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eum incidunt quibusdam necessitatibus consequatur numquam accusantium, voluptate vitae quae id cumque odit? Expedita qui doloribus vitae odio corrupti molestiae distinctio ipsum.	t	2021-08-17 21:45:21.033369+00	2021-08-17 21:45:21.033393+00
\.


--
-- Data for Name: directory_privileges; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.directory_privileges (id, sale, is_active, created, updated, "desc", service_id, user_id) FROM stdin;
\.


--
-- Data for Name: directory_services; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.directory_services (id, name, rate, factor, const, is_active, created, updated, category_id, unit_id) FROM stdin;
1	Холодная вода	27.320	1.00	f	t	2021-08-17 22:50:52.415115+00	2021-08-17 22:50:52.415143+00	1	2
2	Горячая вода	45.654	1.00	f	t	2021-08-17 23:04:41.0245+00	2021-08-17 23:12:32.544808+00	1	2
3	Водоотведение	17.300	1.00	t	t	2021-08-17 23:13:26.173999+00	2021-08-17 23:13:38.066215+00	1	2
4	Вывоз ТБО	1.620	1.00	t	t	2021-08-17 23:14:04.849887+00	2021-08-17 23:14:04.849909+00	1	1
5	Содержание и ТО общего имущества	14.060	1.00	t	t	2021-08-17 23:14:55.393448+00	2021-08-17 23:14:55.393472+00	1	1
\.


--
-- Data for Name: directory_servicescategory; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.directory_servicescategory (id, name, is_active, created, updated) FROM stdin;
1	Базовая	t	2021-08-17 22:23:36.317438+00	2021-08-17 22:23:36.317501+00
\.


--
-- Data for Name: directory_street; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.directory_street (id, street, is_active, created, updated, city_id) FROM stdin;
1	Светлая	t	2021-08-17 22:22:38.412592+00	2021-08-17 22:22:38.412612+00	1
2	Зеленая	t	2021-08-17 22:22:38.414889+00	2021-08-17 22:22:38.414904+00	1
4	Центральная	t	2021-08-17 22:22:38.416615+00	2021-08-17 22:23:42.299308+00	1
3	Пушкинская	t	2021-08-17 22:22:38.415822+00	2021-08-17 22:24:40.728387+00	1
\.


--
-- Data for Name: directory_subsidies; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.directory_subsidies (id, sale, is_active, created, updated, "desc", service_id, user_id) FROM stdin;
\.


--
-- Data for Name: directory_userprofile; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.directory_userprofile (id, gender, is_active, created, updated, user_id) FROM stdin;
3	\N	t	2021-08-17 22:12:47.403836+00	2021-08-17 22:19:01.456751+00	3
4	\N	t	2021-08-17 22:14:12.803378+00	2021-08-17 22:21:08.031458+00	4
5	W	t	2021-08-17 22:14:33.843899+00	2021-08-17 22:29:51.074174+00	5
6	W	t	2021-08-17 22:14:41.375531+00	2021-08-17 22:30:46.037188+00	6
7	M	t	2021-08-17 22:14:54.78833+00	2021-08-17 22:32:12.457471+00	7
1	\N	t	2021-08-17 21:30:47.989554+00	2021-08-17 22:44:01.840633+00	1
2	\N	t	2021-08-17 22:11:53.290191+00	2021-08-17 22:47:21.955911+00	2
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-08-17 21:36:17.499394+00	1	Client	1	[{"added": {}}]	3	1
2	2021-08-17 21:40:11.132279+00	2	Manager	1	[{"added": {}}]	3	1
3	2021-08-17 21:41:48.299649+00	1	Настройки сайта	2	[{"changed": {"fields": ["name", "city", "street", "num_building", "phone", "email", "inn", "ps", "bik", "ks", "bank", "web_addr"]}}]	20	1
4	2021-08-17 21:42:52.407898+00	1	Мы запустились! УРА! - (2021-08-17 21:42:52.404772+00:00)	1	[{"added": {}}]	23	1
5	2021-08-17 21:44:23.556659+00	2	Поздравляем всех женщин с 8-м Марта! - (2021-08-17 21:44:23.554562+00:00)	1	[{"added": {}}]	23	1
6	2021-08-17 21:44:42.956326+00	3	Мир! Труд! Май! - (2021-08-17 21:44:42.954424+00:00)	1	[{"added": {}}]	23	1
7	2021-08-17 21:45:21.035614+00	4	Ура! Мы повышаем тарифы! ВСЕМ! ВСЕМ! ВСЕМ! - (2021-08-17 21:45:21.033393+00:00)	1	[{"added": {}}]	23	1
8	2021-08-17 22:11:53.298169+00	2	(777001) - None	1	[{"added": {}}]	19	1
9	2021-08-17 22:12:14.364579+00	2	(777001) - None	2	[]	19	1
10	2021-08-17 22:12:47.406398+00	3	(777002) - None	1	[{"added": {}}]	19	1
11	2021-08-17 22:12:51.540062+00	3	(777002) - None	2	[]	19	1
12	2021-08-17 22:14:12.805451+00	4	(777003) - None	1	[{"added": {}}]	19	1
13	2021-08-17 22:14:33.846654+00	5	(111001) - None	1	[{"added": {}}]	19	1
14	2021-08-17 22:14:41.378444+00	6	(111002) - None	1	[{"added": {}}]	19	1
15	2021-08-17 22:14:54.791673+00	7	(111003) - None	1	[{"added": {}}]	19	1
16	2021-08-17 22:22:38.417518+00	1	Тюмень	1	[{"added": {}}, {"added": {"name": "\\u0423\\u043b\\u0438\\u0446\\u0430", "object": "\\u0443\\u043b.\\u0421\\u0432\\u0435\\u0442\\u043b\\u0430\\u044f"}}, {"added": {"name": "\\u0423\\u043b\\u0438\\u0446\\u0430", "object": "\\u0443\\u043b.\\u0417\\u0435\\u043b\\u0435\\u043d\\u0430\\u044f"}}, {"added": {"name": "\\u0423\\u043b\\u0438\\u0446\\u0430", "object": "\\u0443\\u043b.\\u041f\\u0443\\u0448\\u043a\\u0438\\u043d\\u0441\\u043a\\u0430\\u044f"}}, {"added": {"name": "\\u0423\\u043b\\u0438\\u0446\\u0430", "object": "\\u0443\\u043b.\\u0426\\u0435\\u043d\\u0442\\u0440\\u0430\\u043b\\u044c\\u043d\\u0430\\u044f"}}]	21	1
17	2021-08-17 22:23:36.320851+00	1	Базовая	1	[{"added": {}}]	25	1
18	2021-08-17 22:23:42.31986+00	4	ул.Центральная	2	[{"added": {"name": "\\u0414\\u043e\\u043c", "object": "\\u0443\\u043b.\\u0426\\u0435\\u043d\\u0442\\u0440\\u0430\\u043b\\u044c\\u043d\\u0430\\u044f, \\u0434.1, \\u043a.-"}}]	28	1
19	2021-08-17 22:24:03.671798+00	3	ул.Пушкинская	2	[{"added": {"name": "\\u0414\\u043e\\u043c", "object": "\\u0443\\u043b.\\u041f\\u0443\\u0448\\u043a\\u0438\\u043d\\u0441\\u043a\\u0430\\u044f, \\u0434.2, \\u043a.-"}}]	28	1
20	2021-08-17 22:24:40.732766+00	3	ул.Пушкинская	2	[{"added": {"name": "\\u0414\\u043e\\u043c", "object": "\\u0443\\u043b.\\u041f\\u0443\\u0448\\u043a\\u0438\\u043d\\u0441\\u043a\\u0430\\u044f, \\u0434.3, \\u043a.-"}}, {"added": {"name": "\\u0414\\u043e\\u043c", "object": "\\u0443\\u043b.\\u041f\\u0443\\u0448\\u043a\\u0438\\u043d\\u0441\\u043a\\u0430\\u044f, \\u0434.4, \\u043a.-"}}, {"added": {"name": "\\u0414\\u043e\\u043c", "object": "\\u0443\\u043b.\\u041f\\u0443\\u0448\\u043a\\u0438\\u043d\\u0441\\u043a\\u0430\\u044f, \\u0434.5, \\u043a.-"}}]	28	1
21	2021-08-17 22:26:07.223184+00	2	ул.Пушкинская, д.2, к.-	2	[{"added": {"name": "\\u041a\\u0432\\u0430\\u0440\\u0442\\u0438\\u0440\\u0430", "object": "\\u0443\\u043b.\\u041f\\u0443\\u0448\\u043a\\u0438\\u043d\\u0441\\u043a\\u0430\\u044f, \\u0434.2, \\u043a\\u0432.1, \\u043a\\u043e\\u043c\\u043d.0"}}, {"added": {"name": "\\u041a\\u0432\\u0430\\u0440\\u0442\\u0438\\u0440\\u0430", "object": "\\u0443\\u043b.\\u041f\\u0443\\u0448\\u043a\\u0438\\u043d\\u0441\\u043a\\u0430\\u044f, \\u0434.2, \\u043a\\u0432.2, \\u043a\\u043e\\u043c\\u043d.0"}}, {"added": {"name": "\\u041a\\u0432\\u0430\\u0440\\u0442\\u0438\\u0440\\u0430", "object": "\\u0443\\u043b.\\u041f\\u0443\\u0448\\u043a\\u0438\\u043d\\u0441\\u043a\\u0430\\u044f, \\u0434.2, \\u043a\\u0432.3, \\u043a\\u043e\\u043c\\u043d.0"}}]	30	1
22	2021-08-17 22:26:54.805953+00	1	м2	1	[{"added": {}}]	22	1
23	2021-08-17 22:26:59.782029+00	2	м3	1	[{"added": {}}]	22	1
24	2021-08-17 22:27:55.137963+00	3	чел.	1	[{"added": {}}]	22	1
25	2021-08-17 22:27:59.673758+00	4	кв.	1	[{"added": {}}]	22	1
26	2021-08-17 22:28:05.159068+00	5	шт.	1	[{"added": {}}]	22	1
27	2021-08-17 22:44:33.201285+00	1	Период - 2021-07-01, ул.Пушкинская, Дом №2, к.-	1	[{"added": {}}]	12	1
28	2021-08-17 22:44:47.957422+00	2	Период - 2021-07-01, ул.Пушкинская, Дом №5, к.-	1	[{"added": {}}]	12	1
29	2021-08-17 22:45:03.727984+00	3	Период - 2021-07-01, ул.Пушкинская, Дом №4, к.-	1	[{"added": {}}]	12	1
30	2021-08-17 22:45:40.303206+00	4	Период - 2021-07-01, ул.Пушкинская, Дом №3, к.-	1	[{"added": {}}]	12	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	mainapp	variablepayments
7	mainapp	standart
8	mainapp	recalculations
9	mainapp	personalaccountstatus
10	mainapp	paymentorder
11	mainapp	mainbook
12	mainapp	househistory
13	mainapp	housecurrent
14	mainapp	historycounter
15	mainapp	headerdata
16	mainapp	currentcounter
17	mainapp	constantpayments
18	mainapp	averageсalculationbuffer
19	authnapp	user
20	personalacc	siteconfiguration
21	directory	city
22	directory	metrics
23	directory	postnews
24	directory	services
25	directory	servicescategory
26	directory	userprofile
27	directory	subsidies
28	directory	street
29	directory	privileges
30	directory	house
31	directory	appartament
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-08-17 21:29:16.733538+00
2	contenttypes	0002_remove_content_type_name	2021-08-17 21:29:16.750128+00
3	auth	0001_initial	2021-08-17 21:29:16.786129+00
4	auth	0002_alter_permission_name_max_length	2021-08-17 21:29:16.822962+00
5	auth	0003_alter_user_email_max_length	2021-08-17 21:29:16.831607+00
6	auth	0004_alter_user_username_opts	2021-08-17 21:29:16.84179+00
7	auth	0005_alter_user_last_login_null	2021-08-17 21:29:16.851822+00
8	auth	0006_require_contenttypes_0002	2021-08-17 21:29:16.855902+00
9	auth	0007_alter_validators_add_error_messages	2021-08-17 21:29:16.865079+00
10	auth	0008_alter_user_username_max_length	2021-08-17 21:29:16.876379+00
11	auth	0009_alter_user_last_name_max_length	2021-08-17 21:29:16.885288+00
12	auth	0010_alter_group_name_max_length	2021-08-17 21:29:16.898272+00
13	auth	0011_update_proxy_permissions	2021-08-17 21:29:16.909039+00
14	authnapp	0001_initial	2021-08-17 21:29:16.947625+00
15	admin	0001_initial	2021-08-17 21:29:17.004199+00
16	admin	0002_logentry_remove_auto_add	2021-08-17 21:29:17.027224+00
17	admin	0003_logentry_add_action_flag_choices	2021-08-17 21:29:17.040931+00
18	directory	0001_initial	2021-08-17 21:29:17.229836+00
19	mainapp	0001_initial	2021-08-17 21:29:17.747313+00
20	personalacc	0001_initial	2021-08-17 21:29:17.840469+00
21	sessions	0001_initial	2021-08-17 21:29:17.859664+00
22	authnapp	0002_auto_20210817_2210	2021-08-17 22:10:18.767308+00
23	directory	0002_remove_userprofile_type_electric_meter	2021-08-17 22:10:18.807176+00
24	mainapp	0002_auto_20210817_2210	2021-08-17 22:10:18.948337+00
25	authnapp	0003_auto_20210817_2317	2021-08-17 23:17:19.931946+00
26	mainapp	0003_auto_20210817_2317	2021-08-17 23:17:20.070309+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: mainapp_averageсalculationbuffer; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public."mainapp_averageсalculationbuffer" (id, col_water, hot_water, sewage, created, updated, user_id) FROM stdin;
\.


--
-- Data for Name: mainapp_constantpayments; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_constantpayments (id, data, total, pre_total, created, updated, user_id) FROM stdin;
\.


--
-- Data for Name: mainapp_currentcounter; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_currentcounter (id, period, col_water, hot_water, created, updated, user_id) FROM stdin;
\.


--
-- Data for Name: mainapp_headerdata; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_headerdata (id, data, created, updated, user_id) FROM stdin;
\.


--
-- Data for Name: mainapp_historycounter; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_historycounter (id, period, col_water, hot_water, created, updated, user_id) FROM stdin;
\.


--
-- Data for Name: mainapp_housecurrent; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_housecurrent (id, period, col_water, hot_water, created, updated, house_id) FROM stdin;
\.


--
-- Data for Name: mainapp_househistory; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_househistory (id, period, col_water, hot_water, created, updated, house_id) FROM stdin;
1	2021-07-01	1000.000	1000.000	2021-08-17 22:44:33.195982+00	2021-08-17 22:44:33.196005+00	2
2	2021-07-01	1000.000	1000.000	2021-08-17 22:44:47.953169+00	2021-08-17 22:44:47.95319+00	5
3	2021-07-01	1000.000	1000.000	2021-08-17 22:45:03.723715+00	2021-08-17 22:45:03.723739+00	4
4	2021-07-01	1000.000	1000.000	2021-08-17 22:45:40.298835+00	2021-08-17 22:45:40.298889+00	3
\.


--
-- Data for Name: mainapp_mainbook; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_mainbook (id, period, direction, amount, created, updated, user_id) FROM stdin;
\.


--
-- Data for Name: mainapp_paymentorder; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_paymentorder (id, period, header_data, constant_data, variable_data, amount, pre_amount, created, updated, user_id) FROM stdin;
\.


--
-- Data for Name: mainapp_personalaccountstatus; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_personalaccountstatus (id, amount, created, updated, user_id) FROM stdin;
\.


--
-- Data for Name: mainapp_recalculations; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_recalculations (id, period, recalc, "desc", created, updated, service_id, user_id) FROM stdin;
\.


--
-- Data for Name: mainapp_standart; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_standart (id, period, col_water, hot_water, created, updated, house_id) FROM stdin;
\.


--
-- Data for Name: mainapp_variablepayments; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.mainapp_variablepayments (id, period, data, total, pre_total, created, updated, user_id) FROM stdin;
\.


--
-- Data for Name: personalacc_siteconfiguration; Type: TABLE DATA; Schema: public; Owner: post
--

COPY public.personalacc_siteconfiguration (id, name, city, street, num_building, phone, email, inn, ps, bik, ks, bank, web_addr, key_ya, lat, lon, footer_copyright, is_active, created, updated) FROM stdin;
1	УК Новый город	г. Тюмень	ул. Свободы	д. 5	79823212334	info@uk.ru	1533455446	48800939999000393949	1009089074	38700939999000393949	ОАО "Cбербанк"	www.uk-newcity.ru				Все права защищены © Тюмень 2015 - 2021 гг.	t	2021-08-17 21:31:01.281353+00	2021-08-17 21:41:48.298024+00
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 85, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 124, true);


--
-- Name: authnapp_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.authnapp_user_groups_id_seq', 9, true);


--
-- Name: authnapp_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.authnapp_user_id_seq', 7, true);


--
-- Name: authnapp_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.authnapp_user_user_permissions_id_seq', 1, false);


--
-- Name: directory_appartament_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.directory_appartament_id_seq', 3, true);


--
-- Name: directory_city_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.directory_city_id_seq', 1, true);


--
-- Name: directory_house_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.directory_house_id_seq', 5, true);


--
-- Name: directory_metrics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.directory_metrics_id_seq', 5, true);


--
-- Name: directory_postnews_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.directory_postnews_id_seq', 4, true);


--
-- Name: directory_privileges_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.directory_privileges_id_seq', 1, false);


--
-- Name: directory_services_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.directory_services_id_seq', 5, true);


--
-- Name: directory_servicescategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.directory_servicescategory_id_seq', 1, true);


--
-- Name: directory_street_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.directory_street_id_seq', 4, true);


--
-- Name: directory_subsidies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.directory_subsidies_id_seq', 1, false);


--
-- Name: directory_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.directory_userprofile_id_seq', 7, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 30, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 31, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- Name: mainapp_averageсalculationbuffer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public."mainapp_averageсalculationbuffer_id_seq"', 1, false);


--
-- Name: mainapp_constantpayments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_constantpayments_id_seq', 1, false);


--
-- Name: mainapp_currentcounter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_currentcounter_id_seq', 1, false);


--
-- Name: mainapp_headerdata_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_headerdata_id_seq', 1, false);


--
-- Name: mainapp_historycounter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_historycounter_id_seq', 1, false);


--
-- Name: mainapp_housecurrent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_housecurrent_id_seq', 1, false);


--
-- Name: mainapp_househistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_househistory_id_seq', 4, true);


--
-- Name: mainapp_mainbook_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_mainbook_id_seq', 1, false);


--
-- Name: mainapp_paymentorder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_paymentorder_id_seq', 1, false);


--
-- Name: mainapp_personalaccountstatus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_personalaccountstatus_id_seq', 1, false);


--
-- Name: mainapp_recalculations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_recalculations_id_seq', 1, false);


--
-- Name: mainapp_standart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_standart_id_seq', 1, false);


--
-- Name: mainapp_variablepayments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.mainapp_variablepayments_id_seq', 1, false);


--
-- Name: personalacc_siteconfiguration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: post
--

SELECT pg_catalog.setval('public.personalacc_siteconfiguration_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authnapp_user authnapp_user_email_key; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user
    ADD CONSTRAINT authnapp_user_email_key UNIQUE (email);


--
-- Name: authnapp_user_groups authnapp_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user_groups
    ADD CONSTRAINT authnapp_user_groups_pkey PRIMARY KEY (id);


--
-- Name: authnapp_user_groups authnapp_user_groups_user_id_group_id_c1a0fa10_uniq; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user_groups
    ADD CONSTRAINT authnapp_user_groups_user_id_group_id_c1a0fa10_uniq UNIQUE (user_id, group_id);


--
-- Name: authnapp_user authnapp_user_personal_account_key; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user
    ADD CONSTRAINT authnapp_user_personal_account_key UNIQUE (personal_account);


--
-- Name: authnapp_user authnapp_user_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user
    ADD CONSTRAINT authnapp_user_pkey PRIMARY KEY (id);


--
-- Name: authnapp_user_user_permissions authnapp_user_user_permi_user_id_permission_id_26a717c2_uniq; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user_user_permissions
    ADD CONSTRAINT authnapp_user_user_permi_user_id_permission_id_26a717c2_uniq UNIQUE (user_id, permission_id);


--
-- Name: authnapp_user_user_permissions authnapp_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user_user_permissions
    ADD CONSTRAINT authnapp_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: directory_appartament directory_appartament_house_id_number_add_number_dd82b8d9_uniq; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_appartament
    ADD CONSTRAINT directory_appartament_house_id_number_add_number_dd82b8d9_uniq UNIQUE (house_id, number, add_number);


--
-- Name: directory_appartament directory_appartament_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_appartament
    ADD CONSTRAINT directory_appartament_pkey PRIMARY KEY (id);


--
-- Name: directory_city directory_city_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_city
    ADD CONSTRAINT directory_city_pkey PRIMARY KEY (id);


--
-- Name: directory_house directory_house_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_house
    ADD CONSTRAINT directory_house_pkey PRIMARY KEY (id);


--
-- Name: directory_metrics directory_metrics_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_metrics
    ADD CONSTRAINT directory_metrics_pkey PRIMARY KEY (id);


--
-- Name: directory_postnews directory_postnews_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_postnews
    ADD CONSTRAINT directory_postnews_pkey PRIMARY KEY (id);


--
-- Name: directory_privileges directory_privileges_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_privileges
    ADD CONSTRAINT directory_privileges_pkey PRIMARY KEY (id);


--
-- Name: directory_services directory_services_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_services
    ADD CONSTRAINT directory_services_pkey PRIMARY KEY (id);


--
-- Name: directory_servicescategory directory_servicescategory_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_servicescategory
    ADD CONSTRAINT directory_servicescategory_pkey PRIMARY KEY (id);


--
-- Name: directory_street directory_street_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_street
    ADD CONSTRAINT directory_street_pkey PRIMARY KEY (id);


--
-- Name: directory_subsidies directory_subsidies_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_subsidies
    ADD CONSTRAINT directory_subsidies_pkey PRIMARY KEY (id);


--
-- Name: directory_userprofile directory_userprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_userprofile
    ADD CONSTRAINT directory_userprofile_pkey PRIMARY KEY (id);


--
-- Name: directory_userprofile directory_userprofile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_userprofile
    ADD CONSTRAINT directory_userprofile_user_id_key UNIQUE (user_id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: mainapp_averageсalculationbuffer mainapp_averageсalculationbuffer_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public."mainapp_averageсalculationbuffer"
    ADD CONSTRAINT "mainapp_averageсalculationbuffer_pkey" PRIMARY KEY (id);


--
-- Name: mainapp_averageсalculationbuffer mainapp_averageсalculationbuffer_user_id_key; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public."mainapp_averageсalculationbuffer"
    ADD CONSTRAINT "mainapp_averageсalculationbuffer_user_id_key" UNIQUE (user_id);


--
-- Name: mainapp_constantpayments mainapp_constantpayments_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_constantpayments
    ADD CONSTRAINT mainapp_constantpayments_pkey PRIMARY KEY (id);


--
-- Name: mainapp_currentcounter mainapp_currentcounter_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_currentcounter
    ADD CONSTRAINT mainapp_currentcounter_pkey PRIMARY KEY (id);


--
-- Name: mainapp_headerdata mainapp_headerdata_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_headerdata
    ADD CONSTRAINT mainapp_headerdata_pkey PRIMARY KEY (id);


--
-- Name: mainapp_historycounter mainapp_historycounter_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_historycounter
    ADD CONSTRAINT mainapp_historycounter_pkey PRIMARY KEY (id);


--
-- Name: mainapp_housecurrent mainapp_housecurrent_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_housecurrent
    ADD CONSTRAINT mainapp_housecurrent_pkey PRIMARY KEY (id);


--
-- Name: mainapp_househistory mainapp_househistory_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_househistory
    ADD CONSTRAINT mainapp_househistory_pkey PRIMARY KEY (id);


--
-- Name: mainapp_mainbook mainapp_mainbook_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_mainbook
    ADD CONSTRAINT mainapp_mainbook_pkey PRIMARY KEY (id);


--
-- Name: mainapp_paymentorder mainapp_paymentorder_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_paymentorder
    ADD CONSTRAINT mainapp_paymentorder_pkey PRIMARY KEY (id);


--
-- Name: mainapp_personalaccountstatus mainapp_personalaccountstatus_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_personalaccountstatus
    ADD CONSTRAINT mainapp_personalaccountstatus_pkey PRIMARY KEY (id);


--
-- Name: mainapp_personalaccountstatus mainapp_personalaccountstatus_user_id_key; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_personalaccountstatus
    ADD CONSTRAINT mainapp_personalaccountstatus_user_id_key UNIQUE (user_id);


--
-- Name: mainapp_recalculations mainapp_recalculations_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_recalculations
    ADD CONSTRAINT mainapp_recalculations_pkey PRIMARY KEY (id);


--
-- Name: mainapp_standart mainapp_standart_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_standart
    ADD CONSTRAINT mainapp_standart_pkey PRIMARY KEY (id);


--
-- Name: mainapp_variablepayments mainapp_variablepayments_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_variablepayments
    ADD CONSTRAINT mainapp_variablepayments_pkey PRIMARY KEY (id);


--
-- Name: personalacc_siteconfiguration personalacc_siteconfiguration_pkey; Type: CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.personalacc_siteconfiguration
    ADD CONSTRAINT personalacc_siteconfiguration_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: authnapp_user_email_43a63878_like; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX authnapp_user_email_43a63878_like ON public.authnapp_user USING btree (email varchar_pattern_ops);


--
-- Name: authnapp_user_groups_group_id_412a245a; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX authnapp_user_groups_group_id_412a245a ON public.authnapp_user_groups USING btree (group_id);


--
-- Name: authnapp_user_groups_user_id_4d5f3c9c; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX authnapp_user_groups_user_id_4d5f3c9c ON public.authnapp_user_groups USING btree (user_id);


--
-- Name: authnapp_user_personal_account_aa717c94_like; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX authnapp_user_personal_account_aa717c94_like ON public.authnapp_user USING btree (personal_account varchar_pattern_ops);


--
-- Name: authnapp_user_user_permissions_permission_id_f279ea2f; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX authnapp_user_user_permissions_permission_id_f279ea2f ON public.authnapp_user_user_permissions USING btree (permission_id);


--
-- Name: authnapp_user_user_permissions_user_id_6095be0e; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX authnapp_user_user_permissions_user_id_6095be0e ON public.authnapp_user_user_permissions USING btree (user_id);


--
-- Name: directory_appartament_house_id_68a76012; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_appartament_house_id_68a76012 ON public.directory_appartament USING btree (house_id);


--
-- Name: directory_appartament_is_active_e410ebf3; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_appartament_is_active_e410ebf3 ON public.directory_appartament USING btree (is_active);


--
-- Name: directory_appartament_user_id_9fc7999f; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_appartament_user_id_9fc7999f ON public.directory_appartament USING btree (user_id);


--
-- Name: directory_city_is_active_133a8c12; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_city_is_active_133a8c12 ON public.directory_city USING btree (is_active);


--
-- Name: directory_house_category_rate_id_27671304; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_house_category_rate_id_27671304 ON public.directory_house USING btree (category_rate_id);


--
-- Name: directory_house_city_id_b8d2c5d0; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_house_city_id_b8d2c5d0 ON public.directory_house USING btree (city_id);


--
-- Name: directory_house_is_active_f23e60d6; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_house_is_active_f23e60d6 ON public.directory_house USING btree (is_active);


--
-- Name: directory_house_street_id_7c93a472; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_house_street_id_7c93a472 ON public.directory_house USING btree (street_id);


--
-- Name: directory_metrics_is_active_85221b95; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_metrics_is_active_85221b95 ON public.directory_metrics USING btree (is_active);


--
-- Name: directory_postnews_is_active_f2fb437e; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_postnews_is_active_f2fb437e ON public.directory_postnews USING btree (is_active);


--
-- Name: directory_privileges_is_active_caaf08b8; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_privileges_is_active_caaf08b8 ON public.directory_privileges USING btree (is_active);


--
-- Name: directory_privileges_service_id_bdf2552a; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_privileges_service_id_bdf2552a ON public.directory_privileges USING btree (service_id);


--
-- Name: directory_privileges_user_id_c9304130; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_privileges_user_id_c9304130 ON public.directory_privileges USING btree (user_id);


--
-- Name: directory_services_category_id_56ef4309; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_services_category_id_56ef4309 ON public.directory_services USING btree (category_id);


--
-- Name: directory_services_const_099d9f8d; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_services_const_099d9f8d ON public.directory_services USING btree (const);


--
-- Name: directory_services_is_active_686f5f8a; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_services_is_active_686f5f8a ON public.directory_services USING btree (is_active);


--
-- Name: directory_services_unit_id_821d86a7; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_services_unit_id_821d86a7 ON public.directory_services USING btree (unit_id);


--
-- Name: directory_servicescategory_is_active_f4e2e6c3; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_servicescategory_is_active_f4e2e6c3 ON public.directory_servicescategory USING btree (is_active);


--
-- Name: directory_street_city_id_bc5b69cd; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_street_city_id_bc5b69cd ON public.directory_street USING btree (city_id);


--
-- Name: directory_street_is_active_39f9fc08; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_street_is_active_39f9fc08 ON public.directory_street USING btree (is_active);


--
-- Name: directory_subsidies_is_active_d517e782; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_subsidies_is_active_d517e782 ON public.directory_subsidies USING btree (is_active);


--
-- Name: directory_subsidies_service_id_85641a8b; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_subsidies_service_id_85641a8b ON public.directory_subsidies USING btree (service_id);


--
-- Name: directory_subsidies_user_id_1265274d; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_subsidies_user_id_1265274d ON public.directory_subsidies USING btree (user_id);


--
-- Name: directory_userprofile_is_active_3749d922; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX directory_userprofile_is_active_3749d922 ON public.directory_userprofile USING btree (is_active);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: mainapp_constantpayments_user_id_16c2d464; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_constantpayments_user_id_16c2d464 ON public.mainapp_constantpayments USING btree (user_id);


--
-- Name: mainapp_currentcounter_user_id_2f0d47ca; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_currentcounter_user_id_2f0d47ca ON public.mainapp_currentcounter USING btree (user_id);


--
-- Name: mainapp_headerdata_user_id_cb0f87de; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_headerdata_user_id_cb0f87de ON public.mainapp_headerdata USING btree (user_id);


--
-- Name: mainapp_historycounter_user_id_1354c610; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_historycounter_user_id_1354c610 ON public.mainapp_historycounter USING btree (user_id);


--
-- Name: mainapp_housecurrent_house_id_55d087e7; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_housecurrent_house_id_55d087e7 ON public.mainapp_housecurrent USING btree (house_id);


--
-- Name: mainapp_househistory_house_id_1b195ca0; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_househistory_house_id_1b195ca0 ON public.mainapp_househistory USING btree (house_id);


--
-- Name: mainapp_mainbook_user_id_96d2e8a4; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_mainbook_user_id_96d2e8a4 ON public.mainapp_mainbook USING btree (user_id);


--
-- Name: mainapp_paymentorder_user_id_dff7020c; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_paymentorder_user_id_dff7020c ON public.mainapp_paymentorder USING btree (user_id);


--
-- Name: mainapp_recalculations_service_id_6719b5d1; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_recalculations_service_id_6719b5d1 ON public.mainapp_recalculations USING btree (service_id);


--
-- Name: mainapp_recalculations_user_id_b5296158; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_recalculations_user_id_b5296158 ON public.mainapp_recalculations USING btree (user_id);


--
-- Name: mainapp_standart_house_id_f506c58e; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_standart_house_id_f506c58e ON public.mainapp_standart USING btree (house_id);


--
-- Name: mainapp_variablepayments_user_id_23c74e13; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX mainapp_variablepayments_user_id_23c74e13 ON public.mainapp_variablepayments USING btree (user_id);


--
-- Name: personalacc_siteconfiguration_is_active_89ee3712; Type: INDEX; Schema: public; Owner: post
--

CREATE INDEX personalacc_siteconfiguration_is_active_89ee3712 ON public.personalacc_siteconfiguration USING btree (is_active);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authnapp_user_groups authnapp_user_groups_group_id_412a245a_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user_groups
    ADD CONSTRAINT authnapp_user_groups_group_id_412a245a_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authnapp_user_groups authnapp_user_groups_user_id_4d5f3c9c_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user_groups
    ADD CONSTRAINT authnapp_user_groups_user_id_4d5f3c9c_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authnapp_user_user_permissions authnapp_user_user_p_permission_id_f279ea2f_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user_user_permissions
    ADD CONSTRAINT authnapp_user_user_p_permission_id_f279ea2f_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authnapp_user_user_permissions authnapp_user_user_p_user_id_6095be0e_fk_authnapp_; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.authnapp_user_user_permissions
    ADD CONSTRAINT authnapp_user_user_p_user_id_6095be0e_fk_authnapp_ FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_appartament directory_appartament_house_id_68a76012_fk_directory_house_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_appartament
    ADD CONSTRAINT directory_appartament_house_id_68a76012_fk_directory_house_id FOREIGN KEY (house_id) REFERENCES public.directory_house(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_appartament directory_appartament_user_id_9fc7999f_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_appartament
    ADD CONSTRAINT directory_appartament_user_id_9fc7999f_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_house directory_house_category_rate_id_27671304_fk_directory; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_house
    ADD CONSTRAINT directory_house_category_rate_id_27671304_fk_directory FOREIGN KEY (category_rate_id) REFERENCES public.directory_servicescategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_house directory_house_city_id_b8d2c5d0_fk_directory_city_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_house
    ADD CONSTRAINT directory_house_city_id_b8d2c5d0_fk_directory_city_id FOREIGN KEY (city_id) REFERENCES public.directory_city(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_house directory_house_street_id_7c93a472_fk_directory_street_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_house
    ADD CONSTRAINT directory_house_street_id_7c93a472_fk_directory_street_id FOREIGN KEY (street_id) REFERENCES public.directory_street(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_privileges directory_privileges_service_id_bdf2552a_fk_directory; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_privileges
    ADD CONSTRAINT directory_privileges_service_id_bdf2552a_fk_directory FOREIGN KEY (service_id) REFERENCES public.directory_services(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_privileges directory_privileges_user_id_c9304130_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_privileges
    ADD CONSTRAINT directory_privileges_user_id_c9304130_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_services directory_services_category_id_56ef4309_fk_directory; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_services
    ADD CONSTRAINT directory_services_category_id_56ef4309_fk_directory FOREIGN KEY (category_id) REFERENCES public.directory_servicescategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_services directory_services_unit_id_821d86a7_fk_directory_metrics_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_services
    ADD CONSTRAINT directory_services_unit_id_821d86a7_fk_directory_metrics_id FOREIGN KEY (unit_id) REFERENCES public.directory_metrics(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_street directory_street_city_id_bc5b69cd_fk_directory_city_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_street
    ADD CONSTRAINT directory_street_city_id_bc5b69cd_fk_directory_city_id FOREIGN KEY (city_id) REFERENCES public.directory_city(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_subsidies directory_subsidies_service_id_85641a8b_fk_directory; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_subsidies
    ADD CONSTRAINT directory_subsidies_service_id_85641a8b_fk_directory FOREIGN KEY (service_id) REFERENCES public.directory_services(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_subsidies directory_subsidies_user_id_1265274d_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_subsidies
    ADD CONSTRAINT directory_subsidies_user_id_1265274d_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: directory_userprofile directory_userprofile_user_id_8d2b7274_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.directory_userprofile
    ADD CONSTRAINT directory_userprofile_user_id_8d2b7274_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_averageсalculationbuffer mainapp_averageсalcu_user_id_0f1ac522_fk_authnapp_; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public."mainapp_averageсalculationbuffer"
    ADD CONSTRAINT "mainapp_averageсalcu_user_id_0f1ac522_fk_authnapp_" FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_constantpayments mainapp_constantpayments_user_id_16c2d464_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_constantpayments
    ADD CONSTRAINT mainapp_constantpayments_user_id_16c2d464_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_currentcounter mainapp_currentcounter_user_id_2f0d47ca_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_currentcounter
    ADD CONSTRAINT mainapp_currentcounter_user_id_2f0d47ca_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_headerdata mainapp_headerdata_user_id_cb0f87de_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_headerdata
    ADD CONSTRAINT mainapp_headerdata_user_id_cb0f87de_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_historycounter mainapp_historycounter_user_id_1354c610_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_historycounter
    ADD CONSTRAINT mainapp_historycounter_user_id_1354c610_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_housecurrent mainapp_housecurrent_house_id_55d087e7_fk_directory_house_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_housecurrent
    ADD CONSTRAINT mainapp_housecurrent_house_id_55d087e7_fk_directory_house_id FOREIGN KEY (house_id) REFERENCES public.directory_house(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_househistory mainapp_househistory_house_id_1b195ca0_fk_directory_house_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_househistory
    ADD CONSTRAINT mainapp_househistory_house_id_1b195ca0_fk_directory_house_id FOREIGN KEY (house_id) REFERENCES public.directory_house(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_mainbook mainapp_mainbook_user_id_96d2e8a4_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_mainbook
    ADD CONSTRAINT mainapp_mainbook_user_id_96d2e8a4_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_paymentorder mainapp_paymentorder_user_id_dff7020c_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_paymentorder
    ADD CONSTRAINT mainapp_paymentorder_user_id_dff7020c_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_personalaccountstatus mainapp_personalacco_user_id_f4e24719_fk_authnapp_; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_personalaccountstatus
    ADD CONSTRAINT mainapp_personalacco_user_id_f4e24719_fk_authnapp_ FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_recalculations mainapp_recalculatio_service_id_6719b5d1_fk_directory; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_recalculations
    ADD CONSTRAINT mainapp_recalculatio_service_id_6719b5d1_fk_directory FOREIGN KEY (service_id) REFERENCES public.directory_services(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_recalculations mainapp_recalculations_user_id_b5296158_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_recalculations
    ADD CONSTRAINT mainapp_recalculations_user_id_b5296158_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_standart mainapp_standart_house_id_f506c58e_fk_directory_house_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_standart
    ADD CONSTRAINT mainapp_standart_house_id_f506c58e_fk_directory_house_id FOREIGN KEY (house_id) REFERENCES public.directory_house(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mainapp_variablepayments mainapp_variablepayments_user_id_23c74e13_fk_authnapp_user_id; Type: FK CONSTRAINT; Schema: public; Owner: post
--

ALTER TABLE ONLY public.mainapp_variablepayments
    ADD CONSTRAINT mainapp_variablepayments_user_id_23c74e13_fk_authnapp_user_id FOREIGN KEY (user_id) REFERENCES public.authnapp_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: post
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE postgres OWNER TO post;

\connect postgres

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: post
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

