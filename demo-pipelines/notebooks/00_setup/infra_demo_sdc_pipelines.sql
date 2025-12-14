CREATE CATALOG IF NOT EXISTS demo_sdc_pipelines COMMENT 'Catalog for SDC pipelines'
CREATE SCHEMA IF NOT EXISTS demo_sdc_pipelines.public_data COMMENT 'Schema for public data'
CREATE VOLUME IF NOT EXISTS demo_sdc_pipelines.public_data.incoming_files COMMENT 'Volume for raw incoming data files'
CREATE VOLUME IF NOT EXISTS demo_sdc_pipelines.public_data.error_files COMMENT 'Volume for files that failed processing'
CREATE VOLUME IF NOT EXISTS demo_sdc_pipelines.public_data.done_files COMMENT 'Volume for successfully processed files'

