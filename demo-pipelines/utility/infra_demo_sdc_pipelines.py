spark.sql("CREATE CATALOG IF NOT EXISTS demo_sdc_pipelines")
spark.sql("CREATE SCHEMA IF NOT EXISTS demo_sdc_pipelines.public_data")
spark.sql("CREATE VOLUME IF NOT EXISTS demo_sdc_pipelines.public_data.incoming_files COMMENT 'Volume for raw incoming data files'")
spark.sql("CREATE VOLUME IF NOT EXISTS demo_sdc_pipelines.public_data.error_files COMMENT 'Volume for files that failed processing'")
spark.sql("CREATE VOLUME IF NOT EXISTS demo_sdc_pipelines.public_data.done_files COMMENT 'Volume for successfully processed files'")

## ToDo: Likely delete this!! 
## See demo-pipelines/notebooks/00_setup/infra_demo_sdc_pipelines.sql 
## DABS doesn't (yet?) handle catalogs or schemas.  Seems like future enhancement - ask Zach. 
## SQL files seem cleaner.  The notebooks folder is strange.  
## Going to the Databricks Kickstart repo for a better example of how to set up the infrastructure.