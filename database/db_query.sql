CREATE TABLE IF NOT EXISTS public.station_service
(
    station_city character varying(50) COLLATE pg_catalog."default" NOT NULL,
    country character varying(2) COLLATE pg_catalog."default" NOT NULL,
    ov_bike boolean NOT NULL,
    elevator boolean NOT NULL,
    toilet boolean NOT NULL,
    park_and_ride boolean NOT NULL,
    lat double precision NOT NULL,
    lon double precision NOT NULL,
    CONSTRAINT station_service_pkey PRIMARY KEY (station_city)
);

CREATE TABLE IF NOT EXISTS public.message_send
(
    name_user character varying(30) COLLATE pg_catalog."default" NOT NULL,
    date_message date NOT NULL,
    time_message time(6) without time zone NOT NULL,
    message_column character varying(255) COLLATE pg_catalog."default" NOT NULL,
    station_city character varying(255) COLLATE pg_catalog."default",
    message_id integer NOT NULL,
    CONSTRAINT message_send_pkey PRIMARY KEY (message_id),
    CONSTRAINT station_city_fkey FOREIGN KEY (station_city)
        REFERENCES public.station_service (station_city) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.message_mod
(
    approval character varying(30) COLLATE pg_catalog."default" NOT NULL,
    mod_email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    mod_date date NOT NULL,
    mod_time time(6) without time zone NOT NULL,
    mod_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    message_id integer NOT NULL,
    CONSTRAINT message_pkey PRIMARY KEY (message_id),
    CONSTRAINT message_id FOREIGN KEY (message_id)
        REFERENCES public.message_send (message_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

INSERT INTO station_service (
     -- station_id, station_code, station_name,
    station_city, country, ov_bike, elevator, toilet, park_and_ride, lat, lon)
VALUES
    ('Arnhem', 'NL', true, false, true, false, 51.985104, 5.898730),
    ('Almere', 'NL', false, true, false, true, 52.350784, 5.264702),
    ('Amersfoort', 'NL', true, false, true, false, 52.156113, 5.387827),
    ('Almelo', 'NL', false, true, false, true, 52.357601, 6.663760),
    ('Alkmaar', 'NL', true, false, true, false, 52.6323813, 4.7533754),
    ('Apeldoorn', 'NL', false, true, false, true, 52.211157, 5.969923),
    ('Assen', 'NL', true, false, true, false, 52.992752, 6.564228),
    ('Amsterdam', 'NL', false, true, false, true, 52.370216, 4.895168),
    ('Boxtel', 'NL', true, false, true, false, 51.588470, 5.326350),
    ('Breda', 'NL', false, true, false, true, 51.571915, 4.768323),
    ('Dordrecht', 'NL', true, false, true, false, 51.7958812, 4.6779351),
    ('Delft', 'NL', false, true, false, true, 51.9994572, 4.3627245),
    ('Deventer', 'NL', true, false, true, false, 52.2695736, 6.2363396),
    ('Enschede', 'NL', false, true, false, true, 52.2209855, 6.8940537),
    ('Gouda', 'NL', true, false, true, false, 52.0181194, 4.7111221),
    ('Groningen', 'NL', false, true, false, true, 53.2190652, 6.5680077),
    ('Den Haag', 'NL', true, false, true, false, 52.0799838, 4.3113461),
    ('Hengelo', 'NL', false, true, false, true, 52.2658726, 6.7924049),
    ('Haarlem', 'NL', true, false, true, false, 52.3837058, 4.6435597),
    ('Helmond', 'NL', false, true, false, true, 51.4790956, 5.6557686),
    ('Hoorn', 'NL', true, false, true, false, 52.6225455, 5.0677266),
    ('Heerlen', 'NL', false, true, false, true, 50.8775239, 5.9815066),
    ('Den Bosch', 'NL', true, false, true, false, 51.6889387, 5.303116),
    ('Hilversum', 'NL', false, true, false, true, 52.2241375, 5.1719396),
    ('Leiden', 'NL', true, false, true, false, 52.1594747, 4.4908843),
    ('Lelystad', 'NL', false, true, false, true, 52.5150949, 5.4768915),
    ('Leeuwarden', 'NL', true, false, true, false, 53.2005936, 5.7918548),
    ('Maastricht', 'NL', false, true, false, true, 50.8512438, 5.6909768),
    ('Nijmegen', 'NL', true, false, true, false, 51.8425749, 5.8389606),
    ('Oss', 'NL', false, true, false, true, 51.7783542, 5.5320836),
    ('Roermond', 'NL', true, false, true, false, 51.1933903, 5.9882649),
    ('Roosendaal', 'NL', false, true, false, true, 51.5331484, 4.4561276),
    ('Sittard', 'NL', true, false, true, false, 50.9974235, 5.8666627),
    ('Tilburg', 'NL', false, true, false, true, 51.5856184, 5.0660616),
    ('Utrecht', 'NL', true, false, true, false, 52.0809856, 5.127684),
    ('Venlo', 'NL', false, true, false, true, 51.3924489, 6.1511724),
    ('Vlissingen', 'NL', true, false, true, false, 51.4943387, 3.4150058),
    ('Zaandam', 'NL', false, true, false, true, 52.4424926, 4.8298607),
    ('Zwolle', 'NL', true, false, true, false, 52.5089759, 6.0943765),
    ('Zutphen', 'NL', false, true, false, true, 52.1396933, 6.194772);
