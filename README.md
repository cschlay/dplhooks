## DPLHooks

A very lightweight solution to manage multiple containers in one server,
so that it would be cheaper to run microservices.

The project does not take scaling in consideration.
If have certain service has exceeded its limits, then it has outgrown its role and
should be run on its own server or using some powerful container orchestration services such as Kubernetes.

## Installation

```bash
# Go to home directory
git clone https://github.com/cschlay/dplhooks.git
cd dplhooks
sudo ./scripts/install.sh
```

### Environment Variables

Put these to `.env` as `KEY=1sadsah`, without quotation marks.
See `examples/.env.example`

```
SECRET_KEY=
DEBUG=
HOST=
API_IP_WHITELIST=[]
API_ACCESS_KEY=
API_CLIENT_SECRET
```

### Update

```bash
# If it was installed in home directory.
cd ~/dplhooks
sudo ./scripts/update.sh
```

## Configuration Files

They are located at `.conf` both in production and development.

See example in `examples/.conf-examples`

### .conf/projects.yaml

Here is syntax reference:

```yaml
version: "1"

projects:
    <project_name>:
      repository: <git_repository>.git
      deploy_token: <a long string> 
      docker_image: <docker_image>  # not supported yet
      # Env files will be copied to root directory of a project.
      # Location for these are .conf/envfiles/
      envfiles:
        - .<envfile_1>
      hosts:
        - <domain_1>
        - <domain_2>
      docker_compose:
         - <filename_1>:
            # the will be set as environment variables to substitute values in docker-compose
            substitute:
              <VARIABLE_1>: <value_1>
      port: <port_number> # Must be unique.
```

To deploy a project, do `curl -X POST /deploy/ -d '{"token":"<deploy_token>", "project":"<project_name>"}' -H "Content-Type: application/json"`
