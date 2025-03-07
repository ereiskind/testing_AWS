# testing_AWS

* **hello_world.py** is the main script
* **hello_world.json** has metadata about and for syncing "hello_world.py" to AWS Glue and is created on initial connection
* **hello_world_download.json** is the result of 'Actions > Download' in AWS Glue, and selecting it in a new job with 'Actions > Upload' will recreate the job as it was at the time of the download