CREATE TABLE IF NOT EXISTS public.incident_logs
(
    id integer NOT NULL DEFAULT nextval('response_plan_id_seq'::regclass),
    tva_mapping_id integer NOT NULL,
    response_plan text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT response_plan_pkey PRIMARY KEY (id),
    CONSTRAINT response_plan_tva_mapping_id_fkey FOREIGN KEY (tva_mapping_id)
        REFERENCES public.tva_mapping (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)
