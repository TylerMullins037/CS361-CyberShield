-- Table: public.mitigation_strategies

-- DROP TABLE IF EXISTS public.mitigation_strategies;

CREATE TABLE IF NOT EXISTS public.mitigation_strategies
(
    id integer NOT NULL DEFAULT nextval('mitigation_strategies_id_seq'::regclass),
    tva_mapping_id integer NOT NULL,
    mitigation_strategy text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT mitigation_strategies_pkey PRIMARY KEY (id),
    CONSTRAINT mitigation_strategies_tva_mapping_id_fkey FOREIGN KEY (tva_mapping_id)
        REFERENCES public.tva_mapping (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.mitigation_strategies
    OWNER to doadmin;
