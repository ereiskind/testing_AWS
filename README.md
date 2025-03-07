# testing_AWS

* **hello_world/hello_world.py** is the main script
* **hello_world/hello_world.json** has metadata about and for syncing "hello_world.py" to AWS Glue and is created on initial connection
* **hello_world/hello_world_download.json** is the result of 'Actions > Download' in AWS Glue, and selecting it in a new job with 'Actions > Upload' will recreate the job as it was at the time of the download
* **step_functions/confirm_job_success/state_machine_code.json** is the code for the state machine that runs the script above and returns an email or fails depending on if the job ran successfully; ic can be created by copying and pasting the contents of the code editor or with the file type under 'Actions > Export definition...', and selecting it as a new job with 'Actions > Import definition...' will recreate the state machine as it was at the time of the download/copy
* **step_functions/confirm_job_success/test_parameters.json** is the parameters for testing the state machine in that same folder