CREATE TABLE IF NOT EXISTS public.response_plan
(
    id SERIAL PRIMARY KEY,
    tva_mapping_id integer NOT NULL,
    response_plan text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT response_plan_tva_mapping_id_fkey FOREIGN KEY (tva_mapping_id)
        REFERENCES public.tva_mapping (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);
